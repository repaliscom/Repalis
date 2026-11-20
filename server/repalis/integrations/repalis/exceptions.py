import uuid

from repalis.exceptions import RepalisError


class RepalisSelfWebhookError(RepalisError): ...


class TransactionFeeBenefitError(RepalisSelfWebhookError): ...


class SupportBenefitError(RepalisSelfWebhookError): ...


class RepalisSelfNotConfigured(RepalisError):
    def __init__(self) -> None:
        super().__init__("Repalis self-billing is not configured.", status_code=404)


class RepalisSelfPlanNotFound(RepalisError):
    def __init__(self, product_id: str) -> None:
        super().__init__(f"Plan {product_id!r} is not available.", status_code=404)
        self.product_id = product_id


class RepalisSelfNoActiveSubscription(RepalisError):
    def __init__(self, organization_id: uuid.UUID) -> None:
        super().__init__(
            f"Organization {organization_id} has no active subscription.",
            status_code=404,
        )
        self.organization_id = organization_id


class RepalisSelfPaidSubscriptionAlreadyExists(RepalisError):
    def __init__(self, organization_id: uuid.UUID) -> None:
        super().__init__(
            "This organization already has an active paid subscription. "
            "Refresh the page to change plans.",
            status_code=409,
        )
        self.organization_id = organization_id


class RepalisSelfOrderNotFound(RepalisError):
    def __init__(self, order_id: str) -> None:
        super().__init__(f"Order {order_id!r} not found.", status_code=404)
        self.order_id = order_id


class RepalisSelfCustomerNotFound(RepalisError):
    def __init__(self, organization_id: uuid.UUID) -> None:
        super().__init__(
            f"Organization {organization_id} has no Repalis customer.",
            status_code=404,
        )
        self.organization_id = organization_id


class RepalisSelfPaymentMethodNotFound(RepalisError):
    def __init__(self, payment_method_id: str) -> None:
        super().__init__(
            f"Payment method {payment_method_id!r} not found.",
            status_code=404,
        )
        self.payment_method_id = payment_method_id


class RepalisSelfBenefitGrantNotFound(RepalisError):
    def __init__(self, benefit_grant_id: str) -> None:
        super().__init__(
            f"Benefit grant {benefit_grant_id!r} not found.",
            status_code=404,
        )
        self.benefit_grant_id = benefit_grant_id


class RepalisSelfPaymentMethodInUse(RepalisError):
    def __init__(self, payment_method_id: str) -> None:
        super().__init__(
            "This payment method is used by an active subscription and "
            "no alternative payment method is available. Add another "
            "payment method before deleting this one.",
            status_code=400,
        )
        self.payment_method_id = payment_method_id


class RepalisSelfNotApproved(RepalisError):
    def __init__(self, organization_id: uuid.UUID) -> None:
        super().__init__(
            "Your organization must complete review and be approved "
            "before changing plan.",
            status_code=403,
        )
        self.organization_id = organization_id


class RepalisSelfInvoiceNotReady(RepalisSelfWebhookError):
    def __init__(self, order_id: str) -> None:
        super().__init__(f"Invoice for order {order_id!r} not yet generated.")
        self.order_id = order_id


class RepalisSelfOrderNotEligible(RepalisSelfWebhookError):
    """Order is permanently ineligible for invoice generation (draft/void).

    Unlike ``RepalisSelfInvoiceNotReady`` (retry later while the PDF renders),
    this is a terminal condition: the order's status disqualifies it and
    retrying will not help. Callers should treat it as out of scope rather
    than schedule a retry.
    """

    def __init__(self, order_id: str) -> None:
        super().__init__(f"Order {order_id!r} is not eligible for invoice generation.")
        self.order_id = order_id
