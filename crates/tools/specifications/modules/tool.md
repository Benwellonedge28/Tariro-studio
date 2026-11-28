# Tool descriptor and authority request

**ZIP-TOOLS-TOOL-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/tool.rs`

## Boundary and inputs

Define an immutable qualified tool descriptor with stable ID, version, exact schema digests, purpose, effect class, required capability, limit requirements and enrolled adapter identity. Keep human display metadata separate from identity. Descriptor discovery supplies a proposition and requires review before registration.

## Behavior and failure handling

Verify the descriptor digest and current registered edition before normalizing a request. Missing or changed scope, schema or adapter requires qualification under the owning registry. A requested name, display label or output statement never changes effect class or permissions.

## Acceptance

**ZIP-TOOLS-TOOL-T01.** Rename a tool's display label to a privileged-sounding name while its effect class remains read-only. Verify unchanged eligibility and scope and no authority to publish.
