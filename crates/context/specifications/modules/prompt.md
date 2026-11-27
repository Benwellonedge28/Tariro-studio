# Authority-aware prompt representation

**ZIP-CONTEXT-PROMPT-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/prompt.rs`

## Required implementation behavior

Assemble typed policy messages and explicitly labeled untrusted content, preserving disclosure scope. Never derive authority from message text.

## Acceptance

**ZIP-CONTEXT-PROMPT-T01.** Repository text requesting extra permissions stays inert data.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
