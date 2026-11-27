# Behavior-preserving extraction

**ZIP-ENGINEERING-REFACTORING-EXTRACTION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/refactoring/extraction.rs`

## Required implementation behavior

Identify selected statements and capture dependencies/control flow, preserve order/ownership, stage candidate with equivalence tests.

## Acceptance

**ZIP-ENGINEERING-REFACTORING-EXTRACTION-T01.** Non-local control escape cannot be silently dropped.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
