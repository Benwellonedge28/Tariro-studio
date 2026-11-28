# Adapter interface selection

**ZIP-TOOLS-ADAPTERS-MOD-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/mod.rs`

## Boundary and inputs

Select a qualified adapter by exact descriptor, stable identity, declared version and mandatory requirements. Registered kinds are native, process, HTTP, MCP and plugin. Check supported effect, containment and observation capability before invoking selected services. Unknown adapters stay unavailable.

## Behavior and failure handling

Do not select an adapter by display label or replace an unavailable tool with a more permissive path. Bind chosen adapter and approved descriptor digest into intent and result. Discovery is observation only. Recovery uses the exact enrolled effect owner or remains unresolved.

## Acceptance

**ZIP-TOOLS-ADAPTERS-MOD-T01.** Remove required evidence for the qualified adapter and leave an arbitrary process adapter available. Verify the tool remains unavailable and no fallback process is invoked.
