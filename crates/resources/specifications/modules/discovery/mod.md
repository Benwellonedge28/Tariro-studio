# Discovery snapshot assembly

**ZIP-RESOURCES-DISCOVERY-MOD-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/mod.rs`

## Boundary and inputs

Collect typed CPU, RAM, accelerator, volume and network probe records from registry-selected local adapters. Bind each record to its physical or service scope, dimension and unit, observation clock domain, freshness and enforceability. Publish a single immutable capacity revision associated with one inventory generation. Missing or unverifiable metrics are Unknown for their specific coordinate.

## Behavior and failure handling

Use finite probe and response budgets. A failed probe may leave unrelated records available only within the same trusted deployment generation. Do not join incompatible device or containment generations. Discard a candidate when inventory changes during assembly, and refresh rather than replay an older known-good sample as current. Publication changes the read model only. In-progress reservations survive capacity revision replacement.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-MOD-T01.** Inject one failed probe, stale generation and inventory change during assembly. Verify only affected metrics become unavailable or the generation is rejected as appropriate, no optimism is substituted, and an existing hold is unchanged. Check zero versus unknown with ZIP-RES-FIX-004 in the [admission fixtures](../../../../../contracts/acceptance/resources/admission-fixtures.json).
