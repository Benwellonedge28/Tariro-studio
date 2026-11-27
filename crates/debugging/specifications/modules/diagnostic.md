# Qualified diagnosis input

**ZIP-DEBUGGING-DIAGNOSTIC-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/diagnostic.rs`

## Required implementation behavior

Normalize error/trace code, version, source spans and provenance, redact logs before model-visible use.

## Acceptance

**ZIP-DEBUGGING-DIAGNOSTIC-T01.** Synthetic secret is absent from normalized diagnostic.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
