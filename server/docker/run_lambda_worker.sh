#!/bin/sh
set -eu

if [ -n "${REPALIS_WORKER_SECRETS_ARN:-}" ]; then
  secret_exports="$(python /var/runtime/export-secrets.py)"
  eval "$secret_exports"
fi

exec /lambda-entrypoint.sh "$@"
