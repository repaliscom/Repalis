import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
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

tf_replacements = [
    # Terraform Cloud
    ('organization = "polar-sh"', 'organization = "repalis"'),
    ('organization = "polarsh"', 'organization = "repalis"'),
    ('app.terraform.io/app/polar-sh/workspaces/polar', 'app.terraform.io/app/repalis/workspaces/repalis'),
    ('ids["polar"]', 'ids["repalis"]'),
    ('workspace = "polar"', 'workspace = "repalis"'),
    ('project   = "Polar"', 'project   = "Repalis"'),
    ('project = "Polar"', 'project = "Repalis"'),
    
    # Render project
    ('resource "render_project" "polar"', 'resource "render_project" "repalis"'),
    ('render_project.polar', 'render_project.repalis'),
    ('name = "Polar"', 'name = "Repalis"'),
    
    # S3 Buckets & Resources
    ('polar-test-files', 'repalis-test-files'),
    ('polar-test-public-files', 'repalis-test-public-files'),
    ('polar-test-customer-invoices', 'repalis-test-customer-invoices'),
    ('polar-test-customer-receipts', 'repalis-test-customer-receipts'),
    ('polar-test-payout-invoices', 'repalis-test-payout-invoices'),
    ('polar-test-logs', 'repalis-test-logs'),
    ('polar-test-diagnostics', 'repalis-test-diagnostics'),
    ('polar-test-tasks', 'repalis-test-tasks'),
    ('polar-test-lambda-worker', 'repalis-test-lambda-worker'),
    ('polar-test-worker', 'repalis-test-worker'),
    ('polar-test-s3-access', 'repalis-test-s3-access'),
    ('polar-test-grafana-cloudwatch', 'repalis-test-grafana-cloudwatch'),
    
    ('polar-sandbox-files', 'repalis-sandbox-files'),
    ('polar-public-sandbox-files', 'repalis-public-sandbox-files'),
    ('polar-sandbox-customer-invoices', 'repalis-sandbox-customer-invoices'),
    ('polar-sandbox-customer-receipts', 'repalis-sandbox-customer-receipts'),
    ('polar-sandbox-payout-invoices', 'repalis-sandbox-payout-invoices'),
    ('polar-sandbox-logs', 'repalis-sandbox-logs'),
    ('polar-sandbox-diagnostics', 'repalis-sandbox-diagnostics'),
    ('polar-sandbox-tasks', 'repalis-sandbox-tasks'),
    ('polar-sandbox-lambda-worker', 'repalis-sandbox-lambda-worker'),
    ('polar-sandbox-worker', 'repalis-sandbox-worker'),
    ('polar-sandbox-s3-access', 'repalis-sandbox-s3-access'),
    ('polar-sandbox-grafana-cloudwatch', 'repalis-sandbox-grafana-cloudwatch'),
    ('polar-sandbox-image-resizer', 'repalis-sandbox-image-resizer'),
    ('polar-sandbox-cdn', 'repalis-sandbox-cdn'),
    
    ('polar-production-files', 'repalis-production-files'),
    ('polar-public-files', 'repalis-public-files'),
    ('polar-customer-invoices', 'repalis-customer-invoices'),
    ('polar-customer-receipts', 'repalis-customer-receipts'),
    ('polar-payout-invoices', 'repalis-payout-invoices'),
    ('polar-production-logs', 'repalis-production-logs'),
    ('polar-production-diagnostics', 'repalis-production-diagnostics'),
    ('polar-production-tasks', 'repalis-production-tasks'),
    ('polar-production-lambda-worker', 'repalis-production-lambda-worker'),
    ('polar-production-worker', 'repalis-production-worker'),
    ('polar-production-s3-access', 'repalis-production-s3-access'),
    ('polar-production-grafana-cloudwatch', 'repalis-production-grafana-cloudwatch'),
    ('polar-image-resizer', 'repalis-image-resizer'),
    ('polar-cdn', 'repalis-cdn'),
    ('polar-lambda-artifacts', 'repalis-lambda-artifacts'),
    ('polar-management-grafana-cloudwatch', 'repalis-management-grafana-cloudwatch'),
    ('polar-sh-backups', 'repalis-backups'),
    ('polar-backups-replication', 'repalis-backups-replication'),
    
    ('polar_sandbox_session', 'repalis_sandbox_session'),
    ('polar_test_session', 'repalis_test_session'),
    
    # Variables
    ('polar_self_config', 'repalis_self_config'),
    ('polar_self', 'repalis_self'),
    ('polar-self-', 'repalis-self-'),
    ('polar-self', 'repalis-self'),
    ('var.polar_access_token', 'var.repalis_access_token'),
    ('var.polar_webhook_secret', 'var.repalis_webhook_secret'),
    ('var.polar_organization_id', 'var.repalis_organization_id'),
    ('var.polar_scale_product_id', 'var.repalis_scale_product_id'),
    ('variable "polar_access_token"', 'variable "repalis_access_token"'),
    ('variable "polar_webhook_secret"', 'variable "repalis_webhook_secret"'),
    ('variable "polar_organization_id"', 'variable "repalis_organization_id"'),
    ('variable "polar_scale_product_id"', 'variable "repalis_scale_product_id"'),
    ('variable "polar_self_config"', 'variable "repalis_self_config"'),
    ('polar_access_token_', 'repalis_access_token_'),
    ('polar_webhook_secret_', 'repalis_webhook_secret_'),
    ('polar_organization_id_', 'repalis_organization_id_'),
    ('polar_scale_product_id_', 'repalis_scale_product_id_'),
    ('polar_checkout_embed_script_allowed_origins', 'repalis_checkout_embed_script_allowed_origins'),
    
    # Generic names & descriptions
    ('Polar webhook secret', 'Repalis webhook secret'),
    ('Polar organization ID', 'Repalis organization ID'),
    ('Polar Scale-tier product ID', 'Repalis Scale-tier product ID'),
    ('email_from_name                      = "Polar"', 'email_from_name                      = "Repalis"'),
    ('email_from_name                                  = "[SANDBOX] Polar"', 'email_from_name                                  = "[SANDBOX] Repalis"'),
    ('email_from_name                      = "[TEST] Polar"', 'email_from_name                      = "[TEST] Repalis"'),
    ('Polar permission boundary', 'Repalis permission boundary'),
    ('Polar management account', 'Repalis management account'),
    ('Polar Infrastructure as Code', 'Repalis Infrastructure as Code'),
    ("Polar's AWS Organizations", "Repalis's AWS Organizations"),
    ('Management account: polar', 'Management account: repalis'),
    ('PolarFinance', 'RepalisFinance'),
    ('github_repo     = "polar"', 'github_repo     = "repalis"'),
    ('github_repo = "polar"', 'github_repo = "repalis"'),
    ('https://github.com/apps/polar-sh/', 'https://github.com/apps/repalis/'),
    ('linear.app/polarsh', 'linear.app/repalis'),
    ('linear.app/polar', 'linear.app/repalis'),
    ('polar_handbook_redirects', 'repalis_handbook_redirects'),
    ('Polar handbook redirects', 'Repalis handbook redirects'),
    ('Polar handbook', 'Repalis handbook'),
    ('polar-for-polar', 'repalis-for-repalis'),
    ('in-polar-', 'in-repalis-'),
    ('to-polar-', 'to-repalis-'),
    ('at-polar-', 'at-repalis-'),
    ('polar-cycle-', 'repalis-cycle-'),
    ('polar-shcheckout-', 'repalis-checkout-'),
    ('name     = "polar"', 'name     = "repalis"'),
    ('name     = "polar-sandbox"', 'name     = "repalis-sandbox"'),
    ('name     = "polar-test"', 'name     = "repalis-test"'),
    ('value = "polar-sh"', 'value = "repalis"'),
    ('value     = "polar-sh"', 'value     = "repalis"'),
    ('SENTRY_ORG", value = "polar-sh"', 'SENTRY_ORG", value = "repalis"'),
]

modified_count = 0
for root, _, files in os.walk('terraform'):
    for f in files:
        p = os.path.join(root, f)
        if replace_in_file(p, tf_replacements):
            modified_count += 1

print(f"Modified {modified_count} files in terraform/")
