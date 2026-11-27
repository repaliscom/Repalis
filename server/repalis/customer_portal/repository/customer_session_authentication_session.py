from uuid import UUID

from sqlalchemy import delete

from repalis.kit.repository import RepositoryBase
from repalis.kit.repository.base import RepositoryIDMixin
from repalis.kit.utils import utc_now
from repalis.models import CustomerSessionAuthenticationSession


class CustomerSessionAuthenticationSessionRepository(
    RepositoryBase[CustomerSessionAuthenticationSession],
    RepositoryIDMixin[CustomerSessionAuthenticationSession, UUID],
):
    model = CustomerSessionAuthenticationSession

    async def delete_expired(self) -> None:
        statement = delete(CustomerSessionAuthenticationSession).where(
            CustomerSessionAuthenticationSession.expires_at < int(utc_now().timestamp())
        )
        await self.session.execute(statement)
