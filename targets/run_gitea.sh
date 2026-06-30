#!/bin/bash
# Demo target: Gitea 1.17 — self-hosted Git, represents internal DevOps tooling
# Run manually before a demo. Not part of the automated workflow.
set -e

podman run -d \
  --name gitea \
  --network vulnforge-net \
  -p 8085:3000 \
  -p 2222:22 \
  --restart=unless-stopped \
  docker.io/gitea/gitea:1.17.3

echo ""
echo "[+] Gitea 1.17.3 running at http://localhost:8085"
echo "    Complete setup : http://localhost:8085  (first visit runs installer)"
echo "    Uses SQLite — no separate DB needed"
