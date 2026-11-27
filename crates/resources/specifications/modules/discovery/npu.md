# NPU capability discovery

**ZIP-RESOURCES-DISCOVERY-NPU-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/npu.rs`

## Required implementation behavior

Report supported adapter and inference primitives independently from memory estimates. Unavailable vendor driver or unsupported meter marks capacity Unknown.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-NPU-T01.** Unknown accelerator demand fails hard reservation while CPU fallback remains policy controlled.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
