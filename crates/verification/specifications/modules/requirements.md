# Required evidence graph

**ZIP-VERIFICATION-REQUIREMENTS-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/requirements.rs`

Resolve each in-scope normative requirement ID from the pinned registry into at least one mandatory gate or an approved documented inapplicability reason. Bind the requirement revision and gate identity to the plan. Inapplicability records need scope, authority and rationale, and cannot be inferred from missing tests. Reject dangling IDs, empty evidence mappings and duplicate gate definitions. Optional gates contribute separately reported observations and cannot cover a mandatory gap. A coverage report preserves which requirements were satisfied, failed, blocked or explicitly inapplicable under the pinned version.

**ZIP-VERIFICATION-REQUIREMENTS-T01.** An unknown required ID or unmapped applicable requirement blocks acceptance even when all supplied optional checks pass.
