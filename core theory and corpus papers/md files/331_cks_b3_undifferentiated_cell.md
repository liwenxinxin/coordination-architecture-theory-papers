# Undifferentiated Cell: The Anti-Pattern That Arises When Cells Are Not Defined With Specific Informational Task Scope per B1.03

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in operational form, the failure mode that arises when the cell-level scope commitment (B1.03) is absent, violated, or only partially satisfied, so that designers and governance practitioners can identify and remediate the pattern without ambiguity.

## Abstract

The Coordination Knowledge Substrate (CKS) architecture structures the AI Self at three levels: cell, aspect, and Self. At the cell level, B1.03 establishes the cell as an atomic unit performing a specific informational task with a clear operational scope — a commitment formalized further in B2.11 through B2.14 and in the content-domain specification requirements at B2.90. The Undifferentiated Cell anti-pattern names the failure mode that occurs when this scope commitment is absent or violated. It takes three recognizable forms: the Monolithic Cell, which handles multiple unrelated informational tasks within a single cell boundary; the Scope-Undefined Cell, which exists without an authored content-domain specification; and the Role-Confused Cell, which performs coordination functions alongside or instead of task execution, behaving as an aspect without having been determined as one under B2.85. The anti-pattern emerges from big-ball-of-mud design practices and from the assumption that scope is obvious enough not to require explicit governance. Its operational consequences span four failure modes: ungoverned boundary drift, untestable behavior, composition failure, and retraceability degradation. Detection proceeds through the content-domain specification check at B2.90, birth verification at B2.44, cell-level inheritance verification at B2.14, the determinism test at A5.06, and composition compatibility assessment at B2.92. Remediation requires decomposing undifferentiated cells into specific-scope cells through governed birth per B1.09, authoring content-domain specifications per B2.90, and, for role-confused cells, considering aspect-level determination per B2.85 where the coordination role is architecturally legitimate.

## 1. The scope commitment at the cell level

The CKS architecture's three-level structure — cell, aspect, Self — assigns a distinct scope to each level. The Self holds multiple aspects as facets of one unified CKS-governed intelligence. The aspect groups cells into a purpose-defined coordination arrangement. The cell performs a specific informational task.

That final assignment is not incidental. B1.03 commits the cell to atomic unit status: each cell handles one informational task with a clear operational territory, carries substrates and orchestration rules specific to that task, and composes with peer cells at the aspect level precisely because each cell's scope is bounded and known. The composition machinery the architecture depends on — mating per B1.07, expression per B1.04, action-feedback evolution per B1.15, content-domain compatibility per B2.92 — operates correctly only when each cell's scope is specific enough to make its DNA layer (the stabilized orchestration and behavior substrates that define how the cell functions) definite, and its action layer (the recorded task instances and outputs that accumulate as lived experience) interpretable in terms of that DNA.

B2.11 through B2.14 decompose this scope commitment: B2.11 names cell scope and the full set of Paper 1 commitments that hold at cell level; B2.12 addresses the cell-internal architecture requirement; B2.14 establishes cell-level inheritance verification as the mechanism that confirms a cell satisfies all scope-relevant commitments. B2.90 states the content-domain specification requirements — what must be authored and present in the substrate for a cell's operational territory to be governed rather than merely assumed. B2.44 establishes birth verification as the point at which completeness is confirmed before a cell enters operational use.

Together, these commitments define what a well-formed cell looks like. The Undifferentiated Cell anti-pattern is what exists when those commitments are not met.

## 2. Recognizable form

The anti-pattern presents in three distinct sub-forms. Each is recognizable from different signals, though all share the same root defect: absence of specific informational task scope at the cell level.

### 2.1 Form 1 — Monolithic Cell

The Monolithic Cell is a single cell handling multiple unrelated informational tasks. Its content-domain per B1.18 is too broad, spanning operational territories that should be separate cells, each with its own DNA layer and governed scope. The cell's substrates accept inputs from multiple unrelated domains; its orchestration rules encode multiple unrelated behavior clusters; its DNA layer is not a coherent body of stabilized behavior logic for one task but an accumulation of behavior logic for several.

