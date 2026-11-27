# Memory command adapter

**ZIP-CLI-COMMANDS-MEMORY-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/memory.rs`

## Required implementation behavior

Search scoped records, export only to an approved destination, and require explicit owner permission for purge. Return durable receipt and visibility status.

## Acceptance

**ZIP-CLI-COMMANDS-MEMORY-T01.** Cross-workspace query reveals no private memory data.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
