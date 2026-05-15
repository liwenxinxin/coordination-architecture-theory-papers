# Resolve-via-Orchestration Tier for Inter-Self Conflicts

**Series D — Paper 3 Derivation Notes**
**Note D1.14 / #479**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 of the CKS theory series establishes a three-tier inter-Self conflict-handling mechanism — preserve, resolve via orchestration, escalate to humans — as the form Paper 1's conflict-handling principles take when extended to the inter-Self coordination scope. This note formalizes the second of those three tiers: the resolve-via-orchestration tier. The tier applies when a conflict surfaced during a Full Aspect Integration (FAI) event fits a class for which prebuilt orchestration rules exist within the shared substrate. When that condition is met, those rules determine the resolution without requiring real-time human decision. The resolution is nonetheless governance-authorized: the orchestration rules are substrate content authored by governance before the conflict arises, and the governance act of authoring them is what authorizes the resolution they produce. The note states what the tier requires (pre-authored rules as substrate content, conflict-class identification, governed outcome, resolution record, override authority), what it enables (governed conflict handling at FAI volume without per-event governance attention), its inheritance from Papers 1 and 2, the four failure modes it defends against, and an operational test for implementation conformance. D1.15 (escalate-to-humans tier) follows as the third of three.

---

## 1. Position in the three-tier mechanism

Paper 3 Claim 3 establishes a three-tier mechanism for handling conflicts surfaced during FAI events within the shared substrate. The three tiers are: (1) **preserve** — conflicts are retained as first-class substrate state when the task does not require resolution; (2) **resolve via orchestration** — prebuilt orchestration rules within the shared substrate determine the resolution when the conflict fits a class those rules cover; (3) **escalate to humans** — conflicts for which no orchestration logic applies surface to the governance authorities of the participating coordination units. These tiers are not alternative strategies of equal standing; they represent an ordered decision structure. The preserve tier (formalized in D1.13) is the architectural default at inter-Self scope — conflicts surface as substrate state and remain there. The resolve tier is the second response: it operates when orchestration rules exist for the conflict's class. The escalate tier (D1.15) is the third response: it operates when no orchestration rules cover the conflict.

D1.14 formalizes the second tier precisely. The central commitment is: when a conflict arising within the shared substrate during an FAI event belongs to a class for which prebuilt orchestration rules have been authored as substrate content, those rules determine the resolution. Real-time human intervention is not required. The resolution is governance-authorized in advance through the act of authoring the rules.

---

## 2. What the resolve tier requires

### 2.1 Pre-authored orchestration rules as substrate content

The orchestration rules that resolve conflicts of a given class must exist as authored substrate content before any conflict of that class arises. They are not runtime decisions, not LLM inferences, and not logic embedded in agent behavior. They are part of the shared substrate's configuration — governance-layer content (DNA-layer content in the terminology of the Paper 2 instinct/reasoning separation) that specifies how the shared substrate handles conflicts of specific types.

Authoring these rules is a governance act. The rules are authored by the governance authorities of the participating coordination units, operating under joint authority across the inter-Self perimeter as Paper 3 specifies. Because the rules are substrate content, all three rights that constitute human governance in the CKS sense apply to them at all times: the right to inspect, the right to modify, and the right to override. The rules are not opaque; they are not sealed inside a runtime; they are not the property of a vendor or an automated system. They are readable, writable, and overridable by governance at any time.

### 2.2 Conflict-class identification

The resolve tier is class-conditional. A conflict that arises during an FAI event must be identified as belonging to a class covered by prebuilt orchestration rules before those rules apply. Tier-decision logic — the substrate-level logic that determines which tier handles a given conflict — is itself substrate content under joint governance authority, as Paper 3 establishes. This means the decision about which tier applies to a given conflict is not made by an LLM or an autonomous runtime; it is the result of authored tier-decision logic operating as governed substrate.

