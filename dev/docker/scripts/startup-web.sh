#!/bin/bash
# Startup script for Repalis Web frontend in development mode
# This script handles dependency installation and starts Next.js with Turbopack.

set -euo pipefail

export DOCKER=1

cd /app/clients

echo "=== Repalis Web Frontend Startup ==="

# Always run pnpm install to ensure dependencies are installed
# pnpm is smart enough to skip if nothing changed
echo "Installing/verifying Node.js dependencies..."
pnpm --config.ignore-scripts=true --filter web... install

# Build packages only if dist doesn't exist (they're built on host and mounted)
# This avoids OOM issues from DTS generation in container
echo "Checking workspace packages..."

if [[ ! -d "packages/client/dist" ]]; then
    echo "Building @repalis/client..."
    pnpm --filter @repalis/client build
else
    echo "@repalis/client already built"
fi

if [[ ! -d "packages/ui/dist" ]]; then
    echo "Building @repalis/ui..."
    pnpm --filter @repalis/ui build
else
    echo "@repalis/ui already built"
fi

if [[ ! -d "packages/orbit/dist" ]]; then
    echo "Building @repalis/orbit..."
    pnpm --filter @repalis/orbit build
else
    echo "@repalis/orbit already built"
fi

if [[ ! -d "packages/currency/dist" ]]; then
    echo "Building @repalis/currency..."
    pnpm --filter @repalis/currency build
else
    echo "@repalis/currency already built"
fi

if [[ ! -d "packages/i18n/dist" ]]; then
    echo "Building @repalis/i18n..."
    pnpm --filter @repalis/i18n build
else
    echo "@repalis/i18n already built"
fi

if [[ ! -d "packages/checkout/dist" ]]; then
    echo "Building @repalis/checkout..."
    pnpm --filter @repalis/checkout build
else
    echo "@repalis/checkout already built"
fi

# Start the requested mode
case "${1:-dev}" in
    dev)
        echo "Starting Next.js development server..."
        echo "Web will be available at http://localhost:3000"
        echo ""
        echo "NOTE: Next.js with Turbopack requires significant memory (~6GB)."
        echo "If the container crashes, increase Docker Desktop memory to 12GB+."
        echo ""
        cd apps/web
        pnpm copy-aup
        exec pnpm exec next dev --port 3000 --hostname 0.0.0.0
        ;;
    build)
        echo "Building production bundle..."
        exec pnpm build
        ;;
    shell)
        echo "Starting shell..."
        exec /bin/bash
        ;;
    *)
        echo "Unknown mode: $1"
        echo "Available modes: dev, build, shell"
        exit 1
        ;;
esac
