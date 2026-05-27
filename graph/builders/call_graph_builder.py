"""
Module  : graph.builders.call_graph_builder
Purpose : Populates CALLS edges between Symbol nodes in Neo4j.
          Resolves call_mapper output to graph IDs and writes directed edges
          with line-number metadata. Enables call-chain traversal for crash analysis.
Layer   : Graph — Knowledge Graph Construction
"""
