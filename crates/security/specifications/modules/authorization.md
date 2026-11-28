# Default-deny execution gate

**ZIP-SECURITY-AUTHORIZATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/authorization.rs`

## Boundary and inputs

Evaluate known actor, live workspace membership, normalized operation and target, current policy and scope epoch, qualified attributes and effect-specific capability. Compose the [permission checks](permissions/mod.md). A role is one eligibility input. Require the exact reviewed action digest, applicable grant and independently authorized approval when policy requests it.

## Behavior and failure handling

Return a redacted scoped decision. Mandatory denial, stale authority and unavailable required evidence deny. Do not create a reusable execution permit from an earlier allowed decision. Governance records guarded effect intent and the owning adapter compares current bindings immediately before irreversible I/O. A lost reply stays tied to the original effect. See [decision ordering](../../../../specifications/2300-security/security.md).

## Acceptance

**ZIP-SECURITY-AUTHORIZATION-T01.** Mix a matching role with an attribute denial, stale policy and missing capability in separate runs. All deny. Alter only the reviewed effect digest after a valid preview and verify no effect call occurs.
