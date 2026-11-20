import pytest

from repalis.auth.models import AuthSubject
from repalis.kit.pagination import PaginationParams
from repalis.models import (
    Account,
    Organization,
    User,
    UserOrganization,
)
from repalis.models.organization import OrganizationStatus
from repalis.models.transaction import TransactionType
from repalis.postgres import AsyncSession
from repalis.transaction.service.transaction import transaction as transaction_service
from tests.fixtures.database import SaveFixture
from tests.transaction.conftest import create_transaction


@pytest.mark.anyio
class TestBlockedOrganizationTransactionAccess:
    @pytest.mark.auth
    async def test_blocked_org_account_transactions_hidden(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
        save_fixture: SaveFixture,
        organization: Organization,
        user_organization: UserOrganization,
        account: Account,
    ) -> None:
        transaction = await create_transaction(
            save_fixture,
            type=TransactionType.balance,
            account=account,
        )

        organization.set_status(OrganizationStatus.BLOCKED)
        await save_fixture(organization)

        results, count = await transaction_service.search(
            session, auth_subject, pagination=PaginationParams(1, 10)
        )

        result_ids = [t.id for t in results]
        assert transaction.id not in result_ids
        assert count == 0
