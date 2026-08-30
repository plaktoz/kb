#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "🧹 Starting Podman factory reset..."

# 1. Forcefully remove the default machine if it exists
echo "🛑 Tearing down existing machine..."
podman machine rm -f podman-machine-default || true

# 2. Run global reset to wipe stuck locks and leftover configurations
echo "🧼 Wiping residual configurations and process locks..."
podman machine reset -f

# 3. Re-initialize using the native Apple Hypervisor provider
echo "🏗️ Initializing brand new clean machine (using applehv)..."
podman machine init --provider applehv

# 4. Start up the newly created machine environment
echo "🚀 Booting fresh Podman environment..."
podman machine start

echo "✅ Podman has been successfully reset to factory defaults!"
