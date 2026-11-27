from typing import Annotated

from fastapi import Path
from pydantic import UUID4, Field

from repalis.customer.schemas.customer import CustomerID, ExternalCustomerID
from repalis.exceptions import ResourceNotFound
from repalis.kit.schemas import (
    CUSTOMER_ID_EXAMPLE,
    IDSchema,
    MultipleQueryFilter,
    TimestampedSchema,
)
from repalis.kit.versioning import QuerySchema
from repalis.models.wallet import WalletType
from repalis.organization.schemas import OrganizationID

WalletID = Annotated[UUID4, Path(description="The wallet ID.")]

WalletNotFound = {
    "description": "Wallet not found.",
    "model": ResourceNotFound.schema(),
}


class WalletBase(TimestampedSchema, IDSchema):
    customer_id: UUID4 = Field(
        description="The ID of the customer that owns the wallet.",
        examples=[CUSTOMER_ID_EXAMPLE],
    )
    balance: int = Field(
        description="The current balance of the wallet, in cents.", examples=[50_00]
    )
    currency: str = Field(description="The currency of the wallet.", examples=["usd"])


class Wallet(WalletBase):
    """
    A wallet represents a customer's balance in your organization.

    The balance can be used to pay for usage.
    """


class WalletListParams(QuerySchema):
    organization_id: MultipleQueryFilter[OrganizationID] | None = Field(
        None, title="OrganizationID Filter", description="Filter by organization ID."
    )
    type: MultipleQueryFilter[WalletType] | None = Field(
        None, title="Wallet Type Filter", description="Filter by wallet type."
    )
    customer_id: MultipleQueryFilter[CustomerID] | None = Field(
        None, title="CustomerID Filter", description="Filter by customer ID."
    )
    external_customer_id: MultipleQueryFilter[ExternalCustomerID] | None = Field(
        None,
        title="ExternalCustomerID Filter",
        description="Filter by customer external ID.",
    )
