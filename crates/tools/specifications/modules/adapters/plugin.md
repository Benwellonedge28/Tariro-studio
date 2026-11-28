# Isolated plugin adapter

**ZIP-TOOLS-ADAPTERS-PLUGIN-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/plugin.rs`

## Boundary and inputs

Bind plugin identity, installed digest, negotiated API edition, permitted imports and effective execution bounds. Select only an enrolled plugin with qualified Sandbox controls and reviewed capabilities. Host imports are exact typed action requests that use their own authority.

## Behavior and failure handling

Verify each protected import's current lifecycle, attempt, budget and grant at dispatch. Enforce approved fuel and memory limits without converting guest termination to external settlement evidence. Plugin revocation fences new calls and preserves all outstanding effect identities for reconciliation.

## Acceptance

**ZIP-TOOLS-ADAPTERS-PLUGIN-T01.** Revoke a plugin between a successful synthetic guest start and a host capability call. Verify the host call denies and the guest's old lease does not convey new access.
