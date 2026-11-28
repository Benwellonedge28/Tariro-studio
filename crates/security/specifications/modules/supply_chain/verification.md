# Supply-chain acceptance rule

**ZIP-SECURITY-SUPPLY-CHAIN-VERIFICATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/supply_chain/verification.rs`

## Boundary and inputs

Aggregate scoped evidence for exact artifact, resolved graph, signer policy and mandatory verification gates. Compare each observation's candidate, revision and required authority. Report verified, violated and unavailable conditions independently. Accept only when every mandatory gate has current matching evidence.

## Behavior and failure handling

Bind the result to the exact candidate and policy, keep immutable references to failing observations and never manufacture success from a signed manifest or incomplete reports. Activation is a separate release operation, rechecking live policy and exact candidate. Reconcile missing receipt through its owner instead of running repeated protected effects.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-VERIFICATION-T01.** Pass digest and signature checks while withholding one mandatory test report. Verify the result remains blocked. Supply a stale passing report and verify it does not change the verdict.
