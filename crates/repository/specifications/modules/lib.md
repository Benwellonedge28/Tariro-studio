# Repository service facade

**ZIP-REPOSITORY-LIB-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/lib.rs`

## Required implementation behavior

Expose snapshots, instructions, staged diffs and qualified provider ports. Compose filesystem, terminal and governance at startup. No hidden remote access.

## Acceptance

**ZIP-REPOSITORY-LIB-T01.** Link facade without network or installed Git and report unsupported adapter when invoked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
