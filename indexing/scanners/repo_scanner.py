"""
Module  : indexing.scanners.repo_scanner
Purpose : Top-level repository scanner. Walks the directory tree, identifies
          source files by extension, respects .gitignore rules, and dispatches
          each file to the parser registry based on detected language.
Layer   : Indexing — Repository Intelligence
"""
