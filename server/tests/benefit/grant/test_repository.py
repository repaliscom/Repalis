import pytest

from repalis.benefit.grant.repository import BenefitGrantRepository
from repalis.benefit.strategies import BenefitActionRequiredError
from repalis.kit.utils import utc_now
from repalis.models import BenefitGrant, Customer, Member, Organization, Payment, Product
from repalis.models.benefit import BenefitType
from repalis.postgres import AsyncSession
from tests.fixtures.database import SaveFixture
from tests.fixtures.random_objects import create_benefit, create_order, create_refund


@pytest.fixture
async def pending_grant(
    save_fixture: SaveFixture,
    organization: Organization,
    customer: Customer,
    product: Product,
) -> BenefitGrant:
    benefit = await create_benefit(
        save_fixture,
        organization=organization,
        type=BenefitType.github_repository,
        properties={
            "repository_owner": "repaliscom",
            "repository_name": "repalis",
            "permission": "pull",
        },
    )
    order = await create_order(save_fixture, customer=customer, product=product)
    grant = BenefitGrant(order=order, customer=customer, benefit=benefit)
    grant.set_grant_failed(BenefitActionRequiredError("Connect GitHub"))
    await save_fixture(grant)
    return grant


@pytest.mark.anyio
class TestListErroredByCustomerAndBenefitType:
    async def test_manually_suppressed_grant_is_skipped_for_oauth_recovery(
        self,
        session: AsyncSession,
        save_fixture: SaveFixture,
        customer: Customer,
        member_owner: Member,
        pending_grant: BenefitGrant,
    ) -> None:
        pending_grant.member = member_owner
        pending_grant.manually_revoked_at = utc_now()
        await save_fixture(pending_grant)

        repository = BenefitGrantRepository.from_session(session)
        assert not await repository.list_errored_by_customer_and_benefit_type(
            customer, BenefitType.github_repository, BenefitActionRequiredError.__name__
        )
        assert not await repository.list_errored_by_member_and_benefit_type(
            member_owner,
            BenefitType.github_repository,
            BenefitActionRequiredError.__name__,
        )

    @pytest.mark.parametrize("revoke_benefits", [False, True])
    async def test_refunded_order(
        self,
        revoke_benefits: bool,
        session: AsyncSession,
        save_fixture: SaveFixture,
        customer: Customer,
        payment: Payment,
        pending_grant: BenefitGrant,
    ) -> None:
        assert pending_grant.order is not None
        refund = await create_refund(save_fixture, pending_grant.order, payment)
        refund.revoke_benefits = revoke_benefits
        await save_fixture(refund)

        repository = BenefitGrantRepository.from_session(session)
        grants = await repository.list_errored_by_customer_and_benefit_type(
            customer,
            BenefitType.github_repository,
            BenefitActionRequiredError.__name__,
        )

        assert list(grants) == ([] if revoke_benefits else [pending_grant])