The recognition signals are consistent. Cell schemas per B2.25 accept inputs from multiple unrelated domains — a cell whose input schemas span, for instance, contract data, personnel records, and system configuration is not handling one informational task. Cell behavior substrates contain multiple unrelated behavior clusters — the DNA layer reads not as a unified policy for one task type but as a collection of policies for several. Boundary enforcement per B2.91 is absent or too permissive — the cell accepts tasks outside any coherent scope without conflict or escalation.

The Monolithic Cell is the CKS counterpart of the well-known monolith failure mode in software architecture, but located at the cell level rather than the service or module level. The problem is not cell size per se; a cell performing a genuinely complex task may legitimately require substantial substrate content. The problem is scope heterogeneity — the cell's content-domain spans territory that does not cohere as one informational task.

### 2.2 Form 2 — Scope-Undefined Cell

The Scope-Undefined Cell exists without an authored content-domain specification per B2.90. Its operational territory is implicit in the behaviors that have accumulated in its substrates rather than explicit in governed substrate content. The cell may be operable — tasks are completed, outputs are produced — but its scope is what practitioners assume it to be rather than what the substrate specifies it to be.

The recognition signals follow directly from what B2.90 requires. The cell's birth specification per B2.40 is incomplete: input domain schemas are absent or too permissive; behavioral scope is not stated. The content-domain specification requirements at B2.90 are not met, because there is nothing in the substrate that specifies what tasks this cell is and is not scoped to handle. Birth verification per B2.44, if run, fails: the cell cannot demonstrate it was born with complete specification because it was not.

The Scope-Undefined Cell is the more operationally insidious of the three forms because it is not immediately visible as a failure. The cell works. Practitioners use it. Its scope, never having been stated, is never observed to be violated — because there is no stated scope against which a violation could be measured. The failure becomes apparent only when boundary drift occurs (see §4), when composition conflicts arise (see §4), or when someone attempts to verify the cell's behavior against a specification that does not exist.

### 2.3 Form 3 — Role-Confused Cell

The Role-Confused Cell performs coordination functions — organizing other cells, invoking peer cells and integrating their outputs — alongside or instead of its own informational task execution. It is, architecturally, behaving as an aspect rather than as a cell, but it has not been determined as an aspect per B2.85. The aspect level is precisely the level at which coordination arrangements of cells operate over constituent cells as content domain; a cell-level entity that performs coordination is operating at the wrong architectural level.

The recognition signals are located in the cell's DNA layer per B2.25. Coordination logic — invocations of other cells, output aggregation across cells, routing decisions about which cells should receive which tasks — appears in the cell's DNA alongside or instead of task execution logic. The B2.09 level-distinguishability test, applied to the entity, produces a partial result: the entity passes aspects distinguishability tests partially, because part of its behavior is aspect-like, while also appearing cell-like in other respects.

The Role-Confused Cell is often the product of incremental growth rather than initial design error. A cell begins as a well-scoped task executor. Over time, as related cells proliferate, the original cell is assigned coordination responsibilities because it has the relevant context. No governed determination is made to change its architectural level. The coordination functions accumulate in its DNA alongside its task functions, and the boundary between the two levels erodes.

## 3. Emergence conditions

Two conditions generate the Undifferentiated Cell anti-pattern. Neither is inevitable; both are predictable.

**Big-ball-of-mud design.** When architects design a CKS system by placing substantial logic in a small number of large cells rather than decomposing into specific-scope cells, the Monolithic Cell form results. The decomposition into specific-scope cells requires upfront governance effort: each new cell requires a birth specification, content-domain authoring, and birth verification per B2.44. That effort is real, and in systems where governance discipline is weak or where time pressure is acute, it tends to be deferred. Placing more logic in existing cells costs less governance effort in the short term. The consequence is that the cell's content-domain broadens with each deferral, and the governance cost of later decomposition compounds.

**Implicit scope assumption.** When architects treat a cell's operational territory as sufficiently obvious that it need not be stated in the substrate — "the cell handles customer queries," "the cell processes contract documents" — the Scope-Undefined Cell form results. Scope that is obvious at design time is not necessarily obvious to practitioners who encounter the cell later, to governance processes that must verify the cell's behavior, or to composition operations that must assess whether the cell's content-domain is compatible with a peer cell's. The implicit scope assumption is the architectural equivalent of undocumented code: the author's intent is present; the governed, verifiable specification is absent.

