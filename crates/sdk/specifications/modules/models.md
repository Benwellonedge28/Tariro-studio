# Verified model client

**ZIP-SDK-MODELS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/models.rs`

## Required implementation behavior

Request scoped registry/availability info and admitted actions under qualified version. Treat unknown readiness separately.

## Acceptance

**ZIP-SDK-MODELS-T01.** Missing model metadata never triggers implicit download.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
