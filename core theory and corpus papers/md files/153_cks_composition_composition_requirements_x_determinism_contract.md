# Determinism Preservation Across Composition: How the Composition Requirements and the Determinism Contract Compose in Multi-Substrate CKS Systems

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone publication, the architectural property that emerges when two of the source paper's foundational commitments — the composition requirements and the determinism contract — compose. The composition produces a property neither commitment yields alone: *determinism preservation across composition*. The note articulates that property, identifies what the composition forces beyond either parent commitment, names the anti-patterns specific to it, and provides an operational test.

## Abstract

The CKS source paper distributes determinism guarantees across §4.1, §6.2, §11.3 and distributes composition requirements across §4.5, §6.1, §13.3. Two prior derivation notes formalize each parent independently: the composition-requirements note enumerates five constraints (per-substrate governance, conflict preservation across boundaries, addressable provenance across boundaries, AI-as-substrate-mediator at every layer, human-selective composition) plus a sixth on plan-and-trace co-preservation; the determinism-contract note enumerates five guarantees (read determinism, cell-behavior determinism modulo LLM, write addressability, conflict preservation, substrate as source of truth) and the bounded non-determinism the contract permits. This note formalizes neither parent. It formalizes the emergent architectural property — *determinism preservation across composition* — that arises when the parents compose: the property under which the contract's five guarantees are preserved at every composition partner through the composition requirement of per-substrate determinism preservation. The note articulates the property as four operational components, identifies what the composition forces beyond either parent alone, names the anti-patterns specific to compositions where determinism is asymmetric across partners, and provides an operational test.

## 1. Why a standalone formalization of this composition is needed

The two parent commitments are independently formalized and independently citable. Neither, alone, articulates what holds when both apply.

The composition requirements name *per-substrate determinism preservation* as one of the constraints any multi-substrate composition must satisfy. They identify the property — composition must not produce a system where some substrates are deterministic and others are not — but they specify it abstractly, by naming what cannot happen, not by specifying which determinism guarantees must be preserved or how. The composition-requirements text reads as "every substrate must continue to satisfy the determinism contract"; it does not, alone, say what that contract is.

The determinism contract specifies, in detail, what a CKS-coherent substrate guarantees: read determinism, cell-behavior determinism modulo LLM, write addressability, conflict preservation, and substrate as source of truth. It also specifies what non-determinism is permitted (LLM outputs, certain timing-dependent operations) and identifies anti-patterns that violate the contract for individual substrates. It does not, alone, say what holds across composition. The contract binds individual substrates; the composition partners are out of its direct scope.

The composition produces the missing piece. When the composition requirements bind multi-substrate compositions to preserve determinism per-substrate *and* the determinism contract specifies what determinism means concretely, the resulting architectural property is operationally precise: every composition partner satisfies all five contract guarantees, cross-substrate operations preserve those guarantees at boundaries, the bounded non-determinism the contract permits operates uniformly across partners, and reproducibility holds across composition rather than varying across partners. Call this property *determinism preservation across composition*. It is what the composition operationally produces; it is what neither parent yields alone.

The motivating cases are concrete. Multi-substrate deployments at the scale CKS systems reach in practice typically involve substrates contributed by different teams, organizations, or vendors. A composition in which the primary substrate is contract-coherent but secondary substrates have non-deterministic behavior — different reads returning different content, cell-behavior differing under identical orchestration rules, contradictions silently collapsed within a partner — produces a multi-substrate system that cannot be reproduced and cannot be audited. The composition requirement that names per-substrate determinism preservation is the architectural mechanism that prevents this asymmetry, and stating the composition's operational property as a standalone publication makes the prevention citable.

This is the fourth note in the composition-requirements cluster, after the compositions with mediator, with governance, and with retraceability. The cluster closes with the composition that formalizes human-selective composition.

## 2. The emergent architectural property as four operational components

The property *determinism preservation across composition* decomposes into four components. Each is necessary; together they are what the composition produces.

**Component 1 — Per-substrate satisfaction of all five contract guarantees.** Every substrate participating in a composition must individually satisfy the determinism contract: same-state-yields-same-read, write determinism modulo LLM, write addressability, conflict preservation, and substrate as source of truth. The composition does not satisfy the property in aggregate while individual substrates fall short. This component prevents the asymmetric-determinism pattern in which one substrate carries the system's reproducibility weight and the others are treated as informally deterministic. The contract is per-substrate; the composition does not relax it.

