# P3↔P2 Additional Inheritance: Home Perimeter and Substrate Source-of-Truth

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026), and "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026).

---

## Abstract

This note formalizes two additional Paper 3 ↔ Paper 2 inheritance edges in the CKS theory trilogy. Inheritance A covers home perimeter governance: Paper 2's three-tier bounded governance architecture implicitly commits each Self's governance to a bounded domain; Paper 3 makes that boundedness explicit as a named architectural property (the additive perimeter) and verifiable as a named governance commitment (home perimeter integrity). Inheritance B covers substrate as source-of-truth: Paper 2 extends Paper 1's per-substrate source-of-truth commitment to the three-tier hierarchy within each Self; Paper 3 extends this further to the inter-Self scope, introducing a shared substrate as the authoritative coordination state during Full Aspect Integration (FAI) events while preserving each home substrate's source-of-truth authority for home governance decisions. Both inheritances follow the same structural extension pattern — implicit becomes explicit, single-authority becomes multi-authority — strengthening the P3↔P2 inheritance argument by showing that the pattern is not accidental but architectural.

---

## 1. Series CC framing

Series CC notes formalize inheritance edges between Paper 3 and Papers 1 and 2 of the CKS trilogy. Each edge establishes that a Paper 3 commitment extends, rather than replaces, a specific prior-paper commitment — that Paper 3 inherits without redefense from its source. This note covers two such edges, both in the CC.2 phase (Paper 3 ↔ Paper 2). Each is treated as a numbered subsection following the five-element structure: (i) source commitment in Paper 2, (ii) extension commitment in Paper 3, (iii) the inheritance relationship, (iv) what is fresh at Paper 3 scope, (v) the prior-art claim.

The two inheritances belong together in one note because they are structurally parallel: each makes explicit what Paper 2 implicitly required, and each extends a single-authority commitment to a multi-authority one. That structural parallel is itself a finding the combined treatment makes visible.

---

## 2. Inheritance A — Home Perimeter Governance

### 2.1 Source commitment in Paper 2

Paper 2's three-tier governance architecture (cell, aspect, Self) operates within each Self as a bounded governance domain. The three tiers govern within one Self; external influence from another Self enters only through governed mechanisms — the canonical mechanism being a governed exchange event. This boundedness is a design property: Paper 2's architecture simply does not specify a channel by which one Self's operations directly alter another Self's governance state. The home governance space is bounded by construction.

Paper 2 does not, however, name this boundedness explicitly as a guarantee or commit to its verifiability. The boundary is load-bearing — all of Paper 2's governance reasoning depends on it — but it operates as an implicit architectural requirement rather than a named commitment practitioners are directed to check.

### 2.2 Extension commitment in Paper 3

Paper 3 introduces FAI as a governed mechanism by which two or more Selves participate jointly in a shared substrate. This creates a new architectural pressure on Paper 2's implicit boundary: if Selves are interacting, what ensures that inter-Self participation does not alter the home perimeter without governance authorization? Paper 3 resolves this pressure with two named commitments.

The **additive perimeter property** establishes that a Self's participation in an FAI event adds an inter-Self governance scope — the governance perimeter now spans the shared substrate — without replacing or subsuming the home governance scope. The two scopes coexist additively. The home governance space retains its Paper 2 architecture unchanged throughout FAI participation.

The **home perimeter integrity commitment** establishes that after each FAI event, governance practitioners verify that the home perimeter remained intact — that no unauthorized changes to the home governance space occurred during FAI participation. Three checks confirm this: home substrate state was not modified outside governance-configured ingestion channels; home orchestration rules were not altered by the inter-Self interaction; home authority assignments were not affected by the joint-authority structure of the FAI event.

### 2.3 The inheritance relationship

Paper 3's additive perimeter and home perimeter integrity both inherit directly from Paper 2's bounded governance architecture. Paper 3 does not introduce a novel constraint from outside the architecture — it names and makes verifiable the constraint that Paper 2's architecture implicitly required. The inheritance is: Paper 2's bounded governance architecture → Paper 3's explicit additive perimeter and verifiable integrity commitment.

### 2.4 What is fresh at Paper 3 scope

