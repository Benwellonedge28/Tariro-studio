# Language development workflow profile

**ZIP-ENG-LANG-001 · v1.0 candidate · Owner** Engineering, Compilation and Testing maintainers

This profile applies the [software lifecycle contract](lifecycle.md) to a language toolchain such as Zamani. The [legacy register](../../LEGACY_FEATURE_REGISTER.md) provides workflow-stage provenance. A project supplies its own language semantics, compiler and tooling. Existing workflow, compilation and testing capabilities own execution.

## Required profile inputs

Pin the project snapshot, language specification revision, toolchain and target, input corpus digest, package or dependency lock digest if applicable, and the requested compatibility mode. Each optional tool declares supported capabilities and produces an explicit unsupported outcome for missing operations. Never infer support from the language name.

| Stage | Contract and required artifact |
| --- | --- |
| Goals and requirements | Review target users, language properties, supported targets and compatibility policy. Produce versioned requirement IDs and scope. |
| Language specification and grammar | Record grammar format, source encoding and semantic specification revision. Parse or otherwise verify the project's grammar with its declared tool. Preserve syntax and semantic diagnostics with spans. |
| Front end | Collect actual lexer, parser and semantic test evidence. Compare diagnostic codes and source spans using project-owned fixtures. Preserve tokens or trees only where supported by the toolchain. |
| Intermediate representation | Bind lowering and optimization evidence to the exact compiler and pipeline. Compare the project's declared observable semantics before and after transformation. |
| Backend and runtime | Build for the selected target with declared flags and toolchain identity. Execute target-compatible fixtures or record unsupported execution. Package only artifacts that meet target checks. |
| Standard library and packages | Resolve pinned dependencies offline when available. Test the project-declared public API and record package format and lock evidence. Missing offline dependencies remain explicit. |
| Tooling and interoperability | Exercise the versioned formatter, debugger, language server and ABI capabilities individually when declared. Fixture formats and expected outcomes belong to each project. |
| Documentation and conformance | Verify executable examples and positive and negative syntax or semantics fixtures against the selected compiler. Preserve the environment and corpus digests. |
| Bootstrap and self-hosting | Record host toolchain, seed compiler identity and staged build digests. Compare outputs according to the project's declared reproducibility contract and rerun conformance before promoting a new bootstrap stage. |
| Release | Validate manifests, artifact signatures, compatibility decisions and release scope. External publication requires a dedicated effect grant and reconciled receipt. |

## Integration and failure handling

Use the [Compilation specification](../1800-compilation/compilation.md) and [Testing specification](../1900-testing/testing.md) for adapters, artifact receipts and evidence. A fixture binds a case ID, language revision, source digest, target and expectation. A negative case passes only when the expected rejection occurs with the declared diagnostic code or exit category. Timeout, denial and resource exhaustion remain failed or blocked execution even if a negative case expects compilation to fail.

Run adapters under acquired leases using the [resource contract](../../RESOURCE_CONTRACT.md). Charge compiler, subprocess and storage use to the same assignment budget. Apply deadline and cancellation before promoting outputs. Retain partial outputs as diagnostic evidence only. The existing reproducibility and artifact contracts determine which build outputs may be reused.

## Acceptance

- **ZIP-ENG-LANG-T01.** Run one valid and one invalid input through a synthetic compiler adapter. A valid artifact and the expected invalid diagnostic pass. A timeout for the invalid input fails the fixture.
- **ZIP-ENG-LANG-T02.** Change the grammar revision or compiler digest and verify that an earlier conformance receipt cannot qualify the new snapshot.
- **ZIP-ENG-LANG-T03.** Build a fixture in stages with pinned seeds and a declared deterministic output. Alter a stage output digest and verify promotion stops with the stage evidence preserved.
- **ZIP-ENG-LANG-T04.** Request an unsupported target, deny network access during resolution and cancel an in-progress build in separate runs. Verify each produces its own outcome and none is promoted as a release artifact.
