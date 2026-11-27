# Assignment ID boundary

**ZIP-ASSIGNMENTS-IDENTIFIER-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/identifier.rs`

## Required implementation behavior

Wrap a validated Foundation Identifier of kind Assignment; construct from namespace UUID and reject nil or other kinds. Expose canonical wire spelling without embedded authority.

## Acceptance

**ZIP-ASSIGNMENTS-IDENTIFIER-T01.** A workspace identifier cannot be decoded as assignment ID.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
