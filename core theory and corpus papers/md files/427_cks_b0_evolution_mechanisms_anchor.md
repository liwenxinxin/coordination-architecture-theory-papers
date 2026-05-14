# Three Evolution Mechanisms as Paper 2's Fourth Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Paper 2's fourth architectural claim — three evolution mechanisms operating in productive tension under unified human governance — as a paper-claim-level commitment with explicit sub-commitments and anti-patterns mapped as derivations.

## Abstract

Paper 2 defends six architectural claims; its fourth states that a CKS-governed Self evolves through three independently-operating mechanisms — *instinct evolution*, *DNA evolution*, and *action-feedback evolution* — targeting architecturally separated layers under distinct governance shapes, composing under the commitment that they do not interfere with each other. Non-interference is itself an architectural commitment, not an incidental coexistence. The claim further commits to bidirectional propagation across both axes (horizontal, refining content within existing structure; vertical, reorganizing structure itself) and to concurrent operation at every level of composition. Paper 1 established the substrate and the LLM mediator role at cell scope but did not define an evolution model for entities; Paper 2 Claim 4 introduces the three-mechanism model as new architectural commitment. This note names each mechanism by its layer target and governance shape, distinguishes governed-effects from governed-choices, locates productive tension as the non-interference contract, maps the derived B1.xx sub-commitments and B3.xx anti-patterns, and provides an operational test.

## 1. Why Claim 4 needs its own anchor

Paper 2 §7 develops three evolution mechanisms — instinct evolution, DNA evolution, and action-feedback evolution — together with the productive-tension framing under which they compose, the multi-level simultaneity that lets cells, aspects, and Selves evolve concurrently, and the dual-axis structure distinguishing refinement within structure from reorganization of structure. The derivation-note program decomposes §7 into six B1.xx sub-commitments (B1.09–B1.14), an operational-variant set, four B3.xx anti-patterns targeting evolution misreadings, and downstream composition pairs, tests, and boundary cases. These decompositions presuppose a named parent at paper-claim level. Phase B0 supplies it.

The motivation is not only structural. The most common misreading of §7 collapses Claim 4 into a single proposition — "CKS Selves evolve under governance" — that erases the architectural separation between mechanisms and the non-interference commitment across them. Under that collapse, a deployment with one mechanism appears compliant when in fact it has dropped two of the three and lost the productive-tension property the claim commits to. Naming Claim 4 as four commitments rather than one — three mechanisms plus their non-interference — makes the misreading visible and the architectural property recoverable.

## 2. The claim, stated

A CKS-governed AI Self evolves through three mechanisms operating concurrently and under unified human governance, with each mechanism targeting a distinct architectural layer and operating under a distinct governance shape. The three mechanisms are *instinct evolution* (operating on the LLM and substrate-platform infrastructure layer), *DNA evolution* (operating on the orchestration substrate content), and *action-feedback evolution* (closing the loop from recorded action experience back into governed DNA refinement). They operate in productive tension: each composes with the others under governance integration without interfering with the others' operation. Evolution operates across both axes — horizontal, refining content within existing structure; vertical, reorganizing structure itself — and at every level of Claim 2's composition concurrently.

Four sub-commitments compose the claim:

1. **Three named mechanisms exist** as architectural primitives, each with a distinct layer target.
2. **Each mechanism operates under a governance shape appropriate to its target** — verification machinery for instinct integration, authority architecture for DNA, proposal-and-acceptance machinery for action-feedback.
3. **Productive tension is itself an architectural commitment** — the three operate on separated layers and do not interfere; non-interference is what the architecture commits to.
4. **Bidirectional propagation across multiple levels** — horizontal and vertical axes, cell/aspect/Self levels, all under the three mechanisms.

## 3. The three mechanisms

### 3.1 Instinct evolution: governed-effects, not governed-choices

Instinct evolution sharpens what a cell can do at the instinct/infrastructure layer through upgrades arriving from upstream. Two kinds carry the mechanism: commercial or upstream LLM upgrades (when a provider releases a more capable model the Self consumes under verification rather than authoring), and substrate-platform infrastructure upgrades (which sharpen what cells can do at the infrastructure layer without changing DNA content). Both arrive from upstream and are mutation-like: undirected from the Self's perspective, capability jumps that may be good or bad in any specific case.

This is the distinctive asymmetry the claim carries. Instinct evolution is not directly human-authorized in the sense the other two mechanisms are — humans do not write the LLM, and humans do not implement the substrate platform. What humans govern is the *effects* of the mutation on the Self's operation: which upgrades the Self consumes, on what verification basis, with what retention of prior reasoning as fallback or as active verification on safety-critical paths, with what pinning of high-stakes decisions to the prior version until verification clears. The choice itself sits upstream of the Self's authority; the integration of that choice is fully within it. Governed-effects versus governed-choices is the load-bearing distinction. B1.10 names this mechanism — *instinct evolution as undirected mutation (LLM and infrastructure)* — preserving the mutation-like character precisely so the asymmetry is not lost downstream.

