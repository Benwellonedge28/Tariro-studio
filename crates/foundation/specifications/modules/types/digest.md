# Tagged digest module

**ZIP-FND-DIG-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate. **Source:** `crates/foundation/src/types/digest.rs`.

## Public contract

```rust
use crate::error::FoundationError;

#[derive(Clone, Copy, Debug, Eq, PartialEq, Hash)]
pub enum DigestAlgorithm { Sha256 }

#[derive(Clone, Copy, Debug, Eq, PartialEq, Hash)]
pub struct Digest { algorithm: DigestAlgorithm, bytes: [u8; 32] }

impl Digest {
    pub const fn from_sha256(bytes: [u8; 32]) -> Self;
    pub const fn algorithm(&self) -> DigestAlgorithm;
    pub const fn as_bytes(&self) -> &[u8; 32];
    pub fn parse(input: &str) -> Result<Self, FoundationError>;
    pub fn write_tagged(&self, out: &mut [u8; 71]);
}
```

The signatures describe the type boundary and require method bodies in implementation. Internal helpers decode ASCII nibbles into bytes and encode bytes into lowercase hexadecimal. Hash computation and content streaming belong to caller adapters. A digest is not a signature or credential. Do not use its equality method as a constant-time secret comparison.

## Encoding and algorithm

Canonical encoding is seven ASCII bytes `sha256:` followed by exactly 64 lowercase hexadecimal digits; total length 71 bytes. Split on exactly one ASCII colon without allocating. Require nonempty tag and payload, allow ASCII letters, digits and hyphen in the tag, and reject any byte outside printable ASCII 0x21–0x7E in the input. Framing failures return `InvalidDigestEncoding`. If framing is valid and the tag differs from `sha256` byte for byte, return `UnsupportedDigestAlgorithm`. For the recognized tag, then enforce exactly 64 lowercase hex digits before writing any decoded byte. Decode each pair into output bytes. Serialization always emits the same tag and canonical digits. Equality and hashing include the algorithm.

The 32-byte size is SHA-256's representation, independent of resource policy. Bounds on hashed input belong to the caller's lease. The type owns no persistence, time, cancellation, synchronization or mutable state, and performs no I/O. Future algorithms must receive explicit encoding/compatibility contracts and reject unsupported tags at every old boundary.

## Acceptance

FND-DIG-T01 uses SHA-256 of the empty byte sequence, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, and checks exact round-trip bytes. FND-DIG-T02 rejects uppercase, missing/extra digits and extra separator. FND-DIG-T03 returns unsupported for the plausible tag `sha999:` with a well-framed payload. FND-DIG-T04 covers arbitrary 32-byte round trips and malformed input without allocation or panic. See [compatibility](../../../../../COMPATIBILITY_STANDARD.md).
