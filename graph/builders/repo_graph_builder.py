"""
Module  : graph.builders.repo_graph_builder
Purpose : Constructs the repository knowledge graph in Neo4j from indexing output.
          Creates labelled nodes: File, Symbol, Module, Service.
          Creates typed edges: IMPORTS, CALLS, INHERITS, IMPLEMENTS, CONTAINS.
          This graph is the "brain" — the primary source of architectural intelligence.
Layer   : Graph — Knowledge Graph Construction
"""
