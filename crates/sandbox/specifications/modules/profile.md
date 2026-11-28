# Immutable isolation policy

**ZIP-SANDBOX-PROFILE-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/profile.rs`

## Boundary and inputs

Construct an immutable versioned profile of allowed roots and rights, network and device rules, environment disclosure, process count and required memory or output controls. Bind policy revision, exact action scope, resolved units, deadlines and applicable adapter evidence requirements. Store an auditable digest without private env values.

## Behavior and failure handling

Intersect requested permissions with mandatory policy and applicable lease bounds. An explicit added permission cannot weaken a deny. Unsupported required controls, contradictory requirements and missing enforceable bounds fail before staging. Profile selection alone cannot authorize effects. A changed profile requires fresh proof and assertion of current authority.

## Acceptance

**ZIP-SANDBOX-PROFILE-T01.** Try to enable egress under a mandatory offline policy and expand a restricted root. Both fail. Verify a compatible narrower profile can stage under separate authorization and exact resource admission.
