from collections.abc import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx2 import ASGITransport, AsyncClient
from repalis.v2026_04 import RepalisAsync

from repalis.auth.scope import Scope
from repalis.kit.utils import utc_now
from repalis.models import Benefit, Customer, Organization, Product, UserOrganization
from tests.fixtures.auth import AuthSubjectFixture
from tests.fixtures.database import SaveFixture
from tests.fixtures.random_objects import (
    create_active_subscription,
    create_checkout,
    create_order,
    create_subscription,
)


@pytest.fixture
async def repalis_sdk(app: FastAPI) -> AsyncGenerator[RepalisAsync]:
    sdk = RepalisAsync("", base_url="http://test")
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        headers={"Authorization": "Bearer ", "Repalis-Version": sdk.version},
    ) as client:
        await sdk._client._client.aclose()
        sdk._client._client = client
        yield sdk


@pytest.mark.anyio
@pytest.mark.auth
class TestSDK:
    """
    Those tests are here to ensure we do not introduce changes to the API that would break the SDK.

    Basically, we just run queries against our ASGI app to see if the SDK is able to parse the response without errors.
    """

    async def test_get_organization(
        self,
        repalis: RepalisAsync,
        organization: Organization,
        user_organization: UserOrganization,
    ) -> None:
        response = await repalis_sdk.organizations.get(str(organization.id))
        assert response is not None

    async def test_list_products(
        self,
        repalis: RepalisAsync,
        product: Product,
        product_second: Product,
        user_organization: UserOrganization,
    ) -> None:
        products = [product, product_second]

        response = await repalis_sdk.products.list()

        assert len(response.items) == len(products)

    async def test_list_benefits(
        self,
        repalis: RepalisAsync,
        benefits: list[Benefit],
        user_organization: UserOrganization,
    ) -> None:
        response = await repalis_sdk.benefits.list()

        assert len(response.items) == len(benefits)

    async def test_list_orders(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        product_one_time: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        subscription = await create_subscription(
            save_fixture, product=product, customer=customer
        )
        orders = [
            await create_order(
                save_fixture,
                product=product_one_time,
                customer=customer,
            ),
            await create_order(
                save_fixture,
                product=product,
                customer=customer,
                subscription=subscription,
            ),
        ]

        response = await repalis_sdk.orders.list()

        assert len(response.items) == len(orders)

    async def test_list_subscriptions(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        subscriptions = [
            await create_subscription(
                save_fixture, product=product, customer=customer, started_at=utc_now()
            ),
            await create_subscription(
                save_fixture, product=product, customer=customer, started_at=utc_now()
            ),
        ]

        response = await repalis_sdk.subscriptions.list()

        assert len(response.items) == len(subscriptions)

    async def test_cancel_subscription(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        subscription = await create_active_subscription(
            save_fixture, product=product, customer=customer
        )

        response = await repalis_sdk.subscriptions.update(
            str(subscription.id),
            cancel_at_period_end=True,
        )

        assert response is not None

    @pytest.mark.auth(
        AuthSubjectFixture(subject="user", scopes={Scope.checkouts_write})
    )
    async def test_create_checkout(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        response = await repalis_sdk.checkouts.create(
            products=[str(product.id)],
            external_customer_id="EXTERNAL_CUSTOMER_ID",
        )
        assert response is not None

        assert response.product_id == str(product.id)
        assert response.external_customer_id == "EXTERNAL_CUSTOMER_ID"

    async def test_create_checkout_link(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        response = await repalis_sdk.checkout_links.create(
            payment_processor="stripe",
            product_id=str(product.id),
        )
        assert response is not None

        assert len(response.products) == 1

    async def test_client_get_checkout(
        self,
        save_fixture: SaveFixture,
        repalis: RepalisAsync,
        product: Product,
        customer: Customer,
        user_organization: UserOrganization,
    ) -> None:
        checkout = await create_checkout(save_fixture, products=[product])
        response = await repalis_sdk.checkouts.client_get(checkout.client_secret)
        assert response is not None

        assert response.product_id == str(product.id)
