# All Six Paper 1 Commitments Hold Within the Shared Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 introduces the shared substrate as the architectural object of inter-Self coordination: a CKS substrate constructed temporarily to mediate between two or more CKS-governed Selves. By calling it a CKS substrate, Paper 3 commits to all six Paper 1 architectural commitments holding within the shared substrate's governance perimeter. This note formalizes that commitment precisely. The commitment is bundled: it is not enough for a shared substrate to inherit some Paper 1 commitments; a compliant shared substrate carries all six. Each commitment is separately violable, and a system that violates any one does not implement a compliant shared substrate. The six commitments apply within the shared substrate's temporary inter-Self perimeter; they do not automatically extend to the organizational spaces outside that perimeter. This note also provides an operational test: six binary questions, one per commitment, that an independent observer can answer during an active FAI event to verify whether each commitment holds within the shared substrate.

---

## 1. The inheritance relationship

Paper 3's shared substrate is not named a "substrate" by analogy. The source paper states explicitly: "Within its scope of operation, the shared substrate carries Paper 1's six architectural commitments." That sentence is Paper 3's architectural commitment, and it is the source claim this note formalizes.

The six Paper 1 commitments are:

1. **Hybrid architecture** — the substrate-LLM division, with a governance boundary separating the two.
2. **Conflict preservation** — conflicts as first-class objects in the substrate, both sides retained.
3. **Human-governed authority** — the three rights (inspect, modify, override) held by humans at all times.
4. **AI as substrate mediator** — five mediator properties governing LLM behavior relative to the substrate.
5. **Tool-agnosticism** — three minimal host requirements, no dependency on a specific platform.
6. **Linear-cost composition** — adding another unit does not compound governance cost.

When Paper 3 commits to a shared substrate, it commits to all six of these holding within the shared substrate's perimeter. The inheritance is not selective. A system that carries five of the six commitments within its coordination medium does not implement a Paper 3 compliant shared substrate; it implements something else, and the difference matters architecturally.

This note covers each of the six at inter-Self scope, states the "within its scope" qualifier precisely, explains why the bundled commitment is the load-bearing prior-art claim, and provides the operational test.

---

## 2. Each commitment at inter-Self scope

### 2.1 Hybrid architecture (Paper 1 Claim 1)

At inter-Self scope, the hybrid architecture commitment means: the shared substrate maintains the substrate-LLM division within its governance perimeter. Any LLM operating within the shared substrate context does so as a governed mediator — reading from and writing to the shared substrate under orchestration rules — not as an autonomous agent over shared-substrate content. The hybrid division does not dissolve at the inter-Self boundary.

Inter-Self coordination is not conducted by two LLMs exchanging messages that bypass the substrate; it is conducted within the shared substrate, with LLMs operating as mediators under orchestration rules. The architectural significance of this commitment at inter-Self scope is the same as at cell scope: it places the inter-Self coordination medium in the human-governable substrate layer, not in the LLM inference layer. The exchange medium is explicit, inspectable, and subject to human authority, not a product of LLM-to-LLM message-passing opaque to governance. This is the direct architectural foil that Paper 3 names: opaque agent-to-agent communication, in which inter-AI exchange is conducted through patterns whose substantive content is not human-governable as authored substrate.

### 2.2 Conflict preservation (Paper 1 Claim 2)

At inter-Self scope, conflict preservation means: conflicts arising within the shared substrate during an FAI event are preserved as first-class objects — both sides retained, not auto-resolved, not silently dropped. This commitment is the direct foundation for Paper 3's three-tier conflict-handling mechanism (Claim 3), whose preserve tier inherits from this Paper 1 commitment applied at the shared substrate's perimeter.

Conflicts within the shared substrate arise when contributing Selves hold positions — on DNA-layer content or action-layer content — that are incompatible or inconsistent. Paper 1 commits to conflict preservation at cell scope as an architectural property, not a deployment option. Paper 3 extends that commitment to the shared substrate: conflicts at inter-Self scope are visible, retained, and available for deliberate handling through the three-tier mechanism. No orchestration rule within the shared substrate may auto-resolve a conflict by silently discarding one side.

### 2.3 Human-governed authority (Paper 1 Claim 3)

At inter-Self scope, the three rights — inspect, modify, override — apply to shared-substrate content at any time. This means:

- The humans who hold governance authority over the participating Selves retain the right to inspect any content within the shared substrate, including content contributed by the other party.
- They retain the right to modify shared-substrate content and the orchestration rules governing how the shared substrate operates.
- They retain the right to override any LLM-produced output or orchestration-driven operation touching shared-substrate content.

