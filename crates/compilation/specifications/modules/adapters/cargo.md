# Cargo build adapter

**ZIP-COMPILATION-ADAPTERS-CARGO-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/cargo.rs`

## Required implementation behavior

Use pinned Cargo/toolchain, explicit package/target/features and locked dependency policy. Bound process tree, build-script and network scope.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-CARGO-T01.** Lock drift or unapproved network denies build.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