### 3.2 DNA evolution: directed selection under governance authority

DNA evolution operates on the CKS substrate's stabilized orchestration content under explicit goals defined by human governance. Where instinct evolution is mutation-like, DNA evolution is the canonical directed-selection form CKS commits to. Selection criteria for accepted, retained, or reverted DNA changes are themselves substrate content — governable under the same authority architecture that governs the content they evaluate.

Direction here means goal-defined-by-human-governance: not by internal system state, not by a fitness function frozen at design time, not by emergent bias. Direction is external (humans set the goals) and persistent (governance authority is ongoing rather than front-loaded into a configuration that runs autonomously). DNA changes may be drafted by LLMs operating under human direction; authority over the orchestration rules and acceptance decisions rests with humans. DNA evolution is also the locus of *horizontal evolution* in its directed-selection variant: when an improvement that emerged in one entity is applied to peers within the same aspect, propagation is governed as a directed-selection event under the same authority architecture. The horizontal axis does not introduce a new mechanism; it instantiates DNA evolution across a peer set. B1.11 names the mechanism — *DNA evolution as directed selection (orchestration substrate)*.

### 3.3 Action-feedback evolution: indirect by commitment

Action-feedback evolution closes the loop from recorded action experience back into governed DNA refinement. The action layer accumulates evidence — what worked, what failed, what surprised — and that evidence is evaluated through proposing-substrate machinery to generate improvement proposals, which are reviewed under governance and, when approved, implemented as directed-selection events on the DNA layer.

The chain has discrete, human-mediated steps. Operational evidence accumulates in the action layer. A proposing substrate evaluates the evidence and generates an improvement proposal — possibly drafted by an LLM under human-authored orchestration rules. Governance review evaluates the proposal at two stages: first at the proposing substrate's own evaluation, then at the governance decision where humans with appropriate authority authorize the DNA change. Approved proposals are implemented as DNA-evolution events with the same provenance, verification, and reversion-path commitments DNA evolution carries on its own.

The mechanism is indirect by design. Operational evidence does not modify DNA. Proposals do not modify DNA. Only authorized governance decisions, executed as DNA-evolution events, modify DNA. Compressing the chain — letting the proposing substrate auto-apply its own proposals, or treating accumulated evidence as authoritative for DNA refinement — is the Evidence Blindness anti-pattern §7 formalizes. B1.12 names the mechanism — *action-feedback evolution as the closing-the-loop mechanism*.

## 4. Productive tension as non-interference commitment

The three mechanisms target different architectural layers: instinct evolution on the instinct/infrastructure layer; DNA evolution on the DNA layer (the stabilized orchestration content Paper 2 Claim 2 commits as a distinguishable substrate layer within every cell); action-feedback evolution on the DNA layer indirectly, through the proposal-to-governance chain.

Productive tension is the commitment that the three operate on these separated layers without interfering with each other:

- **Mutation does not alter DNA specifications.** An LLM version change does not, by itself, modify the orchestration substrate. Verification machinery may *trigger* DNA-evolution events as a downstream response, but those events are themselves governed under DNA evolution's authority architecture; mutation does not write DNA directly.
- **Directed selection does not alter LLM versions.** A governance-authored DNA change does not modify the LLM the cell uses; LLM-version transitions remain governed under instinct evolution's verification machinery.
- **Action-feedback does not bypass governance review.** Operational evidence does not modify DNA; only governance-authorized proposals do, and only via the directed-selection authority architecture. The action layer cannot become a side-channel.

These three non-interference properties together compose the productive-tension commitment. Violating any of them drops Claim 4 to a single-mechanism evolution model and loses the architectural property the claim commits to. Paper 2 §7.2 names the property compactly: the mechanisms operate on architecturally separated layers, so they do not interfere; they compose because governance integrates them.

## 5. Bidirectional and multi-level evolution

Claim 4 commits two further structural properties decomposed as separate sub-commitments.

**Horizontal and vertical axes.** Horizontal evolution refines content within existing structure; vertical evolution reorganizes structure itself — cells split or merge, aspects gain or lose constituent cells, Selves gain or lose aspects, relational roles reconfigure. Vertical evolution is architecturally available because Claim 2 commits the orchestration substrates defining composition to be themselves substrate content humans govern in the same way DNA content is governed; structural reorganization is therefore a substrate-edit operation. Both axes operate through the three mechanisms. B1.14 names the dual-axis commitment.

**Multi-level simultaneous evolution.** The three mechanisms apply at every level of Claim 2's three-level structure concurrently. Cells evolve through their internal DNA/action loops; aspects evolve through their constituent cells' evolution plus aspect-level orchestration changes; Selves evolve through their constituent aspects' evolution plus Self-level structural reorganization. Bidirectional propagation includes both horizontal (peer-to-peer within aspect) and vertical (bottom-up from cell-level improvements to aspect-level and Self-level architecture). B1.13 names the multi-level commitment.

