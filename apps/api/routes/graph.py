"""
Module  : apps.api.routes.graph
Purpose : Endpoints for querying the Neo4j knowledge graph.
          Returns architecture views, dependency chains, call graphs,
          and blast-radius analysis for a given symbol or file path.
Layer   : Application — HTTP Routes
Endpoints:
  GET    /graph/{pid}/architecture
  GET    /graph/{pid}/dependencies?file=...
  GET    /graph/{pid}/call-graph?symbol=...
  GET    /graph/{pid}/blast-radius?symbol=...
"""
from fastapi import APIRouter
router = APIRouter()
