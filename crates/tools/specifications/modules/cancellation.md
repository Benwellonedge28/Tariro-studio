# Tool cancellation ownership

**ZIP-TOOLS-CANCELLATION-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/cancellation.rs`

## Required implementation behavior

Track cancellation against active invocation and deliver via adapter/supervisor. Preserve confirmed results and unresolved effects under durable identity.

## Acceptance

**ZIP-TOOLS-CANCELLATION-T01.** Cancel after effect commit cannot erase confirmed receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
