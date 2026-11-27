# Untrusted tool-call proposal

**ZIP-INTELLIGENCE-TOOL-CALLING-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/tool_calling.rs`

## Required implementation behavior

Parse proposed tool/version and arguments, validate schema and hand to authorized dispatcher. Provider response supplies no permission or invocation authority.

## Acceptance

**ZIP-INTELLIGENCE-TOOL-CALLING-T01.** Generated text suggesting a write cannot execute without matching current grant.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
