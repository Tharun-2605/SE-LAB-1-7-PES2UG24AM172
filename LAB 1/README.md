# Lab 1 — Requirements Engineering & UML Use-Case Modelling
### Problem Statement #16 (Healthcare & Telemedicine): Remote Patient Vitals Alert & Monitoring App

**Course:** PES University — Dept. of CSE
**Actors:** Remote Patient, On-Call Caregiver

---

## 1. Problem Context

A continuous monitoring pipeline for post-operative patients that ingests vital telemetry (SpO2, Heart Rate, BP), detects threshold breaches, and escalates emergency alerts through a caregiver matrix.

## 2. Deliverables in This Repository

| File | Description |
|---|---|
| [`Requirements_Table.pdf`](Requirements_Table.pdf) | FR-001–FR-005 and NFR-001–NFR-002, each with ID, Priority/Type, Description, Acceptance Criteria, and Rationale |
| [`USE_CASE_DIAGRAM.pdf`](USE_CASE_DIAGRAM.pdf) | UML Use-Case Diagram with all actors, primary use cases, one `«include»` and one `«extend»` relationship |
| [`Escalate_Emergency_Alert_Flow.pdf`](Escalate_Emergency_Alert_Flow.pdf) | 1-page flow specification for the core use case: Preconditions, Postconditions, Main Success Scenario, and one Alternate Flow |

## 3. Requirements Summary

| ID | Priority | Description |
|----|----------|-------------|
| FR-001 | High | Continuously evaluate ingested vitals against clinical thresholds and flag critical anomalies within 2 s. |
| FR-002 | High | Ingest continuous telemetry streams from registered devices and persist each reading with a synchronized timestamp and device ID. |
| FR-003 | High | Escalate an emergency alert to the assigned On-Call Caregiver via ≥ 2 independent notification channels on threshold breach. |
| FR-004 | Medium | Auto-escalate an unacknowledged alert to the Backup Caregiver after a configurable timeout (default 3 min). |
| FR-005 | Medium | Provide a real-time + historical (≥ 30 days) vitals dashboard for Patient and Caregiver. |

| ID | Type | Description |
|----|------|-------------|
| NFR-001 | Performance & Security | ≥ 500 concurrent telemetry streams, 99.99% uptime, TLS 1.2+ / AES-256 encryption. |
| NFR-002 | Reliability & Availability | Buffer/retry through 10-min network loss with zero data loss; 99.9% monthly availability with automatic failover. |

## 4. Use-Case Diagram Highlights

- **Actors:** Remote Patient, Vitals Sensor Device (Wearable), On-Call Caregiver, Backup Caregiver, Hospital EMR System
- **«include»:** *Escalate Emergency Alert* includes *Send Multi-Channel Notification* — a mandatory sub-behaviour every escalation needs.
- **«extend»:** *Escalate to Backup Caregiver* extends *Escalate Emergency Alert* at the extension point "No Acknowledgment Within Timeout" — conditional behaviour that only fires on the alternate flow.

## 5. Core Use Case: Escalate Emergency Alert

Full spec is in `Escalate_Emergency_Alert_Flow.pdf`. Summary: on a confirmed threshold breach, the system dispatches a multi-channel alert to the On-Call Caregiver and logs it as Dispatched; if acknowledged within the timeout, it's marked Acknowledged and the flow ends. If not acknowledged in time (Alternate Flow), it auto-escalates to the Backup Caregiver, with a final system-level escalation if that too goes unanswered.
