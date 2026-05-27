"""
Module  : graph.relationship_engine.edge_classifier
Purpose : Classifies relationship strength and coupling type.
          Distinguishes tight coupling (data-flow) from loose coupling (events),
          internal vs external edges, and stable vs volatile dependency edges.
          Edge weights inform the Root Cause Engine's path scoring.
Layer   : Graph — Relationship Intelligence
"""
