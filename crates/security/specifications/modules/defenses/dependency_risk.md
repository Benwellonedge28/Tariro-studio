# Dependency policy evidence

**ZIP-SECURITY-DEFENSES-DEPENDENCY-RISK-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/dependency_risk.rs`

## Required implementation behavior

Evaluate resolved package versions, provenance, licensing, native/unsafe exposure, advisories and approved exceptions against pinned graph.

## Acceptance

**ZIP-SECURITY-DEFENSES-DEPENDENCY-RISK-T01.** An unreviewed dependency cannot qualify with a superficially matching package name.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