Human-governed authority holds during construction (when the shared substrate is being established and contributed content is being loaded), during operation (during the FAI event proper), and during dissolution (when outputs are being recorded and the shared substrate is being closed). The commitment is architectural, not procedural: the rights are a design property of the shared substrate, not a promise that depends on particular deployment conditions or workflow approvals.

The "within its scope" qualifier applies here as it does to every commitment: these three rights govern shared-substrate content within the perimeter. Each Self's home governance authority over its own perimeter continues to operate per Paper 2 and is not altered by the shared substrate's construction.

### 2.4 AI as substrate mediator (Paper 1 Claim 4)

At inter-Self scope, any LLM operating within the shared substrate context operates as a substrate mediator with the five properties Paper 1 establishes:

1. Reads from the shared substrate as the primary source of coordination state.
2. Writes to the shared substrate under orchestration rules.
3. Holds no shadow state outside the shared substrate that could influence the inter-Self coordination in ways not visible to governance.
4. Exercises no authority over shared-substrate content — authority over the shared substrate belongs to the humans with governance rights, not to any LLM.
5. Has its outputs recorded in the shared substrate with attribution.

The AI-as-mediator commitment forecloses a specific class of inter-Self architecture: one in which an LLM makes coordination decisions, manages shared state, or authors content that does not pass through the substrate. Within a Paper 3 shared substrate, the LLM is a governed participant, not the coordination medium itself.

### 2.5 Tool-agnosticism (Paper 1 Claim 5)

At inter-Self scope, tool-agnosticism means: the shared substrate is implementable on any host satisfying the three minimal host requirements Paper 1 establishes — persistent structured state, human read/write access, and LLM access to substrate content. The shared substrate is not tied to a specific inter-organizational communication platform. It does not require a proprietary substrate vendor, a specialized multi-agent runtime, or a specific API format for inter-Self exchange. Any implementation that satisfies the three minimal host requirements and carries the other five commitments within its perimeter is a valid implementation of the Paper 3 shared substrate.

This commitment matters at inter-Self scope because coordinating Selves may not share infrastructure. Tool-agnosticism means that Selves operating on different substrate hosts can construct a shared substrate together, provided both satisfy the three minimal requirements and the shared substrate satisfies all six commitments within its perimeter.

### 2.6 Linear-cost composition (Paper 1 Claim 6)

At inter-Self scope, linear-cost composition means: adding another Self's aspects to the shared substrate costs approximately the same as adding the first. Governance of the shared substrate does not compound super-linearly with the number of participating Selves. The cost of maintaining all six commitments within the shared substrate scales linearly, not combinatorially, with the number of contributing Selves and the volume of aspects they contribute.

This commitment forecloses an architecturally costly alternative: shared substrates whose governance cost grows quadratically or combinatorially with the number of participating parties. Paper 3's shared substrate can serve two-Self FAI events and can generalize to the n-ary case described in Paper 3's Claim 2 without requiring governance mechanisms that scale with the combinatorial product of participants.

---

## 3. The "within its scope" qualifier

The six commitments formalized in §2 hold within the shared substrate's governance perimeter — the temporary inter-Self coordination space that exists for the duration of an FAI event. The qualifier is precise in two directions.

**Inward:** Every piece of content within the shared substrate is subject to all six commitments. There is no region inside the shared substrate's perimeter that is exempt from any one of them. Content contributed by either (or any) Self, orchestration rules governing the FAI event, conflict objects arising during the event, LLM outputs produced during the event — all of these are within scope and all six commitments apply to all of them.

**Outward:** The six commitments, as formalized at inter-Self scope, govern the shared substrate's perimeter. They do not automatically govern each participating Self's home governance perimeter. Paper 2's commitments continue to govern each Self's home perimeter independently. The shared substrate's construction does not alter the governance architecture of any participating Self's home perimeter; it creates a new, temporary coordination space that is governed by all six commitments while it exists.

The dissolution of the shared substrate at the FAI event's completion does not violate any of the six commitments. The shared substrate is by design temporary — its lifespan is the FAI event — and dissolution is a governed operation, not a governance lapse. What persists after dissolution returns to each Self's home governance perimeter under Paper 2's architecture.

---

## 4. Why the bundled commitment is the load-bearing prior-art claim

The prior-art significance of D1.02 rests on the commitment being bundled, not selective.

Each of the six Paper 1 commitments independently forecloses a class of alternative architecture. Hybrid architecture forecloses autonomous-LLM coordination. Conflict preservation forecloses silent auto-resolution. Human-governed authority forecloses LLM-autonomous content management. AI-as-mediator forecloses LLM-as-coordinator patterns. Tool-agnosticism forecloses platform-captive coordination media. Linear-cost forecloses combinatorially-expensive governance structures.

Any coordination medium for inter-Self exchange that satisfies all six commitments within its perimeter is a Paper 3 shared substrate. Any coordination medium that satisfies some but not all six is architecturally distinct and does not satisfy Paper 3's foundational Claim 1.

