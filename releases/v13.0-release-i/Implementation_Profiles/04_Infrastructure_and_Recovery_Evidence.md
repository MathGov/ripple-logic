# Infrastructure and recovery evidence

## Scope
This is a platform-neutral acceptance profile, not a deployment script. PostgreSQL, Kubernetes, HSMs, public ledgers and radio meshes are optional technologies. Their presence does not make the decision architecture validated or safe. A minimal offline review workflow may be sufficient for low-stakes use.

## Durable state
Declare data classes, write authority, consistency model, recovery-point objective, recovery-time objective, failure domains, backup/restore method and retention. Asynchronous streaming replication does not guarantee zero loss of acknowledged transactions. Synchronous replication has latency and availability tradeoffs and requires explicit configuration. A lost reply, stale replica or promotion event must not reset consumed nonces or redispatch an uncertain intervention.

Promotion requires a reviewed leader/fencing method so two partitions cannot independently retain write or execution authority. Test network partition, primary loss, replica lag, split brain, stale credentials, incomplete WAL and restored-but-obsolete action records. A replica is not protection against every logical corruption or accidental deletion. Keep independently verified backups and test restoration.

## Deployment controls
Remove hard-coded credentials and use least-privilege identities with an appropriate secret-management boundary. Persist database storage, restrict network exposure, pin images and dependencies, define readiness/liveness, quotas, health evidence and change rollback. Autoscaling processing workers requires duplicate-action handling and backpressure; increasing replicas must not multiply real-world interventions. A StatefulSet provides orchestration primitives, not a complete multi-region database or fencing protocol.

## Partitioning and archives
Design partition keys, uniqueness and replay rules together. A primary key on (payload_id, timestamp) does not alone enforce global payload_id uniqueness across changing timestamps. Migrations must preserve existing data and constraints, not simply rename the old table and leave it orphaned. Declare the source and destination of exports, verify checksums, row counts and restoreability, then remove eligible records only under authorized retention policy. Compression syntax and extension APIs must be checked against pinned software documentation and actually tested.

## Performance evidence
A load generator supplies demand; it does not prove correct accepted throughput. Distinguish valid signed records, malformed records, duplicate/replayed records, stale records and authority failures. Count durable writes and correct refusals, not just HTTP 200 responses. Measure latency distributions, errors, queue age, memory, storage growth, recovery and preservation of decision-state invariants under overload. Clearly state hardware, network, versions, workload, duration and target service. No million-transaction or geographic-latency result is claimed without logs.

## Release appendix
Profile edition 1.0; companion to MathGov/RippleLogic v13.0. No production database, multi-region failover or Kubernetes deployment was executed here. Primary references: PostgreSQL 16 standby behavior https://www.postgresql.org/docs/16/warm-standby.html ; pg_basebackup https://www.postgresql.org/docs/16/app-pgbasebackup.html ; Kubernetes StatefulSets https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ .
