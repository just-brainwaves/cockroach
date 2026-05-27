"""
Module  : graph.queries.dependency_queries
Purpose : Cypher query library for dependency traversal.
          Provides: all-dependencies-of-file, transitive-closure,
          cycle detection, and critical-path identification.
Layer   : Graph — Query Layer
"""

FIND_DEPENDENCIES = """
MATCH (f:File {path: $path})-[:IMPORTS*1..10]->(dep:File)
RETURN dep.path AS path, dep.language AS language
ORDER BY dep.path
"""

DETECT_IMPORT_CYCLES = """
MATCH path = (f:File)-[:IMPORTS*2..]->(f)
RETURN [n IN nodes(path) | n.path] AS cycle
LIMIT 20
"""
