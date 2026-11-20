import os

def replace_in_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    for t, r in replacements:
        c = c.replace(t, r)
    if orig != c:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {path}")

# config.py
replace_in_file('server/repalis/config.py', [
    ('STRIPE_STATEMENT_DESCRIPTOR: str = "POLAR"', 'STRIPE_STATEMENT_DESCRIPTOR: str = "REPALIS"'),
    ('INVOICES_NAME: str = "Polar Software, Inc."', 'INVOICES_NAME: str = "Repalis Software, Inc."'),
    ('AWS_ACCESS_KEY_ID: str = "polar-development"', 'AWS_ACCESS_KEY_ID: str = "repalis-development"'),
    ('WORKER_SQS_QUEUE_PREFIX: str = "polar-tasks"', 'WORKER_SQS_QUEUE_PREFIX: str = "repalis-tasks"'),
    ('S3_FILES_BUCKET_NAME: str = "polar-s3"', 'S3_FILES_BUCKET_NAME: str = "repalis-s3"'),
    ('S3_FILES_PUBLIC_BUCKET_NAME: str = "polar-s3-public"', 'S3_FILES_PUBLIC_BUCKET_NAME: str = "repalis-s3-public"'),
    ('S3_CUSTOMER_INVOICES_BUCKET_NAME: str = "polar-customer-invoices"', 'S3_CUSTOMER_INVOICES_BUCKET_NAME: str = "repalis-customer-invoices"'),
    ('S3_CUSTOMER_RECEIPTS_BUCKET_NAME: str = "polar-customer-receipts"', 'S3_CUSTOMER_RECEIPTS_BUCKET_NAME: str = "repalis-customer-receipts"'),
    ('S3_PAYOUT_INVOICES_BUCKET_NAME: str = "polar-payout-invoices"', 'S3_PAYOUT_INVOICES_BUCKET_NAME: str = "repalis-payout-invoices"'),
    ('MINIO_USER: str = "polar"', 'MINIO_USER: str = "repalis"'),
    ('POSTGRES_USER: str = "polar"', 'POSTGRES_USER: str = "repalis"'),
    ('POSTGRES_PWD: str = "polar"', 'POSTGRES_PWD: str = "repalis"'),
    ('POSTGRES_DATABASE: str = "polar"', 'POSTGRES_DATABASE: str = "repalis"'),
    ('# Polar frontend CORS configuration', '# Repalis frontend CORS configuration'),
    ("# Polar's usage of Polar", "# Repalis's usage of Repalis"),
])

# logging.py
replace_in_file('server/repalis/logging.py', [
    ('"polar": {', '"repalis": {'),
    ('"formatter": "polar"', '"formatter": "repalis"'),
])

# middlewares.py
replace_in_file('server/repalis/middlewares.py', [
    ('"x-polar-client-version"', '"x-repalis-client-version"'),
    ('"x-polar-client-runtime"', '"x-repalis-client-runtime"'),
    ('"x-polar-client-update"', '"x-repalis-client-update"'),
    ('"X-Polar-Deprecation-Notice"', '"X-Repalis-Deprecation-Notice"'),
    ('"X-Polar-Sandbox"', '"X-Repalis-Sandbox"'),
])

# openapi.py
replace_in_file('server/repalis/openapi.py', [
    ('"x-polar-cli-preview"', '"x-repalis-cli-preview"'),
])

# app.py
replace_in_file('server/repalis/app.py', [
    ('# Polar frontend CORS configuration', '# Repalis frontend CORS configuration'),
])
