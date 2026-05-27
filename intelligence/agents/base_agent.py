"""
Module  : intelligence.agents.base_agent
Purpose : Abstract base class for all Cockroach AI agents.
          Defines the standard interface: context injection, LangGraph node
          integration, structured output contracts (typed FindingSet),
          and retry / fallback behaviour on model errors.
Layer   : Intelligence — Agent Framework
"""
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Inherit to build a specialised Cockroach diagnostic agent."""

    name: str = "base"
    description: str = ""

    @abstractmethod
    async def run(self, context: dict) -> dict:
        """Execute the agent with given context and return structured findings."""
        ...

    async def with_retry(self, context: dict, max_retries: int = 3) -> dict:
        """Wraps run() with exponential-backoff retry on transient model errors."""
        ...