This creates a precise perimeter for prior-art coverage. A subsequent system claiming novelty for a shared coordination medium with five of the six commitments — say, all six except conflict preservation — would be architecturally distinct from the Paper 3 shared substrate at a specific, well-defined point. The six commitments are not interchangeable design dimensions; each names a specific architectural property that is independently required and independently violable. D1.02's formalization of all six as a bundle is what makes the boundary clear.

The bundle also forecloses the adversarial claim that each Paper 1 commitment at inter-Self scope is a separate invention. Paper 3 commits to all six at once, as a single architectural package; the inter-Self scope does not create six separable inventions, because the shared substrate is one architectural object and its commitments are inherited as a unit.

D1.02 is the inter-Self scope analog of C1.06 and C1.07 in the derivation series, which formalize that Paper 2's recursive applicability of Paper 1 commitments at aspect and Self scope is not incidental but architectural. D1.02 formalizes the same principle at the inter-Self scope: the shared substrate inherits all six Paper 1 commitments not incidentally but as the direct consequence of being a CKS substrate.

---

## 5. Operational test

An independent observer can determine whether all six Paper 1 commitments hold within a given shared substrate during an active FAI event by asking six binary questions, one per commitment. All six must be answered affirmatively for the shared substrate to satisfy Paper 3's foundational Claim 1.

**Test 1 — Hybrid architecture.** Can the observer confirm that all LLMs operating within the shared substrate context are reading from and writing to the shared substrate under documented orchestration rules, and that no LLM is autonomously authoring, modifying, or resolving shared-substrate content outside those rules? If yes: the hybrid commitment holds within this perimeter.

**Test 2 — Conflict preservation.** Can the observer confirm that any conflict arising between contributing Selves' content within the shared substrate is present in the substrate as a retained first-class object — both sides visible, no side silently discarded or auto-resolved — and that the shared substrate's orchestration rules contain no mechanism for discarding one side of a conflict without explicit human or escalation authorization? If yes: the conflict-preservation commitment holds within this perimeter.

**Test 3 — Human-governed authority.** Can the observer confirm that a human with appropriate access can at this moment (a) read any content within the shared substrate and any orchestration rule governing it, (b) write to or modify any such content or rule, and (c) override any LLM-produced output touching the shared substrate, without scheduling, approval gating, or runtime intermediation? If yes: the human-governed authority commitment holds within this perimeter.

**Test 4 — AI as substrate mediator.** Can the observer confirm that no LLM operating within this shared substrate context holds shadow state — state relevant to the inter-Self coordination that is not recorded in the shared substrate — and that no LLM's outputs affecting shared-substrate content are produced and applied without being recorded with attribution in the substrate? If yes: the AI-as-substrate-mediator commitment holds within this perimeter.

**Test 5 — Tool-agnosticism.** Can the observer confirm that the shared substrate's host satisfies the three minimal requirements (persistent structured state, human read/write access, LLM access to substrate content) and that the shared substrate does not depend on any specific proprietary platform, vendor API, or specialized runtime beyond those minimal requirements? If yes: the tool-agnosticism commitment holds within this perimeter.

**Test 6 — Linear-cost composition.** Can the observer confirm that adding a third participating Self's aspects to this shared substrate would require governance effort approximately equal to the effort of adding the second — rather than substantially greater — and that no element of the shared substrate's governance architecture grows combinatorially with the number of participating Selves? If yes: the linear-cost composition commitment holds within this perimeter.

A shared substrate that passes all six tests satisfies Paper 3's foundational Claim 1. A shared substrate that fails any one test does not satisfy Claim 1 at the point of failure; the failing commitment names exactly which architectural property the implementation is missing.

---

## 6. Conclusion

Paper 3's commitment to the shared substrate as the architectural object of inter-Self coordination is a commitment to all six Paper 1 architectural commitments holding within the shared substrate's governance perimeter. The commitment is bundled: each of the six must hold; none is optional. Each is separately violable; violating any one produces an architectural object that is not a Paper 3 compliant shared substrate.

The "within its scope" qualifier is precise in both directions. Inward: all content within the shared substrate's perimeter is subject to all six commitments with no exemptions. Outward: the commitments govern the shared substrate's temporary inter-Self perimeter, not each participating Self's home governance perimeter, which continues to be governed per Paper 2.

The operational test in §5 provides six binary questions an independent observer can apply during an active FAI event. All six must pass. The test is not a debugging heuristic; it is the operational form of Paper 3's foundational Claim 1 resolved to the level of individual commitments.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *All Six Paper 1 Commitments Hold Within the Shared Substrate.* May 14, 2026. ORCID: 0009-0004-8065-3235.
