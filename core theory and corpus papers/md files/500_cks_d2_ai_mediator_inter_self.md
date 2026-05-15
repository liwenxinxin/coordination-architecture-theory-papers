# AI-as-Mediator Properties at Inter-Self Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** D2.05 (Series D, Phase 2, Note #500)
**Parent note:** D1.02 — All six Paper 1 architectural commitments hold within the shared substrate

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 1 of the CKS series names AI-as-substrate-mediator as one of its six architectural commitments and specifies five mediator properties that define what the mediator role requires. D1.02 committed that all six Paper 1 architectural commitments hold within the shared substrate's scope of operation. This note is D2.05: the operational decomposition of that commitment specifically for AI-as-mediator, applied to any large language model operating within a shared substrate during a Full Aspect Integration event. The five mediator properties — reads from shared substrate as primary source, writes to shared substrate under orchestration rules, holds no shadow state outside the shared substrate, exercises no authority over shared-substrate content, and outputs recorded with attribution — are each formalized at inter-Self scope. The note identifies how which LLM operates within the shared substrate is governed by the FAI configuration rather than by any participating Self's home configuration, and states three failure modes the formalization defends against. An operational test closes the note.

---

## 1. Position and scope

D1.02 established that the shared substrate carries Paper 1's six architectural commitments within its scope of operation: it is human-governed; conflicts within it are preserved as first-class state; AI operates as mediator over it; it is tool-agnostic; its composition is linear-cost; the substrate-LLM division is the same hybrid commitment Paper 1 defends. D1.02 commits to this inheritance as a package; D2.05 unpacks the AI-as-mediator commitment specifically.

The question D2.05 answers is: what does it mean, operationally, for an LLM to act as mediator over the shared substrate during a Full Aspect Integration event? Paper 1 articulates five properties of the mediator role within a single cell's coordination substrate. Each property has a direct analog at the inter-Self scope of a shared substrate. Naming those analogs precisely is the work of this note, because without the formalization, the inheritance claim in D1.02 is structural rather than operational — it asserts that the mediator role applies at inter-Self scope without saying what that role requires there.

The shared substrate is the architectural object over which the mediator role is exercised. It is a CKS substrate constructed temporarily to serve as the medium of coordination between two or more CKS-governed AI Selves during a FAI event. It spans more than one Self's home governance perimeter. Within its scope, it is the authoritative coordination state for the inter-Self task. D2.05 formalizes what any LLM that operates within this substrate during a FAI event is and is not authorized to do — not as a matter of procedural convention, but as a structural property of the mediator role Paper 1 defines.

---

## 2. Property A — Reads from shared substrate as primary source

At Paper 1 scope, the mediator role requires that the LLM reads from the coordination substrate as its primary source of coordination state, rather than from its own context window, session memory, or parametric knowledge. The substrate is what the LLM is mediating over; reading from it is what makes the mediation possible and auditable.

At inter-Self scope, Property A requires that any LLM operating within the shared substrate context reads from the shared substrate as its primary source of state for the inter-Self coordination task. This means three things specifically. First, the LLM does not read from any participating Self's home substrate directly; those home substrates are outside the shared substrate's perimeter and are not the authoritative record of what is happening within the FAI event. Second, the LLM does not read from its own context window or session memory as an authoritative source of inter-Self coordination state; any such context is either derived from the shared substrate or is not authoritative. Third, the LLM does not substitute parametric knowledge — knowledge encoded in its weights from training — as a source of coordination state for the inter-Self task. What the participating Selves agreed to, what aspects they exchanged, what conflicts exist, what the current state of the FAI event is: all of that lives in the shared substrate, and the LLM reads it from there.

