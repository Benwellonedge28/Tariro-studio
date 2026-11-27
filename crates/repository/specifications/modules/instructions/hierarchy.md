# Component-wise ancestor applicability

**ZIP-REPOSITORY-INSTRUCTIONS-HIERARCHY-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/instructions/hierarchy.rs`

An instruction file applies when its directory components form an exact prefix of the affected file's parent directory components. The root applies to every path. Do not use text prefix, case-folded matching or default-path coercion to calculate authority. Reject paths the host cannot represent without aliases. Applicable rules for each affected endpoint are ordered shallowest to deepest, with evidence tying each rule to the endpoint. Scope restrictions compose across both endpoints. If a deletion or rename removes a rule, the base rule continues governing that candidate. A newly staged rule never widens current authorization and needs dedicated review before becoming an approved base rule.

**ZIP-REPOSITORY-INSTRUCTIONS-HIERARCHY-T01.** A docs-private path inherits the root rule but not the docs directory rule. A moved path is checked under both old and new directories.
