# System boundaries and data flows

**ZIP-ENGINEERING-ARCHITECTURE-SYSTEM-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/system.rs`

## Required implementation behavior

Define layers, trust boundaries, permitted edges and owned data. Bind statements to pinned specs and qualified sources.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-SYSTEM-T01.** Undeclared cross-layer dependency blocks review.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
