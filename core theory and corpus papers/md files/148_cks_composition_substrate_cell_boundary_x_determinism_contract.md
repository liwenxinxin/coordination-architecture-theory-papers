# Cell-Behavior Determinism from Substrate: How the Substrate-Cell Boundary and the Determinism Contract Compose in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 6 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural property that emerges when two foundational CKS commitments — the substrate-cell boundary and the determinism contract — compose: cell-behavior determinism from substrate, the property by which a cell's behavior is determined by substrate state and orchestration rule alone, and by no other input.

## Abstract

The substrate-cell boundary and the determinism contract are each formalized as standalone in this series. Each, taken alone, is satisfied by configurations that are not what the source paper defends. The boundary alone is satisfied by deployments whose cells behave non-deterministically over substrate input, provided the layer separation is preserved. The contract alone is satisfied by configurations whose cell-level guarantee — equivalent substrate writes for equivalent substrate state and rules — holds nominally over an input set wider than substrate state and rule. The architectural property the source paper actually defends is the property the two commitments produce together: cell behavior is determined by substrate state and orchestration rule, with no other inputs admissible as behavior-determinants. This note formalizes that emergent property under a single name — *cell-behavior determinism from substrate* — states its four operational components, identifies what the composition forces beyond either commitment alone, names the anti-patterns that satisfy each commitment in isolation while failing the composition, and gives an operational test built around three sharpening properties.

## 1. Why this composition pair needs to be formalized as standalone

The CKS pattern's architectural commitments are designed to compose, and the composed properties carry architectural content the individual commitments do not. Neither the substrate-cell boundary nor the determinism contract, taken alone, accounts for the property the source paper depends on when it claims that cell-level behavior is testable, reproducible, and architecturally bounded by substrate state (§2.1, §3.3, §4.4, §6.2).

The property the paper depends on is composed. A cell whose behavior is determined by substrate state and orchestration rule alone is testable through substrate state setup — set up the state, execute the cell, observe the writes, repeat. A cell whose behavior may depend on environment, time, randomness, library version, or cell-internal state is testable only conditionally on the deployment's incidental properties. The first is what §2.1 describes when the boundary is taken as load-bearing; the second is what the boundary describes when the determinism contract is omitted from view, and is observably common in deployments that adopt the boundary in form without taking the contract seriously.

This note names the composition's emergent property as standalone architectural content. Two notes in this series — the boundary-and-source-of-truth composition pair (producing authority-locus) and this one (producing behavior-determinism) — together close the boundary's two foundational composition pairs: how the substrate-cell boundary composes with the two commitments that operationalize substrate's role.

## 2. The emergent property: cell-behavior determinism from substrate

In the composition of the substrate-cell boundary and the determinism contract, a cell exhibits **cell-behavior determinism from substrate** when its behavior — every aspect of its execution that affects what is written back to the substrate — is determined by substrate state and orchestration rule alone. The property has four operational components.

**(a) All behavior-determining input is read from the substrate.** A cell that requires input to determine behavior reads that input from substrate content within its scope. The boundary already commits cells to operate by reading from and writing to the substrate; the contract already commits its cell-level guarantee at the substrate-write layer. The composition forces these together: the inputs over which the cell-level guarantee is evaluated are exactly the inputs the boundary commits cells to reading from substrate, and no others.

**(b) Cell processing is a deterministic transformation of substrate state and orchestration rule.** What the cell writes depends on what it reads from substrate and what the orchestration rule prescribes. Inputs not in those two categories — wall-clock time, environment variables, host filesystem state, library version, hardware characteristics, randomness without bounded recording — do not appear in the transformation as behavior-determinants.

**(c) Cell-internal state cannot determine cell behavior.** State that a cell holds during execution is ephemeral. Substrate-relevant state required across executions lives in the substrate, by the boundary's commitment; cell-internal processing state is not authoritative and does not modulate cell behavior beyond the current execution.

**(d) The cell-level determinism guarantee is anchored to substrate state.** The contract's cell-level guarantee — same substrate state plus same rules yields equivalent cell-level behavior — is operationalized to mean that the input over which the equivalence holds is substrate state, specifically and exclusively. The composition rules out a reading in which the guarantee holds nominally over a wider input set (substrate state + environment, substrate state + time, substrate state + cell-internal cache) while still being called determinism.

These four are facets of one architectural property. Failing any one fails the composition; satisfying all four is what cell-behavior determinism from substrate names.

## 3. What the composition forces beyond either commitment alone

