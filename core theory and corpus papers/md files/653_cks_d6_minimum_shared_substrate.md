# Minimum Valid Shared Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series note:** #653 — Phase D6 boundary case note

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The CKS theory series introduces a specific architectural object — the shared substrate — as the medium through which two or more CKS-governed organizations coordinate with each other. This note formalizes the minimum conditions a shared data mechanism must satisfy to qualify as a Paper 3-compliant shared substrate, distinguishing it from superficially similar mechanisms: shared databases, shared document repositories, shared LLM context windows, and jointly-administered message queues. Six conditions are necessary and jointly sufficient for the qualification. A mechanism that satisfies five of six does not qualify — the shared substrate is a specific architectural identity defined by all six conditions together, not a cluster of desirable properties from which a subset suffices. The note presents the six conditions, applies them to each of the four non-qualifying mechanisms to show precisely where and why each fails, and states a bidirectional boundary test for use in subsequent architectural evaluation.

---

## 1. The boundary question

Two organizations want to share AI governance content. They consider several mechanisms: a shared relational database; a shared document repository; a shared LLM context window; a jointly-administered message queue. None of these is the same as the shared substrate Paper 3 introduces. But the differences are not immediately obvious from the outside — all four mechanisms move content between organizational systems; all four can, in principle, carry AI-related material. What separates the Paper 3-compliant shared substrate from each of them?

The question is not merely taxonomic. It is the question adversarial claims in this space must answer. Any party asserting that their "joint AI coordination platform," "shared AI knowledge base," or "cross-organizational AI governance space" is equivalent to — or prior to — the shared substrate must address whether their mechanism satisfies the conditions that constitute the shared substrate's architectural identity. This note states those conditions precisely, so that both the inclusive and exclusive applications of the boundary test are unambiguous.

---

## 2. The six conditions

A shared data mechanism qualifies as a Paper 3-compliant shared substrate if and only if all six of the following conditions hold simultaneously.

**Condition 1 — Temporary by design.** The shared substrate is explicitly constructed for a bounded coordination event and dissolves at the event's completion. It is not a persistent infrastructure installation. What persists after dissolution — ranging from nothing retained to a full auditable record of the interaction — is itself governance-configured content within the substrate. The defining property is not that nothing persists, but that the shared structure's existence is event-scoped by architectural commitment, not open-ended by default. A mechanism designed as permanent shared infrastructure, with no dissolution event in its architecture, does not satisfy this condition even if it is rarely used.

**Condition 2 — All six Paper 1 commitments hold within scope.** The shared substrate inherits, from Paper 1, the full set of architectural commitments that define a CKS substrate: it is human-governed (the three rights — inspect, modify, override — are exercisable by joint governance over its content at any time); conflicts arising within it are preserved as first-class state rather than silently resolved; AI operates as a mediator over it, not as an autonomous agent within it; it is tool-agnostic (the architectural commitments hold independent of implementation); composition within it is linear-cost; and the substrate-LLM division — the hybrid commitment — is maintained. A mechanism that lacks AI mediation, that silently resolves conflicts, or in which no human authority can inspect and override content, does not satisfy this condition.

**Condition 3 — The three governance rights are exercisable under joint authority.** The inspect, modify, and override rights that Paper 1 establishes as the definition of human-governed must, within the shared substrate, be exercisable under joint governance spanning both participating organizations. Neither organization's governance perimeter fully contains the shared substrate; the governance authority over it spans both. A shared data structure in which one party holds unilateral authority — or in which no stable authority structure governs access and override rights across parties — does not satisfy this condition.

**Condition 4 — Aspects are the exchange unit.** The shared substrate must be capable of holding contributed aspects as governed substrate content, where aspects are the Paper 2 architectural object carrying constituent cells, DNA-layer content (orchestration substrates, behavior substrates, schemas, rules), and action-layer content (recorded task instances, outputs, lived experience). Content must be organized at aspect granularity — not as unstructured documents, not as flat key-value pairs, not as undifferentiated data records. A mechanism that holds content at the wrong granularity — even if it holds large volumes of AI-related material — does not satisfy this condition.

