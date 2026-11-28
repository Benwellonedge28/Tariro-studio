# Last-moment agent permissions

**ZIP-AGENTS-PERMISSIONS-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/permissions.rs`

## Boundary and inputs

Check the exact action, approved digest, actor, target scope, current principal and grant epochs, effective deadline and qualified adapter at the effect boundary. Resolve authority through Governance and stage effect intent under the applicable scope. Task data and proposed instructions are untrusted. Read-only discovery has separately bounded permission and cannot invoke mutation.

## Behavior and failure handling

Before an effect claim, recheck revocation with the owning verifier. When revoke wins before claim, deny with no effect. When claim wins first, retain the durable effect obligation and reconcile using separately authorized evidence. A lost reply cannot justify a second dispatch. Keep grant strings and adapter credentials outside agent state and diagnostics. The [governance contract](../../../../specifications/2400-governance/governance.md) supplies the authoritative claim semantics.

## Acceptance

**ZIP-AGENTS-PERMISSIONS-T01.** Race revoke and effect claim in both orders. Verify zero calls when revoke wins, at most one call and retained intent when claim wins, and no disclosure of unrelated grant or target details.
