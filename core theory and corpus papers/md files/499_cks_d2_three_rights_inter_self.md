# Three Rights at Inter-Self Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D1.02 commits that all six Paper 1 architectural properties hold within the shared substrate established for inter-Self coordination. Among those six is Paper 1's human-governed commitment: the right of humans to inspect, modify, and override substrate content and orchestration rules at any time. D2.04 formalizes the operational meaning of that commitment at inter-Self scope — how each of the three rights is exercised when the shared substrate is governed jointly by the governance structures of multiple participating Selves. The note establishes that all three rights exist structurally at inter-Self scope exactly as they exist at intra-Self scope; what changes is the governance mechanism through which each right is exercised. The inspect right is fully open to all participating governance structures without permission from the contributing Self. The modify right requires authorization per the jointly-configured approval mechanics. The override right exists structurally and is exercised through joint mechanism, with emergency override protocols available as governance-configurable substrate content. Four failure modes the note defends against are enumerated, and an operational test for each right is provided.

---

## 1. D2.04 as Operational Decomposition of D1.02

D1.02 commits that all six Paper 1 architectural commitments hold within the shared substrate. Paper 1's human-governed commitment — the sixth of those commitments, and architecturally the one on which the others depend — names three rights: the right to inspect any substrate content and orchestration rule, the right to modify any substrate content and orchestration rule, and the right to override any operation, default, or output that touches substrate content or orchestration rules. These three rights together are what "governance" names in the CKS pattern, and D1.02 extends them, without weakening them, to the shared substrate's inter-Self perimeter.

D2.04 formalizes what this extension means operationally. The shared substrate is a coordination medium spanning more than one Self's home governance perimeter. Authority over it is held jointly by the governance structures of the participating Selves, with jointly-configured approval mechanics determining how that joint authority is exercised. D2.04 asks, for each of the three rights, two questions: what does the right mean at inter-Self scope, and how does the jointly-configured approval mechanics govern its exercise? The answers are the operational decomposition of D1.02 this note contributes.

The central finding of D2.04 can be stated simply: joint authority modifies the governance mechanism for each right, not the existence of the right. The three rights are preserved structurally at inter-Self scope. Governance practitioners holding authority over any participating Self hold those rights over the shared substrate. The change from intra-Self to inter-Self scope is in how the rights are exercised — through jointly-configured approval mechanics rather than through single-Self authority — and not in whether the rights exist or who holds them in structural terms.

---

## 2. The Inspect Right at Inter-Self Scope

### 2.1 What the inspect right requires at this scope

The inspect right at intra-Self scope authorizes any governance practitioner with appropriate access to read any substrate content and any orchestration rule directly, at the time of their choosing, without requiring approval or intermediation. D1.02 extends this right to the shared substrate.

At inter-Self scope, the inspect right is held by all participating Selves' governance structures simultaneously. This means: any governance practitioner with authority over any participating Self can inspect any content in the shared substrate at any time during the Full Aspect Integration (FAI) event. The contributing Self holds no gate over other participants' inspection rights once content is in the shared substrate.

This is not merely a policy choice about openness — it is the architectural property that makes the shared substrate a genuine coordination medium. An exchange medium where each contributor controls what other participants can see is not a shared substrate in the CKS sense; it is a series of conditioned information pushes. The inspect right being fully open to all participating governance structures is what establishes the shared substrate as an environment in which all parties can base governance decisions on the same content, with the same direct access, under the same architectural rights.

### 2.2 What does not change

The inspect right's operational content — direct read access to substrate content and orchestration rules, at the time of the inspector's choosing, without approval gating or intermediation — is identical at inter-Self scope to its content at intra-Self scope. The jointly-configured approval mechanics do not govern the inspect right in the sense of requiring approval before inspection can occur; the approval mechanics govern modify and override, not inspect. Inspection at inter-Self scope remains an exercisable right, not a procedural step inside a governed workflow.

### 2.3 Operational test for the inspect right at inter-Self scope

The inspect right is implemented at inter-Self scope if and only if both of the following are true during the FAI event:

(a) Any governance practitioner with authority over any participating Self can read any shared-substrate content and any orchestration rule within the shared substrate, directly and at the time of their choosing, without requiring permission from the contributing Self or from any other participant's governance structure.

(b) No jointly-configured approval mechanic, contributing-Self access control, or runtime middleware layer can in principle prevent (a) for authorized governance practitioners.

A system in which the contributing Self can restrict what other participants' governance structures may inspect in the shared substrate fails (a) and does not implement the inspect right at inter-Self scope, regardless of how much content is otherwise accessible.

---

