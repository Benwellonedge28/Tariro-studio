# Versioned architectural decision record

**ZIP-ENGINEERING-ARCHITECTURE-DECISIONS-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/decisions.rs`

## Required implementation behavior

Capture issue, reviewed alternatives, decision, authority, impact and superseded revisions. Preserve old decision provenance.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-DECISIONS-T01.** Draft decision cannot silently override current governing choice.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
