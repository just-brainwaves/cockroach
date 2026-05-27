"""
Module  : shared.constants.graph_schema
Purpose : Neo4j node label and relationship type constants.
          Single definition used by all graph builders and query modules
          to prevent string-literal drift across the codebase.
Layer   : Shared — Constants
"""

# Node labels
NODE_FILE    = "File"
NODE_SYMBOL  = "Symbol"
NODE_MODULE  = "Module"
NODE_SERVICE = "Service"

# Relationship types
REL_IMPORTS    = "IMPORTS"
REL_CALLS      = "CALLS"
REL_INHERITS   = "INHERITS"
REL_IMPLEMENTS = "IMPLEMENTS"
REL_CONTAINS   = "CONTAINS"
REL_TESTS      = "TESTS"
