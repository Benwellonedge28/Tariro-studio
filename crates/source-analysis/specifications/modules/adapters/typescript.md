# TypeScript source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-TYPESCRIPT-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/typescript.rs`

## Required implementation behavior

Bind compiler settings and qualified type information to pinned inputs. JS emit is not source identity; unresolved types stay unknown.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-TYPESCRIPT-T01.** Type results from stale settings are discarded.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
