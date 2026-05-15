# Substrate Ingestion as the FAI-to-Home-Evolution Connection Mechanism

**Defensive Publication — Derivation Note #486 (D1.21)**
**Series D — Paper 3 Derivation Notes / Phase D1 — Foundational Sub-Commitments**
**Parent claim: D0.04 — Paper 3 Claim 4 (Four-locus evolution-feed mechanism)**
**Position: D1.21 closes the Claim 4 sub-commitment set (D1.17–D1.21)**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes D1.21 — the fifth and final sub-commitment of Paper 3 Claim 4's four-locus evolution-feed mechanism — establishing that FAI outputs connect to each participating Self's home evolution machinery through substrate ingestion: the same mechanism by which any substrate content enters those mechanisms. The note states the sub-commitment precisely, explains what substrate ingestion means as an architectural concept (no new mechanism; FAI origin is provenance metadata; existing Paper 2 machinery processes everything), develops three architectural significances (no new evolution pathway required, full reuse of Paper 2's governance infrastructure, home governance as sole processing authority after the hand-off), closes the Claim 4 sub-commitment set with a summary of D1.17–D1.21, names four failure modes the commitment defends against, and provides an operational test for conforming implementations. Together with D1.17–D1.20, this note establishes the complete architectural specification of how inter-Self coordination via FAI feeds each home Self's evolution without requiring architectural additions beyond Papers 1 and 2.

---

## 1. Position in the derivation series and the Claim 4 sub-commitment set

Paper 3 Claim 4 specifies a four-locus evolution-feed mechanism — the architectural specification of how FAI events feed each participating Self's home evolution machinery after FAI dissolution. The mechanism has four loci: (a) action-feedback evolution, (b) DNA evolution, (c) instinct evolution (out of scope), and (d) the hand-off boundary as the architectural object marking where joint authority ends and home governance resumes exclusively.

Phase D1 has decomposed Claim 4 into five sub-commitments across five notes:

- **D1.17** — Action-layer records as the action-feedback evolution locus: FAI-origin content enters action-feedback evolution (Paper 2, B1.15) as action-layer records, through the same proposal-and-acceptance machinery that processes home-generated records.
- **D1.18** — DNA evolution as the DNA evolution locus: FAI-absorbed schemas, orchestration patterns, and rules are candidates for directed selection (Paper 2, B1.14) under home governance, processed through the same authority architecture that governs home-generated DNA changes.
- **D1.19** — Instinct non-crossing: LLM weights and instinct-layer content do not exchange across FAI; instinct evolution within each Self continues per Paper 2 independently of FAI events.
- **D1.20** — The hand-off boundary as architectural object: the moment of FAI dissolution constitutes a defined boundary at which joint authority ends and each participating Self's home governance resumes as sole authority.
- **D1.21 (this note)** — Substrate ingestion as the connection mechanism: FAI outputs enter each Self's home evolution machinery as standard substrate content through the existing substrate ingestion mechanism — the same mechanism by which any substrate content enters those mechanisms — requiring no new evolution pathway and confirming home governance as sole processing authority post-hand-off.

D1.21 is the connective note for the set. D1.17 and D1.18 specify which home mechanisms receive FAI outputs; D1.20 specifies where joint authority terminates; D1.21 specifies *how* the connection is made — the mechanism by which outputs flow from the hand-off boundary into the home mechanisms named in D1.17 and D1.18. Substrate ingestion is that mechanism, and the sub-commitment is that it is the *existing* mechanism for all content, not a new one introduced for FAI outputs.

---

## 2. The sub-commitment stated precisely

**D1.21 — Substrate ingestion as the FAI-to-home-evolution connection mechanism:**

FAI outputs — action-layer records and DNA-layer content produced during an FAI event — enter each participating Self's home evolution machinery through substrate ingestion: the mechanism by which substrate content enters a Self's home evolution mechanisms. This is the same mechanism by which any substrate content enters those mechanisms. It is not a new pathway introduced to handle inter-Self coordination. FAI outputs, once they have crossed the hand-off boundary established at FAI dissolution, are home substrate content. They are processed by home evolution mechanisms — action-feedback evolution and DNA evolution, per Paper 2 — as substrate content of the appropriate layer type. The FAI origin of the content is recorded in the provenance record; it is not a processing-path determinant. It does not cause FAI-origin content to travel a different route through home evolution machinery. Home governance is the sole authority for all processing decisions from the moment of hand-off.

---

## 3. What substrate ingestion means as an architectural concept

### 3.1 Content identity at the hand-off boundary

The hand-off boundary (D1.20) is the moment at which FAI dissolution takes place and the shared substrate ceases to operate. At that moment, content that each participating Self's home governance has authorized for absorption begins its transition from the shared substrate into the respective home substrates. The transition is the mechanism Paper 3 calls substrate ingestion.

The critical architectural fact about ingestion is what it does to the identity of the content it processes. Before ingestion, FAI outputs are shared-substrate content — content produced under joint authority during the FAI event, subject to the governance structures of all participating Selves operating over the shared substrate. After ingestion, FAI outputs are home substrate content. They exist within the home substrate under home governance. Their provenance record carries the annotation that they originated in a FAI event, and that annotation may carry information about which contributing Self produced which content and at what provenance depth the receiving Self's governance authorized carry-over. But the annotation is metadata. It does not alter what the content is from the perspective of the home evolution mechanisms that will process it.

Action-layer records from the FAI event that have been ingested into a Self's home action layer are home action-layer records. Paper 2's action-feedback evolution mechanism (B1.15) operates on action-layer records. It operates on these records. The two-stage review structure, the proposal-and-acceptance machinery, the substrate-change cycles that Paper 2 §8 describes — all of these apply to FAI-origin records in exactly the same way they apply to records generated within the home Self's own action layer.

DNA-layer content from the FAI event that has been authorized for absorption into a Self's home DNA is home DNA content from the moment absorption is complete. Paper 2's directed selection mechanism (B1.14) operates on DNA changes under the home Self's authority structure. That governance process applies to DNA changes that absorb FAI-origin content in exactly the same way it applies to DNA changes from any other source. The home authority structure determines which FAI-origin DNA content is candidate for absorption, which is approved, and which is declined — the same determinations it makes for internally-generated DNA change proposals.

### 3.2 FAI origin is provenance metadata, not a processing-path determinant

The FAI origin of ingested content is recorded. The provenance record for an action-layer record may indicate that the record originated in a FAI event, identify the event, and carry whatever provenance depth the governance configuration specified. The provenance record for a DNA change may indicate which contributing Self's aspect was the source of the absorbed content. These records are auditable. They are part of the path-retraceability infrastructure that the trilogy's accountability commitments require.

None of this makes FAI origin a processing-path determinant. The home evolution mechanisms do not branch on origin. They process action-layer content as action-layer content and DNA content as DNA content. The provenance record travels with the content and is available to human governance for inspection, audit, and override at any time — but it does not instruct the evolution mechanism to treat the content differently from home-generated content of the same type.

This is the architectural expression of a general principle that runs through the trilogy: content type governs processing path; content origin governs provenance record. Substrate ingestion is where this principle is applied at the inter-Self perimeter. An action-layer record is processed as an action-layer record whether it was produced by the home Self's own agents or by agents operating in a FAI event. A DNA change is processed as a DNA change whether it reflects internally-developed ideas or ideas absorbed from another Self's contribution to a FAI event.

### 3.3 No new mechanism required

The architectural significance of specifying substrate ingestion as the connection mechanism is precisely that substrate ingestion is not new. It is the existing mechanism by which substrate content enters home evolution machinery. Paper 1 established the substrate as the source of truth for coordination; content that is in the substrate is authoritative content. Paper 2 specified the evolution mechanisms that operate on that content. Neither paper required a special intake procedure for content of particular origins. Content enters the substrate; the substrate is processed by the evolution mechanisms; the mechanisms operate under their respective governance shapes.

Paper 3 extends this architecture to the inter-Self scope. FAI produces outputs. Those outputs need to enter home evolution machinery. The mechanism by which they do so is the same mechanism that handles all substrate content entering all evolution machinery. Paper 3 does not need to specify a new ingestion pathway because the existing pathway handles FAI-origin content without modification. The only architectural work Paper 3 does at this locus is to specify that the pathway is the existing one — which is itself an architectural commitment, because it closes off the alternative of a separate FAI-specific intake mechanism.

---

## 4. Three architectural significances

### 4.1 No new evolution pathway required

A deployment implementing Paper 3's FAI architecture on top of Paper 2's governance architecture does not need to add an evolution pathway. It needs to implement the FAI event structure (the shared substrate, the full-aspect-integration operation, the three-tier conflict handling, the four-locus hand-off mechanism). It does not need to add a new pathway within each home Self for processing FAI-derived content. The action-feedback evolution mechanism processes FAI-origin action-layer records because it processes action-layer records. The directed selection mechanism processes FAI-origin DNA candidates because it processes DNA change candidates. No modification to Paper 2's mechanisms is required to accommodate Paper 3's outputs.

This is the sense in which Paper 3 is a structural extension of Paper 2 rather than an architectural replacement or addition requiring new mechanisms. The extension is at the scope of coordination — from intra-Self to inter-Self — not at the level of evolution machinery. The machinery that operates within each Self remains Paper 2's machinery, unchanged.

### 4.2 Full reuse of Paper 2's governance infrastructure

Because FAI-origin content is processed as substrate content by Paper 2's existing mechanisms, all of Paper 2's governance infrastructure for evolution applies to it. This is not trivially obvious — it is a consequence of the substrate ingestion mechanism being the connection point.

The two-stage action-feedback review that Paper 2 specifies for action-layer evolution applies to FAI-origin action-layer records. Those records are subject to the same review structure as home-generated records. They can be approved, modified, or rejected through the same governance process.

The directed selection governance event that Paper 2 specifies for DNA evolution applies to FAI-absorbed DNA. The home authority structure's determination of which DNA change candidates are approved is the governance event through which FAI-origin content either becomes part of the home Self's DNA or is declined. This is the same event that governs all DNA changes.

The DNA version history, the lineage chain, the audit trail that Paper 2's substrate-as-source-of-truth commitment (inherited from Paper 1) maintains — all of this applies to FAI-origin DNA changes that are approved through directed selection. The approved change enters the DNA version history as a change like any other, with provenance metadata indicating its FAI origin.

The result is that a deployment has one governance infrastructure for evolution — Paper 2's — that operates on all evolution inputs, whether home-generated or FAI-origin. There is no need for a parallel governance structure handling FAI-derived content under different rules.

### 4.3 Home governance as sole processing authority post-hand-off

Substrate ingestion as the connection mechanism is also the mechanism through which the architectural sovereignty of home governance is confirmed at the evolution-feed scope. The joint authority that operates during a FAI event — the authority structure spanning all participating Selves' governance structures, operating over the shared substrate — ends at the hand-off boundary (D1.20). After the hand-off boundary, each participating Self's home governance governs exclusively.

Substrate ingestion is the mechanism that operationalizes this sovereignty. The ingestion determination itself — which content from the shared substrate is authorized for absorption, through which mechanism, at what provenance depth — is a home governance decision. Paper 3 Claim 5 establishes that all FAI configuration dimensions are substrate content under home governance; the ingestion policy is one such configuration dimension. Once the ingestion policy has been applied and the content has entered the home substrate, all processing is home governance's domain.

The contributing Self's governance has no continuing authority over how its contributed content is processed in the receiving Self's home substrate. This is not a policy constraint on the contributing Self — it is the architectural consequence of substrate ingestion as the connection mechanism. Content that has been ingested is home substrate content. Home governance owns it. The contributing Self's governance retains authority over its own home substrate; it has no architectural channel through which to govern the processing of content it contributed to a FAI event that the receiving Self has now ingested.

This is the final confirmation, at the evolution-feed scope, of what D1.20 established at the boundary scope: home governance sovereignty is not merely stated as a principle; it is instantiated in the architecture through the mechanism by which content crosses the perimeter.

---

## 5. Closing the Claim 4 sub-commitment set: D1.17–D1.21

The five notes D1.17–D1.21 together specify the complete architecture of how Paper 3's inter-Self coordination via FAI feeds each participating Self's home evolution machinery.

**D1.17** established the action-feedback locus: FAI-origin action-layer records enter action-feedback evolution as action-layer content. **D1.18** established the DNA evolution locus: FAI-origin DNA-layer content enters directed selection as DNA change candidates. **D1.19** established instinct non-crossing: no FAI input reaches instinct evolution; LLM weights and instinct-layer content remain within each home Self. **D1.20** established the hand-off boundary as an architectural object: the moment of FAI dissolution is defined, joint authority ends there, and home governance resumes as sole authority from that moment. **D1.21** (this note) established the connection mechanism: substrate ingestion connects FAI outputs to home evolution machinery; it is the existing mechanism for all substrate content; no new pathway is required; home governance is sole processing authority.

The set is closed. Together the five notes formalize what Paper 3 Claim 4 asserts: that inter-Self coordination via FAI connects to each participating Self's home evolution machinery through a four-locus mechanism that reuses Paper 2's evolution mechanisms unchanged, requires no new architectural addition at the home evolution layer, and confirms home governance sovereignty at every perimeter through both the hand-off boundary and the substrate ingestion mechanism.

**D1.22 begins the Claim 5 sub-commitment set** — configuration as substrate content with recursive applicability — which formalizes the governance architecture under which all FAI event configuration dimensions, including ingestion policies, are themselves governed as substrate content.

---

## 6. Failure modes the sub-commitment defends against

Four failure modes are closed by the D1.21 sub-commitment.

**FAI-specific evolution pathway.** A deployment could, in principle, route FAI-origin content through a dedicated processing pathway within each home Self — a pathway distinct from the existing action-feedback and directed selection mechanisms, designed specifically for inter-Self content. Such a pathway would constitute a new architectural mechanism for which the trilogy papers provide no specification. It would also create a two-tier evolution infrastructure within each home Self, with home-generated content processed one way and FAI-origin content processed another. The D1.21 sub-commitment forecloses this: there is one pathway, and it is the existing one. Any deployment that routes FAI-origin content through a dedicated FAI-specific mechanism has not implemented the architecture the papers specify.

**FAI outputs as non-home-substrate content.** A related failure mode is treating FAI-origin content as retaining a special status — "external content," "contributed content," "inter-Self content" — within the home substrate after ingestion. Such a distinction would mean that the home evolution mechanisms handle the content differently from home-generated content, applying different governance rules or different processing procedures. The D1.21 sub-commitment closes this: once ingested, FAI-origin content is home substrate content. The provenance record documents origin; it does not create a content category that persists as a processing distinction within the home evolution mechanisms.

**Joint authority persisting after hand-off.** A deployment might attempt to maintain some form of bilateral or multilateral governance over ingested content — arrangements under which the contributing Self retains rights to determine how its contributed content is processed within the receiving Self's home substrate. Such arrangements would be in direct conflict with home governance sovereignty as established in D1.20 and confirmed in D1.21 through the substrate ingestion mechanism. The content, once ingested, is governed exclusively by home governance. Any architectural channel through which a contributing Self exercises authority over the processing of ingested content in the receiving Self's home substrate violates the commitment.

**Substrate ingestion as novel mechanism.** A misreading of the architecture might treat Paper 3's specification of substrate ingestion as introducing a new mechanism — one that the CKS architecture did not previously have and that Paper 3 adds to enable FAI-to-evolution connectivity. This misreading is closed by the sub-commitment: substrate ingestion is the existing mechanism by which any content enters home evolution machinery. Applying it to FAI outputs is not novel. What Paper 3 specifies is that FAI outputs are eligible for this existing mechanism — that is, that FAI outputs are substrate content that the home governance can ingest, and that no special intake pathway is required. The novelty in Paper 3 is the inter-Self coordination architecture; the evolution-feed connection mechanism is inherited from Papers 1 and 2 without modification.

---

## 7. Inheritance from Papers 1 and 2

**From Paper 1 — substrate-as-source-of-truth:** Paper 1 establishes that substrate content is the authoritative record of coordination. FAI-origin content that enters the home substrate through ingestion inherits this commitment directly. It becomes authoritative home substrate content, subject to the inspect-modify-override rights that Paper 1's human-governed commitment establishes over all substrate content. The provenance record is itself substrate content and is therefore subject to the same rights.

**From Paper 2 — evolution mechanisms (B1.14, B1.15):** Paper 2 specifies directed selection (B1.14) and action-feedback evolution (B1.15) as the two reasoning-layer evolution mechanisms operating under home governance. These are the mechanisms that substrate ingestion delivers FAI-origin content to. They operate on that content under the same per-mechanism governance shapes Paper 2 §8 specifies. No modification to either mechanism is required to accommodate FAI-origin inputs; the mechanisms are mechanism-agnostic with respect to content origin.

**From Paper 3 — the hand-off boundary (D1.20):** The hand-off boundary established in D1.20 is the precondition for substrate ingestion as a well-defined operation. Ingestion begins at the hand-off boundary. The boundary is what makes the transition from joint-authority content to home-substrate content architecturally defined rather than gradual or ambiguous.

---

## 8. Operational test

A deployment satisfies the D1.21 sub-commitment if and only if all of the following hold:

1. For any FAI-origin content present in a participating Self's home substrate after FAI dissolution and ingestion, an observer can verify that the content is processed through the same Paper 2 evolution mechanism as home-generated content of the same layer type — the same action-feedback pipeline for action-layer records, the same directed selection governance event for DNA change candidates — with no branch in the processing path based on content origin.

2. The provenance record for FAI-origin content carries the FAI-origin annotation, and that annotation is readable and auditable, but there is no evidence that the annotation causes the evolution mechanism to apply different processing rules to the content.

3. There is no evolution pathway within the home Self that is activated exclusively by FAI-origin content — no FAI-specific intake mechanism, no dedicated FAI-content review structure, no separate governance process for content that happens to carry FAI-origin provenance.

4. The home Self's governance authority has full ownership of all processing decisions over ingested FAI-origin content. There is no architectural channel through which a contributing Self's governance can instruct, constrain, or override the processing of content it contributed to a FAI event that the receiving Self has ingested.

5. The ingestion policy itself — which content was authorized for absorption, through which mechanism, at what provenance depth — was determined by home governance prior to or during FAI dissolution, and is itself substrate content subject to the same governance rights as any other substrate content.

A deployment that fails any of these tests has introduced architectural distinctions between FAI-origin content and home-generated content that the CKS architecture does not specify and the prior-art closure does not support.

---

## 9. Conclusion

Substrate ingestion as the FAI-to-home-evolution connection mechanism is the sub-commitment that makes Paper 3's inter-Self coordination architecture an extension of Paper 2's evolution architecture rather than an addition to or replacement of it. FAI events produce outputs — action-layer records and DNA-layer content — that each participating Self's home governance has authorized for absorption. Those outputs enter the home evolution machinery through substrate ingestion: the same mechanism by which any substrate content enters those mechanisms. No new pathway is required. No new governance infrastructure is required. Home governance is the sole authority for all processing decisions from the moment of hand-off.

The FAI origin of ingested content is documented in the provenance record. It is not a processing-path determinant. Action-feedback evolution processes FAI-origin action-layer records as action-layer records. Directed selection processes FAI-origin DNA candidates as DNA candidates. The governance shapes Paper 2 specifies for each mechanism apply to FAI-origin inputs exactly as they apply to home-generated inputs.

With D1.21, the Claim 4 sub-commitment set is closed. D1.17 through D1.21 together specify the complete architecture of how Paper 3's inter-Self coordination feeds each participating Self's home evolution: the two active loci (action-feedback and DNA evolution), the one inactive locus (instinct non-crossing), the hand-off boundary as architectural object, and substrate ingestion as the connection mechanism. The architecture requires no additions to Paper 2 beyond what Paper 3 specifies at the shared-substrate and FAI-operation scope. The evolution machinery already exists. Paper 3 makes inter-Self coordination an authorized input source for it.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Substrate Ingestion as the FAI-to-Home-Evolution Connection Mechanism* (Derivation Note #486, D1.21). May 14, 2026. ORCID: 0009-0004-8065-3235.
