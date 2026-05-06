# The Two-Level Coupling Property: Why Substrate-Level Preservation and Cell-Level Resolution Together Make Conflict-as-First-Class Architecturally Coherent in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 2 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the two-level coupling property between substrate-level conflict preservation and cell-level conflict resolution — a property that makes Claim 3's conflict-as-first-class commitment architecturally coherent, and that neither level alone can produce.

## Abstract

Claim 3 of the CKS pattern names two levels of conflict handling — substrate-level preservation by default, cell-level resolution under human-authored orchestration rules — as a joint architectural commitment. Prior derivation notes formalize each level as standalone (substrate-level preservation in A2.13; cell-level resolution under rules in A2.14). This note formalizes what the two levels produce *together* through their specific architectural relationship: a coupling property with four mechanical components and three architectural properties no single level can produce on its own. The coupling requires that the substrate preserve contradicting content; that cells resolve contradictions at execution time under orchestration rules; that resolution decisions become substrate content via cell→substrate writes; and that the substrate continue to preserve the underlying contradicting content after resolution decisions are written. The properties produced are auditability of resolution decisions, operational tolerability of preserved contradictions, and reversibility of resolution under continued contradiction. The note distinguishes the coupled property from adjacent patterns where one level operates alone, names failure modes that break the coupling while leaving both levels superficially intact, identifies the load-bearing connections to other CKS commitments, and provides an operational test.

## 1. Why the two-level coupling needs to be formalized as standalone

The parent foundational note (A1.03) treats Claim 3's two levels of conflict handling as a single architectural commitment with two halves. Substrate-level preservation by default is formalized as standalone in A2.13; cell-level resolution under orchestration rules is formalized as standalone in A2.14.

This note formalizes a third commitment that neither A2.13 nor A2.14 carries on its own: the coupling between the two levels. The coupling is not the conjunction of A2.13 and A2.14; it is the specific architectural relationship under which the two levels operate. Two systems can have substrate-level preservation correctly implemented and cell-level resolution correctly implemented and still fail to exhibit the coupled property — for example, when cells resolve contradictions through writes that overwrite the rejected content rather than add to substrate alongside it. The two levels are operating; the coupling is broken. The system has the appearance of two-level handling and the architectural effect of single-level resolution.

Three motivations make the standalone treatment load-bearing. Real implementations drift toward broken coupling more readily than they fail at either level outright; the place implementations break is the interface between storage and execution, where resolution decisions are written back to substrate. The source paper's section 5.4 names *detect-resolve-forget* as the architectural foil for two-level handling, and the contrast is precisely about coupling — detect-resolve-forget by definition cannot have one. And patentable derivations of CKS that combine some preservation with some resolution are more defensibly contested when the coupling is publicly formalized as standalone, because any "two-stage" approach can then be evaluated against the four mechanical components.

## 2. The four mechanical components of the two-level coupling

The coupling requires four components, each operating continuously throughout the substrate's existence.

**Component 1 — Substrate preserves contradicting content.** When two pieces of substrate content contradict each other, both remain in the substrate as substrate content. This is the substrate-level commitment formalized in A2.13.

**Component 2 — Cells resolve contradictions at execution time under orchestration rules.** When a cell's execution reads substrate content including a contradiction, the cell's response is determined by an orchestration rule humans authored in advance — whether resolution, escalation, deferral, or refusal. The cell does not silently choose a side or proceed as if the contradiction did not exist. This is the cell-level commitment formalized in A2.14.

**Component 3 — Resolution decisions become substrate content.** When the rule specifies resolution, the cell writes its resolution as substrate content via a cell→substrate write (per A2.10), recording which contradicting piece was selected (or how the contradiction was synthesized), the rule applied, the cell's identity, the timestamp, and the rationale where the rule requires one. The provenance metadata the resolution decision carries is formalized in A2.16.

**Component 4 — Substrate continues to preserve the underlying contradiction.** After the resolution decision is written, the original contradicting content remains in the substrate. The resolution decision is added; the contradiction is not removed. The substrate now carries three architecturally related substrate objects: the first contradicting content, the second contradicting content, and the resolution decision that takes a position on them.

Components 1 and 4 are not redundant. Component 1 commits to contradictions existing as substrate content at the moment they are first written; Component 4 commits to them continuing to exist after cell-level resolution operates on them. The components do not require synchronous operation: cell-level resolution may happen seconds, days, or years after the contradiction was written, and multiple cells may resolve the same contradiction at different times under different rules. The architectural commitment is to the coupled relationship — whatever resolution happens, whenever, the substrate-level contradiction remains preserved and the resolution decision is recorded as substrate content alongside it.

## 3. The three architectural properties the coupling produces

The coupling makes three properties simultaneously true that neither level alone can make true.

