"""
Module  : domain.models.session
Purpose : User session entity. Tracks auth context, active project, investigation history, and preference state.
Layer   : Domain — Core Model (Framework-Independent)
"""
from dataclasses import dataclass, field
from datetime import datetime
