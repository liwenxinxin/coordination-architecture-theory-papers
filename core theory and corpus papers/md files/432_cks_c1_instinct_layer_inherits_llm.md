# Instinct Layer Execution Inherits Paper 1's AI-as-Mediator Role

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, in operational form, that the instinct layer's execution surface in Paper 2 is the Paper 1 LLM mediator operating under a more constrained, harness-substrate-governed form of the same five-property role — and that this more constrained form is still inherited, not a new or independent LLM role.

## Abstract

Paper 2 introduces a two-layer architecture in which an instinct layer (the LLM executing fast pattern-matching under harness substrate specifications) is explicitly separated from a reasoning layer (the CKS substrate handling governed deliberation). Paper 1 commits to the AI-as-substrate-mediator role: the LLM in any CKS cell reads from substrate content as its primary source, writes under human-authored orchestration rules, holds no shadow state outside the substrate, exercises no authority over substrate content, and has its outputs recorded with attribution. This note formalizes the inheritance edge: the instinct layer's execution surface is the Paper 1 LLM mediator operating under harness substrate governance, which is a stricter form of the mediator role, not a different role. All five mediator properties hold in the instinct layer context, with harness substrates serving as the specific governing objects that discharge Property B's requirement for human-authored rules. The note shows what is new in Paper 2 — harness-substrate governance as a tighter constraint, explicit separation of instinct and reasoning execution surfaces, and mutation (LLM version change) as an evolution mechanism targeting the instinct execution surface — and states the logical principle that more constrained is still inherited. A critical architectural point is also established: the identity of the LLM model does not determine which layer an execution surface belongs to; the governing substrate object does. This note is the third in a three-note sequence (C1.01–C1.03) that together cover the inheritance triple for Paper 2's two-layer architecture; C1.04 moves to the governance-boundary inheritance edge.

## 1. Position in the inheritance triple

C1.01, C1.02, and C1.03 together formalize the three inheritance edges that constitute Paper 2's two-layer architectural commitment as a composed extension of Paper 1. C1.01 established that the full instinct/reasoning separation inherits from Paper 1's substrate/LLM hybrid: the separation is a scope extension of the hybrid commitment, not an independent invention. C1.02 established that the reasoning layer's coordination substrate inherits from Paper 1's substrate: the CKS substrate as the reasoning layer's governing medium preserves all Paper 1 substrate commitments and adds the capacity to govern the instinct/reasoning boundary as substrate content. This note, C1.03, closes the triple by establishing the complementary edge: the instinct layer's execution surface — the LLM executing within the instinct layer under harness substrate specifications — is the Paper 1 LLM mediator, operating in a more constrained form.

Together, C1.01 through C1.03 establish that any system implementing Paper 2's two-layer architecture at cell scope necessarily implements Paper 1's substrate/LLM hybrid, Paper 1's substrate commitment, and Paper 1's AI-as-substrate-mediator role. No part of the two-layer structure is architecturally novel in isolation from Paper 1; the novelty is in the specific structure of the extension and the new mechanisms Paper 2 introduces on top of the inherited base. C1.04 moves to the next inheritance edge: the governance-boundary commitment.

## 2. The inheritance edge stated precisely

**The edge:** The instinct layer's execution surface in Paper 2 is the Paper 1 LLM mediator (Paper 1 §4.1–§4.2, Claim 4) operating under harness substrate governance — a more constrained form of the mediator role.

This statement has two components that must be held together. The first is identity: the execution surface in the instinct layer is the same architectural role as the Paper 1 LLM mediator. It is not a new kind of LLM role defined by Paper 2 independently of Paper 1's commitment. The second is constraint: the instinct layer's execution surface operates under harness substrates — explicit, human-authored specifications governing what patterns the instinct layer recognizes and how it responds — rather than under the open-ended orchestration rules Paper 1 describes at the cell level. This additional constraint narrows the role's operating bounds but does not change what role it is.

Paper 2's instinct layer uses a governed execution surface — typically the LLM operating under harness substrate specifications — to execute fast pattern-matching and response generation (Paper 2 §4). The harness substrates are explicit specifications authored by humans. The LLM executing within the instinct layer does so under these explicit specifications. This is the mediator role operating at tighter bounds: the LLM still mediates between substrate content and execution outputs, but the substrate object governing its behavior is a harness substrate rather than a general-purpose orchestration rule set.

