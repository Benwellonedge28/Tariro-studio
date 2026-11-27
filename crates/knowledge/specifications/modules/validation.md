# Graph invariants and qualification

**ZIP-KNOWLEDGE-VALIDATION-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/validation.rs`

## Required implementation behavior

Check endpoint existence/type, scope, version, provenance and allowed relation semantics. Preserve rejected observations separately.

## Acceptance

**ZIP-KNOWLEDGE-VALIDATION-T01.** Orphan edge blocks activation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