## 3. The Modify Right at Inter-Self Scope

### 3.1 What the modify right requires at this scope

The modify right at intra-Self scope authorizes governance practitioners to write to, edit, or delete any substrate content and any orchestration rule, with the change taking effect as substrate state. At intra-Self scope, this right is exercised under the governance authority of the single Self whose substrate it is.

At inter-Self scope, the shared substrate carries content from multiple contributing Selves, and its governance perimeter spans multiple Selves' home governance structures. Modifying content within the shared substrate therefore requires authorization per the jointly-configured approval mechanics. The level of authorization required for a given modification is itself governance-configurable per event — the approval mechanics are substrate content authored under joint authority and may specify different thresholds for different types of modification.

An important asymmetry applies to the contributing Self's own contributed content: if the jointly-configured approval mechanics authorize a contributing Self's governance structure to modify its own contributions without additional joint authorization, that unilateral modification is architecturally valid. The approval mechanics determine what requires joint authorization; they do not uniformly require joint authorization for every modification regardless of its scope and provenance.

### 3.2 What changes and what does not

The modify right exists structurally at inter-Self scope. Every participating Self's governance structure holds the modify right over the shared substrate. What changes is the authorization pathway: modifications require approval per jointly-configured mechanics rather than per single-Self authority. The jointly-configured approval mechanics are themselves governance-configurable substrate content authored under joint authority; they are not a restriction imposed on the modify right from outside, but a specification of how the right is exercised at this scope.

All modifications to shared-substrate content must be recorded with provenance — the authoring governance structure, the authorization pathway, and the authorization result must be retained as substrate content. This provenance requirement follows from Paper 1's path-retraceability commitment applied to the shared substrate by D1.02 inheritance.

### 3.3 Operational test for the modify right at inter-Self scope

The modify right is implemented at inter-Self scope if and only if both of the following are true during the FAI event:

(a) Any governance practitioner with authority over any participating Self can exercise the modify right over shared-substrate content, with the authorization pathway specified by the jointly-configured approval mechanics determining what authorization is required for each class of modification.

(b) Modifications are recorded with full provenance — authoring governance structure, authorization pathway, and authorization result — as substrate content, accessible through the inspect right.

A system in which one participating Self's governance structure cannot in principle modify any shared-substrate content, even when the approval mechanics would authorize it, fails (a) and does not implement the modify right at inter-Self scope.

---

## 4. The Override Right at Inter-Self Scope

### 4.1 What the override right requires at this scope

The override right at intra-Self scope authorizes governance practitioners to supersede any operation, default, or AI-produced output that touches substrate content or orchestration rules, without requiring justification to the system. At intra-Self scope, this right is exercised by the single Self's governance authority.

At inter-Self scope, the override right exists structurally and applies to shared-substrate content. Exercising override governance over content where joint authority applies requires joint governance authorization per the approval mechanics. This is the same structure that governs the modify right at inter-Self scope, applied to the specific category of governance action the override right names: supersession without requiring system justification.

### 4.2 Emergency override protocols as governance-configurable substrate content

The joint authorization requirement for override does not eliminate the possibility of unilateral action in emergency conditions. Emergency override protocols — which allow one participating Self's governance structure to act unilaterally when specified conditions are met — are themselves governance-configurable as substrate content. They are authored before the emergency conditions arise, under the joint governance authority applicable to the shared substrate. When emergency conditions are met, the unilateral action that follows is not an exception to the joint-governance structure; it is an execution of pre-authorized governance rules under conditions those rules specified.

This framing matters architecturally. The override right's core property at intra-Self scope is that it is available without requiring justification to the system at the moment of exercise. Emergency override protocols at inter-Self scope preserve this property: the governance practitioner exercising emergency override does not justify the override to the system in the moment; they execute authority pre-authorized in authored substrate content. The governance work occurred at rule-authoring time, not at override time. This is Paper 1's governance-as-available-authority property preserved at emergency inter-Self scope.

### 4.3 Override events as substrate content

Override governance events at inter-Self scope must be recorded as substrate content, carrying the authorization source and the provenance of the superseded content and the superseding action. This recording obligation is an extension of the inspect right: any governance practitioner can inspect the history of override events in the shared substrate, including their authorization basis. A system in which override actions are not recorded as inspectable substrate content fails to implement the override right at inter-Self scope in the CKS sense.

### 4.4 Operational test for the override right at inter-Self scope

The override right is implemented at inter-Self scope if and only if both of the following are true during the FAI event:

(a) Any governance practitioner with authority over any participating Self can exercise the override right over shared-substrate content in the conditions the jointly-configured approval mechanics specify, including under emergency override protocols where those protocols are configured as substrate content.

