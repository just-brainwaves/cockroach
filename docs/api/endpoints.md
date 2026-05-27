# Cockroach API Reference

Auto-generated Swagger docs: `http://localhost:8000/docs`
ReDoc: `http://localhost:8000/redoc`

## Key Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /projects/ | Create project + trigger indexing |
| POST | /analysis/ | Start root cause investigation |
| GET | /analysis/{id}/stream | SSE stream of agent reasoning |
| POST | /runtime/ingest/crash | Ingest crash dump |
| GET | /graph/{pid}/blast-radius | Compute change blast radius |
