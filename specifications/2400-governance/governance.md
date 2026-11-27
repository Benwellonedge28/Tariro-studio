# Authorization and oversight

**Contract version** 1.0. Master design §71.

## Contract

An approved scope is immutable. It binds exact commit or repository, owner/principal, permitted effects, resource and spending ceilings, expiry and revocation epoch. Run policy intersection immediately before effect dispatch.

## Execution and integration

For one-time actions bind request digest and expiry, atomically claim once, record result or unknown state, and permit replay only after reconciliation. Emergency stop is durable. Delegation can only attenuate.

## Verification

Race revoke against effect claim and verify no new effect starts. Test stale approval payload and approval requested by an agent role.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [governance crate design](../../crates/governance/DESIGN.md)
- [identity crate design](../../crates/identity/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
