# The Five Mediator Properties as Severable Architectural Commitments: A Decomposition Frame for the AI-as-Substrate-Mediator Role in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 2, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize the five-property definition of the AI-as-substrate-mediator role — already extracted in the parent foundational note (A1.04) — as a *severable set of architectural commitments*: each property has independent operational content that can be specified, defended, and tested as a standalone derivation, while all five together remain jointly necessary for the integrated mediator role.

## Abstract

The CKS pattern's AI-as-substrate-mediator commitment is articulated in the parent foundational note (A1.04) as a single role with five constitutive properties: (A) the LLM reads from substrate as primary state; (B) the LLM writes under orchestration rules; (C) the LLM holds no substrate-relevant state outside the substrate; (D) the LLM exercises no authority over substrate content; (E) LLM writes are recorded with attribution. This note formalizes the structural property that makes the five-property treatment compositional: each property has *independent operational content* — a counterfactual implementation can fail any one while preserving the other four, with a specific failure mode — and yet *all five together are jointly necessary*, since no proper subset suffices to keep the LLM in the mediator position the source paper commits to. The note states the severability argument property by property, the joint-necessity argument as a closed-loop dependency, distinguishes the severable-set frame from three adjacent treatments, specifies how each cross-claim connection from §4.2 grounds in a specific property-subset, and provides an operational test at the parent-frame level. The five property-specific operational tests are deferred to A2.19–A2.23.

## 1. Why the severable-set frame needs to be formalized as standalone

The parent note (A1.04) extracts the AI-as-substrate-mediator role from the source paper's distributed treatment in §4.1 (the substrate/LLM governance boundary) and §4.2 (the cross-claim spine), and states it as a single architectural commitment with five constitutive properties. The parent treatment is correct as far as it goes; this note does not amend it. What it does not articulate is the *structural property* that makes the five-property formulation operationally compositional: that each property carries independent operational content, and that the role's integrated content is the joint satisfaction of all five rather than any proper subset.

Three motivations make standalone formalization of that structural property worth its own derivation note.

**Diagnosability of partial preservations.** Implementations under design pressure consistently drift toward partial preservation of the mediator role. Adding agent memory drops Property C; allowing free-form LLM contributions outside any rule drops Property B; treating LLM outputs as anonymous substrate content drops Property E. Each shortcut is reasonable in some other architectural context; in CKS, each downgrades the role and breaks specific downstream commitments. Without the severable-set frame, partial preservations are difficult to diagnose: the implementation looks like it is "operating on the substrate," and the resulting failures present as governance, traceability, or cost-model failures rather than as specific mediator-role failures. With the frame, each missing property identifies a specific failure mode and a specific commitment that must be restored.

**Prior-art posture.** Patentable derivations of CKS that focus on LLM-substrate integration patterns are more defensibly contested when each of the five properties is publicly formalized as standalone, because any putative "LLM integration innovation" can be evaluated against five separate prior-art commitments rather than one integrated one. The standalone formalization of the structural property is what makes the per-property treatment in A2.19–A2.23 architecturally well-founded rather than an arbitrary partition.

**Operational specificity of the cross-claim spine.** §4.2 names AI-as-substrate-mediator as the cross-claim spine connecting the role to the other architectural commitments. A1.04's §6 names those connections without specifying which property grounds each one. Once the role is decomposed into severable properties, each cross-claim connection grounds in a specific subset, and the spine becomes architecturally specific rather than a structural metaphor.

## 2. The five mediator properties, stated as a severable set

The five properties named in A1.04 are restated here in their parent-frame form. The operational content of each is the subject of its own standalone note (A2.19–A2.23) and is not elaborated here. The treatment in this section is the *joint structure* of the five.

**Property A — Substrate as primary source of state for LLM reads.** The LLM reads from substrate content as the authoritative input for any operation whose execution depends on the system's coordination state.

**Property B — Orchestration rules govern LLM writes to substrate.** When the LLM produces outputs that affect substrate state, those writes happen under orchestration rules humans authored at design time (per A2.04). The LLM does not write on its own judgment; it writes when rules specify writes and as rules specify them.

**Property C — No substrate-relevant state held outside the substrate.** State that affects substrate operations across cell executions lives in the substrate, not in the LLM. The LLM does not maintain agent memory, persistent context, or session storage that holds substrate-relevant state for reuse across executions.

**Property D — No LLM authority over substrate content.** The LLM cannot silently overwrite substrate content, collapse contradictions the substrate preserves, modify orchestration rules, or take actions the human-governed authority structure reserves for humans (per A1.01). The LLM operates within authority granted by rules; it does not exercise independent authority.

**Property E — LLM writes carry provenance attribution.** When LLM operations produce substrate writes (per Property B), the writes carry provenance metadata identifying the LLM as writer, alongside the cell identity, rule reference, timestamp, and other provenance fields the substrate's accountability vocabulary commits to (per A1.07). LLM-mediated writes are architecturally distinguishable from human-mediated writes through this attribution.

