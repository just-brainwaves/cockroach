# Deployment Guide

## Local Development
```bash
git clone <repo> && cd cockroach
bash scripts/setup.sh
uvicorn apps.api.main:app --reload
celery -A apps.worker.main:app worker -Q indexing,analysis,runtime
```

## Docker Compose (All-in-one)
```bash
docker compose up
```

## Production
- API: containerised FastAPI behind nginx
- Workers: separate Celery containers per queue
- Neo4j: dedicated instance (persistent volume)
- Postgres: managed RDS or self-hosted
- Redis: ElastiCache or self-hosted