(b) Override governance events are recorded as substrate content — including authorization source and provenance of both the superseded and the superseding content — accessible through the inspect right.

A system in which no governance practitioner can in principle supersede shared-substrate content or orchestration rules fails (a) and does not implement the override right at inter-Self scope.

---

## 5. Joint Authority Modifies the Mechanism, Not the Existence of the Rights

The analysis across §§2–4 yields a single structural principle: joint authority at inter-Self scope modifies the governance mechanism for each right, not the existence of the right.

At intra-Self scope, all three rights are exercised under a single Self's governance authority. No cross-boundary authorization is required because the substrate's governance perimeter is bounded by a single Self's home perimeter. At inter-Self scope, the shared substrate's governance perimeter spans multiple home perimeters. The three rights continue to exist and continue to be held by all participating governance structures. The change is exclusively in the authorization pathway: from single-Self authority to jointly-configured approval mechanics.

This principle is Paper 1 Claim 3's structural commitment preserved at inter-Self scope, not replaced or weakened by it. The rights are not newly created at inter-Self scope; they are not demoted to procedural promises; they are not made conditional on the contributing Self's approval. They are the same structural commitments, operating through a governance mechanism adapted to the multi-perimeter context the shared substrate occupies.

The implication for implementation is direct. A shared-substrate deployment that implements the six Paper 1 commitments by D1.02 inheritance must implement all three rights at inter-Self scope as structural architectural properties. The jointly-configured approval mechanics are the mechanism through which those properties are exercised; they are not a layer above or outside the rights but the governance specification of how the rights operate at this scope.

---

## 6. Failure Modes This Note Defends Against

Four failure modes are expressly closed by D2.04.

**Failure mode 1 — Inspect right gatekept by the contributing Self.** An implementation in which a contributing Self controls what other participants' governance structures may inspect in the shared substrate fails the inspect right at inter-Self scope. The contributing Self may have governance rights over its own contributed content in other respects, but the inspect right of other participating governance structures is not conditional on the contributing Self's permission. Once content is in the shared substrate, all joint-authority holders may inspect it.

**Failure mode 2 — Modify right exercised unilaterally over another Self's contributed content without joint authorization.** An implementation in which one Self's governance structure modifies another Self's contributed content without authorization per the jointly-configured approval mechanics fails the modify right at inter-Self scope. The approval mechanics specify the authorization threshold for each class of modification; modification without satisfying that threshold is not a governance exercise of the modify right but a governance bypass of the shared substrate's authority structure.

**Failure mode 3 — Override right absent at inter-Self scope.** An implementation that treats the override right as inapplicable to the shared substrate — on the grounds that joint governance makes override impractical or that no single governance structure holds override authority — fails the override right at inter-Self scope. The override right exists structurally. Joint mechanism governs how it is exercised; it does not cancel the right's existence. A shared substrate from which no governance structure can in principle supersede a content element or orchestration rule is not human-governed in the CKS sense.

**Failure mode 4 — Three rights as procedurally promised rather than structurally held at inter-Self scope.** An implementation in which the three rights are honored by workflow convention, vendor policy, or inter-organizational agreement — rather than as architectural properties of the shared substrate's design — fails D1.02's commitment that Paper 1's human-governed property holds within the shared substrate. The commitment is architectural: the rights must be available as properties of the design, not as procedural promises that depend on continued cooperation among the participating Selves. The distinction between structural availability and procedural promise is the same distinction Paper 1's human-governed definition draws at intra-Self scope, extended to inter-Self scope by D1.02.

---

## 7. Conclusion

D2.04 formalizes the operational meaning of Paper 1's human-governed commitment — the three rights to inspect, modify, and override — as applied within the shared substrate at inter-Self scope. The inspect right is fully open to all participating governance structures, without permission from the contributing Self, making the shared substrate a genuine coordination medium rather than a one-directional information push. The modify right is held by all participating governance structures and exercised per jointly-configured approval mechanics, with modifications recorded with full provenance. The override right exists structurally at inter-Self scope and is exercised through joint mechanism, with emergency override protocols available as governance-configurable substrate content that pre-authorize unilateral action under specified conditions.

The structural principle that unifies all three rights at this scope: joint authority modifies the governance mechanism, not the existence of the rights. Paper 1 Claim 3's structural commitment is preserved at inter-Self scope exactly as it exists at intra-Self scope. What changes is the authorization pathway. What does not change is the architectural guarantee that humans hold the three rights over substrate content at all times, regardless of scope.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Three Rights at Inter-Self Scope.* May 14, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
