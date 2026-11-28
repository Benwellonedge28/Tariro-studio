# Qualification evidence DTO

**ZIP-SANDBOX-CAPABILITY-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/capability.rs`

## Boundary and inputs

Represent each control with a kind, effective enforceable bound where applicable, adapter and host edition, scope, observation generation and evidence reference. Distinguish Enforced, Unavailable and Unknown. A platform claim must come from an enrolled observation port and match the exact requested profile binding.

## Behavior and failure handling

Compare required controls and units before activation. A permissive, mutable or absent observation cannot satisfy a hard requirement. Invalidate stale capability evidence without rewriting historic observations. Composition must check installed controls again at the launch boundary.

## Acceptance

**ZIP-SANDBOX-CAPABILITY-T01.** Provide one missing observation, one mismatched bound and one unrelated valid observation. Verify none qualifies the required mode. A matching fresh observation qualifies only its own control.