**Component 2 — Cross-substrate operations preserve determinism at boundaries.** Where one substrate references content in another, where a cell aggregates content from multiple substrates, or where an orchestration rule operates over a composed view, the operation that crosses the boundary must itself be deterministic at the substrate-write layer. Two executions of the same cross-substrate operation, over the same multi-substrate state, must produce the same writes. Boundary operations that introduce non-determinism — non-deterministic merge logic, timing-dependent reference resolution, LLM-inferred linkage between substrates — break this component even when each underlying substrate is contract-coherent.

**Component 3 — Bounded non-determinism operates consistently across partners.** The contract permits specific categories of non-determinism: LLM outputs (the model layer is out of scope), certain timing-dependent operations bounded by the substrate-write contract, and non-determinism that orchestration rules explicitly authorize. The composition requires that these categories operate uniformly across partners. A composition in which one substrate treats LLM outputs as out-of-scope while another permits LLM-inferred substrate writes without addressable origin produces inconsistent non-determinism boundaries. The categories of allowed non-determinism are part of the contract; the composition preserves their definition across partners.

**Component 4 — Reproducibility holds across composition.** The substrate-level reproducibility the contract supports — replay over the same substrate state under the same orchestration rules yields equivalent substrate writes — extends to the composed system. Replay across the multi-substrate composition produces equivalent outcomes; the composition does not introduce reproducibility failure modes that would not occur in any single underlying substrate. This is the composition-scale form of the contract's reproducibility guarantee, and it is the component downstream auditors most often need to rely on.

The four components are jointly the emergent property. A composition that satisfies three but not the fourth has not satisfied the property; the composition specifically requires all four because the contract specifies all four conditions on individual substrates and the composition requirements specify their preservation across partners.

## 3. What the composition forces beyond either commitment alone

The composition forces architectural decisions that neither parent forces alone.

**The composition operationalizes per-substrate determinism preservation through the contract's five guarantees.** The composition-requirements text names per-substrate determinism preservation; the composition fills in what that means by binding it to the contract's specific guarantees. A composition cannot satisfy the requirement abstractly; it must satisfy it in the form of read determinism at every partner, cell-behavior determinism at every partner, write addressability at every partner, conflict-handling determinism at every partner, and substrate-as-source-of-truth at every partner. The five-fold articulation is what the composition forces.

**Cross-substrate determinism preservation is specified.** Neither parent commitment, alone, addresses cross-substrate operations. The composition requirements name composition boundaries; the determinism contract names individual-substrate guarantees. Their composition forces an operational specification at the boundary: cross-substrate operations are deterministic at the substrate-write layer, the same way single-substrate operations are. Boundary operations are within scope.

**Vendor-specific non-determinism must map to the contract's allowed categories.** Multi-substrate compositions frequently involve substrates hosted on different platforms, with different vendor APIs and timing properties. The composition forces a decision: any non-determinism a vendor introduces at a partner must map cleanly to the contract's allowed categories (LLM outputs, bounded timing) or it is contract-violating. Vendor non-determinism that does not map — vendor-side conflict resolution, vendor-side reference inference, vendor-side write rewriting under undocumented conditions — fails the composition.

**Primary/secondary asymmetry is prohibited.** A common deployment shape treats one substrate as the primary, contract-coherent artifact and other substrates as informal stores not held to the contract. The composition prohibits this. Per-substrate determinism preservation means *every* substrate, not the primary alone. The asymmetry must be eliminated before the composition is contract-coherent.

## 4. Anti-patterns specifically violating this composition

Five anti-patterns recur in compositions that approximate determinism preservation across composition without satisfying it. Each is the composition-scope counterpart of an anti-pattern at single-substrate scope.

**Asymmetric determinism across composition.** One substrate satisfies the contract; others do not. The composition is treated as deterministic because the primary substrate is. Violates Component 1. The system as a whole is not contract-coherent regardless of how reliably the primary substrate behaves.

**Cross-substrate non-determinism at boundaries.** Each individual substrate is contract-coherent, but the operations that cross boundaries — merging, referencing, resolving — are not deterministic. Two replays of the same composition, over the same multi-substrate state, produce different composed results. Violates Component 2. The composition's reproducibility is illusory.

**Implicit context compounded across composition.** The implicit-context anti-pattern named at single-substrate scope (cell behavior depending on context not represented in the substrate or in orchestration rules) compounds across composition: each partner has its own implicit-context surface, and the composition aggregates their failure modes. Violates Component 1 at each partner and Component 4. The compounded version cannot be repaired by fixing one substrate; it requires repair at every partner.

**Contradiction collapse compounded across composition.** Silent conflict resolution at each partner aggregates: each partner collapses its own contradictions invisibly, and the composed view exposes none of them. Violates Component 1 (conflict preservation) and Component 4 (the composed view cannot be reproduced once contradictions have been silently resolved differently in different replays). Its compounded form across composition operationally requires the composition-level fix.