The boundary alone admits non-deterministic cells. A deployment may preserve the layer separation in form — substrate persists, cells read from and write to it, orchestration rules are substrate-level content, no cell-to-cell channels run outside substrate — while permitting cells to behave non-deterministically over substrate input. The boundary commits to the layer separation; it does not, on its own, commit to a determinism property over the layer's inputs.

The determinism contract alone admits non-substrate-anchored determinism. The contract's cell-level guarantee is silent, on its own, on whether other inputs that affect cell behavior are themselves part of the equivalent-input bundle or sit outside it. A reading under which cell behavior is "equivalent given the same substrate state, same rules, same environment, same time, same library version, same cache" satisfies the contract textually while breaking the architectural property the source paper defends.

The composition forces the conjunction. Cell behavior depends on substrate state and rule, and on nothing else. Inputs outside this set are either pulled into the substrate (recorded as content the cell reads) or excluded from the cell's behavior-determining set. Inputs that fall in the source paper's allowed non-determinism categories — most prominently the rule-mediated outputs of LLM consultations, where the LLM operates as substrate mediator under §4.2 — are bounded into the architecture and do not break the composition: they are non-deterministic at the LLM-output layer but bounded at the substrate-write layer, where the rule lands the LLM output back to substrate as recorded content. The composition is what makes the "cells are deterministic functions of substrate state plus rule" reading of §2.1 architecturally precise; either commitment alone falls short.

## 4. Anti-patterns that violate the composition specifically

Several anti-patterns satisfy the boundary or the contract individually while failing the composition. Each has its own anti-pattern derivation in this series.

**Implicit context in cells.** Cell behavior depends on context not represented in the substrate or in orchestration rules — environment variables read directly by the cell, host configuration the cell observes outside its substrate scope, locale or timezone implicitly consulted, library version or build flag the cell branches on. The boundary may be preserved nominally; the contract may even hold within a single deployment. The composition fails because cell behavior depends on input outside substrate state and rule. This is the canonical composition violation — the failure mode any test of the composition is most likely to surface.

**Hidden state in cells.** Cells carry state across executions in ways the substrate does not see — local variables persisting in long-running cell processes, instance memory, runtime caches consulted as ground truth, session state outside the substrate. The boundary already names this failure on its own terms; the composition strengthens the consequence — even where the held state is not strictly substrate-relevant in the boundary's sense, its presence as a behavior-determinant fails (a) and (c).

**Cell-as-substrate.** A cell's execution context is treated as if it were substrate — coordination state lives in the cell across turns, with the substrate playing a secondary role or no role at all. Under the composition, the additional failure beyond the boundary inversion is that cell-held state determines cell behavior, breaking (a) and (c) at once.

**Time-, environment-, library-version-, and randomness-dependent behavior.** Cells consult wall-clock time, environment variables, OS state, library versions, or randomness, and behave differently as those inputs change without those inputs being recorded as substrate content. Each failure has the same shape: a behavior-determinant outside substrate state and rule. The remedy is the same: pull the input into substrate as recorded content. Randomness without recording is not part of the source paper's allowed non-determinism categories, which bound non-determinism by recording, not by leaving it unbounded.

The composition is what makes this general failure namable as a single thing.

## 5. Operational decisions the composition forces

Five decisions follow from the composition; together they constitute the architectural posture a CKS-coherent cell takes toward its inputs. First, all behavior-determining input is substrate content — configuration, dates, external values, parameters are recorded as substrate content with provenance, and the cell reads them from there. Second, cells do not consult environment, time, or filesystem directly to determine behavior; they may consult these to satisfy a deployment-level dependency, but the values that determine what they write are read from substrate. Third, randomness, when used, is bounded by recording — a cell that uses a random value records that value to substrate as part of its write. Fourth, cell-internal processing state is treated as ephemeral; variables, caches, accumulators, and intermediate computations do not persist between executions. Fifth, allowed non-determinism categories are documented and bounded — LLM consultations under the AI-as-substrate-mediator role produce non-deterministic outputs at the LLM layer, and the rule lands those outputs as substrate writes with the LLM identity and consultation context recorded.

These five are not deployment recommendations; they are what the composition requires of any cell that is to satisfy both the boundary and the contract jointly.

## 6. What the composition is not

