# Cross-artifact architecture checks

**ZIP-ENGINEERING-ARCHITECTURE-VALIDATION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/validation.rs`

## Required implementation behavior

Compare design, dependency graph, contracts and actual metadata where available. Separate verified and unresolved claims.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-VALIDATION-T01.** Missing metadata cannot be treated as established compatibility.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
