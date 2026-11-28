# Invocation intent and idempotency

**ZIP-TOOLS-INVOCATION-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/invocation.rs`

## Boundary and inputs

Define an immutable invocation descriptor binding stable request identity, exact tool and adapter versions, normalized arguments, effect digest, scoped grant, lease and finite deadline. A request ID is an idempotency locator, not a credential or qualification. Keep opaque references separate from secret values.

## Behavior and failure handling

Validate identity and authority before receipt lookup. A same-key same-digest authorized replay returns stored status or receipt. A different digest is a conflict. If outcome remains unknown, the owning reconciliation path controls any later repeat. A new key cannot be used as a workaround for unsettled work.

## Acceptance

**ZIP-TOOLS-INVOCATION-T01.** Lose the first confirmed result reply and repeat the same request. Verify the prior state or receipt is returned without another invocation. Try a field change and confirm conflict.
