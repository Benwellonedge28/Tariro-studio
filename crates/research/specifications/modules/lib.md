# Scoped research facade

**ZIP-RESEARCH-LIB-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/lib.rs`

## Required implementation behavior

Expose question, plan, source and evidence ports. Work stays offline by default and import starts no searches.

## Acceptance

**ZIP-RESEARCH-LIB-T01.** Local library queries work with network clients disabled.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
