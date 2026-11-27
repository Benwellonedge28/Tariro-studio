# Cancellation-to-supervisor bridge

**ZIP-TERMINAL-CANCELLATION-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/cancellation.rs`

## Required implementation behavior

Stop input and new effects, request cooperative exit, enforce configured grace and reconcile process tree. Preserve committed receipts and report unknowns.

## Acceptance

**ZIP-TERMINAL-CANCELLATION-T01.** Cancel concurrent with exit returns exactly one terminal receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
