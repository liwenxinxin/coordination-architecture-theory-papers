# Shared Substrate Provenance Chain: Six Paper 1 Provenance Metadata Fields at Inter-Self Scope, Cross-Organizational Provenance References, and Traceability Spanning Construction, Operation, and Dissolution Phases

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

D1.02 committed that all six Paper 1 commitments hold within the shared substrate, including commitment A1.07 — path retraceability. This note (D2.03) is an operational decomposition of that commitment: it formalizes what path retraceability means within the shared substrate at inter-Self scope. The six provenance metadata fields Paper 1 A1.07 specifies apply to all shared-substrate content without modification. What is new at inter-Self scope is cross-organizational reach: the "who authored" field now identifies the home governance authority of the contributing Self, and the "what came before" field can reference content in a different organization's home substrate. The depth of that cross-perimeter reference is governance-configured — specified as a dimension of the shared substrate's configuration before construction begins. For any content in the shared substrate, an observer must be able to trace it back through the six fields to its contributing Self's home governance records. This traceability requirement holds across all three phases of a shared substrate's existence: construction, operation, and dissolution.

## 1. D2.03 as operational decomposition of D1.02

D1.02 establishes that all six Paper 1 architectural commitments hold within the shared substrate. Paper 1 Commitment A1.07 — path retraceability — is one of those six. The commitment states that every piece of substrate content must carry sufficient provenance that the path back to its antecedents is reconstructable from substrate content alone, and that the plan-trace coupling holds: a plan specifies what the trace must capture, and the trace records what the plan required.

D1.02 applies this commitment wholesale to the shared substrate. D2.03 does not alter or extend D1.02. It does the narrower work of stating what A1.07's six provenance metadata fields look like operationally when the substrate spans more than one organization's governance perimeter. The fields are inherited unchanged; what changes is the scope of their referents. At inter-Self scope, two of the six fields acquire cross-organizational reach, and that reach introduces the cross-perimeter reference mechanism this note formalizes.

## 2. The six provenance metadata fields at inter-Self scope

Paper 1 A1.07 specifies six provenance metadata fields that every piece of substrate content must carry. At inter-Self scope within the shared substrate, each field applies without modification, and two fields carry additional inter-organizational information.

**Field 1 — WHAT.** The content itself: which DNA-layer or action-layer content is present in the shared substrate, and from which contributing Self's aspect it originates. This field is unchanged from Paper 1 in structure; its value at inter-Self scope identifies the contributing Self in addition to the content type.

**Field 2 — WHO AUTHORED.** The governance authority that authored this content. Within a single organization, "who authored" identifies a human acting under preserved override authority, or an LLM operating under a named orchestration rule. At inter-Self scope, the same identification applies, and the field additionally names the home governance authority of the contributing Self — the governance structure within which that author operates. This is the first field that gains cross-organizational reach: "who authored" now answers not only "which human or cell" but "under which organization's governance."

**Field 3 — WHO AUTHORIZED.** Which joint governance authority authorized this content's presence in the shared substrate. This field is distinctive to inter-Self scope: it identifies the authorization event that permitted content from a contributing Self's home governance to enter the shared substrate under joint governance. The authorization is the plan-layer record of cross-perimeter content entry; without it, content in the shared substrate has no accountable approval trail back to joint governance.

**Field 4 — WHEN.** The timestamp of when the content entered the shared substrate. This field is unchanged from Paper 1. Its role at inter-Self scope is the same as within a single substrate: the timestamp makes the path orderable, without which antecedence relationships cannot be evaluated.

**Field 5 — WHY.** The governance reasoning for inclusion, connected to the FAI event purpose. At inter-Self scope, this field records the rationale as expressed within the shared substrate's governance scope — why the joint governance authority authorized this content's contribution, not only what the contributing Self's internal rationale was.

**Field 6 — WHAT CAME BEFORE.** The prior version or state within the shared substrate, and — at inter-Self scope — the provenance carry-over depth reference to the contributing Self's home substrate. This is the second field that gains cross-organizational reach. "What came before" in Paper 1 refers to antecedent substrate content within the same governance scope. At inter-Self scope, this field additionally carries a reference that crosses the organizational boundary: it points, at governance-configured depth, to the relevant record in the contributing Self's home substrate. The depth of that reference is specified in the shared substrate's configuration substrate before construction begins (D1.22 Dimension 5), as addressed in §3.

## 3. Cross-organizational provenance chain and reference depth

For content contributed by a Self to the shared substrate, the provenance chain crosses organizational boundaries. The chain has two segments.

