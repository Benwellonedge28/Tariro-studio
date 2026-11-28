# Defensive boundary composition

**ZIP-SECURITY-DEFENSES-MOD-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/mod.rs`

## Boundary and inputs

Compose the content trust, structured arguments, scoped egress, dependency and secret-handling checks as bounded typed observations. Associate each check with a declared enforcement point, current policy and exact request. Keep advisory detector outputs separate from mandatory controls.

## Behavior and failure handling

Collect required observations before the relevant claim or disclosure. Missing mandatory controls deny the affected operation. A detector score may trigger scoped review or narrower handling but cannot change the grant or authorize protected operations. Redact evidence before sharing it with other components.

## Acceptance

**ZIP-SECURITY-DEFENSES-MOD-T01.** Return an advisory detector warning for an otherwise scoped proposal, then supply an unavailable mandatory control. Verify the warning grants nothing and the missing control blocks the affected operation.