The rationale for Property A at inter-Self scope follows the same logic as at cell scope. If the LLM reads from sources other than the shared substrate, then the shared substrate is no longer the authoritative record. It becomes one source among several, and the mediator role collapses into a synthesis role — the LLM arbitrating between the substrate and its own context or knowledge, without the substrate having priority. That collapse undermines the governance property that makes the shared substrate useful: human governance authorities can inspect and modify the substrate, but they cannot inspect or modify what the LLM carries in its context or weights. Property A preserves the substrate as the inspectable, governable record by making it the LLM's primary source.

---

## 3. Property B — Writes to shared substrate under orchestration rules

At Paper 1 scope, the mediator role requires that any LLM output that affects substrate state is written to the substrate under the orchestration rules humans have authored, not written directly to external state or committed without governance authorization.

At inter-Self scope, Property B requires that any LLM output that affects shared-substrate state is written to the shared substrate under the shared substrate's orchestration rules — rules authored by joint governance authority across the participating Selves. Two boundaries of Property B at this scope require explicit statement.

The first boundary is write scope. The LLM writes to the shared substrate, not to any participating Self's home substrate. During the FAI event, each participating Self's home substrate is outside the LLM's write scope. The shared substrate is where the inter-Self coordination state lives; the home substrates are where each Self's own operational state lives. These are architecturally distinct; writing to one does not constitute writing to the other. The mechanism through which FAI event outputs eventually reach each participating Self's home substrate is the dissolution hand-off — a governed boundary crossing that occurs after the FAI event completes, not during it.

The second boundary is write authority. The orchestration rules that govern writes to the shared substrate are authored by joint governance authority across the participating Selves, not by any single Self's governance authority unilaterally. The LLM does not author those rules; it operates under them. A write that is not sanctioned by the orchestration rules is not a write the mediator role permits. This is the same constraint Property B imposes at cell scope — the LLM does not commit outputs to the substrate outside the rules humans have established — extended to a multi-perimeter context where the rule-authoring authority is joint rather than single.

---

## 4. Property C — Holds no shadow state outside the shared substrate

At Paper 1 scope, the mediator role requires that the LLM hold no shadow state — no authoritative coordination state that exists outside the substrate, in the LLM's context window, session memory, or agent-internal store.

At inter-Self scope, Property C requires that any LLM operating within the shared substrate context holds no shadow state outside the shared substrate for the inter-Self coordination task. No LLM context window, no session memory, no agent-internal state constitutes authoritative coordination state for the FAI event.

The practical consequence is that if two LLM executions within the same FAI event need to share state, that shared state must pass through the shared substrate rather than through any LLM-internal channel. An LLM that writes coordination state to its own context and reads it back across executions is maintaining shadow state even if it eventually writes a summary to the substrate. The substrate is authoritative; context is instrumental and ephemeral.

Property C is what makes the shared substrate the single source of truth for the inter-Self coordination task. Without it, the authoritative record of the FAI event is split: part in the substrate (governable, inspectable, persistent), part in LLM context (not governable, not persistently inspectable, not subject to the human authority the shared substrate carries). Shadow state is structurally incompatible with the governance property the shared substrate is designed to preserve.

---

## 5. Property D — Exercises no authority over shared-substrate content

At Paper 1 scope, the mediator role requires that the LLM not hold governance authority over substrate content — it cannot gatekeep, approve, or veto what the substrate contains, because governance authority belongs to the humans who hold the inspect, modify, and override rights the CKS pattern defines.

At inter-Self scope, Property D requires that no LLM operating within the shared substrate exercises governance authority over that substrate's content. Specifically, the LLM cannot refuse a participating governance authority's inspect right: if a human holding governance authority over the shared substrate asks to read what the substrate contains, the LLM cannot mediate that access in a way that withholds or filters content. The LLM cannot approve or veto modifications to the shared substrate: modifications authorized by joint governance authority take effect regardless of whether the LLM would produce different content. The LLM does not hold governance authority over what aspects were contributed, what conflicts are preserved, what the shared substrate records as the state of the FAI event.

