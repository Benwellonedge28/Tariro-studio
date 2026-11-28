# Policy regression and dry-run comparison

**ZIP-GOVERNANCE-EVALUATION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/evaluation.rs`

## Boundary and inputs

Compare a reviewed candidate policy against a pinned baseline and finite qualified scenarios. Capture exact versions, authenticated synthetic claims, expected control changes and required optional inputs. Run the same pure decision evaluator for each pair under the same frozen observations. Neither side can perform effects or publish policy.

## Behavior and failure handling

Record canonical decision deltas, including newly allowed, newly denied, newly requiring approval and unresolved mandatory evidence. Report a purported tightening as failing whenever it widens any tested authorized scope. Record unavailable scenarios as incomplete coverage. A passing regression does not prove unspecified scenarios or authorize activation.

## Acceptance

**ZIP-GOVERNANCE-EVALUATION-T01.** Test a candidate that removes one allowed path but accidentally adds another. Report both changes and fail qualification as a tightening, independent of scenario order.
