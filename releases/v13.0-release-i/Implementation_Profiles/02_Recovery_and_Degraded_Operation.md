# Qualified recovery and degraded operation

## Purpose
Preserve protective capability when software, communications or institutions fail, without treating automation or emergency language as permission to bypass the framework. The normative owners remain Canon §9.9A, CSV and Agent System §§23.6–23.7.

## Recovery is an intervention, not a negative score
Changing a database value, sending an opposite-signed vector or announcing “recovery confirmed” does not reverse physical, financial, institutional or welfare harm. A recovery candidate must identify the intervention mechanism, causal warrant, authority, budget, resource carrier, latency, expected effect, uncertainty, externalities, expiry, monitoring and fallback. It passes the applicable qualification route and receives separately bound execution authority. Raw observations and failed attempts remain in the audit trail.

Do not blindly implement “large positive number → inject −90%.” Canonical harms are negative signed impacts, while a nonnegative loss magnitude is a different data type. Detection must use the declared type and endpoint. A numerical threshold is not an observed human or ecological safety boundary without a justified mapping.

## Timing and mitigation
A runtime-prevention claim needs an endpoint-specific upper bound on the complete control critical path and a lower bound on time to unacceptable harm, with a stated margin. Serial, concurrent, automatic and human-dependent paths must be modeled accurately. Failure of this test blocks timely-prevention credit for that endpoint; it does not rule out separately evidenced ex-ante protection or later mitigation of duration or severity. Stopping a system is itself a consequence-bearing action and can be harmful, especially when essential services depend on it.

## Idempotency and uncertain outcomes
Bind an intervention to an incident, option, exact configuration, action type, authority scope and stable action identity. Reserve an action atomically before dispatch. A duplicate worker should find the existing reservation rather than dispatch again. A local durable reservation does not provide exactly-once external execution. If dispatch succeeds but the acknowledgement is lost, the action enters reconciliation, not automatic retry. The reference SQLite ledger demonstrates local reservation and reconciliation states only; it contains no actuator.

## Degradation envelope
Record normal, degraded, isolated, safe-continuation or safe-stop, recovery and requalification conditions as operational states, not new Canon verdicts. Loss of communication narrows operation to the prequalified local envelope. It cannot expand authority. Preserve essential bounded protective functions when stopping them would create greater qualified harm. Reconnection does not restore expired credentials or stale approvals; reconcile events, resource state, clocks and pending actions first.

## Offline communication
A low-bandwidth radio adapter is optional. Define a protocol version, sender, message identity, sequence/nonce, time quality, expiry, hop budget, authentication, replay cache, resource limits and reconciliation procedure. CRC and a magic byte detect some errors; they do not authenticate a sender. Unbounded rebroadcast is prohibited. Do not infer population welfare from a radio's packet statistics. Physical deployment needs power, range, congestion, threat and applicable spectrum evidence.

## Acceptance evidence
Test duplicate deliveries, concurrent workers, restart after reservation, missing acknowledgements, expired approvals, wrong configuration, offline restart, clock uncertainty, unsafe stop, reconnection and stale queue replay. Test actual controls against real endpoints before claiming protection.

## Release appendix
Profile edition 1.0; companion to MathGov/RippleLogic v13.0. No operational daemon or physical mesh was deployed or hardware-tested for this package. The LoRa library's own documentation states that it does not supply addressing/encryption or regulatory duty-cycle enforcement: https://github.com/sandeepmistry/arduino-LoRa .
