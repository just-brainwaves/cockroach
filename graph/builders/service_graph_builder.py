"""
Module  : graph.builders.service_graph_builder
Purpose : Infers service boundaries and builds the SERVICE_CALLS topology.
          Detects API client usage, message queue producers/consumers, and gRPC stubs
          to create a high-level service dependency graph alongside the file-level graph.
Layer   : Graph — Knowledge Graph Construction
"""
