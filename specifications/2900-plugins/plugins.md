# Plugins and extensions

**Contract version** 1.0. Master design §71.

## Contract

Manifest records component digest, interface versions, signer, imports, declared effects and max memory/fuel. Installation stages bytes and verifies integrity and authority before activation.

## Execution and integration

Grant only explicit host imports. Bind calls to the same governance gateway as other agents. Atomic activation and prior compatible generation enable rollback.

## Verification

Test unauthorized host call, fuel exhaustion, revoked plugin, signature mismatch and unsupported interface.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [plugins crate design](../../crates/plugins/DESIGN.md)
- [sandbox crate design](../../crates/sandbox/DESIGN.md)
- [sdk crate design](../../crates/sdk/DESIGN.md)