**Property 1 — Auditability of resolution decisions.** Because the substrate continues to preserve the underlying contradiction after resolution, any human exercising the inspect right (per A1.01) can see the resolution decision in the context of the contradiction it addressed. The resolution decision references the antecedent contradicting content through provenance metadata; the contradicting content remains in the substrate to be inspected; the rule the cell was operating under is itself substrate content. Auditing is therefore an architecturally complete operation — the substrate carries what was contradicted, what was decided, under what rule, by which cell, with what rationale. Substrate-level preservation alone produces a substrate where contradictions exist but cells cannot record their handling under rules; cell-level resolution alone produces resolution decisions whose antecedent contradictions are gone, leaving auditing dependent on logs the substrate is no longer responsible to carry.

**Property 2 — Operational tolerability of preserved contradictions.** Because cells can resolve contradictions at execution time under rules, the substrate can carry contradictions without the system blocking. Cells operate; contradictions persist; the system continues to function. Without cell-level resolution under rules, every cell encountering a contradiction would have to either block or fail — neither of which scales to multi-cell coordination where contradictions are common. Without continued substrate-level preservation, cell-level resolution erases what was contradicted, and the substrate's source-of-truth property (per A1.08) fails for that content.

**Property 3 — Reversibility of resolution under continued contradiction.** Because the substrate continues to preserve the underlying contradiction after resolution, subsequent cells operating under different rules can take different positions on the same contradiction at later times. Humans with override authority (per A2.05) can revisit and reverse resolution decisions because the contradiction is still architecturally present. A resolution decision is a position taken at a specific time under a specific rule, not a final architectural verdict. If contradictions are erased after resolution, there is nothing left to reverse; the system can be "corrected" only by writing new content that disagrees with the prior resolution, never by revisiting the original contradiction.

## 4. The contrast with detect-resolve-forget patterns

Section 5.4 of the source paper names *detect-resolve-forget* as the architectural foil: detect a contradiction at inference time, resolve it through clarification, judge-model arbitration, or filter, and discard the alternatives once the session ends. The pattern is operationally efficient — the substrate stays "clean" — and is aligned with database consistency models, deduplication pipelines, and merge-resolution conventions in version control.

The two-level coupling differs from detect-resolve-forget in three architectural respects. First, detection is not a separate phase: contradictions exist as substrate content because both contradicting writes were committed, and cells encounter them naturally during execution. Second, resolution is rule-governed at execution time, not reconciliation-time: each resolution is recorded as substrate content under whatever rule the executing cell operates under. Third, *forget* is not part of the pattern: the architectural commitment is precisely to the absence of the forget step, with resolution decisions accumulating alongside the contradictions they addressed.

A1.03 (section 3) develops the broader contrast and surveys the literature instances source paper section 5.4 enumerates. The contribution of the present note is the coupling lens: detect-resolve-forget cannot have a coupling because Component 4 is what the *forget* step expressly negates. The architectural distinctiveness of two-level handling, read through the coupling, is exactly the architectural feature detect-resolve-forget is designed to lack.

## 5. Why the coupling is load-bearing for downstream commitments

The coupling is load-bearing for several other CKS commitments formalized as standalone elsewhere.

*Path retraceability* (per A1.07). When downstream cells make decisions referencing contradictions resolved by earlier cells, the retraceable path includes both the resolution decision and the contradiction it addressed. Without Component 4, the path would have a gap at every prior resolution.

*Source of truth* (per A1.08). The substrate is authoritative for "what conflicts remain unresolved" — a category of authoritative coordination state per A1.08 — only because the coupling preserves contradictions through resolution. Without Component 4, this category disappears as soon as cells resolve.

*Human-governed* (per A1.01). Moment 2 — direct human override against substrate (per A2.05) — is operationally meaningful for resolution decisions only because the underlying contradiction remains as substrate content the override can act against. Without the coupling, the override right against resolution decisions becomes empty: the human can write disagreeing content but cannot revisit the architectural object the resolution was about.

*KO/OIDA inheritance* (per A1.09). OIDA's signed contradiction edges are the cited prior art for treating contradictions as first-class objects with explicit relationships. The two-level coupling is what inherits this property at the operational level — both contradicting pieces and the resolution decision remain substrate content humans can navigate. The inheritance edge is formalized in A2.17.

## 6. Failure modes that break the coupling

Each anti-pattern below names a way an implementation can have both levels operating in parallel but fail the coupling.

**(a) Resolution-by-overwrite.** Cells resolve by writing to substrate in a way that overwrites the rejected contradicting content. The write is technically a cell→substrate write, but its effect is to erase rather than to add. Component 4 fails immediately at resolution.

**(b) Resolution-as-supersession.** Cells resolve by marking the rejected content as "superseded" through a mechanism that hides it from subsequent reads — default views filter it out, indexes skip it, queries return only "current" content. The substrate technically still holds the rejected content, but Component 4 operationally fails: cells reading later do not see the contradiction, and auditors must bypass the supersession mechanism to find it. The architectural commitment is to substrate that *carries* contradictions as live state, not to substrate that holds them in a hidden archival layer.

