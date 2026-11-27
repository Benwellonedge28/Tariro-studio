# Effect receipt comparison

**ZIP-RUNTIME-RECOVERY-RECONCILIATION-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate.

**Planned source:** `crates/runtime/src/recovery/reconciliation.rs`

## Decision interface

Expose a crate-private pure comparison over verified observations supplied by the owning effect adapter. The input contains the stable effect key, provider/account/target binding, expected target state and exact approved payload digest from the durable intent. `EffectDecision` has four variants. `Matched` carries a verified receipt digest. `Absent` carries definitive absence and precondition evidence. `Conflict` carries a bounded conflict-evidence digest. `Unknown` carries an available redacted reason and optional evidence digest. Use `Digest` from `foundation::types::digest`. Trusted adapter evidence is obtained under separate read-only reconciliation authority.

| Observation | Decision | Runtime action |
| --- | --- | --- |
| Exact provider, scope, key, approved payload and verified result | Matched | Record the receipt once and preserve the committed effect disposition |
| Provider proves absence for the original key and target, original preconditions still hold | Absent | Permit retry eligibility evaluation after verified teardown, release and terminal predecessor |
| Authoritative observation contradicts identity, payload, result or original preconditions | Conflict | Record conflict and block automatic retry |
| Offline, denied, timed out, incomplete or unable to prove either match or absence | Unknown | Retain open obligation and block automatic retry |

Reconciliation never issues the external mutation. Record comparisons and receipt references under current recovery ownership with expected revision. A previously committed receipt under the same key and digest is a replay. A second authoritative digest for the same receipt is a conflict requiring review. An identical committed effect can survive a timeout or revocation of worker authority. Any new operation or artifact disclosure still requires its own live authority. Keep process occupancy and effect verification separate. Verified teardown and settled metering allow resource release while unresolved effect evidence continues to block successor execution.

## Acceptance

**ZIP-RUNTIME-RECOVERY-RECONCILIATION-T01.** Inject identical, conflicting, absent and unavailable provider observations. Verify the exact result is retained, conflicts and unknown outcomes block, and only a proven absent effect can become eligible for reevaluation under a fresh claim. See [recovery standard](../../../../../RECOVERY_STANDARD.md) and [fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
