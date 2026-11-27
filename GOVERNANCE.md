# Governance and authorization

A grant binds `grant_id`, `principal_id`, `workspace_id`, `repository_id`, `base_revision`, allowed operation set, path scopes, approved destinations, hard resource and spending ceilings, `policy_digest`, expiry and a revocation epoch. Delegation intersects all dimensions and can only shorten expiry. Use deterministic path matching on normalized segments.

| Role | Authority |
| --- | --- |
| Owner | Set workspace policy, issue and revoke scoped grants, approve release and exceptional actions. |
| Maintainer | Plan assignments and request publication within delegated permissions. |
| Developer/agent | Propose or execute explicitly granted tasks in the assigned workspace. |
| Independent reviewer | Assess evidence and attach structured findings. |
| Auditor | Read authorized redacted evidence and verify audit chain integrity. |

RBAC provides eligibility; ABAC checks workspace, repository, revision, scope, sensitivity, destination, time and policy context. Positive decisions require matching capabilities and current revocation epoch. Distinguish assignment approval from merge, deletion, restricted egress, production release and security-policy changes.

Persist approval intent with the proposed effect digest. At execution re-check owner, revision, policy, expiry and digest. New effects stop immediately on revocation. In-flight operations enter reconciliation and must not silently retry. Emergency stop remains effective across restart and requires explicit owner recovery.
