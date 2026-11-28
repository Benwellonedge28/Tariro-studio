# Pre-effect request validation

**ZIP-TOOLS-VALIDATION-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/validation.rs`

## Boundary and inputs

Validate input shape, descriptor identity and exact version against the approved registry. Then normalize typed arguments, bind the requested effect and scope and check applicable live policy and lease. Require finite resource and deadline bounds and qualified mandatory adapter controls.

## Behavior and failure handling

Return a redacted precise denial when any mandatory input fails. Validation yields an immutable scoped candidate and observations, not authorization for effects. Preserve current grant checks at the owning claim. No fallback to an alternate adapter or effect after scope mismatch.

## Acceptance

**ZIP-TOOLS-VALIDATION-T01.** Validate a well-formed tool call with one unapproved target and one unavailable required control. Both stay pre-dispatch. A valid call advances only to the separate live effect gate.