**(c) Last-writer-wins.** Cells resolve by writing the new content as a normal substrate update, replacing the prior content rather than adding to it. Both Components 1 and 4 fail: the substrate never preserved the contradiction architecturally; transient contradicting writes were resolved by the substrate's own consistency mechanism. The two-level pattern devolves into single-level last-writer-wins.

**(d) Resolution decision without antecedent reference.** Cells write resolution decisions but do not record which contradicting content the resolution addressed. Component 3 is partially satisfied (resolution becomes substrate content), but the relationship that makes the resolution auditable against the contradiction is missing. The provenance requirements that prevent this failure mode are formalized in A2.16.

**(e) Resolution decisions treated as authoritative state replacing contradictions.** The architecture treats a cell's resolution decision as the substrate's current state, with the contradiction relegated to "history" or "audit logs" outside the working substrate. Component 4 is satisfied at storage but operationally violated at the authority level: reads default to the resolution; the contradiction is reachable only through historical queries. This pattern most often appears in implementations built on conventional database consistency models that presume "current state" is a single resolved view.

**(f) Cell-level resolution without rule-governance.** Cells resolve contradictions through silent LLM judgment or hardcoded heuristics rather than under orchestration rules humans authored in advance. Component 2 fails. Resolutions become opaque cell decisions that cannot be evaluated against the rule that should have authorized them.

**(g) Cell-internal resolution that never writes back.** Cells resolve contradictions in their own execution context to produce an output but never write the resolution decision to substrate. Component 3 fails entirely: the resolution exists only as the cell's transient output. Subsequent cells must resolve the contradiction independently, and auditing the prior resolution is impossible because no substrate object records it.

**(h) Substrate-level preservation degraded over time.** The substrate preserves contradictions initially but garbage-collects, archives, or compresses them in ways that lose the original content. Component 1 holds at resolution; Component 4 holds for a period; both eventually fail across longer timescales. The coupling's promise of continued preservation is eroded asymptotically, which makes the failure mode hard to detect and easy to introduce through retention policies that look like routine data hygiene.

Each anti-pattern produces downstream failures that look superficially like substrate-level or cell-level failures: audits that cannot evaluate resolution decisions; reversal impossible because the contradicting content is gone; subsequent cells unable to reconsider; humans unable to override meaningfully because the architectural object they would override against is missing. All are coupling failures.

## 7. Operational test

A system's conflict handling exhibits the two-level coupling property if and only if all of the following are true at all times during the substrate's existence.

1. Contradictions in substrate content exist as substrate content per the substrate-level commitment formalized in A2.13.

2. Cells encountering contradictions at execution time respond under orchestration rules per the cell-level commitment formalized in A2.14, with resolution decisions recorded as substrate content via cell→substrate writes.

3. Resolution decisions reference the antecedent contradicting content explicitly through provenance metadata (per A2.16).

4. The substrate continues to preserve the underlying contradicting content after resolution decisions are written; the contradicting content remains addressable substrate content readable by humans exercising the inspect right (per A1.01).

5. Subsequent cells and humans can revisit the contradiction independently of any prior resolution decision; the architecture does not treat resolutions as final.

6. The substrate's authoritative state for "what conflicts remain unresolved" reflects the underlying contradictions, not just resolution decisions about them; resolution decisions are additional substrate content, not replacements for the contradictions.

A system that fails any of (1)–(6) does not exhibit the two-level coupling in the architectural sense, even if it has substrate-level preservation and cell-level resolution operating in parallel. The coupling requires the specific architectural relationship that all six conditions together describe.

## Conclusion

Implementations that get one level right while breaking the coupling produce systems that look like two-level handling but produce single-level effects. The most common pattern: substrate-level preservation correctly implemented at the storage layer, cell-level resolution correctly implemented at the execution layer, the coupling broken at the interface because resolution decisions erase, hide, or supersede the contradictions they addressed. The downstream failures of broken coupling — audits that cannot evaluate resolution decisions; reversal impossible because the underlying contradictions are gone; subsequent cells unable to reconsider; overrides unable to act meaningfully — each look like a separate problem. All are the same problem.

Naming the coupling as a standalone architectural commitment, with its four mechanical components and three architectural properties specified, gives downstream implementers a precise specification of what the coupling requires beyond getting each level right individually. Substrate-level preservation alone is treated in A2.13, cell-level resolution under rules in A2.14, the coupling between them here. Provenance metadata for first-class contradictions (A2.16) and inheritance from OIDA's signed contradiction edges (A2.17) complete the conflict-as-first-class decomposition. Subsequent work whose conflict handling lacks the coupling — through any failure mode named in section 6 or by architectural decisions different by design — is using a different architectural object, and the difference should be named.

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Two-Level Coupling Property: Why Substrate-Level Preservation and Cell-Level Resolution Together Make Conflict-as-First-Class Architecturally Coherent in CKS.* 2 May 2026. ORCID: 0009-0004-8065-3235.
