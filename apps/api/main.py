"""
Module  : apps.api.main
Purpose : FastAPI application factory and entry point.
          Registers all routers, configures CORS, mounts middleware,
          and manages lifespan context (DB pool open/close, Neo4j driver, Redis).
Layer   : Application — HTTP Gateway
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from apps.api.routes import projects, analysis, runtime, reports, graph
from apps.api.middleware.logging import LoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: init DB pools, Neo4j driver, Redis connection
    yield
    # shutdown: close all connections cleanly


app = FastAPI(title="Cockroach API", version="0.1.0", lifespan=lifespan)
app.add_middleware(LoggingMiddleware)
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
app.include_router(runtime.router,  prefix="/runtime",  tags=["runtime"])
app.include_router(reports.router,  prefix="/reports",  tags=["reports"])
app.include_router(graph.router,    prefix="/graph",    tags=["graph"])
