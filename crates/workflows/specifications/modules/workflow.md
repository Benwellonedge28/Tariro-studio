# Workflow lifecycle root

**ZIP-WORKFLOWS-WORKFLOW-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/workflow.rs`

## Required implementation behavior

Pin immutable versioned definition and current execution, validate before activation, and store distinct planned/executing/verified outcomes.

## Acceptance

**ZIP-WORKFLOWS-WORKFLOW-T01.** Updating draft keeps prior reviewed execution unchanged.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
