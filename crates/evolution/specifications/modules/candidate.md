# Immutable candidate snapshot

**ZIP-EVOLUTION-CANDIDATE-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/candidate.rs`

## Required implementation behavior

Pin patch, source tree, diff scope and required artifacts, separating generated candidate from approved activation target.

## Acceptance

**ZIP-EVOLUTION-CANDIDATE-T01.** Altered diff invalidates previously collected evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
