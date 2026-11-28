# Governance failure classification

**ZIP-GOVERNANCE-ERROR-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/error.rs`

## Boundary and inputs

Expose stable codes for unauthenticated caller, unavailable policy, denial, approval required, stale scope, expiry, revocation, conflict, emergency stop and unknown outcome. Preserve Governance status names in the wire decision contract and map internal typed errors at the boundary. Scope evidence and detail to an authorized reader.

## Behavior and failure handling

Validate request shape and identity before returning scope-dependent failures. Distinguish a definite preclaim denial from ambiguous persistence or dispatch. Unknown outcome requires original-intent reconciliation. Do not retry a denied or revoked operation by weakening assumptions or switching policy. Drop raw policy input, credentials and private request data from rendered errors.

## Acceptance

**ZIP-GOVERNANCE-ERROR-T01.** Use an unauthorized actor, unavailable policy and a lost claim acknowledgement. Verify scoped stable codes, no protected configuration disclosure and zero speculative retries.
