from fastapi import APIRouter

from repalis.account.endpoints import router as accounts_router
from repalis.agent.endpoints import router as agent_router
from repalis.auth.endpoints import router as auth_router
from repalis.benefit.endpoints import router as benefits_router
from repalis.benefit.grant.endpoints import router as benefit_grants_router
from repalis.benefit.strategies.slack_shared_channel.endpoints import (
    router as slack_shared_channel_benefit_router,
)
from repalis.catalog.endpoints import router as catalog_router
from repalis.checkout.endpoints import router as checkout_router
from repalis.checkout_link.endpoints import router as checkout_link_router
from repalis.cli.endpoints import router as cli_router
from repalis.custom_field.endpoints import router as custom_field_router
from repalis.customer.endpoints import router as customer_router
from repalis.customer_meter.endpoints import router as customer_meter_router
from repalis.customer_portal.endpoints import router as customer_portal_router
from repalis.customer_seat.endpoints import router as customer_seat_router
from repalis.customer_session.endpoints import router as customer_session_router
from repalis.declarative_config.endpoints import router as declarative_config_router
from repalis.discount.endpoints import router as discount_router
from repalis.dispute.endpoints import router as dispute_router
from repalis.email_update.endpoints import router as email_update_router
from repalis.event.endpoints import ingest_router as event_ingest_router
from repalis.event.endpoints import router as event_router
from repalis.event_type.endpoints import router as event_type_router
from repalis.eventstream.endpoints import router as stream_router
from repalis.feedback.endpoints import router as feedback_router
from repalis.file.endpoints import router as files_router
from repalis.integrations.chargeback_stop.endpoints import (
    router as chargeback_stop_router,
)
from repalis.integrations.discord.endpoints import router as discord_router
from repalis.integrations.github.endpoints import router as github_router
from repalis.integrations.github_repository_benefit.endpoints import (
    router as github_repository_benefit_router,
)
from repalis.integrations.plain.endpoints import router as plain_router
from repalis.integrations.repalis.endpoints import router as repalis_self_router
from repalis.integrations.resend.endpoints import router as resend_router
from repalis.integrations.slack.endpoints import router as slack_router
from repalis.integrations.stripe.endpoints import router as stripe_router
from repalis.license_key.endpoints import router as license_key_router
from repalis.mcp_event.endpoints import router as mcp_event_router
from repalis.member.endpoints import customer_members_router
from repalis.member.endpoints import router as member_router
from repalis.merchant_migration.endpoints import router as merchant_migration_router
from repalis.meter.endpoints import router as meter_router
from repalis.metrics.endpoints import router as metrics_router
from repalis.notifications.endpoints import router as notifications_router
from repalis.oauth2.endpoints.oauth2 import router as oauth2_router
from repalis.order.endpoints import router as order_router
from repalis.organization.endpoints import router as organization_router
from repalis.organization_access_token.endpoints import (
    router as organization_access_token_router,
)
from repalis.organization_domain.endpoints import router as organization_domain_router
from repalis.organization_email.endpoints import router as organization_email_router
from repalis.outpost.endpoints import router as outpost_router
from repalis.payment.endpoints import router as payment_router
from repalis.payout.endpoints import router as payout_router
from repalis.payout_account.endpoints import router as payout_account_router
from repalis.personal_access_token.endpoints import router as pat_router
from repalis.product.endpoints import router as product_router
from repalis.refund.endpoints import router as refund_router
from repalis.search.endpoints import router as search_router
from repalis.sso.endpoints import router as sso_router
from repalis.subscription.endpoints import router as subscription_router
from repalis.support_case.endpoints import router as support_case_router
from repalis.tax.endpoints import router as tax_router
from repalis.transaction.endpoints import router as transaction_router
from repalis.user.endpoints import router as user_router
from repalis.wallet.endpoints import router as wallet_router
from repalis.webhook.endpoints import router as webhook_router

router = APIRouter(prefix="/v1")

# /events
router.include_router(event_router)
router.include_router(event_ingest_router)
# /customer-portal
router.include_router(customer_portal_router)
# /customers
router.include_router(customer_router)
# /checkouts
router.include_router(checkout_router)
# /subscriptions
router.include_router(subscription_router)
# /products
router.include_router(product_router)
# /users
router.include_router(user_router)
# /license-keys
router.include_router(license_key_router)
# /orders
router.include_router(order_router)
# /organizations
router.include_router(organization_router)
# /customer-meters
router.include_router(customer_meter_router)
# /metrics
router.include_router(metrics_router)
# /discounts
router.include_router(discount_router)
# /oauth2
router.include_router(oauth2_router)
# /meters
router.include_router(meter_router)
# /integrations/stripe
router.include_router(stripe_router)
# /benefits
router.include_router(benefits_router)
# /notifications
router.include_router(notifications_router)
# /payments
router.include_router(payment_router)
# /disputes
router.include_router(dispute_router)
# /refunds
router.include_router(refund_router)
# /webhooks
router.include_router(webhook_router)
# /mcp/events
router.include_router(mcp_event_router)
# /stream
router.include_router(stream_router)
# /benefit-grants
router.include_router(benefit_grants_router)
# /checkout-links
router.include_router(checkout_link_router)
# /payouts
router.include_router(payout_router)
# /transactions
router.include_router(transaction_router)
# /auth
router.include_router(auth_router)
# /support-cases
router.include_router(support_case_router)
# /customer-sessions
router.include_router(customer_session_router)
# /payout-accounts
router.include_router(payout_account_router)
# /files
router.include_router(files_router)
# /members
router.include_router(member_router)
# /seats
router.include_router(customer_seat_router)
# /organizations/{id}/domains
router.include_router(organization_domain_router)
# /custom-fields
router.include_router(custom_field_router)
# /organization-access-tokens
router.include_router(organization_access_token_router)
router.include_router(organization_email_router)
# /wallets
router.include_router(wallet_router)
# /event-types
router.include_router(event_type_router)
# /customers/{id}/members (nested member CRUD; defined in the member module)
router.include_router(customer_members_router)
# /integrations/plain
router.include_router(plain_router)
# /taxes
router.include_router(tax_router)
# /integrations/resend
router.include_router(resend_router)
# /merchant-migrations
router.include_router(merchant_migration_router)
# /search
router.include_router(search_router)
# /personal_access_tokens
router.include_router(pat_router)
# /cli
router.include_router(cli_router)
# /integrations/github_repository_benefit
router.include_router(github_repository_benefit_router)
# /accounts
router.include_router(accounts_router)
# /integrations/repalis
router.include_router(repalis_self_router)
# /integrations/chargeback-stop
router.include_router(chargeback_stop_router)
# /integrations/discord
router.include_router(discord_router)
# /feedbacks
router.include_router(feedback_router)
# /update-email
router.include_router(email_update_router)
# /catalogs
router.include_router(catalog_router)
# /config
router.include_router(declarative_config_router)
# /agent
router.include_router(agent_router)
# /integrations/slack
router.include_router(slack_router)
# /organizations/{id}/sso-connections
router.include_router(sso_router)
# /integrations/github
router.include_router(github_router)
# /outpost
router.include_router(outpost_router)
# /benefits/slack
router.include_router(slack_shared_channel_benefit_router)
