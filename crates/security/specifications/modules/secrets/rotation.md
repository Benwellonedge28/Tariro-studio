# Credential generation replacement

**ZIP-SECURITY-SECRETS-ROTATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/secrets/rotation.rs`

## Boundary and inputs

Create a stable rotation intent scoped to the exact credential reference, provider and current generation. Stage and verify the new generation through the owning adapter under current authority. Keep old active selection before activation only when the provider proves staged setup did not invalidate it. Do not infer old availability from local state.

## Behavior and failure handling

Use an expected-revision activation to change the active reference and fence new effects from its old generation. Keep external provider state changes under original intent and reconcile if activation or retirement becomes ambiguous. A recovery handle is only available under approved retention and cleanup authority. No stage writes secret bytes to shared state.

## Acceptance

**ZIP-SECURITY-SECRETS-ROTATION-T01.** Interrupt before local activation and after activation, then lose the provider reply. Confirm old behavior only with supporting provider evidence. After activation verify the old generation cannot start a new effect and recovery does not repeat an uncertain provider mutation.
