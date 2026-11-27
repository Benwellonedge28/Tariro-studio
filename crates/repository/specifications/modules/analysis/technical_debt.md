# Qualified findings

**ZIP-REPOSITORY-ANALYSIS-TECHNICAL-DEBT-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/analysis/technical_debt.rs`

## Required implementation behavior

Emit stable finding ID, classified risk, evidence refs and uncertainty. Findings are proposals; no automatic remediation or security claim.

## Acceptance

**ZIP-REPOSITORY-ANALYSIS-TECHNICAL-DEBT-T01.** Heuristic-only candidate appears as unconfirmed, not as verified issue.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
