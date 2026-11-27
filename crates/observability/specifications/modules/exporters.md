# Opt-in exporter adapters

**ZIP-OBSERVABILITY-EXPORTERS-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/exporters.rs`

## Required implementation behavior

Validate destination, classification, consent and queue budget before emitting. Disable/reroute only under current policy and no implicit fallback.

## Acceptance

**ZIP-OBSERVABILITY-EXPORTERS-T01.** Disabled external exporter sends zero packets.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
