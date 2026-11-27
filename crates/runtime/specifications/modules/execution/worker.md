# Single-attempt worker

**ZIP-RUNTIME-EXECUTION-WORKER-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/worker.rs`

## Required implementation behavior

Run only assigned task and epoch, check live lease before effects, report verified attempt outcome and retained cleanup obligation. Never self-assign replacement work.

## Acceptance

**ZIP-RUNTIME-EXECUTION-WORKER-T01.** Late output from fenced worker is rejected even if execution completed.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
