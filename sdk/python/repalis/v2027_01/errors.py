from __future__ import annotations

from repalis.base import RepalisClientError
from repalis.v2027_01.outputs import (
    AlreadyActiveSubscription as AlreadyActiveSubscriptionModel,
)
from repalis.v2027_01.outputs import (
    AlreadyCanceledSubscription as AlreadyCanceledSubscriptionModel,
)
from repalis.v2027_01.outputs import (
    AmbiguousExternalCustomerID as AmbiguousExternalCustomerIDModel,
)
from repalis.v2027_01.outputs import (
    AmbiguousExternalMeterID as AmbiguousExternalMeterIDModel,
)
from repalis.v2027_01.outputs import (
    AmbiguousExternalWebhookEndpointID as AmbiguousExternalWebhookEndpointIDModel,
)
from repalis.v2027_01.outputs import (
    BadRequest as BadRequestModel,
)
from repalis.v2027_01.outputs import (
    BenefitGrantAlreadyExists as BenefitGrantAlreadyExistsModel,
)
from repalis.v2027_01.outputs import (
    CannotCreateOrganizationError as CannotCreateOrganizationErrorModel,
)
from repalis.v2027_01.outputs import (
    CheckoutForbiddenError as CheckoutForbiddenErrorModel,
)
from repalis.v2027_01.outputs import (
    CheckoutLocked as CheckoutLockedModel,
)
from repalis.v2027_01.outputs import (
    CheckoutPaymentError as CheckoutPaymentErrorModel,
)
from repalis.v2027_01.outputs import (
    CustomerMeterCreditExternalIDConflict as CustomerMeterCreditExternalIDConflictModel,
)
from repalis.v2027_01.outputs import (
    CustomerMeterCreditNotReversible as CustomerMeterCreditNotReversibleModel,
)
from repalis.v2027_01.outputs import (
    CustomerNotReady as CustomerNotReadyModel,
)
from repalis.v2027_01.outputs import (
    DisputeAutoAcceptNotEnabled as DisputeAutoAcceptNotEnabledModel,
)
from repalis.v2027_01.outputs import (
    DisputeNotOpenError as DisputeNotOpenErrorModel,
)
from repalis.v2027_01.outputs import (
    ExpiredCheckoutError as ExpiredCheckoutErrorModel,
)
from repalis.v2027_01.outputs import (
    HTTPValidationError as HTTPValidationErrorModel,
)
from repalis.v2027_01.outputs import (
    InactiveSubscription as InactiveSubscriptionModel,
)
from repalis.v2027_01.outputs import (
    MissingInvoiceBillingDetails as MissingInvoiceBillingDetailsModel,
)
from repalis.v2027_01.outputs import (
    NotPermitted as NotPermittedModel,
)
from repalis.v2027_01.outputs import (
    OffSessionChargesNotEnabled as OffSessionChargesNotEnabledModel,
)
from repalis.v2027_01.outputs import (
    OrderNotDraft as OrderNotDraftModel,
)
from repalis.v2027_01.outputs import (
    OrderNotEligibleForInvoice as OrderNotEligibleForInvoiceModel,
)
from repalis.v2027_01.outputs import (
    OrganizationNotReadyForPayments as OrganizationNotReadyForPaymentsModel,
)
from repalis.v2027_01.outputs import (
    PauseResumeNotAllowed as PauseResumeNotAllowedModel,
)
from repalis.v2027_01.outputs import (
    PaymentActionRequired as PaymentActionRequiredModel,
)
from repalis.v2027_01.outputs import (
    PaymentFailed as PaymentFailedModel,
)
from repalis.v2027_01.outputs import (
    PaymentMethodInUseByActiveSubscription as PaymentMethodInUseByActiveSubscriptionModel,
)
from repalis.v2027_01.outputs import (
    PaymentMethodRequired as PaymentMethodRequiredModel,
)
from repalis.v2027_01.outputs import (
    PaymentMethodSetupFailed as PaymentMethodSetupFailedModel,
)
from repalis.v2027_01.outputs import (
    PaymentNotReady as PaymentNotReadyModel,
)
from repalis.v2027_01.outputs import (
    ProductNotDeletable as ProductNotDeletableModel,
)
from repalis.v2027_01.outputs import (
    RefundedAlready as RefundedAlreadyModel,
)
from repalis.v2027_01.outputs import (
    ResourceNotFound as ResourceNotFoundModel,
)
from repalis.v2027_01.outputs import (
    RotateNotPermitted as RotateNotPermittedModel,
)
from repalis.v2027_01.outputs import (
    SSOEnforcementRequiresConnection as SSOEnforcementRequiresConnectionModel,
)
from repalis.v2027_01.outputs import (
    SSORequiresVerifiedDomain as SSORequiresVerifiedDomainModel,
)
from repalis.v2027_01.outputs import (
    SubscriptionLocked as SubscriptionLockedModel,
)
from repalis.v2027_01.outputs import (
    SubscriptionNotScheduledToCancel as SubscriptionNotScheduledToCancelModel,
)
from repalis.v2027_01.outputs import (
    TrialAlreadyRedeemed as TrialAlreadyRedeemedModel,
)
from repalis.v2027_01.outputs import (
    Unauthorized as UnauthorizedModel,
)
from repalis.v2027_01.outputs import (
    UpdateSubscriptionPlanNotAllowed as UpdateSubscriptionPlanNotAllowedModel,
)
from repalis.v2027_01.outputs import (
    UpdateSubscriptionSeatsNotAllowed as UpdateSubscriptionSeatsNotAllowedModel,
)
from repalis.v2027_01.outputs import (
    UpdateSubscriptionUnitsNotAllowed as UpdateSubscriptionUnitsNotAllowedModel,
)


