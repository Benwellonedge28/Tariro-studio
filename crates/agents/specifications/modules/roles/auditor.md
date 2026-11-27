# Audit reader role

**ZIP-AGENTS-ROLES-AUDITOR-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/auditor.rs`

## Required implementation behavior

Inspect scoped redacted chain and effect receipts without write authority; report gaps and provenance.

## Acceptance

**ZIP-AGENTS-ROLES-AUDITOR-T01.** Missing record cannot be passed over as compliant.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
