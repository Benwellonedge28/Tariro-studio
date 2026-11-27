# Pause at a durable checkpoint

**ZIP-RUNTIME-CONTROL-PAUSE-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/control/pause.rs`

## Required implementation behavior

Stop claiming new work, drain or cancel active tasks to known boundaries and wait for verified checkpoint. Report unresolved effects and unreaped workers as blocked.

## Acceptance

**ZIP-RUNTIME-CONTROL-PAUSE-T01.** Pause between checkpoint and next claim resumes from the recorded unit only.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
