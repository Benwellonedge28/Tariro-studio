# Reference acceptance scenarios

**Contract version** 1.1 candidate. Master design §71.

Qualify the workflow through the [documentation handover](documentation-handover.md). Use an independent verifier, pinned source and instructions, durable per-file checkpoints and a separately authorized publication branch and draft PR. The reference grant requests 30 eligible Markdown changes and has no merge authority. The one-file synthetic smoke profile has its own grant and never relaxes the 30-file reference.

| Gate | Required observation |
| --- | --- |
| Restart after document 17 | Exactly 17 committed verified checkpoints; the next action authors unit 18. |
| Out-of-scope write or file 31 | Deny before the proposed staging write and before remote publication. |
| Only 12 approved eligible files | Enter AwaitingApproval, preserve prior work and issue no push or PR. |
| Applicable AGENTS.md unavailable | Block before mutation and retain the reason for authorized review. |
| Grant expires or is revoked | Fence new effects; the old grant cannot resume execution. |
| Push or PR reply lost | Inspect the original identity; a matching effect settles without duplicate dispatch. |
| Fabricated citation or missing final anchor | Block candidate publication despite matching file count. |
| Required CI failure | Preserve the draft and actual check result; completion cannot pass. |
| Resource pressure | Defer or pause within policy without implicit egress. |
| Offline smoke | Pin and verify a local candidate with zero remote calls. |

Use synthetic fixtures for deliberate faults. Validate the versioned [evidence manifest](../../contracts/acceptance/documentation/evidence-manifest.schema.json) and preserve observations tied to the exact candidate and run. Verify live adapter behavior separately. A release gate fails when a mandatory observation is missing, stale or unresolved. Report findings and actual verification against [requirements](../../REQUIREMENTS.md).

[Assignments](../../crates/assignments/DESIGN.md) · [Documentation](../../crates/documentation/DESIGN.md) · [Verification](../../crates/verification/DESIGN.md) · [Repository](../../crates/repository/DESIGN.md)
