"""
Module  : indexing.parsers.registry
Purpose : Parser registry — maps language IDs to parser class instances.
          Central dispatch point: repo_scanner asks the registry for the
          right parser for each file extension, keeping scanner/parser decoupled.
Layer   : Indexing — AST Parsing
"""
