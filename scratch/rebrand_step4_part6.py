import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return 0
    orig = content
    for pattern, repl in replacements:
        if isinstance(pattern, str):
            content = content.replace(pattern, repl)
        else:
            content = pattern.sub(repl, content)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

# 1. Integrations repalis endpoints & stripe adapter & slack schemas & dispute
replace_in_file('server/repalis/integrations/repalis/endpoints.py', [
    ('PolarWebhookUnknownTypeError', 'RepalisWebhookUnknownTypeError'),
    ('PolarWebhookVerificationError', 'RepalisWebhookVerificationError'),
])

replace_in_file('server/repalis/merchant_migration/adapters/stripe.py', [
    ("never Polar's", "never Repalis's"),
    ('Polar would discount', 'Repalis would discount'),
    ('Polar bills', 'Repalis bills'),
    ('one Polar coupon', 'one Repalis coupon'),
])

replace_in_file('server/repalis/benefit/strategies/slack_shared_channel/schemas.py', [
    ('Polar Slack integration', 'Repalis Slack integration'),
])

replace_in_file('server/repalis/cli/fixtures.py', [
    ('polar_c_', 'repalis_c_'),
    ('polar_st_', 'repalis_st_'),
])

replace_in_file('server/repalis/dispute/dispute_case.py', [
    ('The Polar team', 'The Repalis team'),
    ('Warn that Polar plans', 'Warn that Repalis plans'),
])

replace_in_file('server/scripts/linters/frontend_url.py', [
    ('polar.kit.http', 'repalis.kit.http'),
])

# 2. Tests
replace_in_file('server/tests/organization/test_service.py', [
    ('https://x.com/polar', 'https://x.com/repalis'),
    ('polar-software-inc', 'repalis-software-inc'),
])

replace_in_file('server/tests/e2e/infra/task_drain.py', [
    ('parents[2] / "polar"', 'parents[2] / "repalis"'),
    ('modules under ``polar/``', 'modules under ``repalis/``'),
    ('modules under polar/', 'modules under repalis/'),
])

replace_in_file('server/tests/scripts/test_seeds_load.py', [
    ('organization.slug == "polar"', 'organization.slug == "repalis"'),
    ('organization.slug != "polar"', 'organization.slug != "repalis"'),
    ('polar = next(', 'repalis = next('),
    ('polar.id', 'repalis.id'),
    ('polar_billing_customer_external_ids', 'repalis_billing_customer_external_ids'),
    ('polar_benefit_metadata', 'repalis_benefit_metadata'),
])

replace_in_file('server/tests/test_sentry.py', [
    ('polar_act_xxx', 'repalis_act_xxx'),
    ('polar_it_xxx', 'repalis_it_xxx'),
    ('polar_acl_xxx', 'repalis_acl_xxx'),
    ('polar_rt_xxx', 'repalis_rt_xxx'),
    ('polar_st_xxx', 'repalis_st_xxx'),
])

replace_in_file('server/tests/agent/test_endpoints.py', [
    ('polar_act_claim', 'repalis_act_claim'),
    ('polar_acl_link', 'repalis_acl_link'),
    ('polar_acl_unknown', 'repalis_acl_unknown'),
    ('polar_acl_', 'repalis_acl_'),
])

replace_in_file('server/tests/declarative_config/test_service.py', [
    ('https://example.com/polar', 'https://example.com/repalis'),
])

replace_in_file('server/tests/oauth2/endpoints/test_oauth2.py', [
    ('polar_at_', 'repalis_at_'),
    ('polar_rt_', 'repalis_rt_'),
    ('polar_rt_o_', 'repalis_rt_o_'),
])

replace_in_file('server/tests/worker/test_backoff.py', [
    ('polar-tasks-default', 'repalis-tasks-default'),
    ('polar-tasks-default-dlq', 'repalis-tasks-default-dlq'),
])

replace_in_file('server/tests/order/test_endpoints.py', [
    ('polar-orders.csv', 'repalis-orders.csv'),
    ('polar-orders-', 'repalis-orders-'),
])

replace_in_file('server/tests/refund/test_tasks.py', [
    ('POLAR-2026-00042', 'REPALIS-2026-00042'),
])

replace_in_file('server/tests/integrations/repalis/test_tasks.py', [
    ('polar-customer-123', 'repalis-customer-123'),
    ('test_plain_unlink_retried_after_polar_removal', 'test_plain_unlink_retried_after_repalis_removal'),
])

print("Server Part 6 execution complete.")
