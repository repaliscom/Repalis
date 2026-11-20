from typing import Any

import structlog
from fastapi import Depends, Request, Response
from fastapi.responses import RedirectResponse
from httpx_oauth.integrations.fastapi import OAuth2AuthorizeCallback
from httpx_oauth.oauth2 import OAuth2Token

from repalis.authz.dependencies import AuthorizeWebUserRead, AuthorizeWebUserWrite
from repalis.config import settings
from repalis.eventstream.service import publish
from repalis.exceptions import (
    ResourceAlreadyExists,
    Unauthorized,
)
from repalis.integrations.github_repository_benefit.schemas import (
    GitHubInvitesBenefitRepositories,
)
from repalis.kit import jwt
from repalis.kit.http import ReturnTo, add_query_parameters, get_safe_return_url
from repalis.logging import Logger
from repalis.openapi import APITag
from repalis.postgres import AsyncSession, get_db_session
from repalis.redis import Redis, get_redis
from repalis.routing import APIRouter

from .service import github_oauth_client, github_repository_benefit_user_service

log: Logger = structlog.get_logger()

router = APIRouter(
    prefix="/integrations/github_repository_benefit",
    tags=["integrations_github_repository_benefit", APITag.private],
)


###############################################################################
# OAUTH2
###############################################################################


async def get_decoded_token_state(
    access_token_state: tuple[OAuth2Token, str | None],
) -> tuple[OAuth2Token, dict[str, Any]]:
    token_data, state = access_token_state
    if not state:
        raise Unauthorized("No state")

    try:
        state_data = await jwt.decode(
            token=state, type="github_repository_benefit_oauth"
        )
    except (jwt.DecodeError, jwt.ExpiredSignatureError) as e:
        raise Unauthorized("Invalid state") from e

    return (token_data, state_data)


###############################################################################
# User OAuth
###############################################################################


oauth2_authorize_callback = OAuth2AuthorizeCallback(
    github_oauth_client,
    route_name="integrations.github_repository_benefit.user_callback",
)


@router.get(
    "/user/authorize", name="integrations.github_repository_benefit.user_authorize"
)
async def user_authorize(
    request: Request, return_to: ReturnTo, auth_subject: AuthorizeWebUserWrite
) -> RedirectResponse:
    state = {"return_to": return_to}

    encoded_state = await jwt.encode(data=state, type="github_repository_benefit_oauth")

    authorization_url = await github_oauth_client.get_authorization_url(
        redirect_uri=str(
            request.url_for("integrations.github_repository_benefit.user_callback")
        ),
        state=encoded_state,
        scope=["user", "user.email"],
    )
    return RedirectResponse(authorization_url, 303)


@router.get(
    "/user/callback", name="integrations.github_repository_benefit.user_callback"
)
async def user_callback(
    auth_subject: AuthorizeWebUserWrite,
    session: AsyncSession = Depends(get_db_session),
    access_token_state: tuple[OAuth2Token, str | None] = Depends(
        oauth2_authorize_callback
    ),
) -> RedirectResponse:
    token_data, state = await get_decoded_token_state(access_token_state)
    return_to = state["return_to"]

    if "access_token" not in token_data:
        log.info(
            "github_repository_benefit.user_callback.access_token_missing",
            user_id=str(auth_subject.subject.id),
        )
        redirect_url = get_safe_return_url(
            add_query_parameters(
                return_to,
                error="Failed to get access token. Please try again later.",
            )
        )
        return RedirectResponse(redirect_url, 303)

    try:
        await github_repository_benefit_user_service.create_oauth_account(
            session,
            auth_subject.subject,
            token_data,
        )
    except ResourceAlreadyExists:
        await github_repository_benefit_user_service.update_oauth_account(
            session, auth_subject.subject, token_data
        )

    redirect_url = get_safe_return_url(add_query_parameters(return_to))

    return RedirectResponse(redirect_url, 303)


@router.get(
    "/user/repositories",
    name="integrations.github_repository_benefit.user_repositories",
    description="Lists available repositories for this user",
)
async def user_repositories(
    auth_subject: AuthorizeWebUserWrite,
    session: AsyncSession = Depends(get_db_session),
    redis: Redis = Depends(get_redis),
) -> GitHubInvitesBenefitRepositories:
    oauth = await github_repository_benefit_user_service.get_oauth_account(
        session, auth_subject.subject
    )

    installations = (
        await github_repository_benefit_user_service.list_user_installations(oauth)
    )

    orgs = await github_repository_benefit_user_service.list_orgs_with_billing_plans(
        redis, oauth, installations
    )

    repos = await github_repository_benefit_user_service.list_repositories(
        oauth,
        installations,
    )

    return GitHubInvitesBenefitRepositories(
        organizations=orgs,
        repositories=repos,
    )


###############################################################################
# Installation
###############################################################################


@router.get(
    "/installation/install",
    name="integrations.github_repository_benefit.installation_install",
)
async def installation_install(
    request: Request, auth_subject: AuthorizeWebUserRead
) -> RedirectResponse:
    return RedirectResponse(
        f"https://github.com/apps/{settings.GITHUB_REPOSITORY_BENEFITS_APP_NAMESPACE}/installations/new",
        303,
    )


@router.get(
    "/installation/callback",
    name="integrations.github_repository_benefit.installation_callback",
)
async def installation_callback(
    request: Request, auth_subject: AuthorizeWebUserWrite
) -> Response:
    await publish(
        "integrations.github_repository_benefit.installed",
        payload={},
        user_id=auth_subject.subject.id,
    )

    return Response("Installation successful, you can close this page.")
