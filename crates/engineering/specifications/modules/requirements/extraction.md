# Evidence-linked requirement extraction

**ZIP-ENGINEERING-REQUIREMENTS-EXTRACTION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/requirements/extraction.rs`

## Required implementation behavior

Use approved inputs; record exact source spans, actors and unresolved interpretation. Label inferred requirements.

## Acceptance

**ZIP-ENGINEERING-REQUIREMENTS-EXTRACTION-T01.** Ambiguous language yields review candidate, not assumed normative requirement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