When a conflict fits a covered class, the rules resolve it. When a conflict does not fit any covered class, it either rises to the escalate tier or is preserved per the orchestration logic. The tier-decision logic is not itself a form of autonomous conflict resolution; it is a classification operation operating under authored rules, subject to the same governance rights as all other substrate content.

### 2.3 Resolution as governed outcome

The resolution produced by orchestration rules is a governed outcome, not a system-autonomous decision. The governance authorization for the resolution was established at the moment the orchestration rules were authored. Applying those rules to a specific conflict during an FAI event is the exercise of governance authority already vested in the authored rules — not a new governance act, and not a gap in governance authority.

This is the central structural point of the resolve tier: governance does not need to be present in real time for a resolution to be governance-authorized. A resolution governed by authored substrate content is governed by the same authority that authored that content. The absence of real-time human intervention is not an absence of governance; it is the form governance takes when authority is exercised through authored rules that operate in advance of the specific conflict they resolve.

This structure is identical to Paper 1's cell-level conflict resolution under orchestration rules. Paper 1 commits that the LLM does not decide resolution logic — humans author orchestration rules that determine how conflicts within a cell are handled. The resolve tier is that same structure applied at inter-Self scope: prebuilt orchestration rules within the shared substrate determine the response to known-class conflicts, with the rules themselves substrate content under joint governance authority across the participating coordination units' perimeters.

### 2.4 Resolution record

Every resolution produced by the orchestration rules generates a record as substrate content. The record attributes: which rule resolved which conflict, when, and what outcome was produced. This record is itself substrate content subject to the three governance rights — it can be inspected, modified, or overridden. It is also subject to path retraceability as Paper 1 A1.07 establishes: the resolution event is retraceable from its record back to the authored rule that governed it, and from the rule back to the governance authority that authored it.

The resolution record serves two architectural functions. First, it makes the resolution auditable: any party with appropriate access can verify that a given conflict was resolved by a specific authored rule, not by ad hoc system behavior. Second, it creates the substrate-level basis for governance override: if governance judges a resolution incorrect, the record identifies exactly what needs to be overridden and what rule needs to be modified to prevent the same resolution from occurring again.

### 2.5 Governance override authority

Because the orchestration rules that produce resolutions are substrate content, governance can modify or override them at any time. A resolution produced by the rules is not final in the sense of being beyond governance reach. Governance can override an individual resolution outcome (by modifying the resolution record directly, as a substrate write operation under the override right) and can modify the rules to change how future conflicts of the same class are resolved. Neither the rules nor their outputs accumulate autonomous authority over time; both remain subject to governance throughout the shared substrate's existence.

This override authority is what prevents the orchestration rules from becoming autonomous governance actors. Rules that resolve conflicts under delegated authority are governed entities, not governing entities. The authority they exercise is borrowed from the governance act of authoring them; it does not become self-perpetuating, and it does not displace the human governance authority that remains available at all times.

---

## 3. What the resolve tier enables

### 3.1 Governed conflict handling at FAI volume

FAI events can be high-frequency operations: multiple coordination units contributing aspects to the shared substrate, producing conflicts that surface as substrate state in volume that grows with the number of participating coordination units and the frequency of their FAI activity. A mechanism that required real-time governance attention for every conflict of every class would not be compatible with this volume. The resolve tier makes high-volume governed conflict handling possible by moving the governance act upstream: governance authors the rules once, at design time, and those rules operate at coordination time without per-event governance overhead.

This is not a reduction in governance — it is governance at the right moment. The cost of authoring orchestration rules is paid once and amortizes across every resolution those rules subsequently produce. The cost is proportional to the variety of conflict classes that require authored rules, not to the volume of FAI events. This cost structure is structurally identical to the one Paper 1 establishes for cell-level governance: governance cost grows with rule variety, not with substrate size or event volume.

### 3.2 Governance-authored policy expressed as operational rules