The five together constitute the architectural content of the mediator role. The remainder of this note formalizes the structural property of that constitution.

## 3. Why each property is severable

Severability here is a property of the *content* of each commitment: each property has independent operational meaning, exhibits independent failure modes, and can ground its own standalone derivation. The argument is by counterfactual: for each property, an implementation can fail that property specifically while preserving the other four, with a failure mode identifiable to that property alone.

**Severability of Property A.** An implementation can fail Property A by giving the LLM primary input from a source other than the substrate — operator prompts containing substrate-relevant content not drawn from substrate, agent memory presented as authoritative input, external retrieval that bypasses substrate. Such an implementation may still write under rules (B), hold no external state (C), exercise no authority (D), and attribute its writes (E). The failure mode is specific to A: the LLM may produce decisions that contradict substrate content because it was not reading the substrate as authoritative.

**Severability of Property B.** An implementation can fail Property B by allowing LLM writes outside orchestration-rule authorization — autonomous LLM agents that decide their own writes, free-form LLM contributions that bypass rules, emergent LLM behaviors that produce substrate writes without specification. Such an implementation may still read from substrate (A), hold no external state (C), respect human authority passively (D), and attribute its writes (E). The failure mode is specific to B: substrate writes happen without rule-governance, breaking the human-governed commitment at the LLM-write layer.

**Severability of Property C.** An implementation can fail Property C by holding substrate-relevant state in LLM-internal locations — context windows persisted across calls, agent memory, session storage, in-weight memory of substrate content treated as authoritative. Such an implementation may still read from substrate (A) in addition to its external store, write under rules (B), respect authority (D), and attribute its writes (E). The failure mode is specific to C: the source paper's §6.2 *context rot* — capacity overflow, compaction loss, and goal drift under repeated compression of state the substrate could have held instead.

**Severability of Property D.** An implementation can fail Property D by granting the LLM write authority that bypasses the human-governed authority structure — LLM-issued overrides, LLM-modified orchestration rules, LLM-collapsed contradictions under emergent judgment. Such an implementation may still read from substrate (A), write under some rules (B), hold no external state (C), and attribute its writes (E). The failure mode is specific to D: the LLM operates as a governance actor rather than within governance.

**Severability of Property E.** An implementation can fail Property E by allowing LLM outputs to become substrate content without provenance metadata identifying the LLM as writer. Such an implementation may still be a clean substrate reader (A), rule-governed writer (B), stateless across executions (C), and authority-respecting (D). The failure mode is specific to E: downstream traceability fails for any analysis depending on writer identity — audits of LLM-authored content, retrospective examination of which rule produced which write, identification of patterns of LLM behavior across cells.

The five properties are therefore severable in the strong sense the standalone-note treatment requires: each has independent failure modes, each grounds its own derivation, and each requires its own operational test in addition to the parent-frame test in §7.

## 4. Why all five together are jointly necessary

Severability is a property of content; joint necessity is a property of the *role*. The integrated content of the AI-as-substrate-mediator role is that the LLM operates over the substrate as a substrate operation rather than as an independent agent. That integrated content requires all five together because each closes a specific architectural failure mode that no other property addresses.

Without Property A, the LLM operates over something other than the substrate as primary input — not mediating the substrate but mediating its own context. Without Property B, the LLM writes autonomously rather than under rules — acting independently rather than mediating under governance. Without Property C, the LLM accumulates substrate-relevant state externally — partially substituting for the substrate rather than mediating it. Without Property D, the LLM exercises authority that belongs to humans — itself a governance actor rather than a mediator within governance. Without Property E, LLM outputs are anonymous in the substrate — the substrate cannot architecturally distinguish LLM from human contributions, and path retraceability fails.

The five form a closed loop: each closes a specific failure mode, and together they constitute the role. Severally they each ground a specific commitment; jointly they constitute the integrated mediator role.

## 5. What the severable-set frame is NOT

Three adjacent treatments are commonly conflated with the severable-set frame. Naming what the frame is not prevents the misreading.

**Not a layered model.** Layered models arrange commitments in a hierarchy where higher layers depend on lower layers. The severable-set frame is not hierarchical: the five properties are co-equal, none dependent on the others in a layered sense. The joint-necessity argument in §4 does not establish ordering. The frame is a set, not a stack; severability is the absence of layered dependency.

**Not a sufficiency-only treatment.** Sufficiency-only treatments specify what must be true for a system to satisfy a role without specifying what each requirement contributes individually. The severable-set frame goes further: each property has individual operational content, with specific failure modes for each. The frame is operational at both the integrated level and the individual-property level.

