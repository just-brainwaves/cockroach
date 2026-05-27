"""
Module  : intelligence.agents.crash_investigator
Purpose : Receives crash dump / stack trace, correlates frames with the knowledge graph, traces causality backwards through call chains, and ranks probable root causes with commit-level attribution.
Layer   : Intelligence — Specialised Agent
"""
from intelligence.agents.base_agent import BaseAgent


class CrashInvestigator(BaseAgent):
    name = "crash_investigator"
    description = """Receives crash dump / stack trace, correlates frames with the knowledge graph, t..."""

    async def run(self, context: dict) -> dict:
        ...
