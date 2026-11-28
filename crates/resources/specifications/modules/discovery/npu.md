# NPU capability discovery

**ZIP-RESOURCES-DISCOVERY-NPU-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/npu.rs`

## Boundary and inputs

Use a registered local accelerator adapter to report validated device identity, backend edition and supported primitives independently from available memory or throughput. Bind capabilities to the exact device and driver revision. A disconnected adapter or incomplete inventory makes the affected measurement unknown.

## Behavior and failure handling

Publish enforceable accelerator bytes only when the same qualified adapter proves accounting and required containment for the selected workload. Unsupported metrics stay advisory even if supported operations are known. Never combine NPU and GPU memory or infer CPU fallback permission. Any compatible fallback is selected by the owning inference route and passes fresh resource admission.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-NPU-T01.** Provide an NPU with supported primitives and no qualified capacity evidence. Verify capability discovery succeeds while a hard NPU memory request fails. Supply a separate policy-authorized CPU candidate and show it is evaluated independently.