**Not a closed-set treatment.** A closed-set treatment would foreclose extension. The frame is not closed. The five are derived from the source paper's specific claims (§4.1, §4.2) and are jointly sufficient for the architectural content the source paper commits to; future extensions may add further properties. What the frame establishes is that *whatever* properties constitute the role must be severable in the sense of §3 and jointly necessary in the sense of §4.

## 6. The cross-claim spine, grounded in property-subsets

§4.2 of the source paper identifies AI-as-substrate-mediator as the cross-claim spine connecting the role to the other architectural commitments. A1.04's §6 states the connections at the integrated-role level; the severable-set frame makes them architecturally specific by grounding each connection in a specific subset of the five.

**Connection to human-governed (per A1.01) grounds in Property D.** The human-governed commitment is preserved at the LLM layer precisely because Property D forecloses LLM authority. The other four properties are silent on authority directly; D is what makes the architectural commitment to human authority hold at the LLM layer.

**Connection to conflict preservation grounds in D plus E.** Conflict preservation requires that contradictions are not silently collapsed. Property D forecloses the LLM collapsing contradictions on its own initiative; Property E ensures that LLM writes engaging with contradictions are attributed and traceable, so any collapse occurring under rule authorization is examinable.

**Connection to tool-agnosticism grounds in A plus B.** Tool-agnosticism requires that the substrate operate in any environment satisfying the three minimal requirements of §7.1. The third — LLM access to substrate content — grounds in Property A (reads) and Property B (writes). Because the LLM operates over the substrate through standard read and write operations rather than specialized runtime middleware, the substrate can live in any environment supporting those operations.

**Connection to linear-cost scaling grounds in Property C.** Linear-cost requires that LLM work scale with cell executions rather than substrate size. Property C makes that the case: the LLM does not maintain global state proportional to substrate size, so its work per cell execution does not grow with how much the substrate carries. An in-weight or agent-memory model would couple LLM cost to substrate size; C decouples them.

**Connection to substrate-as-source-of-truth (per A1.08) grounds in A plus C.** Source-of-truth status requires that the substrate be the authoritative location for the categories of state it commits to carrying. Property A makes the substrate the LLM's primary input; Property C ensures the LLM does not hold substrate-relevant state externally that could compete with the substrate as source of truth. Either alone would be insufficient.

**Connection to path retraceability (per A1.07) grounds in Property E.** Path retraceability requires that substrate writes carry provenance metadata identifying authorship, rule reference, cell identity, and timestamp. Property E is the LLM-layer expression of that requirement: LLM-mediated writes are traceable because they carry attribution identifying the LLM as writer.

The cross-claim spine is therefore not a single connection between AI-as-substrate-mediator and the other commitments. It is a set of specific connections, each grounded in a specific subset of the five properties.

## 7. Operational test at the parent-frame level

A system implements the AI-as-substrate-mediator role at the integrated level if and only if all of the following are true at all times during the substrate's existence:

1. The LLM reads substrate content as the primary source of state for its operations (Property A).
2. The LLM writes to substrate under orchestration rules humans authored (Property B).
3. The LLM does not hold substrate-relevant state outside the substrate (Property C).
4. The LLM does not exercise authority over substrate content beyond what rules grant (Property D).
5. LLM outputs that become substrate content carry provenance attribution identifying the LLM as writer (Property E).

A system satisfying (1)–(5) implements the integrated mediator role. The individual operational tests for each property are specified in A2.19–A2.23 and are not redundant with the parent-frame test, since each individual test specifies the operational shape of one property at a level of detail this test does not reach.

A system that fails any of (1)–(5) does not implement the integrated mediator role, regardless of how well it satisfies the others. The role is integrated; its components are severable in the sense that each has independent content (per §3), but they are not independent in the sense that any subset would suffice (per §4).

## 8. Why naming the severable-set frame as standalone matters

The drift toward partial preservation is structural, not incompetent: each property looks individually optional from the perspective of an implementer focused on a particular design problem. The resulting failures present as governance failures, traceability failures, or cost-model failures rather than as mediator-role failures. The severable-set frame is what makes the mediator-role failures architecturally diagnosable — each downstream failure traces back to a specific missing property, and each missing property identifies a specific commitment that must be restored.

The standalone notes A2.19–A2.23 specialize each property's independent architectural content, completing the AI-as-substrate-mediator decomposition. A reader who finishes this note knows the shape of the decomposition; a reader who finishes A2.19–A2.23 knows each property's standalone content and operational test.

Subsequent work that adopts, extends, or composes the AI-as-substrate-mediator commitment should treat the five properties as a severable set in the sense formalized here. Subsequent work that treats them as fewer than five, or as not severable, or as not jointly necessary, is using a different architectural treatment, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Five Mediator Properties as Severable Architectural Commitments: A Decomposition Frame for the AI-as-Substrate-Mediator Role in CKS.* May 2, 2026. ORCID: 0009-0004-8065-3235.