**Vendor-specific non-determinism unmapped to allowed categories.** A partner introduces non-determinism that does not map to the contract's allowed categories — vendor-side merge logic, vendor-side timing dependency outside the bounded category, vendor-side LLM inference at write time without addressable origin. Violates Component 3. The composition's bounded-non-determinism boundary is broken at the partner that introduces the unmapped category.

In each anti-pattern, the composition may continue to operate, may produce outputs that look correct in any given session, and may be useful for some purpose. What it loses is determinism preservation across composition. Downstream consumers cannot rely on the property regardless of how the composition appears to behave in any single observation.

## 5. What this composition is NOT

The composition is not the composition requirements alone. The composition requirements name per-substrate determinism preservation as a constraint; without the determinism contract, the constraint has no operational content. A composition that satisfies the other composition requirements (governance preservation, conflict preservation across boundaries, retraceability across boundaries, mediator at every layer, human-selective composition, plan-and-trace co-preservation) but does not specify what determinism means at each partner has not satisfied this composition.

The composition is not the determinism contract alone. The contract binds individual substrates; without the composition requirements, the contract is silent on what holds across substrate boundaries. A multi-substrate system in which each substrate independently satisfies the contract but no requirement binds them to do so jointly is not a CKS-coherent multi-substrate composition.

The composition is not "approximately deterministic" composition. The contract is a five-fold specification with universal quantifiers ("any reader, at any time, through any cell"); the composition extends each quantifier across partners. Approximate satisfaction at any partner is not satisfaction.

## 6. Operational test

A multi-substrate composition satisfies *determinism preservation across composition* if and only if all of the following are true at every composition boundary at all times during the composition's existence.

**(e.1) Per-substrate determinism guarantees.** Every substrate participating in the composition individually satisfies the five guarantees of the determinism contract: read determinism, cell-behavior determinism modulo LLM, write addressability, conflict preservation, and substrate as source of truth. Verification per partner uses the same operational test the contract specifies for any single substrate.

**(e.2) Cross-substrate determinism preservation.** Two replays of the composition, over the same multi-substrate state, under the same orchestration rules, produce the same substrate writes at every partner and at every cross-substrate operation. Equivalence is judged at the substrate-write layer, not at the LLM-output layer, in the same way the contract specifies equivalence for individual substrates.

**(e.3) Composition-scale reproducibility.** Reproducibility — the property that replay over the same multi-substrate state produces equivalent substrate writes across the composition — holds uniformly across partners. The composition does not exhibit reproducibility at the primary substrate alone while secondary substrates produce different writes on replay.

**One-sentence test.** A multi-substrate composition preserves determinism across composition when, for any reader at any time through any cell that supports reading, the contract's five guarantees hold at every composition partner and every cross-substrate operation.

A composition that fails any of (e.1)–(e.3) may continue to operate, may have other valuable properties, and may instantiate other valid design patterns; it is not contract-coherent across composition in the CKS sense.

## 7. Why naming this composition matters

Three reasons.

The first is structural completeness of the composition-requirements cluster. The composition-requirements parent names five operational requirements (plus the plan-and-trace sixth). Each requirement is the composition-scope counterpart of a single-substrate commitment, and each composition pair formalizes the architectural property that emerges. The cluster, in sequence, formalizes mediator preservation, governance preservation, retraceability preservation, *determinism preservation* (this note), and human-selective composition. Without this note, the cluster has a gap precisely where the source paper's most operationally consequential property — reproducibility — is composed across partners.

The second is reproducibility at composition scale. CKS deployments at scale are multi-substrate; the reproducibility property the contract supports at single-substrate scope is what auditors and downstream consumers most often need. Its preservation across composition is what makes multi-substrate CKS deployments auditable as a whole rather than auditable only at a primary substrate. Naming the composition gives auditors a single citable target — four components, three operational tests, five anti-patterns — against which any multi-substrate deployment can be checked.

The third is differentiation from asymmetric-determinism multi-substrate systems. Many multi-substrate systems in practice treat one substrate as the contract-coherent artifact and others as informal. The CKS pattern does not. Stating the composition explicitly draws the line: a multi-substrate system that exhibits asymmetric determinism across partners is not a CKS-coherent multi-substrate composition, regardless of how reliably the primary substrate behaves. The next note in the cluster will close it by formalizing human-selective composition, completing the operational specification of what makes a multi-substrate composition CKS-coherent.

The composition formalizes a property already implicit in the source paper's commitments. Naming it makes the implication citable and the property defensible against the asymmetric-determinism alternative.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Determinism Preservation Across Composition: How the Composition Requirements and the Determinism Contract Compose in Multi-Substrate CKS Systems.* May 6, 2026. ORCID: 0009-0004-8065-3235.
