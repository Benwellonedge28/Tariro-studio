# Scoped context cache

**ZIP-CONTEXT-CACHE-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/cache.rs`

## Required implementation behavior

Key by source pin, policy, auth scope, template and tokenizer. Expire or invalidate on relevant revision changes; never share confidential objects between scopes.

## Acceptance

**ZIP-CONTEXT-CACHE-T01.** Changed credential/authorization epoch does not reuse old broad context.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
