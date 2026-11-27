# Provider capability negotiation

**ZIP-INTELLIGENCE-CAPABILITY-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/capability.rs`

## Required implementation behavior

Compare required version, modality, context, tools/structured response and deployment locality; reject incompatible or unknown claims.

## Acceptance

**ZIP-INTELLIGENCE-CAPABILITY-T01.** A text-only adapter cannot satisfy an image request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