## 3. All five mediator properties preserved

Paper 1's AI-as-substrate-mediator commitment names five properties that must hold for every LLM operation in a CKS system (Paper 1 §4.2). This section states each property and shows that it is satisfied in the instinct layer context.

**Property A — Reads from substrate content as primary source.** In the instinct layer, the execution surface reads from harness substrates as its primary source of behavioral specification. The harness substrates carry the pattern definitions, response templates, and routing logic the execution surface operates over. This is the same structural relationship Paper 1 requires: the LLM's operating inputs are substrate content, not in-weight memory or agent-maintained state treated as authoritative. Property A is preserved.

**Property B — Writes under human-authored rules.** In the instinct layer, the execution surface operates under the explicit specifications carried in harness substrates. Harness substrates are authored by humans: they are the substrate objects humans write to define what the instinct layer does. This discharges Property B's requirement that the LLM writes under human-authored rules. The specific form of the governing object is a harness substrate rather than a general orchestration rule set, but the structural requirement — that a human-authored object governs the execution surface's operation — is satisfied in the stricter form. Property B is preserved, and more tightly instantiated than Paper 1's general case requires.

**Property C — Holds no shadow state outside the substrate.** The execution surface in the instinct layer does not maintain substrate-relevant state across invocations outside the substrate. The harness substrates carry the governing specifications; the execution surface operates over them at execution time and does not accumulate session-specific state treated as authoritative. Property C is preserved.

**Property D — Exercises no authority over substrate content.** The instinct layer's execution surface does not hold authority over the harness substrate content that governs it. Humans hold that authority — they write, modify, and govern the harness substrates. The execution surface executes within the specifications the harness substrates carry; it does not override, silently modify, or collapse them. Property D is preserved.

**Property E — Outputs recorded with attribution.** Outputs produced by the instinct layer's execution surface are recorded in the substrate with attribution identifying them as LLM-produced, under which harness substrate, in which cell execution. The path-retraceability commitment (Paper 1 §3.1) applies to instinct layer outputs as to all LLM outputs in a CKS cell. Property E is preserved.

All five properties hold. The instinct layer's execution surface is the Paper 1 LLM mediator, not a role that satisfies some of the mediator properties under a different name.

## 4. What is new in Paper 2

Three things in Paper 2's instinct layer are genuinely new relative to Paper 1's mediator commitment. They are additive constraints and mechanisms, not replacements for the inherited properties.

**Harness substrate governance as the specific governing object.** Paper 1 commits to human-authored orchestration rules as the form of governance over LLM writes, without specifying the internal structure of those rules. Paper 2 names harness substrates as the specific class of substrate object that governs instinct layer execution — explicit, human-authored specifications encoding pattern-recognition scope and response behavior. This is a narrowing within Property B's requirement: where Paper 1 permits any human-authored governing object, the instinct layer commits to a specific class. The narrowing is a strict specialization, not a departure.

