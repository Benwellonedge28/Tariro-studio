# Terminology and shared data

**Contract version** 1.0. Master design §71.

A principal is an authenticated actor. A capability describes an eligible operation. A grant is scoped authority issued by the owner. A plan is an immutable revision-specific intended execution. A lease is temporary placement authority with a fencing epoch. A checkpoint is a durable verified progress boundary. Evidence is an observed, digest-bound record. An artifact is immutable content referenced by a digest.

## Implementation and acceptance

Represent typed IDs as non-nil UUIDs with canonical lowercase hyphenated form. Use UTF-8 normalized field names and tagged digests. Use UTC RFC 3339 for interchange and monotonic time for live deadlines. Represent durations in integer milliseconds, storage in bytes and budgeted currency as integer minor units plus currency code.
