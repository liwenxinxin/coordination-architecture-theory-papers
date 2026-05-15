# Additional Composition Pair: Multi-Domain Self and Cross-Organizational Agreement

**Series D — Paper 3 Derivation Notes | Note D4.23 | #628**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes a composition pair within the CKS Paper 3 derivation series: the governance requirements that arise when a multi-domain Self (D2.58) maintains cross-organizational governance agreements (D2.34). The combination produces three non-obvious governance requirements that neither commitment generates alone: the need for a domain-specific agreement portfolio rather than a universal cross-domain agreement; the need to prevent cross-domain governance contamination across that portfolio; and the governance architecture choice that arises when the same partner participates in coordination events across more than one of the multi-domain Self's content domains. These requirements constitute prior art for any governed architecture that combines multi-domain participation with formal bilateral governance agreements.

---

## 1. Pair Identification

**Commitment A — Governance for Multi-Domain Selves (D2.58).** A Self whose aspects span multiple content domains — for example, healthcare, finance, and operations — may participate in coordination events with different partners for different domains. Governance for such a Self must support domain-selective participation: the Self can engage a healthcare partner in a healthcare-domain coordination event without committing its finance or operations aspects to that event. Each domain-selective participation relationship is governed independently, subject to its own domain-specific governance requirements.

**Commitment B — Cross-Organizational Governance Agreement (D2.34).** A bilateral governance framework for ongoing coordination relationships between two Selves. The framework has five components: (1) mutual governance standards establishing the baseline each party commits to; (2) joint authority configuration specifying how decisions over the shared substrate are made; (3) conflict domain specification identifying the classes of conflict that the relationship is expected to produce and how each class is handled; (4) evolution ingestion boundaries governing what each Self absorbs from coordination outputs; and (5) dissolution terms governing what happens to shared substrate content when the relationship ends.

Neither commitment alone determines what happens when both hold simultaneously. D2.58 covers multi-domain governance requirements within a single Self; D2.34 covers the bilateral agreement structure for a single ongoing relationship. Their composition raises requirements that neither anticipates.

---

## 2. Governance Scenario Requiring Both Simultaneously

A Self has three distinct content domains — healthcare, finance, and operations — each covered by one or more aspects. It maintains ongoing coordination relationships with three different partner Selves: Partner H engages it exclusively in the healthcare domain; Partner F engages it exclusively in the finance domain; Partner O engages it exclusively in the operations domain. Each relationship is ongoing, not one-off, and each therefore requires a cross-organizational governance agreement under D2.34.

All three agreements are active simultaneously. The multi-domain Self must therefore maintain a portfolio of three bilateral governance agreements, each applicable to a different domain of its own internal structure. The three agreements must collectively govern without contradiction, must collectively satisfy all applicable regulatory requirements for all three domains, and must not create governance confusion when any one of them is amended or enforced.

This is the governance scenario the composition targets. Neither D2.58 nor D2.34 in isolation specifies what this portfolio must look like or how it must be managed.

---

## 3. Non-Obvious Governance Requirements from the Combination

### Requirement 1 — Domain-Specific Agreement Portfolio

A universal cross-organizational agreement — one document covering all three domains — is not a viable substitute for domain-specific agreements when the domains have distinct regulatory requirements and distinct conflict profiles.

Consider Component 1 of the D2.34 framework: mutual governance standards. A healthcare domain agreement's Component 1 must address healthcare-specific compliance requirements. A finance domain agreement's Component 1 must address financial services compliance requirements. An operations domain agreement's Component 1 may address neither. A single document attempting to serve all three would either conflate these requirements — creating ambiguity about which standard applies in any given situation — or enumerate all three in parallel sections so lengthy and internally cross-referenced that amendment to one domain's standards would require carefully scoped edits throughout the document.

Consider Component 3: conflict domain specification. The classes of conflict that arise in healthcare coordination events differ categorically from those in finance or operations. Healthcare conflicts may concern patient data handling, scope of clinical recommendation, and jurisdiction of care. Finance conflicts may concern information barriers, trading context, and regulatory disclosure. Operations conflicts may concern resource allocation, scheduling authority, and quality standards. A combined document's conflict domain specification must enumerate all three, with routing rules precise enough to direct any given conflict to the correct handling mechanism — an engineering challenge that grows combinatorially as domains are added.

The composition therefore requires that the multi-domain Self manage a portfolio of domain-specific agreements rather than a universal agreement. Each agreement in the portfolio governs one domain's coordination relationship. This architecture is simpler per agreement, more focused in its compliance scope, and independently amendable as any one domain's requirements evolve.

### Requirement 2 — Cross-Domain Contamination Prevention

Maintaining a portfolio of domain-specific agreements introduces a second governance requirement that a single universal agreement does not surface: the need to ensure that each agreement's governance content remains isolated to its domain.