**Condition 5 — Exchange is bounded.** The shared substrate accepts DNA-layer and action-layer content; it does not accept instinct-layer content or LLM weight content. This is the inter-Self extension of Paper 2's instinct/reasoning separation: what crosses the organizational perimeter is reasoning-layer substrate content, not fast-pattern behavioral weights or raw instinct-layer processing. A shared data store that accepts any content type — including LLM weights, raw model outputs, or instinct-layer behavioral content — does not satisfy this condition.

**Condition 6 — Dissolution hand-off capability.** The shared substrate must support the four evolution loci through which FAI event outputs reach each participating organization's home substrate, and must be capable of the dissolution event that routes those outputs appropriately. This is not merely a technical persistence question; it is an architectural property: the mechanism must have dissolution as a named operation, and the hand-off to participating organizations' home substrates must be a designed part of its lifecycle. A shared store with no dissolution mechanism, no hand-off operation, and no distinction between its own content and the content that should persist in participating organizations' home substrates does not satisfy this condition.

All six conditions are necessary. No five-of-six subset is sufficient. The shared substrate is not a mechanism that scores well on most of these properties — it is a mechanism that satisfies all of them simultaneously. This conjunctive structure is what gives the shared substrate its specific architectural identity.

---

## 3. Why the four common mechanisms do not qualify

Each of the four mechanisms considered at the outset fails at least one condition. The failures are named specifically, not as criticisms of those mechanisms' utility in other contexts, but as precise statements of where their architectural identities diverge from the shared substrate.

**Shared database.** A shared relational or document database typically lacks AI mediation as an architectural property (Condition 2 fails: the database holds content but no AI operates as mediator over it in the CKS sense), typically lacks the temporary-by-design commitment (Condition 1 fails: databases are designed for persistence, not event-scoped construction and dissolution), and typically lacks the aspect-granularity exchange unit (Condition 4 fails: database records are not organized as aspects carrying DNA-layer and action-layer content). A shared database may satisfy Condition 3 if access control is jointly administered, but joint access control alone does not bring a database within the prior art's scope.

**Shared document repository.** A shared document store or knowledge base typically lacks aspect granularity (Condition 4 fails: documents are not aspects; they do not carry the structured DNA/action-layer distinction), typically lacks exchange bounding (Condition 5 fails: a document repository holds whatever documents are deposited, with no architectural enforcement of the instinct/reasoning separation), and typically lacks the full six Paper 1 commitments (Condition 2 fails: document repositories generally have no AI-as-mediator property and no conflict-preservation mechanism). Whether a document repository is temporary or persistent is an implementation choice, not an architectural commitment, so Condition 1 is indeterminate.

**Shared LLM context window.** A shared LLM context window — whether a single model context shared between two organizations or a multi-agent context visible to multiple LLM instances — lacks governance rights as an architectural property (Condition 3 fails: no human authority structure holds inspect-modify-override rights over a context window's content; the content is transient and not persistently addressable), lacks path retraceability (a component of Condition 2: context windows do not provide the substrate-level traceability Paper 1 commits to), and lacks the temporary-by-design dissolution mechanism (Condition 6 fails: context windows do not have dissolution events that route outputs to participating organizations' home substrates). The shared LLM context window is the mechanism most frequently confused with the shared substrate because both involve AI processing of cross-organizational content — but the architectural commitments are entirely different.

**Jointly-administered message queue.** A shared message queue lacks aspect granularity (Condition 4 fails: messages are not aspects), lacks exchange bounding (Condition 5 fails: queues route whatever messages are produced), lacks the AI-as-mediator property (Condition 2 fails), and typically lacks dissolution hand-off architecture (Condition 6 fails). Message queues are coordination infrastructure at the transport layer; the shared substrate is a governance artifact at the coordination layer. These are not the same architectural layer.

