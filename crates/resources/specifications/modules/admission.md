# Enforceable demand gate

**ZIP-RESOURCES-ADMISSION-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/admission.rs`

## Required implementation behavior

reserve(request: AdmissionRequest, revision: CapacityRevision) -> Result<ResourceLease, AdmissionError>. Verify demand, actor scope, policy and coordinate enforceability first. Delegate atomic vector accounting to allocator.

## Acceptance

**ZIP-RESOURCES-ADMISSION-T01.** Missing mandatory GPU enforceability denies before spawn; admitted zero and unknown stay distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
