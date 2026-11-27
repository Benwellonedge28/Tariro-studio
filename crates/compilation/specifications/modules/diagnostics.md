# Bounded normalized diagnostics

**ZIP-COMPILATION-DIAGNOSTICS-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/diagnostics.rs`

## Required implementation behavior

Parse qualified tool output into code, severity and revision-bound spans. Preserve raw redacted receipt and report truncated diagnostics.

## Acceptance

**ZIP-COMPILATION-DIAGNOSTICS-T01.** Truncated output cannot be treated as complete diagnostics.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
