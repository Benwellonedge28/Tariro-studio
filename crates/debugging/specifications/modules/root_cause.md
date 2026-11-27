# Evidence-bound cause assessment

**ZIP-DEBUGGING-ROOT-CAUSE-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/root_cause.rs`

## Required implementation behavior

Rank candidate causes by observed reproducibility and falsifying tests; retain alternative hypotheses and confidence provenance.

## Acceptance

**ZIP-DEBUGGING-ROOT-CAUSE-T01.** A successful repair suggestion alone does not prove root cause.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
