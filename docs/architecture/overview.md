# Cockroach — Architecture Overview

## System Layers

| Layer | Technology | Role |
|-------|-----------|------|
| Desktop | Tauri + React + TypeScript | User Interface |
| API Gateway | FastAPI | HTTP / WebSocket |
| Intelligence | LangGraph Agents | AI Reasoning |
| Indexing | tree-sitter | Repository Understanding |
| Graph | Neo4j | Relationship Intelligence |
| Runtime | OpenTelemetry | Production Signal Processing |
| Storage | Postgres + Redis + FAISS/Qdrant | Data Persistence |

## Core Data Flows

### Indexing Flow
```
Repo → Scanner → Parser → Chunker → Embedder → [FAISS + Neo4j]
```

### Debug Investigation Flow
```
Crash Context
     +
Knowledge Graph  →  LangGraph Workflow  →  Ranked Root Causes
     +                (multi-agent)
Runtime Signals
```

## Competitive Moats
1. **Graph Intelligence** — understands relationships, not just files
2. **Runtime + Source Correlation** — bridges production signals to code
3. **Root Cause Ranking** — confidence-scored hypotheses, not raw logs
4. **Production-Only Failure Detection** — race conditions, retry loops, cache bugs
5. **Historical Debugging Memory** — learns from past investigations
