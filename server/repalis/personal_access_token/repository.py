from sqlalchemy import or_
from sqlalchemy.orm import contains_eager

from repalis.kit.crypto import get_token_hash_candidates
from repalis.kit.repository import RepositoryBase, RepositoryTokenHashMixin
from repalis.kit.utils import utc_now
from repalis.models import PersonalAccessToken, User


class PersonalAccessTokenRepository(
    RepositoryTokenHashMixin[PersonalAccessToken],
    RepositoryBase[PersonalAccessToken],
):
    model = PersonalAccessToken
    token_hash_attribute = "token"

    async def get_by_token(
        self, token: str, *, expired: bool = False
    ) -> PersonalAccessToken | None:
        candidates = get_token_hash_candidates(token)
        statement = (
            self.get_base_statement()
            .join(PersonalAccessToken.user)
            .where(
                self.token_hash_clause(candidates),
                ~PersonalAccessToken.is_deleted,
                User.can_authenticate,
            )
            .options(contains_eager(PersonalAccessToken.user))
        )
        if not expired:
            statement = statement.where(
                or_(
                    PersonalAccessToken.expires_at.is_(None),
                    PersonalAccessToken.expires_at > utc_now(),
                )
            )
        personal_access_token = await self.get_one_or_none(statement)
        if personal_access_token is None:
            return None
        return await self.rehash_token(personal_access_token, candidates)
