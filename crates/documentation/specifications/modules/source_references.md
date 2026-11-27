# Verified source references

**ZIP-DOCUMENTATION-SOURCE-REFERENCES-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/source_references.rs`

A repository reference binds stable repository identity, full commit ID, canonical path, Git blob ID, and an optional inclusive 1-based line range. Fetch through the pinned snapshot, validate declared range and compare exact source with the claim. A reachable link alone proves no factual assertion. When lines are supplied, enforce `1 <= first <= last <= line_count` using repository raw UTF-8 lines. A renamed or mutable head cannot substitute for the declared revision. Historical references can remain valid for claims explicitly about that snapshot.

An approved external source reference binds its canonical identity, observed source digest, scope, retrieval time and exact excerpt/range when applicable. Honor offline and privacy policy. No local path, unresolved citation or solely generated summary counts as external evidence. Respond distinctly to missing, denied, malformed and unfetched sources. Even a resolved reference requires a verified support judgment for the exact claim. Preserve source origin and verifier evidence under bounded retention.

**ZIP-DOCUMENTATION-SOURCE-REFERENCES-T01.** A nonexistent path, invalid source range or unobserved blob cannot support a factual claim. A historical path at its valid old commit remains usable only for the historical claim.