The within-shared-substrate segment is governed by the six fields described in §2: content, authorship under home governance, joint authorization, timestamp, governance rationale, and the antecedent record within the shared substrate. This segment is what a reader within the shared substrate's scope can reconstruct from substrate content alone.

The cross-perimeter segment is what Field 6 points to: the relevant record in the contributing Self's home substrate. This reference is what allows an observer to trace content in the shared substrate back to its governance origin in a contributing organization — back to the home substrate record that established this content before it was contributed, and to the governance authority that approved its authorship there.

The depth of the cross-perimeter reference is governance-configured. Depth is specified as a dimension of the shared substrate's configuration substrate — authored before the shared substrate is constructed, under joint governance, as substrate content — and it determines how far Field 6's "what came before" reference reaches into the contributing Self's home substrate.

At shallow depth, the reference is a pointer to the contributing aspect: the shared substrate carries an identifier that names which aspect of which Self contributed this content, but does not carry the full antecedent chain from within that aspect's home substrate. This is sufficient for identification and first-level traceability; an observer who needs deeper lineage follows the pointer to the contributing Self's home substrate and queries there.

At deep depth, the reference carries the contributing Self's antecedent lineage chain as part of the shared substrate's Field 6 record: prior versions, prior governance decisions, the full provenance chain as it existed in the home substrate at contribution time. This is appropriate when the shared substrate must remain independently auditable — when an observer should be able to reconstruct the full provenance chain without accessing the contributing Self's home substrate directly.

The governance-configured nature of reference depth is architecturally significant: depth is a decision made under joint human authority before the FAI event begins, not an implementation choice made at ingestion time. Different contributing Selves may contribute content at different configured depths within the same shared substrate event, if the configuration substrate specifies this. The configuration substrate is itself substrate content subject to the same six provenance fields, and its provenance is therefore fully traceable under the same commitment.

## 4. Operational traceability requirement

For any content in the shared substrate, the traceability requirement is that an observer can:

**(a)** Identify which contributing Self provided this content and from which of that Self's aspects. This is a Field 1 (WHAT) and Field 2 (WHO AUTHORED) read. The content record names the aspect and the contributing Self's home governance.

**(b)** Find the home-substrate governance records that authorized the contribution. This is a Field 2 and Field 3 read. Field 2 identifies the home governance of the author; Field 3 identifies the joint authorization event. Together they give the observer two audit paths: one into the contributing Self's home governance records and one into the joint governance record of the authorization event within the shared substrate.

**(c)** Determine when the content entered the shared substrate and under what joint governance authority. This is a Field 4 (WHEN) and Field 3 (WHO AUTHORIZED) read. These fields together establish the accountability trace record for the content's arrival in the shared substrate.

**(d)** Trace the content's antecedents across the organizational boundary, to governance-configured depth. This is a Field 6 (WHAT CAME BEFORE) read. The depth of that trace is what the configuration substrate specifies. A shallow-depth configuration satisfies the traceability requirement to the pointer level; a deep-depth configuration carries the full antecedent chain.

**(e)** If the persistence policy retains Locus 2 content — the durable record produced when the shared substrate dissolves — trace content in that durable record back to its shared-substrate provenance chain. The same six fields apply in the Locus 2 record; the dissolution phase's provenance requirements are addressed in §5.

The requirement is that each of (a)–(d) is satisfiable from substrate content alone for in-scope content, and (e) is satisfiable from the durable record for post-dissolution content. Where the reference is a pointer to a contributing Self's home substrate rather than a carried chain, satisfying (b) and (d) involves following that pointer into the contributing Self's substrate — this is within scope of the traceability commitment, since the pointer itself is substrate content and the path to the external record is reconstructable from it.

## 5. Provenance chain spanning three phases

The shared substrate exists across three phases, and the provenance chain must span all three.

**Construction phase.** Provenance of the shared substrate's creation and initial configuration. The configuration substrate — which specifies the contributing Selves, the aspects each contributes, the provenance carry-over depth, and the persistence policy — is itself governed by the six fields. Who authored the configuration, under whose governance authority, when, and what prior drafts came before: all of these are substrate content. Joint authorization of the configuration is recorded in Field 3 for each configuration element. Construction-phase provenance is what makes the shared substrate's initial state accountable before any FAI event content is contributed.

