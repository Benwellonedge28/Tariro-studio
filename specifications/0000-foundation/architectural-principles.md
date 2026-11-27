# Architectural principles

**Contract version** 1.0. Master design §71.

Default to owner-local execution. Enforce capability attenuation and scope at the external effect boundary. Store state before dispatch and verify before publishing. Keep model-derived proposals separate from authoritative evidence and execution receipts.

## Implementation and acceptance

Use explicit error classes. Validate resource bounds before allocations or dispatch. Inject platform/provider adapters at a composition root. Contract tests check that unsupported capabilities remain discoverable as unavailable.
