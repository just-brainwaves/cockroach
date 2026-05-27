# Cockroach — AI-Native Production Debugger

> AI forensic investigator for production systems.
> Understands repositories, correlates runtime failures, and finds production-only bugs.

## Architecture
```
Frontend (Tauri + React)  →  FastAPI Gateway
                                    ↓
                         AI Orchestrator (LangGraph)
                                    ↓
          ┌─────────────────────────────────────────────┐
          │  Parser Engine  │  Runtime Analyzer          │
          │  Semantic Search │  Root Cause Engine        │
          └─────────────────────────────────────────────┘
                                    ↓
          ┌──────────┬──────────┬────────────┬─────────┐
          │ Postgres │  Neo4j   │  VectorDB  │  Redis  │
          └──────────┴──────────┴────────────┴─────────┘
                                    ↓
                             Workers (Celery)
