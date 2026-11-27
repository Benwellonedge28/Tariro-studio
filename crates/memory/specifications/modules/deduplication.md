# Scope-aware duplicate detection

**ZIP-MEMORY-DEDUPLICATION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/deduplication.rs`

## Required implementation behavior

Dedupe exact digest only within same authorization/retention context. Confirm collision using content identity and preserve required links.

## Acceptance

**ZIP-MEMORY-DEDUPLICATION-T01.** Same text under different scope remains distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
