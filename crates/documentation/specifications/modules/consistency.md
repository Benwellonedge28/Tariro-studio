# Cross-document rule compatibility

**ZIP-DOCUMENTATION-CONSISTENCY-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/consistency.rs`

Compare referenced normative rules at the pinned revision and planned candidate overlay. Normalize by stable requirement ID, version, component owner, approved authority, typed unit and scope. Keep behavior constraints separate from examples and explanatory prose. A different amount with another unit or assignment scope is not automatically conflicting. Compare normalized semantics and require an approved escalation record where two applicable canonical definitions disagree.

Report both paths, evidence digests and affected gates. Block a dependent document or batch until the conflict is resolved in the correct authority. Revalidate affected documents when an authoritative contract or requirement changes. Never synthesize a middle value or silently prefer the nearest file.

**ZIP-DOCUMENTATION-CONSISTENCY-T01.** Two different mandatory limits for the same ID and scope block. Distinct approved defaults and assignment constraints remain distinguishable.
