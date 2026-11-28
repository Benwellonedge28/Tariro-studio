# Controlled input streaming

**ZIP-TERMINAL-STDIN-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/stdin.rs`

## Boundary and inputs

Accept only an explicitly admitted input adapter with finite bytes, live deadline, approved data class and exact process attempt. Attach it only after qualified launch. Default to closed input when no source is approved. Interactive input and credential delivery each require their own capability.

## Behavior and failure handling

Stream only bounded chunks, enforce the exact operation scope, and close the input once at EOF or authorized cancellation. Detach pending producers without exposing buffered data. Keep pipe closure distinct from tree exit and prevent retry under stale ownership.

## Acceptance

**ZIP-TERMINAL-STDIN-T01.** Cancel a synthetic blocked input read. Verify the child observes closure, no additional bytes are delivered, and a foreground observer dropping its own wait does not remove cleanup supervision.
