"""
Module  : apps.api.routes.projects
Purpose : REST endpoints for project lifecycle management.
          Handles create / read / list / delete for Cockroach projects
          and triggers the async repository indexing job on creation.
Layer   : Application — HTTP Routes
Endpoints:
  POST   /projects/              — Create project, enqueue indexing job
  GET    /projects/              — List user projects
  GET    /projects/{id}          — Get project detail + index status
  DELETE /projects/{id}          — Remove project and all indexed data
  POST   /projects/{id}/scan     — Re-trigger full re-index
"""
from fastapi import APIRouter
router = APIRouter()
