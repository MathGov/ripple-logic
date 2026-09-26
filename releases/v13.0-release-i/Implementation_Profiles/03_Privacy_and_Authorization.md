# Privacy-preserving evidence and authorization

## Purpose
Preserve protection, accountable authorization and legitimate audit while minimizing unnecessary disclosure. Cryptographic mechanisms implement a declared trust and threat model; they do not establish the truth or ethical sufficiency of the underlying data.

## Bound the signed object
Use a reviewed, precisely versioned encoding. Bind all decision-material fields, including configuration, audience, action, scope, nonce, issuance/expiry and applicable authority state. Verify the signature against the content actually submitted, not merely against an unrelated supplied digest. Domain, chain and verifier separation are needed where applicable. EIP-712 is an optional Ethereum-specific typed-signature mechanism, not a universal requirement, and explicitly does not include replay protection. Application-level nonce, expiry and authoritative replay handling remain necessary.

A content hash detects change relative to a trusted reference under its cryptographic assumptions; it does not make collision or forgery mathematically impossible. A signature authenticates the relevant key and bound message, not automatically the stakeholder's identity, the evidence, the legal mandate or physical admissibility. Do not identify a protected human by tx.origin or by possession of a machine credential.

## Hardware-backed keys
An implementation may use an HSM, secure element or independently justified equivalent. Validate actual algorithm support, signing format, key generation, authenticated sessions, least privilege, rotation, revocation, recovery and key-custody procedures. Non-exportable keys reduce key-extraction exposure but cannot stop an authorized application from requesting malicious signatures. Do not log key material or embed operational passwords in examples. SDK snippets and hardware compatibility require actual compilation and device tests.

## Threshold authority
A multi-party profile records signers, threshold, independence and conflicts, competence, mandate, protected-party representation, quorum availability, compromise assumptions, emergency powers, expiry, challenge and remedy. A 4-of-7 vote, seven constituencies or a 72-hour window is a design choice requiring justification, not a theorem or automatic source of legitimacy. An emergency freeze must itself be bounded and assessed for harm. It cannot retroactively legalize an unqualified action.

## Selective disclosure and zero knowledge
A proof must identify the exact relation, public inputs, hidden witness, trusted registry/root when needed, input provenance, arithmetic range, freshness, circuit identity, verifier identity and setup assumptions. The verifier must require the desired public result; merely proving that a program returned false is not passage. Finite-field multiplication by a known nonzero constant is invertible, so secret × 41923 = public is not a hiding commitment. Registry membership requires a real commitment and membership relation, not that equation.

Proof validity only establishes the specified relation under the stated assumptions. It does not prove that a sensor reading is true, a registry is complete, a welfare measure is valid or a person deserves less protection. Protection cannot be denied because a person lacks a key, network access, a caloric reserve or a proof. Minimize linkability and sensitive public commitments; hashing a predictable identifier alone is not anonymity.

## Retention and reconstruction
Define record classes, access tiers, retention justifications, evidence needed for appeal/remedy, cryptographic-key lifecycles, independent archive verification and restore drills. Do not purge sole decision evidence because a timed job ran. Replication is not an independent backup against propagated errors. Retain enough to reconstruct the decision without keeping unnecessary sensitive content indefinitely.

## Release appendix
Profile edition 1.0; companion to MathGov/RippleLogic v13.0. No SNARK circuit, HSM integration or on-chain system is certified by this package. Primary references: EIP-712 https://eips.ethereum.org/EIPS/eip-712 ; ZoKrates field semantics https://zokrates.github.io/language/types.html ; existing ripple.md §19 and RPAP dependency boundary.