The foil here is LLM autonomy within the shared substrate — a failure mode in which the LLM, operating with wide latitude, effectively becomes the decision-maker about what the shared substrate contains, which content is visible, and which modifications are permitted. Property D forecloses this by positioning the LLM as the mediator over the substrate's content, not the authority over it. The distinction is structural: a mediator operates under authority that humans hold; an authority makes governance decisions that humans cannot independently override.

---

## 6. Property E — Outputs recorded with attribution

At Paper 1 scope, the mediator role requires that every LLM output that enters the substrate is recorded with attribution — which LLM produced it, under which orchestration rule, at what point in the cell's execution. Attribution is what makes provenance tracing possible and what makes the substrate's contents inspectable in a meaningful sense: a human inspecting the substrate can see not just what it contains but how each piece of content came to be there.

At inter-Self scope, Property E requires that every LLM output that enters the shared substrate is recorded as substrate content with attribution. The attribution record must identify which LLM produced the output, under which orchestration rules it was operating, and at what point in the FAI event the output was produced. This is the basis for provenance tracing within the shared substrate — the ability to trace any piece of content in the shared substrate back to its origin, whether that origin is a human governance authority, an LLM operating under orchestration rules, or an aspect contributed by a participating Self.

Property E connects to the inspect right the CKS governance commitment preserves. A substrate that contains outputs but does not record their provenance is inspectable in a limited sense: a human can read what the substrate contains, but cannot determine which outputs came from which source, under which authority. Attribution extends inspectability to the provenance dimension. Without Property E, the shared substrate satisfies a weaker version of human governance than the CKS pattern commits to.

---

## 7. Governance of which LLM operates in the shared substrate

The five properties above specify what any LLM operating within the shared substrate during a FAI event must do and not do. A separate question is which LLM or LLMs operate in the shared substrate for any given FAI configuration.

Different participating Selves may use different LLMs in their home operations. Paper 1's tool-agnosticism commitment means that no specific LLM is required at cell scope; the same commitment holds at inter-Self scope. The shared substrate is not tied to any specific LLM. For operations within the shared substrate during a FAI event, the FAI configuration — which is itself substrate content under Paper 3's Claim 5 — governs which LLM or LLMs are used for coordination tasks within the shared substrate.

This has two practical implications. First, different FAI configurations between different pairs or groups of Selves can use different LLMs for shared-substrate coordination, as long as whichever LLM is used satisfies the three minimal host requirements the CKS pattern specifies: persistent structured state, human read/write access, and LLM access to substrate content. Second, the five mediator properties above hold regardless of which LLM is used. They are properties of the mediator role at inter-Self scope, not properties of any particular model. A new LLM configuration introduced through a change to the FAI configuration inherits the mediator role's requirements immediately; there is no separate specification of the mediator role for each LLM choice.

The governance-configured character of LLM selection at inter-Self scope is architecturally significant: the authority to determine which LLM operates in the shared substrate belongs to the joint governance authority of the participating Selves, not to any individual Self, and not to the LLM itself.

---

## 8. Three failure modes this note defends against

This formalization of Property A through Property E at inter-Self scope is motivated by three specific failure modes that the inherited commitment in D1.02 does not, by itself, preclude.

The first failure mode is LLM autonomy within the shared substrate. In this failure mode, an LLM operating within the shared substrate effectively decides what content to include or exclude, which aspects to record, which conflicts to surface, and which governance authority's requests to satisfy. This failure mode violates Property D. The mediator role requires that the LLM operate under governance authority, not as its holder.

The second failure mode is LLM-as-source-of-truth at inter-Self scope. In this failure mode, the LLM's context window, session memory, or parametric knowledge serves as the authoritative record of inter-Self coordination state, with the shared substrate functioning as a secondary or derivative store. This failure mode violates Properties A and C simultaneously: the LLM is reading from sources other than the shared substrate, and it is maintaining shadow state outside the shared substrate. The governance consequence is that the authoritative record is no longer inspectable or modifiable by human governance authority — it lives inside the LLM, outside the substrate's perimeter.

