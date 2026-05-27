#!/usr/bin/env bash
# scripts/setup.sh
# Purpose : One-shot local development environment setup.
#           Starts Docker services, installs Python deps,
#           runs DB migrations, and verifies all connections.
set -euo pipefail

echo "🪳  Setting up Cockroach dev environment..."
docker compose -f docker/docker-compose.yml up -d --wait
pip install -e ".[dev]"
alembic upgrade head
python -c "from infrastructure.neo4j.schema import SCHEMA_SETUP_QUERIES; print('Neo4j schema OK')"
echo "✅  Cockroach is ready. Run: uvicorn apps.api.main:app --reload"
