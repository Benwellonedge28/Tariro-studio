# Trust separation for content

**ZIP-SECURITY-DEFENSES-PROMPT-INJECTION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/prompt_injection.rs`

## Required implementation behavior

Label repository/tool/model content with source, scope and trust. Treat embedded instructions as data unless explicitly endorsed through trusted policy; model proposals undergo normal gate.

## Acceptance

**ZIP-SECURITY-DEFENSES-PROMPT-INJECTION-T01.** Repository text claiming delegated authority does not change permissible effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
