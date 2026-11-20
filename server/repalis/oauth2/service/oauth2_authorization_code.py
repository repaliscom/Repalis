import structlog

from repalis.enums import TokenType
from repalis.kit.services import ResourceServiceReader
from repalis.logging import Logger
from repalis.models import OAuth2AuthorizationCode
from repalis.oauth2.repository import OAuth2AuthorizationCodeRepository
from repalis.postgres import AsyncSession

log: Logger = structlog.get_logger()


class OAuth2AuthorizationCodeService(ResourceServiceReader[OAuth2AuthorizationCode]):
    async def revoke_leaked(
        self,
        session: AsyncSession,
        token: str,
        token_type: TokenType,
        *,
        notifier: str,
        url: str | None = None,
    ) -> bool:
        repository = OAuth2AuthorizationCodeRepository.from_session(session)
        authorization_code = await repository.get_by_code(token)

        if authorization_code is None:
            return False

        authorization_code.set_deleted_at()
        session.add(authorization_code)

        log.info(
            "Revoke leaked authorization code",
            id=authorization_code.id,
            notifier=notifier,
            url=url,
        )

        return True


oauth2_authorization_code = OAuth2AuthorizationCodeService(OAuth2AuthorizationCode)
