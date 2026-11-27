# ADR-0002 · Local-first operation

**Status** Accepted in the master design. Implementation evidence is required separately.

## Decision

Keep durable state in the owner-controlled environment. Run local capabilities offline and require approved egress for optional network features.

## Consequences

Run compatibility and model capability checks at configuration time. Restore and export use versioned manifests. Deployments can add explicit remote adapters.

## Acceptance

Run the offline reference suite with zero external network traffic.

[Master design](../../ZIPPORAH-STUDIO-DESIGN.md)
