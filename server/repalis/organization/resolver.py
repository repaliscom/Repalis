from typing import Protocol

from pydantic import UUID4

from repalis.auth.models import AuthSubject, is_agent, is_organization
from repalis.authz.service import get_accessible_org_ids
from repalis.exceptions import RepalisRequestValidationError
from repalis.models import Agent, Organization, User
from repalis.organization.repository import OrganizationRepository
from repalis.postgres import AsyncReadSession


class _OrganizationIDModelNone(Protocol):
    organization_id: UUID4 | None


class _OrganizationIDModel(Protocol):
    organization_id: UUID4


OrganizationIDModel = _OrganizationIDModelNone | _OrganizationIDModel


async def get_payload_organization(
    session: AsyncReadSession,
    auth_subject: AuthSubject[User | Organization | Agent],
    model: OrganizationIDModel,
) -> Organization:
    if is_organization(auth_subject):
        if model.organization_id is not None:
            raise RepalisRequestValidationError(
                [
                    {
                        "type": "organization_token",
                        "msg": (
                            "Setting organization_id is disallowed "
                            "when using an organization token."
                        ),
                        "loc": (
                            "body",
                            "organization_id",
                        ),
                        "input": model.organization_id,
                    }
                ]
            )
        return auth_subject.subject

    repository = OrganizationRepository.from_session(session)

    if model.organization_id is None:
        # An agent, or a credential down-scoped to exactly one organization,
        # resolves it implicitly, restoring organization-token ergonomics on
        # create endpoints.
        if is_agent(auth_subject) or (
            auth_subject.organization_ids is not None
            and len(auth_subject.organization_ids) == 1
        ):
            accessible = await get_accessible_org_ids(session, auth_subject)
            if len(accessible) == 1:
                organization = await repository.get_by_id(next(iter(accessible)))
                if organization is not None:
                    return organization
        raise RepalisRequestValidationError(
            [
                {
                    "type": "missing",
                    "msg": "organization_id is required.",
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "input": None,
                }
            ]
        )

    accessible = await get_accessible_org_ids(session, auth_subject)
    if model.organization_id not in accessible:
        raise RepalisRequestValidationError(
            [
                {
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "msg": "Organization not found.",
                    "type": "value_error",
                    "input": model.organization_id,
                }
            ]
        )

    organization = await repository.get_by_id(model.organization_id)

    if organization is None:
        raise RepalisRequestValidationError(
            [
                {
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "msg": "Organization not found.",
                    "type": "value_error",
                    "input": model.organization_id,
                }
            ]
        )

    return organization