The orchestration rules authored to resolve conflict classes are governance policy expressed in operational form. When governance decides that conflicts of class C should be resolved by outcome O, that decision is recorded as a prebuilt orchestration rule that produces outcome O when a class-C conflict is detected. The rule is inspectable evidence of the governance policy; it is not a post-hoc reconstruction of what governance intended. The policy and its operational expression are the same substrate content.

This directness — governance policy as authored rules, not as documentation of intended behavior somewhere outside the substrate — is what makes the resolution traceable back to governance authority. There is no interpretive gap between what governance decided and what the rules do; the rules are what governance decided.

### 3.3 Separation of governance time from coordination time

The resolve tier enables a clean separation between the time at which governance exercises authority over conflict resolution (when rules are authored or modified) and the time at which conflicts are actually resolved (when FAI events surface conflicts and rules operate on them). This separation does not weaken governance; it makes governance sustainable at coordination scale. Governance does not need to operate in real time at the pace of FAI events; it needs to operate at the pace of rule authoring and review, which is bounded by the variety of conflict classes the shared substrate must handle.

---

## 4. Inheritance from Papers 1 and 2

### 4.1 Paper 1 inheritance

The resolve tier inherits directly from Paper 1's cell-level conflict resolution under orchestration rules (Paper 1 §5.3). Paper 1 establishes that humans author the orchestration rules that determine how conflicts within a cell are handled; the LLM does not decide resolution logic. This commitment — human-authored rules determine resolution; the LLM executes the rules as substrate mediator — is the structural source of the resolve tier. The inter-Self extension adds the joint-authority dimension (rules are authored under joint authority across participating coordination units' governance perimeters) and the class-conditionality emphasis (the resolve tier applies to conflicts that fit a covered class), but the core architectural commitment is unchanged: prebuilt orchestration rules authored by humans determine conflict resolution outcomes.

Paper 1 also provides the traceability commitment (A1.07) that the resolution record requirement inherits. Path retraceability at cell scope means every substrate operation can be traced back to the authored logic that governed it; the resolution record requirement is the inter-Self scope expression of that same commitment.

### 4.2 Paper 2 inheritance

Paper 2 extends Paper 1's conflict-handling principles to operations within a coordination unit, including conflict handling at aspect scope (cross-component conflicts) and Self scope (cross-aspect conflicts). Paper 2's coordination-rule-mediated conflict handling within a coordination unit is the intra-unit scope analog of the resolve tier; the resolve tier is the inter-unit scope extension. The T1.06 entry in the CKS trilogy ambiguity map documents this relationship: conflict handling across the trilogy is one architectural commitment — preserve conflicts as first-class state, govern their resolution under human-authored rules — extended to progressively larger coordination scopes.

---

## 5. Four failure modes the sub-commitment defends against

**Real-time-human-only resolution.** An architecture that requires real-time governance intervention for every conflict, treating pre-authored rules as insufficient governance authorization, misreads governance as a review workflow rather than an authority architecture. The resolve tier forecloses this reading: governance exercises its authority at rule-authoring time; real-time intervention is not architecturally required for the resolution to be governed.

**Ungoverned resolution.** An architecture in which rules resolve conflicts but are not authored substrate content — embedded in agent behavior, sealed in runtime logic, or otherwise outside governance inspection and modification — produces resolutions that cannot be traced to governance authority. The resolve tier forecloses this: the rules must be substrate content, authored under governance authority, subject to the three rights at all times. Resolution logic that lives outside the substrate is not governed resolution logic in the CKS sense.

**Permanent resolution through rules.** An architecture in which resolutions produced by orchestration rules cannot be overridden by governance — because the rules are immutable, or because the resolution record is sealed, or because the rules are treated as having autonomous authority once authored — converts the rules from governed entities into governing entities. The resolve tier forecloses this: governance override authority over both the rules and their outputs is preserved at all times.

**Undifferentiated resolution.** An architecture that applies the same resolution logic to all conflicts regardless of class — resolving every conflict the same way, with no authored rules distinguishing between conflict types — loses the governance information that class-differentiated rules carry. The resolve tier forecloses this by requiring that orchestration rules apply to conflicts of a *known class*: the class identification is itself a governance act (encoded in tier-decision logic as substrate content), and the class-specificity of the rules is what makes them accurate policy rather than blunt override.

