# Additional Composition Pair: Determinism Contract and Non-Delegation Principle

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two architectural commitments in the CKS pattern — the Determinism Contract (D2.66) and the Governance Non-Delegation Principle (D2.43) — each govern a distinct dimension of how governance operates in the shared substrate. Composed, they produce three governance requirements that neither commitment produces alone. First, the determinism contract requires governance-traceable reproducibility, not merely computational reproducibility: an automated decision that is algorithmically deterministic still fails the contract if its decision logic is not authored substrate content traceable to human governance authorization. Second, pre-authorized governance labor — the automation mode permitted under D2.43 — is the specific automation architecture that satisfies both commitments simultaneously, because the pre-authorization is itself authored substrate content and the authorization chain is navigable by any observer. Third, violating the non-delegation principle by delegating governance authority to automated systems necessarily violates the determinism contract as well, because automated governance decisions whose logic is not authored by human governance cannot satisfy the contract's write-addressability and source-of-truth guarantees. Any "governed AI coordination architecture with automation and governance auditability" must address these three requirements, and governance-traceable determinism specifically forecloses the adversarial argument that computationally deterministic automation satisfies the determinism contract.

---

## 1. Pair Identification

**Commitment A — The Determinism Contract (D2.66).** Governance decisions recorded in the shared substrate must be reproducible from authored governance records alone. The contract states five guarantees: the same substrate state yields the same content when read; the same substrate state under the same orchestration rules yields equivalent cell-level behavior at the write layer; every substrate state change has a locatable origin in a writer, rule, and rationale; conflict states are preserved rather than silently collapsed; and the substrate is the source of truth for what has been decided and by what authority. The five guarantees bind the representation layer — what the substrate carries — and not the model-output layer.

**Commitment B — The Governance Non-Delegation Principle (D2.43).** Governance authority over the shared substrate cannot be delegated to automated systems. The architecture distinguishes authority from labor: authority — the right to determine what is decided and on what basis — is non-delegable and must remain with human governance; labor — the execution work of applying pre-authorized governance decisions — is allocable and may be automated. What D2.43 permits is pre-authorized governance labor: automated execution that references a human-authored pre-authorization record in the substrate. What it prohibits is automated governance: systems that determine the substance of governance decisions without that substance being authored by human governance.

---

## 2. The Governance Scenario

A governance event uses extensive automated execution — multiple parallel automated workflows processing registrations, assignments, communications, and status updates. The automation is D2.43-compliant: each workflow operates under a pre-authorization record that is authored substrate content, specifying what the workflow may do and under what conditions. Post-event, a governance audit must verify two things simultaneously. First, that governance authority was properly exercised — that the automated workflows acted under human governance authorization and did not themselves determine the substance of governance decisions. Second, that the governance record satisfies the determinism contract — that an observer reading the substrate records can reproduce, from those records alone, what was decided, by what authority, and why.

Both commitments apply to the same artifact: the substrate record that the automated workflows produced. The audit must establish that the record is both authority-compliant (D2.43) and governance-reproducible (D2.66). The scenario is not contrived. Any governance operation that uses automation at scale — and any post-event audit of such an operation — faces exactly this requirement. The composition is what the audit must verify; neither commitment alone is sufficient.

---

## 3. Non-Obvious Governance Requirements from the Composition

**Requirement 1 — Governance-traceable determinism is a higher bar than computational determinism.** A well-engineered automated workflow can be computationally deterministic in the standard software sense: given the same inputs, the algorithm produces the same outputs, every time, verifiably. A practitioner familiar with software engineering might argue that this satisfies the determinism contract: the system is reproducible, the outputs are predictable, what more could reproducibility require?

The composition establishes that computational reproducibility is necessary but not sufficient. The determinism contract requires governance-traceable reproducibility: the decisions recorded in the substrate must be traceable to authored governance content that a human observer can read and evaluate. The distinction turns on the location of the decision logic. In computationally deterministic automation, the decision logic lives in code — in algorithms, in model parameters, in configuration files that are not authored governance records. The substrate records reflect the outputs of that logic, but the logic itself is not in the substrate and is not authored by human governance. An auditor reading the substrate can confirm that the automation ran, but cannot confirm from the substrate records alone what reasoning produced the outcome. The write-addressability guarantee of the determinism contract — that every substrate state change has a locatable origin in a writer, rule, and rationale — is not satisfied by code provenance. It is satisfied only when the decision logic is authored substrate content.

This requirement forecloses a specific adversarial argument: that because an automated system is computationally deterministic, it satisfies the determinism contract, and governance-traceable determinism is an unnecessary additional requirement. The composition shows that the adversarial argument confuses two different reproducibility properties. Governance-traceable determinism is not a stricter version of computational determinism; it is a different property, operating at a different architectural layer, binding what the substrate carries rather than what an algorithm computes.

**Requirement 2 — Pre-authorized labor is the automation architecture that satisfies both commitments simultaneously.** The composition identifies a specific automation approach — pre-authorized governance labor under D2.43 — as the approach that satisfies both commitments at the same time, not as a compromise between them.

