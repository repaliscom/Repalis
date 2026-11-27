import time
import uuid
from collections.abc import Sequence
from typing import Any
from uuid import UUID

import structlog
from pydantic import MISSING
from sqlalchemy import UnaryExpression, asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import OrderByList

from repalis.auth.models import AuthSubject, Organization
from repalis.auth.permission import OrganizationPermission
from repalis.auth.scope import Scope
from repalis.authz.service import (
    assert_organization_permission,
    assert_resource_permission,
    get_accessible_org_ids,
)
from repalis.config import settings
from repalis.email.schemas import (
    OrganizationAccessTokenLeakedEmail,
    OrganizationAccessTokenLeakedProps,
)
from repalis.email.sender import enqueue_email_template
from repalis.enums import TokenType
from repalis.exceptions import RepalisRequestValidationError
from repalis.kit.crypto import generate_token_hash_pair, get_token_hash
from repalis.kit.pagination import PaginationParams
from repalis.kit.sorting import Sorting
from repalis.kit.utils import utc_now
from repalis.logging import Logger
from repalis.models import OrganizationAccessToken, User
from repalis.organization.resolver import get_payload_organization
from repalis.postgres import AsyncSession
from repalis.user_organization.service import (
    user_organization as user_organization_service,
)

from .repository import OrganizationAccessTokenRepository
from .schemas import OrganizationAccessTokenCreate, OrganizationAccessTokenUpdate
from .sorting import OrganizationAccessTokenSortProperty

log: Logger = structlog.get_logger()

TOKEN_PREFIX = "repalis_oat_"