**Explicit separation of instinct and reasoning execution surfaces.** Paper 2 explicitly separates the instinct layer's execution surface from the reasoning layer's execution surface (Paper 2 §4). The two surfaces may run on the same LLM model — the identity of the model does not determine which layer an execution surface belongs to. What determines layer membership is the governing substrate object: a harness substrate governs instinct execution; the orchestration substrate governs reasoning execution. This separation is architecturally significant for two reasons. First, it makes the two layers independently evolvable (C1.01's territory). Second, it establishes that the mediator role is discharged twice in a Paper 2 cell — once under harness substrate governance for instinct, and once under orchestration substrate governance for reasoning — with different governing objects for each.

**Mutation as an evolution mechanism targeting the instinct execution surface.** Paper 2 introduces instinct evolution as an undirected mutation mechanism: LLM version changes and infrastructure upgrades alter the instinct layer's execution behavior without direct human specification of the change (Paper 2 §7.2). This is a new evolution mechanism Paper 1 does not specify. The mechanism targets the instinct execution surface — the same surface this note identifies as the Paper 1 LLM mediator under harness governance. Mutation does not change what the execution surface is (the mediator role); it changes which model instantiates it. The mediator role is preserved across mutations because the role is defined by the five properties, not by which model version satisfies them. Governance over mutation is maintained through verification substrates (Paper 2 §8.2), which are themselves substrate objects under human authority.

## 5. The "more constrained is still inherited" principle

The logical relationship between harness substrate governance and Paper 1's mediator role requires a precise statement, because it is the relationship adversarial interpretation would most likely contest.

**The principle:** A system that satisfies all five Paper 1 mediator properties AND operates under additional constraints imposed by a specific class of governing substrate object satisfies the Paper 1 mediator role. More constrained is still inherited.

This is a basic set-theoretic relationship. The Paper 1 mediator role defines a set of behaviors (those satisfying properties A–E). The instinct layer's harness-governed execution defines a strict subset of those behaviors: it satisfies all five properties and adds the constraint that the governing object is a harness substrate rather than any human-authored object. A member of a strict subset is a member of the set. A system implementing the instinct layer necessarily implements Paper 1's mediator role.

The principle has a direct corollary for prior-art analysis: it forecloses the adversarial framing that Paper 2's instinct layer introduces a new form of LLM role unrelated to Paper 1's mediator commitment. To sustain that framing, an adversarial reader would need to show that at least one of the five mediator properties fails to hold in the instinct layer context. Section 3 above shows all five hold. The harness-substrate constraint is an addition within the role, not a departure from it.

The principle also guards against the inverse misreading: that the additional constraint is so minor as to make C1.03 uninteresting. The harness substrate governance constraint is architecturally significant because it is what makes the instinct layer independently evolvable (C1.01) and what makes mutation a well-defined evolution mechanism (§4 above). The constraint matters; it is simply not a new role.

## 6. Layer identity is determined by governing substrate object, not model identity

A consequence of the inheritance relationship established in §§2–5 deserves explicit statement because it is a common source of misreading in dual-process architectures.

**The instinct layer's execution surface and the reasoning layer's execution surface may run on the same LLM model.** Paper 2 does not require different models for the two layers. The instinct layer may use the same model as the reasoning layer. This fact would, in some architectural frameworks, imply that the two execution surfaces are the same: if the same model runs both, the behavior is the same behavior.

That inference does not hold in CKS. Layer identity is not determined by model identity. It is determined by the governing substrate object. The instinct layer's execution surface is governed by harness substrates — human-authored specifications defining pattern scope and response behavior. The reasoning layer's execution surface is governed by the orchestration substrate — the CKS substrate carrying coordination and governance logic. These are different substrate objects with different content, different authoring processes, and different authority relationships. A single model operating under a harness substrate is in the instinct layer; the same model operating under the orchestration substrate is in the reasoning layer.

This distinction is load-bearing for instinct evolution. When the LLM model version changes, the instinct layer's behavior changes because the execution surface changes — but the layer's identity and its mediator role are not affected. The harness substrates remain the governing objects; what changes is which model version instantiates the execution surface that operates under them.

## 7. Prior-art significance

The inheritance edge this note formalizes has specific prior-art significance for the CKS theory series.

**It forecloses independent-invention claims on the instinct layer's execution surface.** Any architecture that introduces a fast-pattern-matching execution surface governed by explicit human-authored specifications, with the LLM's mediator properties preserved, is implementing a form of Paper 1's AI-as-substrate-mediator commitment applied under harness substrate governance. The instinct layer's execution surface is the Paper 1 LLM mediator — that commitment exists in Paper 1 and extends directly into Paper 2's instinct layer. There is no independent architectural claim for an LLM execution surface that satisfies properties A–E under explicit governance specifications; that is the Paper 1 mediator role.

**It establishes that C1.01's scope-extension claim is specifically about the two-layer structure, not about a new LLM role.** C1.01 established that the instinct/reasoning separation inherits from the substrate/LLM hybrid. A reader might interpret that inheritance as implying that the LLM in the instinct layer is a new kind of LLM role — the "instinct LLM" as something distinct from the "Paper 1 LLM mediator." C1.03 closes that interpretation: the instinct layer's LLM is the Paper 1 LLM mediator under tighter constraints, not a new role. C1.01's novelty is in the structural relationship between two layers, not in the identity of either layer's execution component.

**Together with C1.02, it establishes that both components of the two-layer architecture are inherited.** C1.02 showed that the reasoning layer's substrate is inherited from Paper 1's substrate. C1.03 shows that the instinct layer's execution surface is inherited from Paper 1's LLM mediator. The two-layer architecture in Paper 2 is, at the level of its component roles, a composed extension of Paper 1's hybrid — which is precisely what C1.01 establishes at the structure level. All three notes converge on the same finding: Paper 2's two-layer architecture is Paper 1's hybrid extended, not Paper 1's hybrid replaced.

## 8. Operational test

For any cell implementing Paper 2's instinct layer, an observer can verify the inheritance edge this note formalizes by checking all of the following. If all hold, the instinct layer's execution surface implements the Paper 1 LLM mediator role under harness substrate governance.

1. **Harness substrates as governing objects.** The instinct layer's execution surface operates under explicit, human-authored specifications carried as harness substrates in the cell's substrate. These specifications are inspectable and modifiable by humans at any time.

2. **Primary-source reading (Property A).** The execution surface reads from harness substrate content as its primary behavioral source. It does not treat in-weight parametric memory as the authoritative source of what the instinct layer should do.

3. **Write governance (Property B).** Every output the execution surface produces within the instinct layer is produced under the harness substrate specifications. The execution surface does not produce outputs outside those specifications and record them as instinct outputs.

4. **No shadow state (Property C).** The execution surface does not maintain substrate-relevant state across cell invocations outside the substrate. Between executions, the only authoritative record of the instinct layer's governing specifications is the harness substrates.

5. **No authority over harness substrates (Property D).** The execution surface does not modify, override, or silence harness substrate content on its own initiative. Authority over harness substrate content is held by humans.

6. **Attributed output recording (Property E).** Instinct layer outputs are recorded in the cell's substrate with attribution identifying them as LLM-produced, under which harness substrate, and in which cell execution.

7. **Layer identity by governing object, not model.** If the cell also operates a reasoning layer execution surface, the two surfaces are distinguishable by their governing substrate objects — harness substrate for the instinct surface, orchestration substrate for the reasoning surface — regardless of whether both run on the same LLM model.

A cell that satisfies (1)–(7) implements the Paper 1 LLM mediator role in the instinct layer context, and the inheritance edge this note formalizes holds for that cell. A cell that fails any of (1)–(6) may instantiate an LLM execution surface for instinct-like processing, but does not implement the CKS AI-as-substrate-mediator commitment within the instinct layer.

## 9. Conclusion

The instinct layer's execution surface in Paper 2 is the Paper 1 LLM mediator — all five mediator properties are preserved — operating under harness substrate governance, which is a stricter form of the role's governing constraint. More constrained is still inherited: the instinct layer's execution surface is a strict specialization of the Paper 1 mediator, and any system implementing it necessarily implements Paper 1's Claim 4 commitment. Layer identity in Paper 2 is determined by the governing substrate object, not the model: the same LLM model may serve both layers, but different substrate objects govern each. Three things are genuinely new in Paper 2's instinct layer: harness substrates as the specific governing object class, the explicit architectural separation from the reasoning execution surface, and mutation as an evolution mechanism targeting the instinct surface while leaving the mediator role intact.

This note completes the two-layer inheritance triple (C1.01–C1.03). Together, the three notes establish that Paper 2's two-layer architecture is a composed extension of Paper 1's hybrid commitment: both the reasoning layer's substrate (C1.02) and the instinct layer's execution surface (C1.03) are inherited Paper 1 components, and the full instinct/reasoning separation (C1.01) is an inherited scope extension of the hybrid. C1.04 turns to the next inheritance edge: the governance-boundary commitment.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* [Paper 1]. April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model* [Paper 2]. April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *C1.01 — Paper 2 Instinct/Reasoning Separation Inherits Paper 1 Substrate/LLM Hybrid: Scope-Extension Inheritance.* May 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *C1.02 — Paper 2 Reasoning Layer Inherits Paper 1 Substrate: Substrate Identity Preservation.* May 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct Layer Execution Inherits Paper 1's AI-as-Mediator Role.* May 14, 2026. ORCID: 0009-0004-8065-3235.
