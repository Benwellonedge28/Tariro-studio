# Minimal profile rules

**ZIP-CONFIGURATION-PROFILES-MINIMAL-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/minimal.rs`

## Boundary and inputs

Read the [minimal manifest](../../../../../configurations/profiles/minimal.toml) as a validated preference layer. It chooses serial and deterministic-first local execution and explicitly sets the local generation model limit to zero. The local orchestration cap is the configured value in the file. Keep that zero as a resolved finite bound.

## Behavior and failure handling

Admission for local generation must require the applicable model-slot coordinate even on systems with spare accelerator or RAM capacity. Deterministic jobs still need measured fit and own authorization. Treat absent or unsupported accelerator data separately from a zero policy cap. Profile selection does not grant remote inference or remove any containment requirement. Report the explicit profile origin for the local slot decision.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-MINIMAL-T01.** Provide abundant synthetic RAM and a valid model under the minimal profile. Reject local model loading by the zero cap, then admit an independently fitting deterministic operation under the same resolved profile.
