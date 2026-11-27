# Evidence reference validation

**ZIP-AUDIT-EVIDENCE-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/evidence.rs`

## Required implementation behavior

Link only authorized immutable evidence by digest and requirement/tool version; preserve missing evidence status and avoid payload duplication.

## Acceptance

**ZIP-AUDIT-EVIDENCE-T01.** Wrong digest cannot satisfy an audit finding.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