The mechanism is precise. The pre-authorization record is authored substrate content: a human governance decision, written into the substrate, specifying what an automated workflow may do, under what conditions, and with what scope. The automated workflow's execution references that pre-authorization record. The substrate record of any automated action therefore carries a complete and navigable authorization chain: automated action → pre-authorization record → human governance authorization. This chain satisfies D2.66 because every automated substrate write has a locatable origin traceable to authored governance content. It satisfies D2.43 because governance authority — the determination of what may be done — was exercised by human governance in the pre-authorization, not by the automated workflow at execution time.

Pre-authorized labor is not a workaround that narrowly threads both constraints. It is the designed solution that correctly partitions what the architecture keeps separate: authority, which is non-delegable, and labor, which is allocable. An automated workflow operating under pre-authorized governance labor is not a concession to automation pressure. It is the automation approach the architecture was designed to support.

**Requirement 3 — Unpermitted delegation of governance authority necessarily violates the determinism contract.** The non-delegation principle prohibits delegating governance authority to automated systems. When that prohibition is violated — when an automated system is permitted to determine the substance of governance decisions — the composition shows that the determinism contract fails as a consequence, not merely as a separate problem.

The mechanism is as follows. An automated system that determines governance decisions produces substrate records reflecting those decisions. But the decision logic — the reasoning by which the automated system chose the outcome — is not authored governance content. The substrate records carry the outputs of that logic, but the logic itself is not traceable to any authored human governance specification. This means the write-addressability guarantee fails: the origin of the governance decision is the automated system's internal logic, not a human-authored rule or rationale. The source-of-truth guarantee also fails: the substrate records do not tell an observer what reasoning produced the outcome, because that reasoning was not authored into the substrate.

The implication runs in one direction: violation of D2.43 in the governance-authority domain implies violation of D2.66 in the same domain. The converse does not generally hold — a substrate can fail the determinism contract for other reasons without delegating governance authority — but in the governance-decision domain, undelegated automation produces a black box: substrate records whose decision logic cannot be recovered from the records themselves. This connects the non-delegation anti-pattern to the black-box substrate anti-pattern through the composition. Automated governance and opaque governance are not independent failure modes; the former produces the latter through the mechanism the composition identifies.

---

## 4. Prior-Art Significance

Governance-traceable determinism as distinct from computational determinism, pre-authorized labor as the jointly compliant automation architecture, and the implication from non-delegation violation to determinism contract failure are specific governance properties of this composition. They are not derivable from either commitment examined in isolation, and they are not addressed by prior work that treats automation and governance auditability as separable concerns.

Any "governed AI coordination architecture with automation and governance auditability" that satisfies both requirements must address these three properties. Work that satisfies computational reproducibility but not governance traceability has not satisfied the determinism contract. Work that automates governance labor without pre-authorization records has not satisfied either commitment. Work that treats determinism violations and non-delegation violations as independent problems has not observed the implication the composition establishes.

The prior-art gap is narrow and specific: not the general idea of auditable automated systems, which is well-developed, but the specific requirement that the decision logic behind governance decisions must itself be authored substrate content — not just code, not just logs, not just outputs — and the specific automation architecture (pre-authorized labor) that achieves this while permitting automation at scale.

---

## 5. Operational Test

For any automated governance record in a substrate making D2.66 and D2.43 compliance claims, an auditor can verify the following three conditions from the substrate records alone, without access to external code, configuration files, or agent memory:

**(a) Authorization chain completeness.** The automated action references a pre-authorization record that is authored substrate content, and that pre-authorization record is itself traceable to a human governance authorization. The chain — automated action → pre-authorization record → human governance authorization — must be present and navigable within the substrate. A record that references only code provenance, a log entry, or an external system state does not satisfy this condition.

**(b) Chain navigability.** An observer reading the substrate records can traverse the complete chain from any automated action to the human governance authorization that permitted it, using only information carried in the substrate. No step in the chain requires consulting a resource outside the substrate — no code repository, no configuration database, no runtime log — to establish what authorized the action.

**(c) Absence of unanchored decision logic.** No automated decision logic is present in the substrate records that lacks a corresponding authored governance specification. Every parameter, condition, and scope boundary that the automated workflow applied must be traceable to authored substrate content. Decision logic that resides only in code and that influenced governance outcomes fails this condition, even if the code is version-controlled and the outputs are logged.

A substrate that satisfies all three conditions is governance-traceable determinism compliant in the sense this composition establishes. A substrate that satisfies (a) and (b) but fails (c) has pre-authorized its automation but allowed unanchored decision logic to influence governance outcomes — a partial compliance that fails the determinism contract. A substrate that fails (a) has not achieved pre-authorized governance labor at all and violates D2.43 in addition to D2.66.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Additional Composition Pair: Determinism Contract and Non-Delegation Principle.* Derivation Note D4.25 (#630), CKS Derivation Note Series. May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
