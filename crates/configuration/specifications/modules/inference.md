# Inference route preferences

**ZIP-CONFIGURATION-INFERENCE-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/inference.rs`

## Boundary and inputs

Build a read-only inference preference from the validated snapshot described by [schema](schema.md). Bind model and context requirements, quality floor references, route preference and approved opaque endpoint references. Distinguish explicit zero model slots, admission-derived slots and unavailable configuration. Configuration consumes verified capability observations supplied by composition. It neither opens the endpoint nor loads weights.

## Behavior and failure handling

Intersect requested format, context and precision with supported capabilities, effective policy and request requirements. Prefer an exact supported fit. Offer a smaller context only when the assignment explicitly allows it and its floor remains satisfied. Treat absent required evidence as unavailable. The Inference owner revalidates actual model and tokenizer identity, while Resources admits memory, model slots and metered demand. An unsupported local route creates no remote permission. Freeze the configuration and policy revisions used in each candidate. See [native inference](../../../../specifications/0500-inference/inference.md).

## Acceptance

**ZIP-CONFIGURATION-INFERENCE-T01.** Test unsupported model format, oversized context with and without permission to shrink, and explicit zero local slots on a capable host. Verify no endpoint traffic or model reservation originates from Configuration.
