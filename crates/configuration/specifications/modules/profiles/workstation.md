# Workstation profile rules

**ZIP-CONFIGURATION-PROFILES-WORKSTATION-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/workstation.rs`

## Boundary and inputs

Load the [workstation manifest](../../../../../configurations/profiles/workstation.toml) and resolve local best-fit preferences. Derive finite model and agent slot upper bounds against qualified capacity and current policy without aggregating device memory. Model/device compatibility and stable per-device identities come from the Inference and Resources owners.

## Behavior and failure handling

For an unsharded request evaluate candidate devices individually with complete per-device demand and host headroom. For a sharded request require a qualified adapter and an approved exact shard plan specifying per-device demand and inter-device requirements. Admission still checks the complete demand vector atomically. A local placement failure does not enable offloading.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-WORKSTATION-T01.** Offer two qualified devices with enough summed memory and insufficient individual memory. Deny unsharded placement. Under a separately approved sharding plan, verify each device's bound and that the selected combination needs explicit support and atomic admission.
