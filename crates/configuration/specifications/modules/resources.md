# Resource budget view

**ZIP-CONFIGURATION-RESOURCES-001 · v1.1 candidate · Owner** Configuration maintainers

**Planned source** `crates/configuration/src/resources.rs`

Configuration publishes an immutable revision of validated resource settings. Read from the resolved configuration provided by [validation](validation.md). Include the catalog key, typed normalized value with declared unit, contributing origins, root configuration revision and applied policy revision. A bound can be finite (including zero where allowed), derived, or explicitly inherited with an enforceable ancestor. Missing required keys and contradictory ranges prevent activation. A derived setting carries the scope and meaning of its bound. Resources resolves it against fresh hardware or provider facts; Configuration neither probes hardware nor issues leases.

Apply the [configuration authority rules](../../../../CONFIGURATION_STANDARD.md) before activation. A configuration reload validates the full snapshot and publishes one coherent revision or preserves the prior valid revision. Running work retains the revision it was admitted against for evidence. The live policy and revocation check is still required before any new permit. Looser settings do not extend existing leases. Tighter mandatory restrictions fence affected work under the [resource contract](../../../../RESOURCE_CONTRACT.md) and still allow independently authorized cleanup. Where a key lacks a catalog reload classification, apply a newly validated value to future admissions only; mandatory revocation continues to take effect independently.

Resources depends on Configuration. This module exports configuration-owned data only and has no dependency on the resources crate. Provider credentials live in their existing adapters. Diagnostics identify the responsible key and policy class and omit secrets. Retain provenance under the normal configuration audit policy.

**ZIP-CONFIGURATION-RESOURCES-T01.** Permute unordered inputs and verify the normalized snapshot digest is identical. Reject a workspace network enable under offline organization policy, and keep the previous complete snapshot after an invalid reload. A derived bound and an explicit zero retain distinct representations at the admission boundary.
