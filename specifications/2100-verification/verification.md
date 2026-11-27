# Verification and evidence

**Contract version** 1.1 candidate. Master design §§44 and 71.

Seal an immutable candidate and plan before collecting evidence. Bind each observation to the pinned requirement, gate, candidate, input, tool version, policy, verifier and output. Resolve claims through scoped authoritative sources. Source citations name the exact revision and blob. Provider checks name the stable repository and exact reviewed commit. A manual-only gate requires an authenticated reviewer who meets the defined independence rule.

## Acceptance

Evaluate current qualified mandatory failures first. Otherwise block on missing, stale, conflicting or incomplete mandatory evidence or unresolved blocking findings. Pass only after all applicable mandatory checks pass, with explicit reviewed treatment for inapplicable requirements. Report optional and historical observations separately. Recheck candidate, authority and policy before acting on an acceptance receipt.

The verifier uses bounded immutable reads, independently executed qualified checks and scoped reviewer inputs. No runner or assessor claim can replace actual observed evidence. A response loss preserves the original attempt identity for reconciliation. Verified repository scope requires the full staged tree and both endpoints for moves.

Use the [evidence fixtures](../../contracts/acceptance/verification/evidence-fixtures.json) to test candidate edits after review, stale CI, fabricated citations, self-review, missing evidence and exact scope. Bind release observations to [requirements](../../REQUIREMENTS.md). Logical checks, runner qualification and independent review remain distinct gates.

## Implementing components

- [Verification](../../crates/verification/DESIGN.md)
- [Audit](../../crates/audit/DESIGN.md)
