"""
Module  : apps.api.routes.analysis
Purpose : Endpoints for triggering and retrieving AI analysis results.
          Accepts project ID + optional crash / error context, dispatches
          to the Root Cause Engine via Celery, and streams findings via SSE.
Layer   : Application — HTTP Routes
Endpoints:
  POST   /analysis/              — Start new analysis session
  GET    /analysis/{id}          — Poll analysis status + results
  GET    /analysis/{id}/stream   — SSE stream of agent reasoning steps
  GET    /analysis/{id}/report   — Download structured report
"""
from fastapi import APIRouter
router = APIRouter()
