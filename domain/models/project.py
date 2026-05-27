"""
Module  : domain.models.project
Purpose : Project aggregate root. Represents an indexed codebase with metadata, scan history, configuration, and health status.
Layer   : Domain — Core Model (Framework-Independent)
"""
from dataclasses import dataclass, field
from datetime import datetime
