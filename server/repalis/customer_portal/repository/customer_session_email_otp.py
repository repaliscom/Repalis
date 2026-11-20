from uuid import UUID

from sqlalchemy import delete

from repalis.kit.repository import RepositoryBase
from repalis.kit.repository.base import RepositoryIDMixin
from repalis.kit.utils import utc_now
from repalis.models import CustomerSessionEmailOTP


class CustomerSessionEmailOTPRepository(
    RepositoryBase[CustomerSessionEmailOTP],
    RepositoryIDMixin[CustomerSessionEmailOTP, UUID],
):
    model = CustomerSessionEmailOTP

    async def delete_expired(self) -> None:
        statement = delete(CustomerSessionEmailOTP).where(
            CustomerSessionEmailOTP.expires_at < int(utc_now().timestamp())
        )
        await self.session.execute(statement)
