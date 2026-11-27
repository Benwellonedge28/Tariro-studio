# Foundation Rust API and implementation boundaries

**ZIP-FND-API-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate. **Basis:** Zipporah main `9551b0fde3d792be82bcdf419b5fa45c43559c7e`.

The 26 linked [file contracts](../DESIGN.md#file-contracts) define operations and module locations. This document fixes shared type, lifetime and serialization decisions. These decisions are proposed for review. No implementation or independent design approval has been established.

## Common API rules

- The crate root has no first-party dependency. Required standard-library features and the qualified `uuid` boundary are documented in [dependency-contract.md](dependency-contract.md). Nothing starts background work or reads configuration on import.
- `FoundationError` and `Result<T>` are the common leaf error surface. No I/O, cancellation, authorization or persistence is implied by constructing a value.
- `Clone + Copy + Debug + Eq + PartialEq + Hash` are required on `IdKind`, `Identifier`, `DigestAlgorithm`, `Digest`, `DurationMillis`, `Timestamp` and `Version`. `Timestamp` and `Version` additionally implement lexicographic `Ord + PartialOrd` over their numeric fields in declaration order. Root contracts define any other required traits; no blanket serialization or logging of payloads.
- `Quantity<U>` uses `PhantomData<U>` to prevent implicit unit conversion. It defines `new`, `get` and same-unit checked addition. Callers provide a concrete unit marker and an enclosing wire unit. Do not infer public generic trait bounds from a derive. Copy and formatting of generic quantities are outside the required API.
- Constructors accepting borrowed inputs do not keep that borrow unless the declaration explicitly says so. `Namespace::as_str`, `Identifier::as_uuid`, `Digest::as_bytes` and `BoundedBytes::as_slice` borrow only from their receiver. `into_vec` consumes ownership. Component and capability descriptors borrow approved metadata and confer no authority.
- Thin module declaration, prelude and alias modules have no internal API, data record, effects or migration state. They have compile-time fixtures to detect public surface drift.

## Representations and failure precedence

| Value | Representation and rejection |
| --- | --- |
| Identifier | Canonical lower-case hyphenated UUID; reject malformed input before nil. Equality and hashing include the kind. Generic records carry kind separately. |
| Namespace | Lowercase ASCII dotted labels; compare byte budget before lexical validation and allocate only after both pass. Expose borrowed canonical spelling. |
| Digest | Canonical lower-case tagged SHA-256. Verify tag framing before deciding unsupported algorithm. Reject length or hex of a recognized tag before decoding. |
| Timestamp | Floor Unix seconds plus nonnegative nanosecond component. Accept `-62135596800..=253402300799` seconds and `0..=999999999` nanoseconds. Compare eligibility in the normalized UTC instant; never construct a live deadline from wall time alone. |
| Duration | Unsigned milliseconds. Canonical JSON decimal string has no signs, suffix, or leading zeros except zero. Arithmetic overflow returns `QuantityOverflow`. |
| Version | Three canonical decimal `u16` components. Validate the complete lexeme before numeric conversion so malformed input returns `InvalidIdentifier` even if a component also overflows. |
| Limits | Inclusive and finite. Checked addition precedes limit comparison for charging. Failure leaves usage unchanged. |
| Bounded bytes | Enforce caller limit before growth. Fallible reserve precedes copying. Going out of scope drops owned storage without I/O. |

Enclosing wire adapters can implement codecs once the DTO schema is qualified. Foundation values do not expose persistence adapters or require runtime decimal, time zone or wire dependencies. A version change follows [the compatibility standard](../../../COMPATIBILITY_STANDARD.md).

## Cancellation invariants

The source owns setting the sticky flag; cloned tokens can only observe it. Under the mutex, keep a one-to-one relation between active registration IDs and waiters. Cancellation sets the flag and detaches all registrations atomically. All waker cloning, dropping and invoking occurs outside the mutex, including rejection and replacement paths. A wait is fused after a terminal result. No callback invokes an effect or changes the flag unless independently authorized and holding the source. Result races and cleanup belong to [the cancellation file contract](modules/cancellation.md).

## Open qualification gates

- Qualify the precise UUID dependency version, enabled features and offline dependency supply.
- Compile every positive and compile-fail fixture against the actual tree. Run the targeted cancellation scheduler and property fixtures on supported targets.
- Review identifier-kind registry ownership with identity, repository, assignment and artifact consumers. No guessed discriminants may enter storage schemas.
- Require independent review of API and fixture evidence before D5. Lossy changes or unresolved compatibility block promotion.
