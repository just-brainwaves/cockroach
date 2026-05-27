"""
Module  : graph.queries.impact_queries
Purpose : Cypher queries for change impact analysis.
          Computes blast radius: what breaks if symbol X changes?
          Finds all direct and transitive callers, and downstream service consumers.
          Critical for risk-ranking incoming changes and crash causality tracing.
Layer   : Graph — Query Layer (High Value)
"""

BLAST_RADIUS = """
MATCH (s:Symbol {fqn: $fqn})<-[:CALLS*1..8]-(caller)
RETURN caller.fqn, caller.file_path, count(*) AS call_depth
ORDER BY call_depth DESC
"""
