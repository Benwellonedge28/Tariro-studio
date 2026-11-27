# Go build adapter

**ZIP-COMPILATION-ADAPTERS-GO-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/go.rs`

## Required implementation behavior

Pin Go, target and module contents, configure approved module resolution and keep native toolchain separately qualified.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-GO-T01.** Module fetch cannot occur under local-only authority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
