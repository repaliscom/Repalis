import inspect
from typing import Annotated

from fastapi import Path
from pydantic import UUID4, Field

from repalis.customer.schemas.customer import CustomerID, ExternalCustomerID
from repalis.dispute.schemas import DisputeBase
from repalis.kit.currency import format_currency
from repalis.kit.metadata import (
    MetadataInputMixin,
    MetadataOutputMixin,
)
from repalis.kit.schemas import IDSchema, MultipleQueryFilter, Schema, TimestampedSchema
from repalis.kit.versioning import QuerySchema
from repalis.models.refund import (
    ManualRefundReason,
    RefundReason,
    RefundStatus,
)
from repalis.openapi import destructive_when_equals
from repalis.order.schemas import OrderID
from repalis.organization.schemas import OrganizationID
from repalis.subscription.schemas import SubscriptionID

RefundID = Annotated[UUID4, Path(description="The refund ID.")]


class RefundDispute(DisputeBase):
    """
    Dispute associated with a refund,
    in case we prevented a dispute by issuing a refund.
    """


class Refund(MetadataOutputMixin, IDSchema, TimestampedSchema):
    status: RefundStatus
    reason: RefundReason
    amount: int
    tax_amount: int
    currency: str
    organization_id: UUID4
    order_id: UUID4
    subscription_id: UUID4 | None
    customer_id: UUID4
    revoke_benefits: bool
    dispute: RefundDispute | None

    def get_amount_display(self) -> str:
        return format_currency(self.amount, self.currency)


class RefundCreate(MetadataInputMixin, Schema):
    order_id: UUID4
    reason: ManualRefundReason = Field(description="Reason for the refund.")
    amount: int = Field(description="Amount to refund in cents. Minimum is 1.", gt=0)
    comment: str | None = Field(
        None, description="An internal comment about the refund."
    )
    revoke_benefits: bool = Field(
        False,
        json_schema_extra=destructive_when_equals(True),
        description=inspect.cleandoc(
            """
            Should this refund trigger the associated customer benefits to be revoked?

            **Note:**
            Only allowed in case the `order` is a one-time purchase.
            Subscriptions automatically revoke customer benefits once the
            subscription itself is revoked, i.e fully canceled.
            """
        ),
    )


class RefundListParams(QuerySchema):
    id: MultipleQueryFilter[RefundID] | None = Field(
        None, title="RefundID Filter", description="Filter by refund ID."
    )
    organization_id: MultipleQueryFilter[OrganizationID] | None = Field(
        None, title="OrganizationID Filter", description="Filter by organization ID."
    )
    order_id: MultipleQueryFilter[OrderID] | None = Field(
        None, title="OrderID Filter", description="Filter by order ID."
    )
    subscription_id: MultipleQueryFilter[SubscriptionID] | None = Field(
        None, title="SubscriptionID Filter", description="Filter by subscription ID."
    )
    customer_id: MultipleQueryFilter[CustomerID] | None = Field(
        None, title="CustomerID Filter", description="Filter by customer ID."
    )
    external_customer_id: MultipleQueryFilter[ExternalCustomerID] | None = Field(
        None,
        title="ExternalCustomerID Filter",
        description="Filter by customer external ID.",
    )
    succeeded: bool | None = Field(
        None,
        title="RefundStatus Filter",
        description="Filter by `succeeded`.",
    )
