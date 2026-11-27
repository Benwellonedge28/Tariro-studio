# Acceptance requirements binding

**ZIP-ASSIGNMENTS-REQUIREMENTS-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/requirements.rs`

## Required implementation behavior

Normalize stable requirement IDs, attach exact gate refs and validate uniqueness. Plan binds immutable set; changing mandatory requirements produces a new revision and approval when scope expands.

## Acceptance

**ZIP-ASSIGNMENTS-REQUIREMENTS-T01.** Missing or duplicate gate and mismatched plan digest block acceptance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
