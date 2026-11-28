# Last-moment effect check

**ZIP-GOVERNANCE-AUTHORIZATION-OPERATION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/operation.rs`

## Boundary and inputs

Accept exact approved action, normalized target and preconditions, stable effect identity, authenticated actor and current grant. Before claim verify live authority, policy, emergency-stop state, path and egress bindings, relevant lease, deadline, approval when required and reviewed digest. Treat a preview, role label or grant reference without live validation as insufficient authority.

## Behavior and failure handling

In one guarded transaction serialize effect claim against policy and scope epoch changes, consume a matching one-time approval when required, and record intent and decision before dispatch. Recheck the owning live dispatch boundary. A deny that wins before claim yields zero calls. A claimed operation requires reconciliation if completion is uncertain. Store verified receipt or explicit unknown without repeated dispatch. Authorize reads before exposing replay status. Use the [external-effect recovery rules](../../../../../RECOVERY_STANDARD.md) for matching, verified absence and conflict.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-OPERATION-T01.** Revoke after preview before claim and verify zero dispatch. Race exact claims, then lose a confirmed provider reply and verify one occurrence reconciles under the original identity. A shifted path or payload fails before effect.
