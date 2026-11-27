# npm build adapter

**ZIP-COMPILATION-ADAPTERS-NPM-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/npm.rs`

## Required implementation behavior

Pin Node/npm and lockfile, authorize script execution separately as part of scoped build containment, and avoid default network fetch.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-NPM-T01.** A script cannot read secrets or modify unapproved paths.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