Cross-domain contamination occurs when governance standards, conflict specifications, or escalation routing from one domain appear in a different domain's agreement — either through drafting error, through template reuse without adequate domain-specific revision, or through amendment to one agreement that inadvertently propagates terms to another. Contamination is not merely a governance complexity problem; in regulated domains it creates regulatory risk.

If healthcare compliance language appears in the finance agreement, the finance relationship may be interpreted as subject to healthcare regulatory requirements, subjecting the multi-domain Self to dual-regulatory scrutiny it did not intend. If operations conflict-handling routing appears in the healthcare agreement, escalation pathways in a healthcare event may resolve to the wrong authority. Neither outcome is merely inconvenient; both create legal and operational exposure.

The governance requirement that follows is structural: each agreement in the portfolio must reference only the governance standards, conflict classes, and escalation routing specific to its domain. Review cycles for any one agreement must include an explicit check that no cross-domain content has been introduced. Amendment processes for any one agreement must not propagate terms to others without deliberate review. Portfolio-level governance quality is therefore a distinct governance obligation over and above the per-agreement obligations that D2.34 specifies.

### Requirement 3 — Same-Partner Multi-Domain Agreement Architecture Choice

The scenario above assumed different partners for each domain. A harder governance question arises when the same partner Self participates in coordination events across two or more of the multi-domain Self's content domains. This situation surfaces a governance architecture choice with implications that must be explicitly resolved.

**Option A — One comprehensive agreement per partner.** A single bilateral agreement covers all shared domains with the same partner. Component 1 enumerates mutual governance standards for each shared domain. Component 3 enumerates conflict specifications for each shared domain with domain-specific routing. This is simpler to manage from a counterparty relationship perspective — one agreement per partner, one amendment process per partner — but it reintroduces the complexity and contamination risks that domain-specific agreements were designed to avoid. An amendment to the healthcare conflict specification requires working within the document that also carries the operations conflict specification. A compliance reviewer examining the healthcare relationship must read past finance terms in the same document.

**Option B — Separate domain-specific agreements per partner.** Two bilateral agreements with the same partner: one covering the healthcare domain, one covering the operations domain. Each agreement is governed independently. Amendment to the healthcare agreement does not touch the operations agreement. This multiplies the number of agreements per partner and therefore the governance overhead per partner relationship — but each agreement is cleaner, more focused, and independently amendable.

Neither option is architecturally prescribed. The composition produces the choice, not the answer. What the composition does prescribe is that the governance record must document which option was chosen for each same-partner multi-domain relationship, and why. The documentation of the choice and its rationale is the governance requirement — not the selection of any particular option.

---

## 4. Prior-Art Significance

Three specific governance properties are established as prior art by this composition:

**Domain-specific agreement portfolio management.** The architectural preference for a portfolio of domain-specific agreements over a universal cross-domain agreement, in any governance system combining multi-domain participation with bilateral governance frameworks, is prior art for any "multi-domain governed AI coordination agreement architecture."

**Cross-domain contamination prevention as a governance quality requirement.** The identification of cross-domain contamination as a regulatory risk — not merely a governance complexity problem — and the corresponding structural obligation to isolate each agreement's content to its domain, is prior art for any governance system managing a portfolio of domain-differentiated bilateral agreements.

**Same-partner multi-domain agreement architecture choice documentation.** The requirement to explicitly document the architecture choice (single comprehensive vs. domain-specific agreements) when the same partner engages across multiple domains, and to record the rationale, is prior art for any governance system that must handle this configuration.

Any subsequent architecture claiming to govern multi-domain AI coordination with formal bilateral agreement structures must address all three requirements or explain why its design makes them inapplicable.

---

## 5. Operational Test

For a multi-domain Self's agreement portfolio, governance satisfies the composition's requirements if and only if an observer can verify the following:

**(a) Domain isolation per agreement.** Each agreement's Component 1 (mutual governance standards) and Component 3 (conflict domain specification) address only the governance requirements and conflict classes specific to that agreement's content domain. No healthcare compliance terms appear in the operations agreement. No operations conflict routing appears in the healthcare agreement.

**(b) No cross-domain contamination.** The portfolio as a whole contains no instance of governance standards, conflict specifications, or escalation routing from one domain appearing in a different domain's agreement — whether introduced through drafting, template reuse, or amendment.

**(c) Same-partner architecture choice documented.** For every partner Self that participates in coordination events across two or more of the multi-domain Self's content domains, a governance record exists that identifies the architecture choice made (one comprehensive agreement or separate domain-specific agreements) and documents the rationale for that choice.

A governance system that satisfies all three verification conditions instantiates the composition's requirements. A governance system that fails any one of them has an unresolved requirement from this composition, regardless of whether it satisfies D2.58 and D2.34 individually.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Additional Composition Pair: Multi-Domain Self and Cross-Organizational Agreement.* Derivation Note D4.23 (#628), CKS Derivation Note Series. May 15, 2026. ORCID: 0009-0004-8065-3235.
