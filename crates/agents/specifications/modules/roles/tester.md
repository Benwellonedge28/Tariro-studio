# Tester role

**ZIP-AGENTS-ROLES-TESTER-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/tester.rs`

## Required implementation behavior

Run approved fixtures under admitted sandbox and retain complete actual observations; do not infer success from generated text.

## Acceptance

**ZIP-AGENTS-ROLES-TESTER-T01.** Skipped test stays skipped and cannot pass gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