The Role-Confused Cell typically emerges from neither of these conditions directly but from the absence of governed architectural-level determination as a system grows. When no mechanism forces the question "is this entity a cell or an aspect," and when practical pressures make incremental scope expansion easier than governed reorganization, cells accumulate coordination responsibilities that should belong at the aspect level.

## 4. Operational consequences

The Undifferentiated Cell anti-pattern generates four categories of operational consequence. All four are traceable to the absence of specific informational task scope at the cell level.

**Ungoverned boundary drift.** Without an authored content-domain specification per B2.90, a cell's scope expands organically as new requirements arrive. Each new task assigned to the cell is not measured against a stated boundary; there is no stated boundary to measure against. The scope drift is not visible in the substrate because scope was never substrate content. What began as a cell handling contract queries may, over months of incremental expansion, be handling contract queries, document routing decisions, personnel action tracking, and configuration state — without any governed determination having been made to extend the scope. The drift compounds: each added responsibility makes it less likely that the cell will be decomposed, because decomposition cost grows with accumulated scope.

**Untestable behavior.** A cell whose content-domain is too broad or undefined cannot be efficiently verified under A5.06 cell-behavior-determinism. The determinism test requires that expected behavior be specifiable precisely enough to test — which requires a stated scope that names what inputs the cell handles and what outputs it is expected to produce for each. A Monolithic Cell handling several unrelated task types must be verified across the behavioral space of all of them; any test suite that covers the space adequately is very large and expensive to maintain. A Scope-Undefined Cell cannot be verified against specification at all, because specification was never authored. The practical result is that testing is shallow — practitioners verify the cases they know about, not the cases the cell's actual scope produces — and regression is invisible.

**Composition failure.** The CKS composition architecture depends on content-domain compatibility per B2.92: cells that compose at the aspect level must have content-domains that do not conflict or overlap in ways that produce A1.03 conflicts — competing, contradictory, or redundant substrate content that must be preserved and resolved. An undifferentiated cell whose content-domain spans multiple operational territories is likely to overlap with peer cells' content-domains in some of those territories. The overlap produces composition incompatibility: the aspect cannot be formed cleanly, conflicts proliferate at the composition boundary, and the conflict-handling machinery is taxed by conflicts that should have been prevented by scope design rather than handled at composition time.

**Retraceability degradation.** The action layer within each cell accumulates recorded task instances and their outputs — the lived experience from which action-feedback evolution per B1.15 draws. When a cell handles multiple unrelated task types, its action layer accumulates records across all of them, interleaved without clear demarcation. Analyzing the action layer for action-feedback evolution becomes difficult: determining which recorded instances are relevant to a proposed DNA refinement requires distinguishing records by task type, which is possible only if the task types were governed and named in the first place. A Scope-Undefined Cell produces an action layer whose records cannot be reliably attributed to any governed task scope. Path retraceability per A1.07 — the ability to trace the provenance of substrate state through the six-field provenance metadata — degrades when the action layer records lack the scope context that makes them interpretable.

## 5. Detection

Five checks identify the Undifferentiated Cell anti-pattern with specificity. Each targets a different aspect of the scope commitment.

**B2.90 content-domain specification requirements check.** For each cell under review: is the input domain specified in the substrate, naming the task types this cell is scoped to handle? Is the behavioral scope specified, naming what outputs the cell is expected to produce and under what conditions? A cell that fails either check is a Scope-Undefined Cell at minimum. This is the primary detection mechanism and should be applied as part of any cell governance review.

**B2.44 birth verification.** Was this cell born with a complete specification? Birth verification confirms, at the point of cell creation, that the cell's birth specification per B2.40 includes the elements required for governed operation. A cell that was never birth-verified, or that failed birth verification and was deployed anyway, has operated without the completeness guarantee. This check surfaces cells that entered the system without governed scope, even if scope has since been informally accreted.

**B2.14 cell-level inheritance verification.** Does the cell satisfy all Paper 1 commitments at cell scope? Inheritance verification is broader than content-domain specification; it confirms that the full set of architectural commitments — human governance, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling, path retraceability — hold at cell level. A cell that fails cell-level inheritance verification on the scope-relevant commitments is undifferentiated in ways that extend beyond missing content-domain specification.

