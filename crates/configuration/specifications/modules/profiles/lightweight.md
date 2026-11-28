# Lightweight profile rules

**ZIP-CONFIGURATION-PROFILES-LIGHTWEIGHT-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/lightweight.rs`

## Boundary and inputs

Accept an explicitly installed, registered lightweight profile definition for this candidate. Resolve a serial preference and prefer the smallest compatible local model among verified candidates with a comparable measured demand. Use the inference preference contract and the assignment's quality floor. Register the actual installed definition through [profile dispatch](mod.md). Availability cannot be inferred from the profile name or example hardware.

## Behavior and failure handling

When multiple models meet the floor, compare peak admitted host-memory demand first, then a stable model digest. Rank only compatible candidates with usable measurements. Ask Resources to admit the chosen mode before loading. If no local request fits, surface typed unavailability. A remote route is considered only when independently selected and authorized. Keep all preference values and effective bounds in the snapshot provenance.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-LIGHTWEIGHT-T01.** Use one smaller model below the floor, one compatible model and one merely advertised model. Verify only the compatible measured model can be considered. Remove it and verify a stable unavailable result with zero implied remote calls.
