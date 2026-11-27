# Production specification standard

**ZIP-SPEC-001 · v1.0 · Owner:** Zipporah architecture maintainers. **Maturity:** D4 candidate. Approve in a reviewed commit before applying as repository policy.

## Applicability

A component is a planned crate, application or integration with a public, persistent or execution boundary. Each component has an inventory covering every planned source file. Each source file has a linked contract with an exact repository-relative path. Closely related files may share a document only when separate headings give each file its own API, algorithm, invariants, tests and integration. Planned and implemented files have separate status.

## Required component sections

| Section | Review checks |
| --- | --- |
| Identity | Stable component ID, contract version, accountable owner and maturity |
| Purpose | Observable capability and consumer |
| Scope | Owned behavior, excluded behavior and delegated responsibilities |
| Dependencies | Allowed edges, forbidden boundaries, optional features and target conditions |
| Terminology | Distinct definitions for terms used across interfaces |
| Architecture | Boundaries, data flow and ownership |
| Directory structure | Exact source and test paths linked to file contracts |
| Data model | Types, fields, units, validation and mutation owner |
| Public API | Complete Rust signatures, type definitions and behavioral contract |
| Internal API | Internal visibility, ownership and dependency direction |
| Algorithms | Ordered inputs, branches, outputs and partial-failure behavior |
| State machines | Complete transition table or precise statelessness justification |
| Invariants | Conditions maintained across every entry and exit |
| Configuration | Key, type, origin, precedence, reload and failure policy |
| Resource management | Admission, charge, cleanup, bounds and degradation |
| Concurrency | Synchronization, lock order, race outcomes and ownership |
| Cancellation | Safe points, irreversible boundaries and lost-response behavior |
| Error handling | Typed errors, precedence, retry and recovery |
| Security | Threats, trusted sources, privileges and denials |
| Persistence | Storage schema, transaction boundaries and durability |
| Serialization | Exact shape, version, canonicalization and invalid-input handling |
| Integration | Caller/provider contracts and compatibility |
| Observability | Evidence, metric dimensions, instrumentation and redaction |
| Performance | Measured criteria, fixture, benchmark method and approval owner |
| Portability | Supported targets, enforcement parity and unsupported behavior |
| Testing | Stable test IDs, fixtures, commands, outcomes and expected failures |
| Acceptance | Exact gate and evidence required |
| Migration | Read/write compatibility, upgrade steps and rollback |
| Implementation order | Prerequisites and construction sequence |
| Completion criteria | Evidence, independent reviewer and remaining blockers |

An inapplicable section names the boundary that owns the behavior or explains why it cannot arise. A Rust signature must name all types, their modules and lifetime/ownership behavior. A pseudocode sample must be marked as such. A proposed threshold does not qualify as a measured performance requirement.

## Authority and maturity

The constitution governs all artifacts. Approved structured contracts are canonical for machine-checked fields, including dependency edges, key names and requirement IDs. Approved Markdown is canonical for behavior that schemas cannot express. Any disagreement blocks the affected review and release. Make paired edits to canonical and explanatory artifacts in one PR.

D0 = placeholder; D1 = concept; D2 = architecture; D3 = detailed; D4 = complete implementation contract; D5 = independently reviewed complete contract with validation evidence. A draft can state D4 candidate but must record open blockers. D5 requires review against a pinned revision and [design validation](DOCUMENTATION_VALIDATION.md). Runtime readiness requires implementation and measured acceptance separately.
