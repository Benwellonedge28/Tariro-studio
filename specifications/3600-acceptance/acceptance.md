# Reference acceptance scenarios

**Contract version** 1.0. Master design §71.

## Contract

Pin an authorized fixture modeled on Vimbai. Inventory actual sources and all applicable AGENTS.md at reviewed commit. Author and independently verify one document at a time and checkpoint every verified work unit.

## Execution and integration

Seal exactly 30 eligible Markdown changes, validate staged diff and references, publish via dedicated branch and draft PR, reconcile lost acknowledgment, and record PR ID and checks. Less than 30 enters AwaitingApproval. Never merge as part of this fixture.

## Verification

Test shutdown after 17, Rust write denied, 31st file denied, 12 remaining paused, required instructions unavailable, expiry or revocation, push/PR interruption, broken citations, CI failure and resource pressure.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Test run checkpoints

| Injection | Required observation |
| --- | --- |
| Kill after document 17 | Exactly 17 durable verified checkpoints; next action authors document 18 |
| Attempt Rust change or 31st Markdown file | Effect denied before mutation or publication |
| Only 12 eligible files remain | AwaitingApproval; no PR with silently changed batch size |
| Required AGENTS.md unavailable | Block before mutation and identify the missing instruction scope |
| Grant expires or owner revokes | Stop new effects and retain existing work; audit denies resume under old grant |
| Lost push or PR response | Reconcile expected ref/operation key and confirm one intended PR |
| Invented source reference | Verification fails with file and claim context |
| CI failure | Capture actual check result and retain verified local checkpoint |
| Resource pressure | Shrink within policy or pause; no implicit online fallback |

Use a synthetic fixture for forced failures and a separately authorized live smoke run for provider behavior. Evidence contains base/head SHA, git diff summary, scoped grant ID, checkpoint list, grounded source references and actual GitHub check identifiers. The release gate fails if any mandatory case is missing.

## Implementing components

- [assignments crate design](../../crates/assignments/DESIGN.md)
- [documentation crate design](../../crates/documentation/DESIGN.md)
- [verification crate design](../../crates/verification/DESIGN.md)
- [repository crate design](../../crates/repository/DESIGN.md)
