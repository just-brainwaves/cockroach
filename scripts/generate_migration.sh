#!/usr/bin/env bash
# scripts/generate_migration.sh
# Purpose : Wrapper for Alembic auto-migration generation.
#           Usage: bash scripts/generate_migration.sh "add findings table"
set -euo pipefail
MESSAGE=${1:-"auto migration"}
alembic revision --autogenerate -m "$MESSAGE"
echo "Migration generated. Review before committing."
