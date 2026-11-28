# Case and component normalization

**ZIP-FILESYSTEM-NORMALIZATION-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/normalization.rs`

## Boundary and inputs

Convert validated repository spelling to a lookup and collision key using the qualified target volume's declared case and equivalence rules. Separate canonical comparison keys, raw repository spelling and safe display. Charge byte and depth limits before mapping.

## Behavior and failure handling

Reject two distinct entries with the same comparison key for an affected destination. Avoid silently changing the requested spelling or treating unproven encodings as safe. Return typed unavailable if target semantics cannot be determined for the requested mutation. Bind outputs to the root generation and policy.

## Acceptance

**ZIP-FILESYSTEM-NORMALIZATION-T01.** Offer two spellings that map to one key on a synthetic case-insensitive volume. Reject the ambiguous batch. Repeat on a separately qualified case-sensitive target and preserve both identities when policy permits.
