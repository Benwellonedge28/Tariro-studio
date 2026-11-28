# Cancellation-to-supervisor bridge

**ZIP-TERMINAL-CANCELLATION-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/cancellation.rs`

## Boundary and inputs

Consume authorized stop and sticky cancellation observations bound to the exact attempt and process ownership. Close input and new dispatch, record first accepted stop cause at the owner, then signal cooperative exit. Deadline and explicit cancel remain distinguishable. The supervising owner supplies the approved grace budget.

## Behavior and failure handling

After grace request termination of the approved contained tree. Compare durable exit and stop transitions using the owner's revision checks. A prior accepted result remains retained. Publish terminal receipt only once with required teardown proof. Lost stop reply stays scoped to the original operation and observer disconnection does not end supervision.

## Acceptance

**ZIP-TERMINAL-CANCELLATION-T01.** Race stop with a verified process exit in both orders. Verify one terminal receipt, no duplicate tree termination credit, and no cleanup settlement merely because foreground waiting ended.
