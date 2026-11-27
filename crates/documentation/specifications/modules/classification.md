# Evidence-based document classification

**ZIP-DOCUMENTATION-CLASSIFICATION-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/classification.rs`

Classify each reviewed target as Substantive, Incomplete, CandidatePlaceholder, Missing or Unknown. Missing requires authoritative path absence at the pinned commit. Unknown covers unavailable data, unclear role or unresolved content interpretation. Incomplete needs an identified normative gap under its role. Empty content and recognized placeholder patterns can nominate candidates. Length, filename, code examples and marker words alone cannot establish that existing prose is disposable.

Record the exact blob, rule version, reason and reviewer decision before replacement. Preserve substantive valid work and existing evidence unless the approved scope explicitly requires an edit. A short decision record with supported purpose and outcome can be complete for its role. Use role-specific sections from the pinned specification requirements rather than padding all documents with identical prose.

**ZIP-DOCUMENTATION-CLASSIFICATION-T01.** A valid short decision and a real placeholder receive different outcomes. An inaccessible file is Unknown.
