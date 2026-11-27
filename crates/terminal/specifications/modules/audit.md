# Execution audit intent and outcome

**ZIP-TERMINAL-AUDIT-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/audit.rs`

## Required implementation behavior

Record command schema and redacted digest, grant/lease, process status, output artifact and reconciliation state. Omit raw secrets and env values.

## Acceptance

**ZIP-TERMINAL-AUDIT-T01.** Canary strings from argv or environment never appear in audit record.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
