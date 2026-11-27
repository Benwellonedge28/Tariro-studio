# Scoped local artifact adapter

**ZIP-RESEARCH-PROVIDERS-LOCAL-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/providers/local.rs`

## Required implementation behavior

Read approved rooted files under finite bounds; hash and record provenance. No external fetch on missing data.

## Acceptance

**ZIP-RESEARCH-PROVIDERS-LOCAL-T01.** Unsafe path or unapproved artifact refused before reading.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
