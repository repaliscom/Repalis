from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.orm import contains_eager

from repalis.kit.crypto import get_token_hash_candidates
from repalis.kit.repository import RepositoryBase, RepositoryTokenHashMixin
from repalis.kit.utils import utc_now
from repalis.models.customer import Customer
from repalis.models.customer_email_verification import CustomerEmailVerification


class CustomerEmailVerificationRepository(
    RepositoryTokenHashMixin[CustomerEmailVerification],
    RepositoryBase[CustomerEmailVerification],
):
    model = CustomerEmailVerification
    token_hash_attribute = "token_hash"

    async def get_valid_by_token(self, token: str) -> CustomerEmailVerification | None:
        statement = (
            select(CustomerEmailVerification)
            .join(CustomerEmailVerification.customer)
            .where(
                self.token_hash_clause(get_token_hash_candidates(token)),
                CustomerEmailVerification.expires_at > utc_now(),
                Customer.deleted_at.is_(None),
            )
            .options(
                contains_eager(CustomerEmailVerification.customer).joinedload(
                    Customer.organization
                )
            )
        )
        result = await self.session.execute(statement)
        return result.scalars().unique().one_or_none()

    async def delete_by_customer_id(self, customer_id: UUID) -> None:
        statement = delete(CustomerEmailVerification).where(
            CustomerEmailVerification.customer_id == customer_id,
        )
        await self.session.execute(statement)

    async def delete_expired(self) -> None:
        statement = delete(CustomerEmailVerification).where(
            CustomerEmailVerification.expires_at < utc_now(),
        )
        await self.session.execute(statement)