class OrganizationAccessTokenService:
    def __init__(self) -> None:
        self._cache: dict[str, tuple[float, OrganizationAccessToken]] = {}

    async def list(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User | Organization],
        *,
        organization_id: Sequence[uuid.UUID] | None = None,
        pagination: PaginationParams,
        sorting: Sequence[Sorting[OrganizationAccessTokenSortProperty]] = (
            (OrganizationAccessTokenSortProperty.created_at, False),
        ),
    ) -> tuple[Sequence[OrganizationAccessToken], int]:
        repository = OrganizationAccessTokenRepository.from_session(session)
        org_ids = await get_accessible_org_ids(
            session, auth_subject, permission=OrganizationPermission.organization_manage
        )
        statement = repository.get_statement_by_org_ids(org_ids)

        if organization_id is not None:
            statement = statement.where(
                OrganizationAccessToken.organization_id.in_(organization_id)
            )

        order_by_clauses: list[OrderByList | UnaryExpression[Any]] = []
        for criterion, is_desc in sorting:
            clause_function = desc if is_desc else asc
            if criterion == OrganizationAccessTokenSortProperty.created_at:
                order_by_clauses.append(
                    clause_function(OrganizationAccessToken.created_at)
                )
            elif criterion == OrganizationAccessTokenSortProperty.comment:
                order_by_clauses.append(
                    clause_function(OrganizationAccessToken.comment)
                )
            elif criterion == OrganizationAccessTokenSortProperty.last_used_at:
                order_by_clauses.append(
                    clause_function(OrganizationAccessToken.last_used_at)
                )
            elif criterion == OrganizationAccessTokenSortProperty.organization_id:
                order_by_clauses.append(
                    clause_function(OrganizationAccessToken.organization_id)
                )
        statement = statement.order_by(*order_by_clauses)

        return await repository.paginate(
            statement, limit=pagination.limit, page=pagination.page
        )

    async def get(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User | Organization],
        id: UUID,
    ) -> OrganizationAccessToken | None:
        repository = OrganizationAccessTokenRepository.from_session(session)
        org_ids = await get_accessible_org_ids(
            session, auth_subject, permission=OrganizationPermission.organization_manage
        )
        statement = repository.get_statement_by_org_ids(org_ids).where(
            OrganizationAccessToken.id == id,
            ~OrganizationAccessToken.is_deleted,
        )
        return await repository.get_one_or_none(statement)

    async def get_by_token(
        self, session: AsyncSession, token: str, *, expired: bool = False
    ) -> OrganizationAccessToken | None:
        repository = OrganizationAccessTokenRepository.from_session(session)
        ttl = settings.ORGANIZATION_ACCESS_TOKEN_CACHE_TTL_SECONDS
        if expired or ttl <= 0:
            return await repository.get_by_token(token, expired=expired)

        key = get_token_hash(token)
        cached = self._cache.get(key)
        if cached is not None and cached[0] > time.monotonic():
            return await session.merge(cached[1], load=False)

        organization_access_token = await repository.get_by_token(token)
        if organization_access_token is not None and not session.is_modified(
            organization_access_token
        ):
            now = time.monotonic()
            self._cache = {k: v for k, v in self._cache.items() if v[0] > now}
            with Session() as detached_session:
                self._cache[key] = (
                    now + ttl,
                    detached_session.merge(organization_access_token, load=False),
                )
        return organization_access_token

    async def create(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User | Organization],
        create_schema: OrganizationAccessTokenCreate,
    ) -> tuple[OrganizationAccessToken, str]:
        organization = await get_payload_organization(
            session, auth_subject, create_schema
        )
        await assert_organization_permission(
            session,
            auth_subject,
            organization.id,
            OrganizationPermission.organization_manage,
        )
        self._validate_scopes_within_caller(auth_subject, create_schema.scopes)
        token, token_hash = generate_token_hash_pair(prefix=TOKEN_PREFIX)
        organization_access_token = OrganizationAccessToken(
            **create_schema.model_dump(
                exclude={"scopes", "expires_in", "organization_id"}
            ),
            organization=organization,
            token=token_hash,
            expires_at=utc_now() + create_schema.expires_in
            if create_schema.expires_in
            else None,
            scope=" ".join(create_schema.scopes),
        )
        repository = OrganizationAccessTokenRepository.from_session(session)
        organization_access_token = await repository.create(
            organization_access_token, flush=True
        )

        return organization_access_token, token

    async def update(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User | Organization],
        organization_access_token: OrganizationAccessToken,
        update_schema: OrganizationAccessTokenUpdate,
    ) -> OrganizationAccessToken:
        await assert_resource_permission(
            session,
            auth_subject,
            organization_access_token,
            OrganizationPermission.organization_manage,
        )
        repository = OrganizationAccessTokenRepository.from_session(session)

        update_dict = update_schema.model_dump(exclude={"scopes"}, exclude_unset=True)
        if update_schema.scopes is not MISSING:
            self._validate_scopes_within_caller(auth_subject, update_schema.scopes)
            update_dict["scope"] = " ".join(update_schema.scopes)

        return await repository.update(
            organization_access_token, update_dict=update_dict
        )

    def _validate_scopes_within_caller(
        self,
        auth_subject: AuthSubject[User | Organization],
        requested_scopes: Sequence[str],
    ) -> None:
        caller_scopes = auth_subject.scopes
        requested = {Scope(s) for s in requested_scopes}
        excess = requested - caller_scopes
        if excess:
            raise RepalisRequestValidationError(
                [
                    {
                        "type": "value_error",
                        "loc": ("body", "scopes"),
                        "msg": ("Requested scopes exceed the caller's own scopes."),
                        "input": sorted(s.value for s in excess),
                    }
                ]
            )

    async def delete(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User | Organization],
        organization_access_token: OrganizationAccessToken,
    ) -> None:
        await assert_resource_permission(
            session,
            auth_subject,
            organization_access_token,
            OrganizationPermission.organization_manage,
        )
        repository = OrganizationAccessTokenRepository.from_session(session)
        await repository.soft_delete(organization_access_token)

    async def revoke_leaked(
        self,
        session: AsyncSession,
        token: str,
        token_type: TokenType,
        *,
        notifier: str,
        url: str | None = None,
    ) -> bool:
        organization_access_token = await self.get_by_token(session, token)

        if organization_access_token is None:
            return False

        repository = OrganizationAccessTokenRepository.from_session(session)
        await repository.soft_delete(organization_access_token)

        organization_members = await user_organization_service.list_by_org(
            session, organization_access_token.organization_id
        )
        for organization_member in organization_members:
            email = organization_member.user.email
            enqueue_email_template(
                OrganizationAccessTokenLeakedEmail(
                    props=OrganizationAccessTokenLeakedProps(
                        email=email,
                        organization_access_token=organization_access_token.comment,
                        notifier=notifier,
                        url=url or "",
                    )
                ),
                to_email_addr=email,
                subject="Security Notice - Your Repalis Organization Access Token has been leaked",
            )

        log.info(
            "Revoke leaked organization access token",
            id=organization_access_token.id,
            notifier=notifier,
            url=url,
        )

        return True


organization_access_token = OrganizationAccessTokenService()