The fresh content at Paper 3 scope is not the boundary itself (that is Paper 2's property) but the naming and the verification protocol. Before Paper 3, a practitioner building a multi-Self system on CKS foundations would have no explicit architectural commitment to point to that guaranteed the home perimeter's survival during inter-Self coordination. Paper 3 provides that commitment, names it, and specifies the post-event checks that operationalize it. The naming is architecturally significant because it shifts the boundary from background design property to first-class governance commitment — something that can be inspected, tested, and cited as prior art.

### 2.5 Prior-art claim

Any architecture that (a) allows two or more governed AI entities to engage in a shared coordination event and (b) names an explicit post-event verification protocol confirming that each entity's home governance space was not altered outside authorized channels inherits from and formalizes the pattern Paper 2's bounded architecture commits to and Paper 3 makes explicit. This combination — governed inter-entity coordination with explicit home perimeter integrity verification — is formalized here as public prior art under Wenxin Li's name, derived from the CKS trilogy.

---

## 3. Inheritance B — Substrate as Source-of-Truth

### 3.1 Source commitment in Paper 2

Paper 1 establishes the substrate-as-source-of-truth commitment at cell scope: the substrate is the authoritative answer to coordination questions within a cell's governance domain. Paper 2 inherits this commitment and extends it to the three-tier hierarchy — the substrate at cell scope, aspect scope, and Self scope is the authoritative state for governance decisions at that scope. Each Self's home substrate is the authoritative coordination state for that Self's governance. A design that answers coordination questions from LLM context, cell-internal memory, or informal communication rather than from the home substrate violates the commitment.

### 3.2 Extension commitment in Paper 3

Paper 3 introduces the shared substrate as a new coordination artifact. During an FAI event, the shared substrate is the authoritative coordination state for inter-Self coordination: what is being exchanged, what conflicts have been surfaced and at which tier, what the joint authority configuration specifies — all of this lives in the shared substrate, not in the LLM context of either participating Self, not in informal communication between their practitioners, not in recollections of prior events. The shared substrate is source-of-truth at the inter-Self scope during the event.

Paper 3 also introduces **locus differentiation**: the architecture now has three distinct source-of-truth loci, each carrying authority over a different governance domain. The shared substrate is authoritative for inter-Self coordination state during FAI. Each home substrate is authoritative for each Self's governance decisions about FAI outputs — what to ingest, how to route layer-specific content through the home evolution mechanisms, which conflicts to carry forward as annotations. The loci are not in competition: each answers a different class of governance question, and the boundary between classes is itself substrate content under the appropriate authority.

### 3.3 The inheritance relationship

Paper 3's shared substrate source-of-truth inherits directly from Paper 2's per-Self substrate source-of-truth, which itself inherited from Paper 1. The inheritance chain is: Paper 1's per-cell substrate source-of-truth → Paper 2's per-Self substrate source-of-truth (at three tiers) → Paper 3's multi-locus substrate source-of-truth (shared substrate for inter-Self scope plus home substrates for home scope). Each step extends the prior commitment to a larger coordination scope without replacing it.

### 3.4 What is fresh at Paper 3 scope

The fresh content at Paper 3 scope is locus differentiation. Paper 2 operates with a single governance authority per Self; the source-of-truth commitment has one clear answer for each Self because there is one substrate and one governance authority. At inter-Self scope, two or more governance authorities coexist during an FAI event, each with legitimate source-of-truth authority over different governance questions. The architecture must specify which substrate answers which question — otherwise the source-of-truth commitment becomes ambiguous at the moment it is most needed. Paper 3's locus differentiation resolves this: it names the three loci, assigns source-of-truth authority to each, and specifies the class of governance questions each locus answers. This differentiation is not optional precision — it is architecturally required by the existence of multiple governance authorities.

### 3.5 Prior-art claim

Any architecture that (a) governs inter-entity coordination through a shared coordination artifact and (b) differentiates source-of-truth authority across multiple loci — assigning the shared artifact authority over inter-entity coordination state and each entity's home artifact authority over its own governance decisions about exchange outputs — inherits from and formalizes the pattern Paper 2's per-Self source-of-truth commits to and Paper 3 extends to multi-locus scope. This locus-differentiated source-of-truth architecture is formalized here as public prior art under Wenxin Li's name, derived from the CKS trilogy.

---

## 4. The consistent extension pattern

Both inheritances in this note follow the same structural extension pattern, and that structural parallel merits naming explicitly.

**Implicit → explicit.** Paper 2's bounded governance architecture is a design property — it holds because of how the architecture is constructed, not because Paper 2 names a guarantee and commits to verifying it. Paper 2's per-Self source-of-truth is a commitment that, at the single-Self scope, requires no differentiation. In both cases, Paper 3 makes explicit what Paper 2 required implicitly: naming the additive perimeter and the home perimeter integrity checks; naming the three loci and their respective source-of-truth authorities. The extension is not architectural invention but architectural articulation — the architecture requires it; Paper 3 names it.

**Single-authority → multi-authority.** Paper 2 operates within each Self's unified governance domain: one governance authority, one home substrate, one source-of-truth per scope level. Paper 3 introduces joint authority across participating Selves' governance spaces. Both inheritances respond to this structural change in the same way: by differentiating what had been unified. The additive perimeter differentiates the home governance scope from the inter-Self governance scope. Locus differentiation differentiates the home source-of-truth from the shared source-of-truth. In both cases, the multi-authority context requires that what was unified at single-Self scope be given structural precision at inter-Self scope.

The consistent pattern across both inheritances is evidence that the extensions are architecturally derived rather than ad hoc. Paper 2's bounded, unified architecture produces these extensions when extended to the inter-Self scope by construction. Paper 3 articulates them; Papers 1 and 2 require them.

---

## Conclusion

This note formalizes two P3↔P2 inheritance edges. In Inheritance A, Paper 2's implicitly bounded governance architecture becomes Paper 3's explicitly named additive perimeter with verifiable home perimeter integrity. In Inheritance B, Paper 2's per-Self substrate source-of-truth becomes Paper 3's locus-differentiated source-of-truth, with the shared substrate authoritative at inter-Self coordination scope and each home substrate authoritative at home governance scope. Both follow the same extension pattern — implicit to explicit, single-authority to multi-authority — and together constitute named prior art for any subsequent system combining governed inter-entity coordination with explicit home governance boundary preservation and differentiated source-of-truth architecture.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *P3↔P2 Additional Inheritance: Home Perimeter and Substrate Source-of-Truth.* May 15, 2026. ORCID: 0009-0004-8065-3235.