---

## 6. Operational test

For a conflict resolved by orchestration rules in an FAI event, an implementation instantiates the D1.14 resolve-via-orchestration tier if and only if all of the following are true:

1. **Pre-authored rule locatable.** A human observer can locate, within the shared substrate's configuration, the specific orchestration rule that governed the resolution — as authored substrate content with provenance (when authored, by which governance authority).

2. **Resolution record attributable.** A resolution record exists as substrate content, attributing which rule resolved which conflict, what outcome was produced, and when. The record is retraceable to the authored rule that governed it.

3. **Class identification governed.** The classification of the conflict as belonging to the class covered by the applied rule is itself the output of authored tier-decision logic within the substrate, not an ad hoc system determination.

4. **Governance override available.** A human with governance authority can, without requiring system approval or architectural gating, modify the orchestration rule that produced the resolution, override the resolution record directly, or both — with the modification or override taking effect as substrate state.

5. **No autonomous rule authority.** The orchestration rules do not claim or exercise authority beyond what was delegated by the governance act of authoring them. The rules execute under governance authority; they do not accumulate independent authority over the conflicts they resolve.

An implementation that fails any of (1)–(5) may still resolve conflicts, but does not instantiate the resolve-via-orchestration tier as formalized here. The most common failure modes are: rules that exist but are not substrate content (fail (1) and (4)); resolutions that occur but produce no record (fail (2)); class identification embedded in opaque runtime logic (fail (3)); rules that once authored cannot be modified without system-level approval (fail (4)); and rules whose outputs are treated as binding on governance (fail (5)).

---

## 7. Relation to D1.13 (preserve tier) and D1.15 (escalate tier)

The resolve tier occupies the middle position in the three-tier mechanism. It presupposes D1.13's preserve tier: conflicts must surface as first-class substrate state before any tier can operate on them. A conflict that is silently resolved at the FAI merge point — never preserved as substrate state — is not reachable by the resolve tier or any other tier. Preservation is the prerequisite.

The resolve tier is bounded above by D1.15's escalate tier: conflicts that do not fit any class covered by prebuilt orchestration rules are not resolved by the resolve tier. They surface to the escalate tier, which brings them to the governance authorities of the participating coordination units for direct human resolution. The three tiers together cover the full conflict-handling space at inter-Self scope: preserve when no resolution is needed; resolve when prebuilt rules cover the class; escalate when no prebuilt rules exist or when governance authority must be exercised directly. D1.15 formalizes the escalate tier.

---

## 8. Conclusion

The resolve-via-orchestration tier is the second of three responses to conflicts surfaced during FAI events within the shared substrate. Its defining architectural commitment is that governance authority over conflict resolution is exercised through pre-authored orchestration rules, not through real-time human intervention. When a conflict fits a class covered by those rules, the rules govern the resolution. The resolution is governance-authorized by the act of authoring the rules; applying them to a specific conflict is the exercise of authority already established. The rules are substrate content, subject to governance inspection, modification, and override at all times. Every resolution they produce generates a traceable record. The tier enables governed conflict handling at FAI volume without requiring per-event governance attention, while preserving full governance authority over both the rules and their outputs.

The tier inherits from Paper 1's cell-level conflict resolution under orchestration rules and Paper 2's intra-unit conflict handling through authored coordination rules — both are the same commitment at smaller coordination scopes. The resolve tier is what those commitments produce when extended to the inter-Self scope: prebuilt orchestration rules within the shared substrate, authored under joint governance authority across participating coordination units' perimeters, resolving known-class conflicts without displacing the governance authority that remains available to modify, override, or escalate at any time.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Resolve-via-Orchestration Tier for Inter-Self Conflicts.* May 14, 2026. ORCID: 0009-0004-8065-3235. (CKS Derivation Note D1.14 / #479.)
