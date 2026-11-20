from uuid import UUID

from sqlalchemy import Select

from repalis.auth.models import User
from repalis.kit.repository import (
    Options,
    RepositoryBase,
    RepositorySoftDeletionIDMixin,
    RepositorySoftDeletionMixin,
)
from repalis.models import PayoutAccount


class PayoutAccountRepository(
    RepositorySoftDeletionIDMixin[PayoutAccount, UUID],
    RepositorySoftDeletionMixin[PayoutAccount],
    RepositoryBase[PayoutAccount],
):
    model = PayoutAccount

    async def get_by_stripe_id(
        self,
        stripe_id: str,
        *,
        options: Options = (),
        include_deleted: bool = False,
    ) -> PayoutAccount | None:
        statement = (
            self.get_base_statement(include_deleted=include_deleted)
            .where(PayoutAccount.stripe_id == stripe_id)
            .options(*options)
        )
        return await self.get_one_or_none(statement)

    def get_statement_by_user(self, user: User) -> Select[PayoutAccount]:
        return self.get_base_statement().where(PayoutAccount.admin_id == user.id)
