"""
Module  : infrastructure.neo4j.client
Purpose : Async Neo4j driver wrapper.
          Manages driver lifecycle, session pooling, query execution with
          parameter binding, and automatic retry on transient Neo4j errors.
Layer   : Infrastructure — Graph Database
"""
from neo4j import AsyncGraphDatabase
