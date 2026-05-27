"""
Module  : intelligence.agents.security_reviewer
Purpose : Scans code graph for injection risks, insecure deserialisation, hardcoded secrets, auth bypass patterns, and CVE-adjacent code signatures. Cross-references runtime traces for active exploitation signals.
Layer   : Intelligence — Specialised Agent
"""
from intelligence.agents.base_agent import BaseAgent


class SecurityReviewer(BaseAgent):
    name = "security_reviewer"
    description = """Scans code graph for injection risks, insecure deserialisation, hardcoded secret..."""

    async def run(self, context: dict) -> dict:
        ...