None of the four mechanisms qualifies. Each fails at least two conditions; most fail three or more.

---

## 4. The bidirectional boundary test

The six-condition test is bidirectional.

**Inclusive direction.** A mechanism that satisfies all six conditions qualifies as a Paper 3-compliant shared substrate, regardless of what it is called. An organization implementing a "joint AI governance space" or "cross-organizational AI coordination platform" that is temporary by design, carries all six Paper 1 commitments, holds joint governance rights, organizes content at aspect granularity, enforces exchange bounding, and supports dissolution hand-off is implementing the shared substrate within the prior art's scope. The name chosen for the mechanism does not determine its architectural identity; the six conditions do.

**Exclusive direction.** A mechanism that fails any single condition does not qualify, and coordination conducted through it is not Full Aspect Integration in the Paper 3 sense. This exclusion applies even if the mechanism satisfies five conditions robustly — the identity test is conjunctive, not approximate. An adversary cannot argue that their mechanism is architecturally equivalent to the shared substrate by demonstrating that it satisfies most of the conditions while omitting one.

The bidirectional test covers both the claim that a prior system already constitutes the shared substrate (the inclusive direction determines whether that claim falls within the prior art) and the claim that a non-conforming mechanism is equivalent to it (the exclusive direction forecloses that equivalence claim when any condition is missing).

---

## 5. Operational test

For any shared data mechanism between AI-governed organizations, apply the following test in sequence. The mechanism qualifies as a Paper 3-compliant shared substrate if and only if all six questions receive a confirmatory answer:

1. Is the mechanism explicitly constructed for a bounded event and dissolved at the event's completion, with persistence policy as governed content? *(Condition 1)*
2. Do all six Paper 1 architectural commitments — human-governed authority, conflict preservation, AI-as-mediator, tool agnosticism, linear-cost composition, substrate-LLM hybrid division — hold within the mechanism's scope? *(Condition 2)*
3. Do joint governance rights — inspect, modify, override — span both participating organizations' governance perimeters over the mechanism's content? *(Condition 3)*
4. Is the unit of exchange the aspect, with constituent cells, DNA-layer content, and action-layer content surfaced at aspect granularity? *(Condition 4)*
5. Is exchange bounded to DNA-layer and action-layer content, with instinct-layer content and LLM weights excluded by architectural commitment? *(Condition 5)*
6. Does the mechanism support dissolution with hand-off to participating organizations' home substrates as a named architectural operation? *(Condition 6)*

A "no" answer to any question is a disqualifying failure. No partial credit applies. A mechanism that fails question 2 because it lacks AI mediation does not become the shared substrate by adding AI mediation while retaining all other failures — it becomes a mechanism that now satisfies two conditions and must be re-evaluated against the remaining four.

---

## 6. Prior-art significance

The six-condition boundary test is the precise scope boundary for the shared substrate prior art. Claims involving shared AI governance mechanisms, joint AI coordination platforms, or cross-organizational AI knowledge structures fall within the prior art's scope if and only if the mechanism in question satisfies all six conditions. Claims involving mechanisms that lack any condition fall outside the shared substrate's scope — they may represent other prior art, but they are not the architectural object Paper 3 introduces.

The test's value is not exclusionary for its own sake. It is that the shared substrate has a specific architectural identity — a temporary, human-governed, jointly-authoritative, aspect-organized, exchange-bounded, dissolution-capable coordination medium — and that identity is what makes Paper 3's inter-Self coordination architecture coherent. Mechanisms that lack any component of that identity are not approximations of the shared substrate; they are different objects serving different roles.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Minimum Valid Shared Substrate.* May 15, 2026. Derivation note #653, Phase D6. ORCID: 0009-0004-8065-3235.
