"""
Module  : apps.api.routes.reports
Purpose : Endpoints for generating, listing, and exporting debug reports.
          Builds structured reports from completed analysis sessions
          in markdown, JSON, or PDF format.
Layer   : Application — HTTP Routes
Endpoints:
  POST   /reports/generate       — Generate report from analysis session
  GET    /reports/{id}           — Retrieve report
  GET    /reports/{id}/download  — Download as file
"""
from fastapi import APIRouter
router = APIRouter()
