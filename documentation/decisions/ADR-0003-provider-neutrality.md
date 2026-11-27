# ADR-0003 · Provider neutrality

**Status** Accepted in the master design. Implementation evidence is required separately.

## Decision

Access inference, hosting, storage and distributed work through stable, negotiable interfaces. GitHub is a first-class adapter and local Git remains supported.

## Consequences

Adapters describe their capabilities and limitations. The gateway selects only routes supported by user policy and model configuration.

## Acceptance

Use two compatible model adapters and a disconnected provider fixture.

[Master design](../../ZIPPORAH-STUDIO-DESIGN.md)
