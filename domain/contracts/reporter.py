"""
Module  : domain.contracts.reporter
Purpose : Abstract contract for report generators. Allows new output formats (PDF, Slack, Jira) without touching the report service.
Layer   : Domain — Interface Contract
"""
from abc import ABC, abstractmethod
