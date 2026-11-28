# Bounded decision presentation

**ZIP-GOVERNANCE-OVERSIGHT-HUMAN-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/oversight/human.rs`

## Boundary and inputs

Render a bounded authenticated review view with exact scope, expected base, candidate/effect digest, deadline, requested destinations, resource obligations and irreversible outcomes. Each view names the request version and approved review target. Omit secret values and separately protect restricted evidence.

## Behavior and failure handling

Verify the submitted decision is from the current qualified human authority and binds the exact displayed request and digest. Canonical validation happens server-side. A material change invalidates the preview and requires a fresh review. Client text, prefilled fields, votes and agent messages supply no approval. Persist the human decision before making it available to the [approval gate](../authorization/approval.md).

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-HUMAN-T01.** Preview a proposal, edit one target field and submit the previously displayed digest. Verify rejection. Repeat with stale role membership and confirm a new qualified decision is necessary.
