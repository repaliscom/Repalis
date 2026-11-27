import uuid
from collections.abc import Sequence

from repalis.auth.models import AuthSubject, Customer, Member
from repalis.kit.db.postgres import AsyncSession
from repalis.kit.pagination import PaginationParams
from repalis.kit.services import ResourceServiceReader
from repalis.kit.sorting import Sorting
from repalis.models import Wallet

from ..repository.wallet import CustomerWalletRepository
from ..sorting.wallet import CustomerWalletSortProperty


class CustomerWalletService(ResourceServiceReader[Wallet]):
    async def list(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[Customer | Member],
        *,
        pagination: PaginationParams,
        sorting: Sequence[Sorting[CustomerWalletSortProperty]] = (
            (CustomerWalletSortProperty.created_at, True),
        ),
    ) -> tuple[Sequence[Wallet], int]:
        repository = CustomerWalletRepository.from_session(session)
        statement = repository.get_readable_statement(auth_subject).options(
            *repository.get_eager_options()
        )

        statement = repository.apply_sorting(statement, sorting)

        return await repository.paginate(
            statement, limit=pagination.limit, page=pagination.page
        )

    async def get_by_id(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[Customer | Member],
        id: uuid.UUID,
    ) -> Wallet | None:
        repository = CustomerWalletRepository.from_session(session)
        statement = (
            repository.get_readable_statement(auth_subject)
            .where(Wallet.id == id)
            .options(*repository.get_eager_options())
        )
        return await repository.get_one_or_none(statement)


customer_wallet = CustomerWalletService(Wallet)