**A5.06 determinism test.** Can the cell's expected behavior be specified precisely enough to test? If a practitioner attempting to write a test specification for the cell finds that they cannot specify the expected output without first determining which of several unrelated task types the input belongs to — and that task-type classification is itself ungoverned — the cell is exhibiting Monolithic Cell behavior. The determinism test surfaces scope heterogeneity operationally.

**B2.92 composition compatibility check.** Does the cell's content-domain, as it can be recovered from the substrate, create conflicts or overlaps with peer cells in the aspects to which it belongs? Composition incompatibility is often the first operationally visible symptom of undifferentiation, because it surfaces when cells that should compose cleanly do not. A cell generating composition conflicts with multiple peers is a candidate for the Monolithic Cell or Scope-Undefined Cell form.

## 6. Remediation

Remediation follows from the commitment the anti-pattern violates: the cell must be brought into conformance with B1.03 by establishing specific informational task scope through governed process.

**Decompose monolithic cells through governed birth.** When a cell's content-domain is too broad, the remediation is decomposition into multiple cells, each carrying a specific informational task scope. Decomposition must proceed through governed birth per B1.09: each new cell is born with a complete specification, including authored content-domain per B2.90, and confirmed through birth verification per B2.44 before entering operational use. The decomposition is not merely a code refactoring; it is a governed determination that the original cell's scope is being partitioned into governed, specific-scope successors. The original cell's action layer — which carries the lived experience accumulated under the broad scope — must be attributed to the successor cells where possible, and the attribution itself recorded as provenance.

**Author content-domain specification for all cells.** Whether or not decomposition is required, every cell must carry an authored content-domain specification per B2.90. For existing Scope-Undefined Cells, authoring the specification is a governance action that makes the operational territory explicit in the substrate for the first time. This is not a description of what the cell currently does; it is a governed statement of what the cell is scoped to do. The distinction matters because cells may have accreted responsibilities outside their intended scope during the period of implicit operation. Authoring the specification creates the reference against which current behavior can be assessed and against which future scope expansion can be governed.

**Use directed selection to add missing specifications.** Where a cell's birth specification is incomplete but decomposition is not yet warranted, directed selection per B1.14 — the governance mechanism for making specific, targeted modifications to cell DNA — is the appropriate mechanism for adding the missing content-domain specification. Directed selection preserves the cell's existing behavior while adding the governance content it lacked. The addition should be followed by birth verification per B2.44 applied retroactively, confirming the cell now meets the completeness requirement.

**For role-confused cells, determine architectural level.** When a cell is performing coordination functions that belong at the aspect level, the remediation requires a governed determination: is the coordination role legitimate and sufficiently substantial to warrant aspect-level determination per B2.85? If so, the entity should be transitioned to aspect status through governed determination, with its task execution functions separated out into a cell and its coordination functions governing as an aspect. If the coordination role is not substantial enough to warrant aspect status, the coordination logic should be removed from the cell's DNA and relocated to the aspect level at which it properly belongs. In either case, the cell left behind after remediation should have a specific informational task scope meeting B1.03 and a complete content-domain specification meeting B2.90.

## 7. Conclusion

The Undifferentiated Cell anti-pattern names what happens at the cell level when the scope commitment of B1.03 is absent or violated. Its three forms — Monolithic Cell, Scope-Undefined Cell, Role-Confused Cell — share a single underlying failure: the cell does not have a specific, governed, authored operational territory. The consequences of that failure compound over time: scopes drift without boundary, behaviors become unverifiable, compositions conflict, and action layers lose the provenance context that makes evolution possible.

The positive commitment the anti-pattern violates — specific informational task scope, authored as governed substrate content, verified at birth — is not primarily a documentation requirement. It is an architectural requirement: the composition machinery, the evolution mechanisms, and the retraceability guarantees that the CKS architecture provides all depend on cells whose scope is specific enough to make their DNA layers definite, their action layers interpretable, and their composition behavior predictable. A cell without specific scope is not a well-formed CKS artifact; it is an accumulation site for ungoverned complexity at the level where governance is most consequential.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Undifferentiated Cell: The Anti-Pattern That Arises When Cells Are Not Defined With Specific Informational Task Scope per B1.03.* May 12, 2026. ORCID: 0009-0004-8065-3235.
