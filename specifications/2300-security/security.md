# Security and trust boundaries

**Contract version** 1.0. Master design §71.

## Contract

Role eligibility never grants execution on its own. Evaluate principal, environment attributes, authenticated session, capability, path/root, current policy, expiry and generation before effects.

## Execution and integration

Resolve opaque credential references in the minimum adapter boundary. Redact prior to durable output and model egress. Sandbox untrusted tools and block unsupported isolation; retain redacted decision and outcome evidence.

## Verification

Use synthetic secret canaries, confused-deputy and symlink scenarios, and reject unapproved endpoints and artifacts.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Policy decision ordering

1. Authenticate principal, audience and workspace membership.
2. Load mandatory policy and the current revocation epoch from trusted storage.
3. Evaluate capability plus RBAC/ABAC against normalized operation, resource, path, destination and budget.
4. Confirm expiry, exact scope and any separate owner approval. Fail closed if inputs are absent or ambiguous.
5. Persist redacted intent and execute through the adapter. Recheck scope and revocation immediately before irreversible I/O.
6. Audit outcome or mark it unknown and reconcile with the narrowest read capability.

The return is `Allowed(decision_id, policy_digest, scope_digest)`, `Denied(code, decision_id)` or `AwaitingApproval(request_id, effect_digest)`. Denied decisions expose reason codes without secret values. An approval is never serialized into model context.

## Implementing components

- [security crate design](../../crates/security/DESIGN.md)
- [identity crate design](../../crates/identity/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
