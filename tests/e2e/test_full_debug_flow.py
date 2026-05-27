"""
Tests   : tests.e2e.test_full_debug_flow
Purpose : End-to-end test of the complete Cockroach debugging workflow.
          1. Indexes a fixture repository with a known planted bug
          2. Submits a matching crash context via the API
          3. Asserts the Root Cause Engine identifies the planted issue
          4. Validates confidence score, affected file, and fix suggestion
"""
