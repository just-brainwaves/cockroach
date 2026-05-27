"""
Module  : intelligence.agents.performance_investigator
Purpose : Correlates OTel slow spans with source code hotspots. Identifies N+1 query patterns, inefficient loops, and blocking calls in async code. Ranks findings by estimated user-facing latency impact.
Layer   : Intelligence — Specialised Agent
"""
from intelligence.agents.base_agent import BaseAgent


class PerformanceInvestigator(BaseAgent):
    name = "performance_investigator"
    description = """Correlates OTel slow spans with source code hotspots. Identifies N+1 query patte..."""

    async def run(self, context: dict) -> dict:
        ...
