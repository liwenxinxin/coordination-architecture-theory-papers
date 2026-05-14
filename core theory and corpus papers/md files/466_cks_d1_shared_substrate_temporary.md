# Shared Substrate as Temporary Construction

**Series:** CKS Derivation Notes — Series D (Paper 3 Sub-Commitments)
**Note ID:** D1.01 (Note #466)
**Derives from:** D0.01 / Paper 3 Claim 1
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 of the CKS theory series introduces one new architectural object — the shared substrate — and specifies that this object is a *temporary construction*: it is built for a Full Aspect Integration (FAI) event, exists for the event's duration, and dissolves on the event's completion. This note formalizes the temporariness of the shared substrate as an architectural commitment rather than a practical convenience. It identifies the three governed events in the shared substrate's lifecycle — construction, operation, and dissolution — and shows that each is subject to the same governance rights Paper 1 establishes over substrate content. It specifies the persistence policy as the governance-configured property that determines what remains after dissolution, ranging from nothing retained to a full durable audit record, with the architecture leaving the range's selection to governance rather than prescribing it. It explains why temporariness is architecturally important: the commitment is what prevents inter-Self coordination from creating permanent governance dependencies between organizations, thereby preserving each participating Self's home-perimeter independence. It distinguishes the shared substrate's temporariness from the persistent substrate objects Paper 2 establishes within a Self's home perimeter. Finally, it states the inheritance from Papers 1 and 2 and provides an operational test for whether a dissolved shared substrate was genuinely governed as a temporary construction.

---

## 1. Why temporary construction is an architectural commitment

The CKS theory series is built around a single organizing principle: coordination knowledge, governance semantics, and conflict-handling logic live in a persistent substrate outside the AI model, under human authority. Paper 1 establishes this principle at the cell scope. Paper 2 extends it to the Self scope — a unified architecture of cells, aspects, and Self-level substrate that persists across operational sessions within one organization. Paper 3 extends it further: across the perimeter between two or more distinct organizational Selves.

The extension introduces a new architectural object — the shared substrate — that carries a distinctive property none of Paper 2's substrate objects carry: it does not persist by default. It is constructed for a specific inter-Self coordination event, the FAI event, and dissolves when that event completes.

The temporariness is not a matter of convenience. It is not merely a default setting that a particular governance configuration can override by choosing persistent retention. The architectural commitment is to inter-Self coordination as an *event-scoped activity*. Each FAI event has a beginning, a scope of work, and an end. The shared substrate is the medium through which that event's coordination takes place; when the event is complete, the medium's coordinating function is also complete.

If the shared substrate persisted indefinitely by architectural default — if it accumulated as permanent shared state between two organizations — it would create a standing governance object spanning both organizations' governance perimeters with no natural closure. The governance rights established by Paper 1 (inspect, modify, override) would apply to a shared substrate that neither organization fully controls under its own home governance alone. Permanent shared governance dependencies of this kind introduce coordination obligations that are not bounded by any specific task, conflict-resolution requirements that have no natural completion point, and governance exposure that neither organization consented to beyond the specific event they initiated. None of this is what the architecture intends.

The commitment to temporariness closes this risk at the architectural level. The shared substrate is a temporary bridge between organizations, not a permanent merger. Each organization's governance perimeter remains intact. The bridge serves its purpose and then dissolves — with governance-configured terms for what, if anything, remains after dissolution.

This makes temporariness an architectural commitment in the same sense that human governance is an architectural commitment in Paper 1: it is a property of the system's design, not a procedural choice that depends on a particular deployment's preferences. An architecture in which the shared substrate might accumulate as permanent shared state — in which nothing in the design ensures eventual dissolution — does not satisfy D1.01.

---

## 2. The three governed lifecycle events

The shared substrate has three governed lifecycle events: construction, operation, and dissolution. This lifecycle is the inter-Self analog of the entity lifecycle Paper 2 establishes at the cell scope — birth, operation, death — and the parallel is architecturally deliberate. The shared substrate is a governed object that comes into existence under governance authorization, operates under governance authority, and closes its governed existence per a governance-configured plan.

### 2.1 Construction

The shared substrate is constructed through a human-authorized governance event. Construction is not spontaneous: it requires that participating organizations' governance structures jointly authorize the event, specify which Selves participate, configure which aspects each Self contributes, and authorize the configuration substrate that will govern how the shared substrate operates. The configuration substrate — which specifies participation, contribution boundaries, and the persistence policy for dissolution — is itself substrate content authored under the governance rights Paper 1 establishes. The construction event produces a new governed object with a governance record, governance specifications, and provenance tracing to the originating governance decisions.

The parallel to Paper 2's entity birth (B0.03, Claim 3) is direct: just as a new cell or aspect comes into existence with a governance record that traces its origination, the shared substrate comes into existence with a governance record tracing its construction to the joint governance authorization event.

### 2.2 Operation

Once constructed, the shared substrate operates as the coordination medium for the FAI event's duration. During operation, all six Paper 1 architectural commitments hold within the shared substrate's scope: the substrate is human-governed; conflicts surfaced within it are preserved as first-class state; AI operates as substrate mediator over it; it is tool-agnostic; its composition is linear-cost; the substrate–AI division maintains the hybrid commitment Paper 1 establishes. The shared substrate carries the full weight of the CKS pattern at the inter-Self scope, not a relaxed version of it.

Governance retains all three rights — inspect, modify, override — over shared substrate content throughout operation. The Paper 1 commitment that governance rights are available at any time, not only at predetermined checkpoints, holds at the shared substrate scope as well. Governance can inspect what is being contributed, what conflicts have been surfaced, how the orchestration rules are functioning, and what the configuration substrate specifies — at any moment during the event's operation.

The participating Selves' home governance perimeters remain in force during operation. The shared substrate's governance perimeter spans both; home governance perimeters are not suspended. Humans at each participating organization retain the rights Paper 1 guarantees.

### 2.3 Dissolution

The shared substrate dissolves when the FAI event completes. Dissolution is the third governed lifecycle event, and it is governed in the same sense as construction: it does not happen arbitrarily, and what happens at dissolution is not architecturally prescribed. Instead, dissolution proceeds according to the persistence policy that was configured as part of the shared substrate's construction — itself substrate content under governance, subject to the three Paper 1 rights.

The parallel to Paper 2's governed death is direct: just as a cell's retirement is governed under type-appropriate decision processes (functional obsolescence or lineage supersession), the shared substrate's dissolution is governed under the persistence policy governance configured for the specific FAI event. The shared substrate exits its active governance existence per a governance-configured plan, not by falling out of use without record.

After dissolution, the shared substrate no longer exists as an active governance object. What existed during operation — the contributed aspect content, surfaced conflicts, provenance records, orchestration rules — either persists in some form per the persistence policy or is fully gone. The governance record of the construction and dissolution events is itself subject to the persistence policy, ensuring that the event's governed nature remains traceable even after the active substrate is dissolved.

---

## 3. The persistence policy

The persistence policy is the governance knob that determines what remains after dissolution. It is configured as part of the shared substrate's construction and is itself substrate content under the three Paper 1 governance rights.

The policy can take any value within a range. Paper 3 names two poles of this range:

**Nothing retained.** The shared substrate fully dissolves on event completion. The only artifacts that remain are the evolution outputs that each participating Self has ingested into its home substrate through Paper 2's governed evolution mechanisms — DNA-layer content and action-layer content that each Self's home governance authorized for ingestion. The shared substrate itself leaves no cross-organizational record.

**Full durable record.** Some or all of the shared substrate's content is retained after dissolution as an inter-organizational audit record. This content — contributed aspects, surfaced conflicts, provenance chains, configuration substrate, orchestration rules — remains inspectable per the governance rights Paper 1 establishes. The full durable record option makes the FAI event's governed character verifiable after the fact.

Between these poles, any governance-configured intermediate is available. Partial retention — retaining, for example, the configuration substrate and conflict records but not the raw aspect contributions — is one intermediate. Governance determines the appropriate point on this range per FAI event, based on the event's purposes, the organizations' governance obligations, and the anticipated need for post-event audit or accountability.

The architecture does not prescribe the appropriate point. Prescribing it would overstep what the architecture can know: the appropriate persistence configuration depends on the specific FAI event's governance context, which the architecture cannot anticipate. What the architecture commits to is that the range exists and that the governance configuration is itself substrate content — not an external parameter held outside the governed system.

A critical implication of the persistence policy as substrate content: the policy is subject to the three governance rights during the shared substrate's operation. Governance can inspect it, modify it, and override it while the event proceeds, up to the point of dissolution. The policy is not frozen at construction; it is a live governance object until dissolution closes the shared substrate.

---

## 4. Why temporary is architecturally important

The significance of D1.01 is not merely definitional. The temporary-construction commitment does load-bearing architectural work, and identifying what work it does is necessary to understand why D1.01 is a sub-commitment of Paper 3 Claim 1 rather than an incidental feature.

**Preserving home-perimeter independence.** Each participating Self's home governance perimeter remains the authoritative governance scope for that Self's ongoing operation. The shared substrate's governance perimeter spans both organizations during the FAI event — that is the mechanism by which inter-Self coordination is possible — but the spanning is bounded. When the event dissolves, the spanning closes. Neither organization inherits standing governance obligations toward the other simply because a FAI event occurred. Each Self's home substrate, home governance, and home authority structure operate continuously, uninterrupted by the FAI event's existence. The temporary construction commitment is what ensures that inter-Self coordination does not accumulate as a permanent governance entanglement between organizations.

**Bounding the governance scope.** Permanent shared state between organizations would require continuous joint governance — ongoing authority over content neither organization controls unilaterally, ongoing conflict-handling between governance structures that were not designed to merge, ongoing compliance with governance obligations that span both perimeters indefinitely. Temporary construction bounds all of this: the governance scope of the shared substrate is exactly the FAI event's duration. After dissolution, governance returns to each organization's home perimeter entirely.

**Supporting the full persistence range.** Persistent shared infrastructure as default would preclude the nothing-retained end of the persistence range. Organizations with governance obligations that require minimizing cross-organizational data retention — or organizations that simply prefer not to maintain permanent shared infrastructure — could not use the architecture without abandoning the persistence-range option the architecture intends to support. Temporary construction as default is what makes the full range available. Persistent retention is one configuration option within the range, not the baseline the architecture imposes.

---

## 5. Distinction from Paper 2's persistent substrates

Paper 2 establishes a set of substrate objects — the DNA layer, the action layer, aspect DNA, Self DNA — that persist within a Self's home perimeter across operational sessions. These objects carry the substrate-mediator commitment Paper 1 establishes and accumulate the Self's coordination knowledge and operational history through governed evolution mechanisms. Their persistence is architecturally appropriate and intended: a Self's substrate is the record of its accumulated governance and evolution, and that record must persist for the evolution mechanisms to function.

The shared substrate is explicitly different from these objects in its persistence property. It does not persist across sessions or across the post-dissolution period by architectural default. The contrast is not accidental; it reflects the different governance context of each object type.

Paper 2's persistent substrate objects are home to one Self. Their governance is under one organization's authority. Their persistence creates governance obligations that one governance structure can manage and that benefit that structure's continued operation. Accumulation is a feature: the Self improves through accumulated substrate content.

The shared substrate is not home to any one Self. Its governance spans two or more organizations' authority structures. Its persistence would create governance obligations that no single organization's authority structure was designed to manage indefinitely. Accumulation is a risk: permanent shared state between organizations creates the governance entanglements D1.01's commitment exists to prevent.

This means that an implementation which treats the shared substrate as a persistent object — maintaining it between FAI events, allowing it to accumulate inter-organizational coordination state across events without dissolution — violates D1.01 even if it carries all six Paper 1 commitments within the shared substrate's scope during events. The violation is not at the level of governance rights but at the level of the shared substrate's temporal property. D1.01 is not derivable from Papers 1 and 2 alone; it is a new commitment at the inter-Self scope that the temporary-construction principle establishes.

---

## 6. Inheritance from Papers 1 and 2

D1.01 inherits from three prior commitments without re-defending them.

**Construction inherits from Paper 1 substrate origination.** Paper 1 establishes that substrate content originates under human authorship at the cell scope — governed creation with provenance tracing to the origination event. The shared substrate's construction event carries this commitment to the inter-Self scope: the shared substrate is a governed substrate object whose origination is recorded and whose governance configuration is authored under the authority structures Paper 1 establishes.

**Dissolution inherits from Paper 2's governed death.** Paper 2 establishes that a cell's exit from active operation is governed — not arbitrary, not ad hoc, but proceeding per a governance-configured plan that determines what happens to the substrate content and what audit record remains. The shared substrate's dissolution carries this commitment at the inter-Self scope: dissolution proceeds per the persistence policy governance configured at construction, producing a closed governed existence rather than an ungoverned disappearance.

**Persistence policy inherits from Paper 2's archival reactivatability.** Paper 2 establishes that lineage-superseded cells retire with archival, their substrate content remaining addressable through governed processes. The persistence policy at the shared substrate scope is the inter-Self generalization of this commitment: governance configures what of the shared substrate remains addressable after dissolution, ranging from nothing (the nothing-retained pole) to a fully retained audit record (the full-durable-record pole). The architecture does not prescribe which end of the range is correct; it commits to the range being governance-configured substrate content.

---

## 7. Operational test

A dissolved shared substrate was governed as a temporary construction if and only if all of the following are true:

1. **The shared substrate no longer exists as an active governance object.** An observer examining the shared substrate's state at dissolution time can confirm that it is not maintaining active coordination state, is not processing new contributions, and is not subject to new governance decisions — its active governed existence has closed.

2. **The persistence policy that governed dissolution is traceable.** An observer can find the persistence policy that was configured as substrate content in the shared substrate, confirm that it authorized the retention level that actually resulted from dissolution, and confirm that the policy was itself substrate content under the three Paper 1 governance rights during the event's operation.

3. **The construction and dissolution events are traceable in the governance record.** An observer can trace the construction event — the joint governance authorization, the configuration substrate specifying participation and contribution boundaries, the provenance record of origination — and the dissolution event — the closure of the shared substrate's active governance existence per the persistence policy — to the governance decisions that authorized each.

A dissolved shared substrate that fails any of these conditions did not instantiate D1.01. The most common failure modes are: the shared substrate persisted beyond its FAI event without a governance decision authorizing continued retention (fails condition 1); the persistence policy was not itself substrate content under governance rights but an external parameter applied at dissolution without governance authorization (fails condition 2); the construction or dissolution events occurred without governance record, making the shared substrate's existence ungoverned (fails condition 3).

---

*End of D1.01.*