## 6. Paper 1 inheritance and what Paper 2 adds

Paper 1 §3.3's authority-vs-labor distinction holds across all three of Claim 4's mechanisms. Paper 1 §4's substrate/LLM division at the governance boundary holds throughout: instinct evolution operates on the inside-the-model layer through upstream upgrades; DNA evolution and action-feedback evolution operate on the outside-the-model layer through governed substrate-content modification.

What Paper 1 did not define is the three-mechanism evolution architecture itself. Paper 1 deployments can change — substrate content can be edited, orchestration rules can be revised, the underlying LLM can be upgraded — but Paper 1 does not commit those changes to a structured three-mechanism model with distinct governance shapes and a non-interference contract among them. Claim 4 introduces that model. The model is what makes evolution itself a governed property of the Self rather than a deployment-level operational concern.

## 7. Derived sub-commitments and anti-patterns

Six B1.xx sub-commitments derive from Claim 4:

- **B1.09 — Three evolution mechanisms in productive tension.** The umbrella sub-commitment naming all three mechanisms together with the non-interference contract.
- **B1.10 — Instinct evolution as undirected mutation (LLM and infrastructure).** The mutation-like mechanism with governed-effects machinery.
- **B1.11 — DNA evolution as directed selection (orchestration substrate).** The canonical directed-selection mechanism.
- **B1.12 — Action-feedback evolution as the closing-the-loop mechanism.** The indirect, proposal-mediated evidence-to-DNA chain.
- **B1.13 — Multi-level simultaneous evolution.** Concurrent evolution at cell, aspect, and Self levels under governance integration.
- **B1.14 — Horizontal vs. vertical evolution.** The dual-axis commitment with structural reorganization as substrate-edit operation.

Four B3.xx anti-patterns formalize the commitment by naming what violates it:

- **B3.20 — Instinct evolution without verification governance** (the Ungoverned Mutation anti-pattern). An LLM version change reaches operational cells without verification machinery, retention decisions, or pinning of high-stakes decisions; governed-effects is dropped.
- **B3.21 — DNA evolution without authority architecture.** Orchestration substrate changes occur outside the authority architecture Paper 1 §3.3 and Paper 2 §8 commit to; directed selection becomes ad hoc edit.
- **B3.22 — Action-feedback as automatic DNA modification** (the Evidence Blindness / Ungoverned Evolution anti-pattern). Operational evidence drives DNA changes directly, or the proposing substrate auto-applies its own proposals; action-feedback's indirect-by-commitment structure is collapsed.
- **B3.23 — Collapsed mutation/directed-selection.** Two or more mechanisms are present in name but one dominates such that the others are non-operational; productive tension is lost.

Each anti-pattern names a specific way Claim 4's commitments can be locally compromised while the surrounding deployment continues to appear compliant.

## 8. Operational test

A deployment instantiates Claim 4 if and only if an independent observer can verify each of the following at any point during operation:

1. **Three mechanisms exist as nameable architectural artifacts.** Instinct evolution has identifiable verification machinery (parallel-run patterns, retention decisions, pinning records). DNA evolution has identifiable authority architecture (proposal records, authorization records, reversion paths). Action-feedback evolution has identifiable proposing substrate, proposal history, and two-stage review.
2. **Each mechanism targets its declared layer.** Instinct-evolution events are recorded against the LLM/infrastructure layer; DNA-evolution events against the DNA layer; action-feedback events terminate as DNA-evolution events under the same DNA-layer authority architecture as direct-selection events.
3. **Non-interference is observable.** A search for instinct-evolution events that directly modified DNA returns empty. A search for DNA-evolution events that directly modified LLM versions returns empty. A search for action-layer entries that produced DNA changes without an intervening proposal-and-authorization record returns empty.
4. **Bidirectional and multi-level evolution is exercised, not merely declared.** Evolution events at cell, aspect, and Self levels appear in the substrate's evolution history. Horizontal events (peer propagation within aspect) and vertical events (structural reorganization) are both identifiable.
5. **Governance is exercised per mechanism.** Verification-substrate machinery for instinct integration is distinct from authority architecture for DNA evolution, which is distinct from proposal-and-acceptance machinery for action-feedback.

A deployment satisfying (1)–(5) instantiates Claim 4. A deployment that fails any of them may govern its evolution in some other sense but does not instantiate the three-mechanisms-in-productive-tension architectural commitment.

## 9. Conclusion

Paper 2's fourth architectural claim commits a CKS-governed Self to evolve through three independently-operating mechanisms — instinct evolution, DNA evolution, and action-feedback evolution — targeting architecturally separated layers, operating under distinct governance shapes, composing under a non-interference contract. The non-interference contract is itself the architectural commitment; productive tension is not an observation about how the three mechanisms happen to coexist but a property the architecture commits to preserve. The asymmetry between governed-effects and governed-choices is what makes the claim distinctive against single-mechanism evolution models and against mechanism-agnostic governance overlays.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Three Evolution Mechanisms as Paper 2's Fourth Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
