"""
Module  : services.project_service.schemas
Purpose : Pydantic request/response schemas for project_service.
          Defines the data contract between the HTTP layer and business logic,
          decoupling API shape from domain model implementation.
Layer   : Services — Data Contracts
"""
from pydantic import BaseModel