The third failure mode is ungoverned LLM output in the shared substrate. In this failure mode, LLM contributions to the shared substrate are committed without satisfying Property B (written under orchestration rules) or Property E (recorded with attribution). The content reaches the substrate but without governance authorization and without provenance tracing. This failure mode makes the shared substrate's contents ungovernable in practice even if the governance rights formally exist: a human inspecting the substrate cannot determine the authority under which content was committed, and modification rights cannot be meaningfully exercised against content whose origin is unknown.

---

## 9. Operational test

For any LLM operating within a shared substrate during a FAI event, an observer can verify that the five mediator properties hold by checking each of the following independently.

**Test for Property A.** When the LLM processes a coordination task within the FAI event, is the shared substrate the source from which it reads inter-Self coordination state? A system passes if the LLM's access pattern during the FAI event reads from the shared substrate, and the shared substrate's content would determine the LLM's outputs for that task if the LLM's context were otherwise reset. A system fails if the LLM can produce coordination-relevant outputs by reading from a participating Self's home substrate, from session memory established outside the shared substrate, or from parametric knowledge in the absence of corresponding shared-substrate content.

**Test for Property B.** When the LLM produces an output that affects shared-substrate state, is that write performed under the shared substrate's orchestration rules? A system passes if writes to the shared substrate can only occur through mechanisms that enforce the orchestration rules joint governance authority has authored, and if no LLM output reaches the shared substrate outside those mechanisms. A system fails if the LLM can write to any participating Self's home substrate during the FAI event, or if LLM-produced content reaches the shared substrate without passing through a governed write mechanism.

**Test for Property C.** If all LLM context windows and session memories were reset during a FAI event, would the shared substrate contain a complete and sufficient record of inter-Self coordination state for the event to continue? A system passes if the answer is yes. A system fails if the reset would lose coordination state that exists only in LLM context or session memory and not in the shared substrate.

**Test for Property D.** When a human holding governance authority over the shared substrate exercises an inspect or modify right, does any LLM operating within the shared substrate have the architectural ability to block, filter, or approve that exercise? A system passes if the answer is no — the governance authority's rights are exercisable without LLM intermediation. A system fails if the LLM can withhold content from inspection, defer or condition a modification, or gate access to shared-substrate content for a human holding governance authority.

**Test for Property E.** For each LLM output recorded in the shared substrate, does the substrate carry a record identifying which LLM produced it, under which orchestration rule, and at what point in the FAI event? A system passes if this attribution record exists for every LLM-produced contribution and is itself inspectable by a human exercising the inspect right. A system fails if any LLM-produced content in the shared substrate lacks attribution, or if attribution metadata exists but is not accessible through the inspect right.

A shared substrate deployment satisfies the AI-as-mediator commitment at inter-Self scope if and only if all five tests pass independently.

---

## 10. Conclusion

The AI-as-mediator commitment that Paper 1 establishes at cell scope has a precise operational meaning at inter-Self scope. Any LLM operating within a shared substrate during a FAI event inherits five constraints: reading from the shared substrate as primary source, writing to the shared substrate under orchestration rules and only to the shared substrate during operation, holding no shadow state outside the shared substrate, exercising no authority over the shared substrate's content, and having its outputs recorded with attribution. These five constraints are the mediator role as D1.02's inheritance claim requires it to apply at inter-Self scope.

The note does not add new architectural commitments beyond what Paper 3 and D1.02 establish. Its contribution is to make D1.02's inheritance claim operationally checkable — each of the five properties can be verified independently, and the three failure modes the note names identify the gaps that would appear in a deployment that satisfies the structural inheritance claim without satisfying its operational content.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *AI-as-Mediator Properties at Inter-Self Scope.* May 14, 2026. ORCID: 0009-0004-8065-3235. Note D2.05 (#500), CKS Derivation Note Series. CC BY 4.0.
