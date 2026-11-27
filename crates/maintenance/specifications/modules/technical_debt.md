# Evidence-linked maintenance findings

**ZIP-MAINTENANCE-TECHNICAL-DEBT-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/technical_debt.rs`

## Required implementation behavior

Record observed source, severity rationale, scope and candidate remediation. Findings do not authorize edits.

## Acceptance

**ZIP-MAINTENANCE-TECHNICAL-DEBT-T01.** Heuristic-only signal stays advisory.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
