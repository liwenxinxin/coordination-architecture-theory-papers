# AP-1: Ungoverned Construction

**A Shared Substrate That Begins Operation Without Pre-Construction Authorization or Construction Record, Violating Paper 3 Claim 1 and Paper 1 Claim 3, Analog of Paper 2 Ungoverned Birth (B3.10)**

**Series:** D — Inter-Self Coordination Derivation Notes
**Phase:** D3 — Anti-Pattern Formalizations
**Note:** D3.02 (Note #577 in the CKS derivation series)
**Taxonomy Category:** 1 — Lifecycle Governance Failures
**Anti-Pattern ID:** AP-1

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Ungoverned Construction (AP-1) is the governance failure mode in which a shared substrate begins operation without the governance records that Paper 3 Claim 1 requires: a pre-construction authorization record in each participating Self's home substrate, and a construction record in the shared substrate itself. When a Full Aspect Integration (FAI) event starts without these records, every governance decision made within the shared substrate lacks an authoritative foundation. This note defines the anti-pattern, specifies how to detect it in governance records, identifies the governance commitments it violates, traces the consequences that follow from each violation, connects it to its intra-Self structural analog (Paper 2 B3.10, Ungoverned Birth), and provides resolution guidance for both prevention and retroactive remediation.

---

## 1. Anti-Pattern Name and Category

**Name:** Ungoverned Construction

**Category:** Taxonomy Category 1 — Lifecycle Governance Failures

Lifecycle Governance Failures are anti-patterns that violate the governance requirements attached to a specific lifecycle event of the shared substrate — construction, operation, or dissolution. AP-1 covers the first lifecycle event: construction. A shared substrate's lifecycle begins the moment it is constructed and first accepts content from participating Selves; AP-1 names the failure mode in which that beginning occurs outside any jointly authorized governance framework.

---

## 2. Description

Paper 3 Claim 1 establishes the shared substrate as the architectural object of inter-Self coordination. The shared substrate is not a temporary communication channel or an ad hoc workspace: it is a constructed object governed by the joint authority of the Selves whose governance perimeters it spans. Construction — the event in which the shared substrate is brought into existence and configured for a specific FAI event — is itself a governed event. Before the shared substrate accepts any content, the participating Selves' governance authorities must have jointly agreed on what is being constructed, how it is configured, and what each Self's governance authority within the shared substrate entails. That agreement produces two governance records: a pre-construction authorization record in each participating Self's home substrate, and a construction record in the shared substrate documenting what was built and under what joint authority.

**Ungoverned Construction** is the failure mode in which one or both of these records are absent when the shared substrate begins operation. The shared substrate exists and processes content — an FAI event is underway — but the governance foundation for that event was never established in the governance record. The configuration of the shared substrate is implicit rather than authored as substrate content. The joint authorization from participating governance authorities either did not occur or occurred in a form that was never written into the governance record. The FAI event has a technical substrate but no governance substrate.

The anti-pattern name — Ungoverned Construction — is precise: it is the *construction* that is ungoverned, not just the *operation*. A shared substrate operating without governance records for a specific operation might be a different anti-pattern (operational drift, implicit configuration, or silent conflict resolution). AP-1 is the prior failure: the shared substrate was never legitimately constructed from a governance standpoint, because the construction itself produced no record.

---

## 3. Detection Criteria

AP-1 is present when any one or more of the following conditions holds in the governance record:

**3.1 No pre-construction authorization record in participating home substrates.** Each participating Self's home substrate should contain an authorization record established before the shared substrate was constructed — a record that documents that the Self's governance authority approved participation in the specific FAI event, under the specific configuration proposed. If no such record exists in one or both home substrates, the construction lacks joint authorization and AP-1 is present.

**3.2 The shared substrate has no construction record, or the construction record lacks authorization references.** A construction record is the shared substrate's founding governance document: it names the participating Selves, records the configuration agreed upon, and references the pre-construction authorization records from each home substrate. If no construction record exists, or if one exists but cannot reference the home-substrate authorization records (because those records do not exist), AP-1 is present.

**3.3 The FAI configuration cannot be found as authored substrate content.** Paper 3 Claim 5 requires that all configurable dimensions of the shared substrate — which aspects each Self contributes, the merge pattern, persistence rules, conflict-handling thresholds, dissolution conditions — be authored as substrate content under human authority. If the configuration is instead implicit (encoded only in the minds of the participants, in informal communications, or in runtime behavior of the orchestration layer but not authored into the substrate), AP-1 is present in combination with AP-6 (Implicit Configuration). The two anti-patterns frequently co-occur: a construction without a record is also typically a construction without authored configuration.

**3.4 The participating Selves' governance authorities cannot produce documentation of what they jointly agreed before construction.** This is the governance-record audit test. If the governance authorities of both participating Selves are asked to produce the documentation of their pre-construction agreement and neither can do so, AP-1 is present regardless of what the participants believe or recall about what was agreed.

Detection of AP-1 does not require that all four conditions hold simultaneously. A single condition is sufficient. Conditions 3.1 and 3.2 together are the canonical form of the anti-pattern; conditions 3.3 and 3.4 serve as corroborating indicators when the canonical evidence is ambiguous.

---

## 4. The Governance Commitment Violated

AP-1 violates two governance commitments from the CKS source papers, one primary and one secondary.

**Primary violation: Paper 3 Claim 1 — shared substrate as architectural object.**

Claim 1 establishes that the shared substrate is the *architectural object* of inter-Self coordination. This language is load-bearing. An architectural object has an authorized construction event, carries governance properties as a consequence of that construction, and its existence as an object within the governance record is what makes subsequent operations over it legitimate. If the shared substrate is never constructed as a governed architectural object — if it comes into existence without a construction event documented in the governance record — then it is not a shared substrate in the Claim 1 sense. It is a technical workspace that two Selves happen to use, without the governance foundation that makes it a CKS-governed shared substrate. Every operation over an ungoverned workspace is architecturally unsupported regardless of how operationally useful that workspace may be.

Construction is the lifecycle event at which the shared substrate acquires its governance identity. Every subsequent governance property of the shared substrate — the three-tier conflict-handling mechanism of Claim 3, the four-locus evolution feed of Claim 4, the configuration-as-substrate-content requirement of Claim 5 — derives its legitimacy from the legitimately constructed shared substrate. Ungoverned Construction is therefore not merely a procedural failure at one lifecycle event; it undermines the governance legitimacy of every subsequent event in the shared substrate's lifecycle.

**Secondary violation: Paper 1 Claim 3 — human-governed authority.**

Paper 1 Claim 3 establishes that the three governance rights — the right to inspect, the right to modify, and the right to override — must be available at all times as a property of the system's design. In the inter-Self context, these rights are exercised by the governance authorities of the participating Selves over the shared substrate and its content. But governance rights are exercised over a governance object: the rights attach to an object that has been constructed under governance and documented in the governance record. A shared substrate that has no construction record is not an object over which governance rights can be meaningfully exercised. There is no documented configuration to inspect, no authorized baseline to modify against, no established governance framework within which override makes sense. The three rights exist formally but cannot be operationally grounded because the governance object they would apply to was never constituted.

The secondary violation is structural: Paper 1 Claim 3 does not fail by being disabled; it fails by lacking an object to attach to.

---

## 5. Consequences

The consequences of AP-1 compound: each consequence creates conditions for the next.

**5.1 Every governance decision within the shared substrate lacks an authoritative foundation.** Governance decisions made during an FAI event — how a conflict is handled, which aspects are merged, how outputs are attributed — must be traceable to a governance framework that was authorized before the event began. Without a construction record, there is no authorized governance framework. Decisions made during the event are technically effective but governance-groundless: they cannot be defended by reference to what the participating authorities agreed, because no such agreement was documented.

**5.2 The determinism contract fails from the start.** The determinism contract requires that governance decisions be reproducible from governance content — that a governance auditor can follow the chain from decision to authorized governance record to understand why the decision was made. This requires that the construction record exist and that it document the configuration under which decisions were made. Without a construction record, the chain is broken at the first link. Governance outputs from the FAI event exist, but they cannot be traced to an authorized source. The event is determinism-opaque from its beginning.

**5.3 Process disputes are structurally unresolvable.** When a dispute arises about a governance decision made during the FAI event — a participating Self questions how a conflict was handled, or a governance authority challenges how aspects were merged — the first step in dispute resolution is to consult the pre-construction authorization record and the construction record to determine what the parties agreed. Without those records, there is no authoritative reference for dispute resolution. The dispute cannot be resolved by reference to what was agreed; it can only be resolved by what the participants now assert they agreed, which is a relational dispute rather than a governance one, and which the governance architecture has no mechanism to resolve.

**5.4 Trust calibration for future inter-Self events is degraded.** Governance track records are the foundation of calibrated trust between Selves contemplating future FAI events. An ungoverned construction in the record signals that the governance floor established by Paper 3's construction requirements was not met for this event. Participating Selves and their governance authorities observe this in the governance record; the calibrated-trust basis for future events is weakened. This consequence compounds across time: if ungoverned construction becomes a pattern, the governance record's value as a trust instrument degrades accordingly.

**5.5 Evolution outputs from the FAI event trace back to a governance-void event.** If the FAI event produces outputs that feed into a participating Self's evolution mechanisms — DNA-layer updates, action-layer records, instinct-evolution inputs — those outputs carry provenance that traces back to the FAI event. If the FAI event is ungoverned, the provenance trace ends at a governance void. The Self's evolution incorporates content whose governance origin cannot be verified. This is the most persistent consequence of AP-1: its effects do not end when the shared substrate dissolves; they persist in the participating Selves' home substrates through the content the ungoverned event produced.

---

## 6. Intra-Self Analog: Paper 2 B3.10 — Ungoverned Birth

AP-1 is not a novel failure mode at the inter-Self scope. It is the structural recurrence of an anti-pattern already identified at the intra-Self scope in Paper 2: B3.10, Ungoverned Birth.

Paper 2 establishes that a cell's lifecycle begins with a birth event — a governed event that produces a birth record documenting the cell's initial governance specifications, its DNA-layer configuration, and the authority under which it was brought into existence. B3.10 names the failure mode in which a cell begins operation without a birth record: the cell exists and executes, but there is no governance record of its construction, configuration, or authorizing governance authority. Every operation the cell performs is architecturally unsupported because the cell was never constituted as a governed object.

The structural identity between B3.10 and AP-1 is exact:

| Dimension | B3.10 (Intra-Self) | AP-1 (Inter-Self) |
|---|---|---|
| Scope of the constructed object | Cell within one Self | Shared substrate spanning two or more Selves |
| The governed event | Cell birth | Shared substrate construction |
| The required record | Birth record with initial governance specifications | Construction record with joint authorization references |
| What authorizes the event | Cell's home governance authority | Joint governance authority of participating Selves |
| The failure mode | Birth without birth record | Construction without construction record |
| Primary commitment violated | Paper 2 lifecycle governance | Paper 3 Claim 1 (shared substrate as architectural object) |

The analog is the inheritance closure: Paper 3 does not invent a new failure mode when it specifies that construction is a governed event. It extends an already-specified intra-Self failure mode to the inter-Self scope. B3.10 is what ungoverned construction looks like when the constructed object is a cell; AP-1 is what it looks like when the constructed object is a shared substrate. The governance requirement is structurally the same; the authorization mechanism is more complex at inter-Self scope because it requires joint authorization across governance perimeters rather than authorization from a single Self's governance authority.

This analog also performs a diagnostic function: governance practitioners familiar with Paper 2's intra-Self lifecycle requirements should recognize AP-1 immediately by structural translation. The question "does this shared substrate have a construction record with joint authorization?" is the inter-Self version of the question "does this cell have a birth record with initial governance specifications?"

---

## 7. Resolution

Resolution addresses two situations: prevention (the shared substrate has not yet been constructed) and remediation (the shared substrate is already operating without adequate governance records).

### 7.1 Prevention: Pre-Construction and At-Construction Requirements

Prevention consists of satisfying the construction governance requirements before the shared substrate begins operation. These requirements span two phases.

**Pre-construction requirements** are satisfied in each participating Self's home substrate before construction begins:

1. Each participating Self's governance authority reviews and approves the proposed FAI event, including the proposed configuration of the shared substrate.
2. That approval is authored as substrate content in the participating Self's home substrate — a pre-construction authorization record that names the FAI event, identifies the other participating Self or Selves, and documents the configuration that was approved.
3. The governance authorities of all participating Selves confirm that the pre-construction authorization records exist in each home substrate before proceeding to construction.

**At-construction requirements** are satisfied at the moment the shared substrate is constructed:

4. The FAI configuration — all configurable dimensions — is authored as substrate content within the shared substrate. This satisfies Paper 3 Claim 5 and ensures the configuration is an inspectable governance object rather than an implicit arrangement.
5. A construction record is produced in the shared substrate. The construction record names the participating Selves, documents the configuration established, and references the pre-construction authorization records from each home substrate by governance-record identifier.
6. The shared substrate begins operation only after the construction record is complete and the authorization references are verified to exist in the home substrates they reference.

These six requirements, collectively, ensure that the shared substrate begins operation as a governed architectural object under Paper 3 Claim 1. The governance floor established by this set of requirements is the minimum consistent with Paper 3's commitments.

### 7.2 Remediation: Retroactive Record Production

When governance discovers that a shared substrate is already operating — or has already dissolved — without adequate construction records, the situation is not fully correctable, but it is not entirely unaddressable. Retroactive remediation follows a defined path.

**Step 1: Produce what records are possible.** The participating Selves' governance authorities work together to produce the documentation that can be retroactively reconstructed. If pre-construction discussions occurred but were not documented, those discussions should be documented now to the extent they can be reconstructed from available evidence (communications, meeting records, technical artifacts). If a configuration was implicitly agreed upon and can be inferred from the shared substrate's actual behavior, that inferred configuration should be authored as substrate content now.

**Step 2: Document what cannot be retroactively reconstructed.** Some elements of the pre-construction record cannot be retroactively produced: there is no way to certify after the fact that joint authorization occurred before construction if no record of that authorization was made at the time. This limitation must be documented explicitly. The governance record should contain a notation that the construction record was produced retroactively and that elements unavailable for retroactive reconstruction are identified.

**Step 3: Treat the governance gap as a process dispute.** The absence of pre-construction authorization records constitutes a governance gap that affects the legitimacy of every governance decision made during the ungoverned operation. This gap should be registered as an open process dispute in the governance record, naming the scope of the gap (which FAI event or events were affected, which decisions lack authoritative governance foundation) and documenting how the participating governance authorities have agreed to treat those decisions given the gap.

**Step 4: Do not treat retroactive production as equivalent to prospective authorization.** Retroactively produced records serve the governance record's integrity function — they make the gap visible, document what can be known, and create a foundation for learning — but they do not retroactively legitimize the construction. Governance decisions made during the ungoverned period remain governance-groundless at their time of making. The retroactive record production makes this visible in the governance record rather than hiding the gap.

**Step 5: Establish compliant construction governance for all future events.** The remediation process should produce, as its final output, a commitment — authored as substrate content in each participating Self's home substrate — that future inter-Self events between these Selves will be constructed under the pre-construction and at-construction requirements of §7.1. The past governance gap should not recur.

The retroactive remediation path does not resolve the governance failures listed in §5; it manages them. The determinism contract failure, the unresolvable process disputes, and the degraded trust calibration are consequences that persist. Retroactive remediation's function is to prevent further accumulation of governance void and to give governance practitioners the most complete record possible given the situation they are in.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-1: Ungoverned Construction — A Shared Substrate That Begins Operation Without Pre-Construction Authorization or Construction Record, Violating Paper 3 Claim 1 and Paper 1 Claim 3, Analog of Paper 2 Ungoverned Birth (B3.10).* CKS Derivation Note D3.02 (#577). May 15, 2026. ORCID: 0009-0004-8065-3235.
