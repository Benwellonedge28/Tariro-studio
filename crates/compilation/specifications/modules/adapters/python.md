# Python build adapter

**ZIP-COMPILATION-ADAPTERS-PYTHON-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/python.rs`

## Required implementation behavior

Pin interpreter, build backend and locked deps, authorize build hooks under containment, and verify output package digests.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-PYTHON-T01.** Missing backend yields failure without installing globally.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