**Operation phase.** Provenance of all content that enters, changes, or is governed within the shared substrate during the FAI event. Every contribution from a Self, every conflict record, every resolution under the three-tier conflict mechanism, every orchestration-rule execution — all carry the six fields. The cross-organizational dimensions of Fields 2 and 6 apply throughout the operation phase. A full operation-phase provenance chain means that an observer who inspects the shared substrate at any point during the FAI event can reconstruct the accountability record for every piece of content present.

**Dissolution phase.** Provenance of the dissolution event and persistence policy execution. When the shared substrate dissolves, the dissolution event is itself a governed action with provenance: who authorized dissolution, when, under what joint governance authority, and in accordance with which persistence policy. The persistence policy specifies what is retained at each of the three persistence loci; the execution of that policy is a governed transition that leaves a provenance record. If the policy retains a Locus 2 durable record, that record inherits the provenance chain from the operation phase, and the dissolution event adds its own provenance as the final link in the chain.

A shared substrate that carries complete provenance across all three phases is one from which an observer can reconstruct the full accountability record: what was decided before the event, what happened during it, and how it closed. The three phases together constitute the plan-trace structure: the construction phase establishes the plan (the configuration substrate specifies what the trace must capture); the operation phase accumulates the trace; the dissolution phase closes it with a governed terminal record.

## 6. Inheritance from Paper 1 A1.07

The analysis in this note is entirely derived from Paper 1 A1.07. The six provenance metadata fields are Paper 1's; the plan-trace coupling is Paper 1's; the requirement that provenance is carried as substrate content rather than as external logs is Paper 1's. D1.02 commits that these Paper 1 requirements hold within the shared substrate, and D2.03 applies them at inter-Self scope.

What this note contributes is specificity about two derivable consequences of that inheritance. First, that the inter-organizational dimension of "who authored" and "what came before" is a structural consequence of applying Paper 1's fields to a substrate whose governance perimeter spans multiple organizational boundaries — not a new field requirement, but an expanded referential scope of existing fields. Second, that the depth of the cross-perimeter reference is governance-configured rather than fixed — a consequence of Paper 3's general principle that configuration dimensions are substrate content under joint human authority (D1.22), applied to the "what came before" field specifically.

Neither consequence introduces a new architectural primitive. Both follow from applying Paper 1's existing provenance commitment to Paper 3's perimeter-spanning substrate.

## 7. Operational test

A shared substrate instantiates the provenance chain commitment if and only if, for any piece of content within the shared substrate, all of the following hold:

1. An observer can identify, from shared-substrate content alone, which contributing Self provided this content and from which aspect.
2. An observer can find, from shared-substrate content, the joint governance authorization event that permitted this content's entry into the shared substrate.
3. An observer can follow Field 6's reference to the contributing Self's home substrate, to at least the governance-configured reference depth, and find the home-governance record that corresponds to this contribution.
4. An observer can trace the content's full shared-substrate provenance chain — from construction-phase configuration through operation-phase contribution to dissolution-phase closure — without consulting sources external to the shared substrate (or the Locus 2 durable record, post-dissolution).
5. The reference depth configured in the construction-phase configuration substrate is itself subject to the six provenance fields — an observer can trace who authored the depth configuration, under whose joint governance authority, and when.

A shared substrate that fails (1) or (2) does not satisfy the traceability requirement at inter-Self scope. A shared substrate that fails (3) at its configured depth has a broken cross-perimeter provenance chain. A shared substrate that fails (4) has an incomplete operation-phase trace. A shared substrate that fails (5) has an unaccountable configuration — the depth decision itself is outside the provenance commitment, which is an architectural gap.

## 8. Conclusion

Paper 1 A1.07's path retraceability commitment, applied within the shared substrate by D1.02, means the following at inter-Self scope. The six provenance metadata fields apply to all shared-substrate content. Two of those fields — "who authored" and "what came before" — carry cross-organizational referents at inter-Self scope: the first identifying the home governance of the contributing Self, the second referencing content in the contributing Self's home substrate at governance-configured depth. The depth of that cross-perimeter reference is a configuration dimension specified before the shared substrate is constructed, as joint-authority substrate content. The traceability requirement is that an observer can trace any shared-substrate content back to its contributing Self's home governance records. That requirement holds across all three phases — construction, operation, and dissolution — spanning the full plan-trace structure of the FAI event. This is Paper 1 A1.07 at inter-Self scope: same fields, same commitment, cross-organizational reach.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Shared Substrate Provenance Chain: Six Paper 1 Provenance Metadata Fields at Inter-Self Scope, Cross-Organizational Provenance References, and Traceability Spanning Construction, Operation, and Dissolution Phases.* May 14, 2026. ORCID: 0009-0004-8065-3235.
