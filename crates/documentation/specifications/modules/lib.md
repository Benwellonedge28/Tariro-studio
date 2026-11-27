# Documentation service facade

**ZIP-DOCUMENTATION-LIB-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/lib.rs`

## Required implementation behavior

Expose bounded read, plan, author, validate and seal contracts. Publication uses an independently authorized repository port.

## Acceptance

**ZIP-DOCUMENTATION-LIB-T01.** Constructing parser cannot trigger Git publication.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
