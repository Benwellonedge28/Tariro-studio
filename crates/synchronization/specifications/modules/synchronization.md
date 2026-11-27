# Staged synchronization workflow

**ZIP-SYNCHRONIZATION-SYNCHRONIZATION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/synchronization.rs`

## Required implementation behavior

Plan from approved manifest and cursor, stage bounded changes, verify all artifacts/conflicts, commit exact revision then acknowledge.

## Acceptance

**ZIP-SYNCHRONIZATION-SYNCHRONIZATION-T01.** Acknowledgment loss causes exact duplicate detection rather than repeated mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
