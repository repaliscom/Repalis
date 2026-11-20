import itertools

from sqlalchemy import select

from repalis.exceptions import RepalisError
from repalis.kit.services import ResourceServiceReader
from repalis.models import Transaction
from repalis.models.transaction import TransactionType
from repalis.postgres import AsyncSession


class BaseTransactionServiceError(RepalisError): ...


class BaseTransactionService(ResourceServiceReader[Transaction]):
    async def _get_balance_transactions_for_payment(
        self, session: AsyncSession, *, payment_transaction: Transaction
    ) -> list[tuple[Transaction, Transaction]]:
        statement = (
            select(Transaction)
            .where(
                Transaction.type == TransactionType.balance,
                Transaction.payment_transaction_id == payment_transaction.id,
            )
            .order_by(
                Transaction.balance_correlation_key,
                Transaction.account_id.nulls_first(),
            )
        )

        result = await session.execute(statement)
        transactions = list(result.scalars().all())
        return [
            (t1, t2)
            for _, (t1, t2) in itertools.groupby(
                transactions, key=lambda t: t.balance_correlation_key
            )
        ]