class HTTPValidationError(RepalisClientError):
    error_type = HTTPValidationErrorModel
    error: HTTPValidationErrorModel

    def __init__(self, status_code: int, error: HTTPValidationErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResourceNotFound(RepalisClientError):
    error_type = ResourceNotFoundModel
    error: ResourceNotFoundModel

    def __init__(self, status_code: int, error: ResourceNotFoundModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class NotPermitted(RepalisClientError):
    error_type = NotPermittedModel
    error: NotPermittedModel

    def __init__(self, status_code: int, error: NotPermittedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodSetupFailed(RepalisClientError):
    error_type = PaymentMethodSetupFailedModel
    error: PaymentMethodSetupFailedModel

    def __init__(self, status_code: int, error: PaymentMethodSetupFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerNotReady(RepalisClientError):
    error_type = CustomerNotReadyModel
    error: CustomerNotReadyModel

    def __init__(self, status_code: int, error: CustomerNotReadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodInUseByActiveSubscription(RepalisClientError):
    error_type = PaymentMethodInUseByActiveSubscriptionModel
    error: PaymentMethodInUseByActiveSubscriptionModel

    def __init__(
        self, status_code: int, error: PaymentMethodInUseByActiveSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalCustomersCheckEmailUpdate401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalCustomersVerifyEmailUpdate401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalCustomersVerifyEmailUpdate422Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsListSeats401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsListSeats403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsListSeats404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsAssignSeat400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsAssignSeat401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsAssignSeat403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsAssignSeat404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsRevokeSeat401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsRevokeSeat403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsRevokeSeat404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsResendInvitation400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsResendInvitation401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsResendInvitation403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsResendInvitation404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSeatsListClaimedSubscriptions401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class Unauthorized(RepalisClientError):
    error_type = UnauthorizedModel
    error: UnauthorizedModel

    def __init__(self, status_code: int, error: UnauthorizedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class RotateNotPermitted(RepalisClientError):
    error_type = RotateNotPermittedModel
    error: RotateNotPermittedModel

    def __init__(self, status_code: int, error: RotateNotPermittedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class BadRequest(RepalisClientError):
    error_type = BadRequestModel
    error: BadRequestModel

    def __init__(self, status_code: int, error: BadRequestModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersListMembers401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersListMembers403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersAddMember400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersAddMember401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersAddMember403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersRemoveMember400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersRemoveMember401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersRemoveMember403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersRemoveMember404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersUpdateMember400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersUpdateMember401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersUpdateMember403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalMembersUpdateMember404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotEligibleForInvoice(RepalisClientError):
    error_type = OrderNotEligibleForInvoiceModel
    error: OrderNotEligibleForInvoiceModel

    def __init__(
        self, status_code: int, error: OrderNotEligibleForInvoiceModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class MissingInvoiceBillingDetails(RepalisClientError):
    error_type = MissingInvoiceBillingDetailsModel
    error: MissingInvoiceBillingDetailsModel

    def __init__(
        self, status_code: int, error: MissingInvoiceBillingDetailsModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class AlreadyCanceledSubscription(RepalisClientError):
    error_type = AlreadyCanceledSubscriptionModel
    error: AlreadyCanceledSubscriptionModel

    def __init__(
        self, status_code: int, error: AlreadyCanceledSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentFailed(RepalisClientError):
    error_type = PaymentFailedModel
    error: PaymentFailedModel

    def __init__(self, status_code: int, error: PaymentFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSubscriptionsUpdate403Error(RepalisClientError):
    error_type = (
        AlreadyCanceledSubscriptionModel
        | PauseResumeNotAllowedModel
        | UpdateSubscriptionPlanNotAllowedModel
        | UpdateSubscriptionSeatsNotAllowedModel
        | UpdateSubscriptionUnitsNotAllowedModel
    )
    error: (
        AlreadyCanceledSubscriptionModel
        | PauseResumeNotAllowedModel
        | UpdateSubscriptionPlanNotAllowedModel
        | UpdateSubscriptionSeatsNotAllowedModel
        | UpdateSubscriptionUnitsNotAllowedModel
    )

    def __init__(
        self,
        status_code: int,
        error: AlreadyCanceledSubscriptionModel
        | PauseResumeNotAllowedModel
        | UpdateSubscriptionPlanNotAllowedModel
        | UpdateSubscriptionSeatsNotAllowedModel
        | UpdateSubscriptionUnitsNotAllowedModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerPortalSubscriptionsUpdate409Error(RepalisClientError):
    error_type = PaymentMethodRequiredModel | SubscriptionNotScheduledToCancelModel
    error: PaymentMethodRequiredModel | SubscriptionNotScheduledToCancelModel

    def __init__(
        self,
        status_code: int,
        error: PaymentMethodRequiredModel | SubscriptionNotScheduledToCancelModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class AmbiguousExternalCustomerID(RepalisClientError):
    error_type = AmbiguousExternalCustomerIDModel
    error: AmbiguousExternalCustomerIDModel

    def __init__(
        self, status_code: int, error: AmbiguousExternalCustomerIDModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckoutsUpdate403Error(RepalisClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ExpiredCheckoutError(RepalisClientError):
    error_type = ExpiredCheckoutErrorModel
    error: ExpiredCheckoutErrorModel

    def __init__(self, status_code: int, error: ExpiredCheckoutErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckoutsClientUpdate403Error(RepalisClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckoutLocked(RepalisClientError):
    error_type = CheckoutLockedModel
    error: CheckoutLockedModel

    def __init__(self, status_code: int, error: CheckoutLockedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckoutsClientConfirm400Error(RepalisClientError):
    error_type = CheckoutPaymentErrorModel
    error: CheckoutPaymentErrorModel

    def __init__(self, status_code: int, error: CheckoutPaymentErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckoutsClientConfirm403Error(RepalisClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionsCreate409Error(RepalisClientError):
    error_type = AlreadyActiveSubscriptionModel | TrialAlreadyRedeemedModel
    error: AlreadyActiveSubscriptionModel | TrialAlreadyRedeemedModel

    def __init__(
        self,
        status_code: int,
        error: AlreadyActiveSubscriptionModel | TrialAlreadyRedeemedModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionLocked(RepalisClientError):
    error_type = SubscriptionLockedModel
    error: SubscriptionLockedModel

    def __init__(self, status_code: int, error: SubscriptionLockedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionsUpdate402Error(RepalisClientError):
    error_type = PaymentFailedModel | PaymentActionRequiredModel
    error: PaymentFailedModel | PaymentActionRequiredModel

    def __init__(
        self, status_code: int, error: PaymentFailedModel | PaymentActionRequiredModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionsUpdate403Error(RepalisClientError):
    error_type = (
        AlreadyCanceledSubscriptionModel
        | InactiveSubscriptionModel
        | PaymentNotReadyModel
    )
    error: (
        AlreadyCanceledSubscriptionModel
        | InactiveSubscriptionModel
        | PaymentNotReadyModel
    )

    def __init__(
        self,
        status_code: int,
        error: AlreadyCanceledSubscriptionModel
        | InactiveSubscriptionModel
        | PaymentNotReadyModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionsUpdate409Error(RepalisClientError):
    error_type = SubscriptionLockedModel | SubscriptionNotScheduledToCancelModel
    error: SubscriptionLockedModel | SubscriptionNotScheduledToCancelModel

    def __init__(
        self,
        status_code: int,
        error: SubscriptionLockedModel | SubscriptionNotScheduledToCancelModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class ProductNotDeletable(RepalisClientError):
    error_type = ProductNotDeletableModel
    error: ProductNotDeletableModel

    def __init__(self, status_code: int, error: ProductNotDeletableModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrdersFinalize402Error(RepalisClientError):
    error_type = PaymentFailedModel | PaymentActionRequiredModel
    error: PaymentFailedModel | PaymentActionRequiredModel

    def __init__(
        self, status_code: int, error: PaymentFailedModel | PaymentActionRequiredModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrdersFinalize403Error(RepalisClientError):
    error_type = OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel
    error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel

    def __init__(
        self,
        status_code: int,
        error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotDraft(RepalisClientError):
    error_type = OrderNotDraftModel
    error: OrderNotDraftModel

    def __init__(self, status_code: int, error: OrderNotDraftModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CannotCreateOrganizationError(RepalisClientError):
    error_type = CannotCreateOrganizationErrorModel
    error: CannotCreateOrganizationErrorModel

    def __init__(
        self, status_code: int, error: CannotCreateOrganizationErrorModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrganizationsUpdate403Error(RepalisClientError):
    error_type = NotPermittedModel | DisputeAutoAcceptNotEnabledModel
    error: NotPermittedModel | DisputeAutoAcceptNotEnabledModel

    def __init__(
        self,
        status_code: int,
        error: NotPermittedModel | DisputeAutoAcceptNotEnabledModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrganizationsUpdate409Error(RepalisClientError):
    error_type = SSOEnforcementRequiresConnectionModel | SSORequiresVerifiedDomainModel
    error: SSOEnforcementRequiresConnectionModel | SSORequiresVerifiedDomainModel

    def __init__(
        self,
        status_code: int,
        error: SSOEnforcementRequiresConnectionModel | SSORequiresVerifiedDomainModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerMetersCredits409Error(RepalisClientError):
    error_type = (
        CustomerMeterCreditExternalIDConflictModel | AmbiguousExternalCustomerIDModel
    )
    error: CustomerMeterCreditExternalIDConflictModel | AmbiguousExternalCustomerIDModel

    def __init__(
        self,
        status_code: int,
        error: CustomerMeterCreditExternalIDConflictModel
        | AmbiguousExternalCustomerIDModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerMeterCreditNotReversible(RepalisClientError):
    error_type = CustomerMeterCreditNotReversibleModel
    error: CustomerMeterCreditNotReversibleModel

    def __init__(
        self, status_code: int, error: CustomerMeterCreditNotReversibleModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class AmbiguousExternalMeterID(RepalisClientError):
    error_type = AmbiguousExternalMeterIDModel
    error: AmbiguousExternalMeterIDModel

    def __init__(self, status_code: int, error: AmbiguousExternalMeterIDModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class DisputeNotOpenError(RepalisClientError):
    error_type = DisputeNotOpenErrorModel
    error: DisputeNotOpenErrorModel

    def __init__(self, status_code: int, error: DisputeNotOpenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class RefundedAlready(RepalisClientError):
    error_type = RefundedAlreadyModel
    error: RefundedAlreadyModel

    def __init__(self, status_code: int, error: RefundedAlreadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class AmbiguousExternalWebhookEndpointID(RepalisClientError):
    error_type = AmbiguousExternalWebhookEndpointIDModel
    error: AmbiguousExternalWebhookEndpointIDModel

    def __init__(
        self, status_code: int, error: AmbiguousExternalWebhookEndpointIDModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class BenefitGrantAlreadyExists(RepalisClientError):
    error_type = BenefitGrantAlreadyExistsModel
    error: BenefitGrantAlreadyExistsModel

    def __init__(self, status_code: int, error: BenefitGrantAlreadyExistsModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsListSeats401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsListSeats403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsListSeats404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsAssignSeat400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsAssignSeat401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsAssignSeat403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsAssignSeat404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsRevokeSeat401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsRevokeSeat403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsRevokeSeat404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsResendInvitation400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsResendInvitation401Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsResendInvitation403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsResendInvitation404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsGetClaimInfo400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsGetClaimInfo403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsGetClaimInfo404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsClaimSeat400Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerSeatsClaimSeat403Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class EventTypesUpdate404Error(RepalisClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)