The composition is not the boundary without determinism; a deployment may preserve the boundary while permitting cells to behave non-deterministically over substrate input, and such a deployment satisfies the boundary in isolation but not the composition. It is not the determinism contract without boundary specification; a deployment may satisfy the contract's five guarantees while reading the cell-level guarantee over an input set wider than substrate state and rule. It is not "mostly deterministic" cell behavior — the composition is binary, and a cell whose behavior depends on any input outside substrate state, rule, and the source paper's allowed non-determinism categories does not satisfy the composition regardless of how rare the dependency is. It is not deterministic cells with cell-internal state — a cell that exhibits deterministic outputs while carrying state outside the substrate satisfies neither the composition nor the boundary alone, even when its outputs happen to be reproducible under controlled conditions. And it is not a binding on LLM outputs — the composition binds cell behavior at the substrate-write layer, not at the LLM-output layer, and the rule lands the LLM's intermediate text as substrate content.

## 7. Why the composition is load-bearing

The composition is what makes substrate-state-setup-based testing possible — a cell whose behavior depends only on substrate state and rule can be tested by setting up substrate state, executing the cell, and observing what is written back, without the test outcome depending on inputs outside the test's setup. It is the prerequisite for reproducibility under path retraceability — replay over recorded substrate state can only produce equivalent cell writes if cell writes depend only on substrate state and rule, and the path-retraceability-and-determinism composition pair takes the property formalized here and combines it with provenance to support replay. It interfaces with bounded non-determinism within the mediator — the mediator-and-determinism composition pair bounds non-determinism inside the mediator role; this composition forces all behavior-determining input outside that bounded non-determinism to come from substrate state and rule, and together they specify how cells can use LLM consultations while preserving architectural determinism over substrate writes. It complements the boundary-and-source-of-truth composition — that composition covers authority-locus on the state side, this one covers behavior-determinism on the execution side, and the two together specify the boundary's two foundational compositional roles. And it distinguishes CKS from systems with hidden state or environmental dependencies — agent frameworks holding session state across turns, workflow engines branching on environment configuration, retrieval-augmented systems whose retrieval is driven by inputs outside the recorded substrate — all of which satisfy neither the composition nor any commitment that produces it.

## 8. Operational test

A system instantiates cell-behavior determinism from substrate if and only if the following three properties hold at all times during the substrate's existence.

**(e.1) Substrate state determines behavior.** For any cell and any substrate state within the cell's scope, executing the cell over that state and the orchestration rule that governs it yields equivalent substrate writes — equivalence judged at the substrate-write layer — across executions. Tests verify by setting up substrate state, executing the cell, and comparing writes against an independently produced expected result for the same state and rule.

**(e.2) Cell-internal state does not determine behavior.** For any cell, executing the cell over substrate state X following any prior sequence of executions yields writes equivalent to executing the same cell over substrate state X with no prior executions. Tests verify by exercising cells in different orders and confirming that the writes for each cell over a given substrate state are independent of execution order.

**(e.3) Environment does not determine behavior.** For any cell and any substrate state, executing the cell across distinct host environments — different OS configurations, library versions within the deployment's supported set, regional locales, time zones — yields equivalent writes. Tests verify by exercising cells across environments and confirming that the writes for a given substrate state and rule are equivalent across environments.

A one-sentence operational summary: *a cell's writes are determined by the substrate state it reads and the rule it executes under, and by no other input.*

A system that fails any of (e.1)–(e.3) may be useful and may exhibit one or more CKS-adjacent properties, but does not instantiate the composition formalized in this note.

## 9. Why naming this composition matters

The composition of the substrate-cell boundary and the determinism contract is not a new architectural commitment. It is the emergent property that arises when two commitments the source paper has already defended compose together, and naming it as standalone is what makes the property citable, testable, and arguable on its own terms.

Three consequences follow. Deployments claiming CKS coherence can be evaluated against the composition's three operational properties directly, rather than against each commitment in isolation and judged conformant when one is satisfied while the composition fails. Anti-patterns that satisfy each commitment in isolation while failing the composition — implicit context the most prominent — become identifiable as specific composition failures rather than as ambiguously-classified bad practice. And the boundary's two foundational composition pairs — boundary × source-of-truth on the state side, and this one on the execution side — together specify the boundary's full operational role, so that downstream derivation can reference the pair as a closed set rather than an open one.

Subsequent composition-pair notes in this series formalize further pairs across the source paper's foundational commitments. The composition treated here is one of the more operationally consequential, because the property it produces is what supports downstream concerns about testable and reproducible AI behavior at the architectural layer the source paper occupies. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat cell-behavior determinism from substrate as the architectural content this composition produces. Subsequent work that uses cell-level determinism in a different sense — over a wider input set, or with hidden-state behavior-determinants — is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell-Behavior Determinism from Substrate: How the Substrate-Cell Boundary and the Determinism Contract Compose in the Coordination Knowledge Substrate Pattern.* 6 May 2026. ORCID: 0009-0004-8065-3235.
