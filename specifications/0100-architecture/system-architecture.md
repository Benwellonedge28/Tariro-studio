# System architecture and data flow

**Contract version** 1.0. Master design §71.

A client sends a typed command through the gateway. The gateway authenticates, resolves workspace and policy, allocates correlation identity and records durable intent. An application service plans and a supervisor dispatches under a lease. Outputs flow through verification before a durable state change and event publication.

## Implementation and acceptance

The write boundary owns authorization and audit coupling. Object storage owns staged immutable bytes. Consumers subscribe from their last acknowledged cursor. Recover unknown effects by typed reconciliation before retry.
