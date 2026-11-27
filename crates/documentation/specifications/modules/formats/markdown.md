# Safe Markdown normalization

**ZIP-DOCUMENTATION-FORMATS-MARKDOWN-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/formats/markdown.rs`

## Required implementation behavior

Parse bounded input, retain headings and local refs, escape untrusted content for output; resolve repository links at pin without automatic external fetch.

## Acceptance

**ZIP-DOCUMENTATION-FORMATS-MARKDOWN-T01.** Relative path escape or missing target yields typed finding.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
