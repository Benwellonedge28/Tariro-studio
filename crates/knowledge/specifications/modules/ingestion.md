# Idempotent scoped staging

**ZIP-KNOWLEDGE-INGESTION-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/ingestion.rs`

## Required implementation behavior

Authorize source, normalize candidates, validate schema/provenance, dedupe by stable key and stage a bounded update.

## Acceptance

**ZIP-KNOWLEDGE-INGESTION-T01.** Repeated identical input cannot create duplicate edge.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
