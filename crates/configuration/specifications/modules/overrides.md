# Mandatory restriction intersection

**ZIP-CONFIGURATION-OVERRIDES-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/overrides.rs`

## Boundary and inputs

Start with baseline defaults. Apply the selected profile, permitted user, workspace, environment and explicit flag preferences in that order. A later scalar replaces a permitted earlier scalar. A permitted array or set replaces the entire preference value. Preserve the origins that determine the final result. If a scope attempts to set a capability reserved for mandatory policy, reject the candidate before considering precedence.

## Behavior and failure handling

Then apply constitution, system, organization, workspace and assignment restrictions under the [configuration standard](../../../../CONFIGURATION_STANDARD.md). Maximums take the minimum, minimums take the maximum, explicit available permissions intersect, required sets union and exact values must agree. Keep absence distinct from an empty set and never treat it as a wildcard permission. A contradictory range or required capability outside an allowed set is PolicyConflict. Preference overrides never clear or reclassify an enforceable restriction. Deterministically order normalized sets and provenance before snapshot hashing.

## Acceptance

**ZIP-CONFIGURATION-OVERRIDES-T01.** Give identical policy sets in different orders and verify identical effective values and digest. Attempt to widen destination access and memory capacity from a workspace layer. Verify the denied destination remains denied and an applicable ceiling remains effective. Test conflicting exact values and an explicitly empty allow set.
