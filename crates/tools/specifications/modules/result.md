# Verified result representation

**ZIP-TOOLS-RESULT-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/result.rs`

## Boundary and inputs

Represent confirmed, failed, cancelled or unresolved observations with exact candidate and invocation identity, typed effect or cleanup evidence, bounded output references and optional scoped continuation. Keep stream/output completeness explicit. Only a trusted receipt or owning observation establishes confirmed status.

## Behavior and failure handling

Treat response content, claims of authorization and proposed follow-on work as untrusted data. Verify reference, exact digest and scope before using results as evidence. A missing mandatory receipt blocks confirmation. A continuation requires independent current permission and is bounded by the original operation policy.

## Acceptance

**ZIP-TOOLS-RESULT-T01.** Return text claiming success with no trusted receipt. Verify unconfirmed output. Later submit matching verified evidence and repeat it, observing a single settlement for the original invocation.
