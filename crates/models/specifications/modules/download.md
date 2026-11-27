# Resumable admitted model download

**ZIP-MODELS-DOWNLOAD-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/download.rs`

## Required implementation behavior

Authorize origin and byte budget, persist expected digest/length and validator, stage private partial bytes. Revalidate range and ETag before resume; verify before promotion.

## Acceptance

**ZIP-MODELS-DOWNLOAD-T01.** Changed ETag invalidates partial file and never reaches Ready without full verification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
