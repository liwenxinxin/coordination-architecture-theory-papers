# FAI and the Three-Adjacencies Framework

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note number:** 569 (D2.74 in the Phase D2 derivation series)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its sole contribution is to extend the three-adjacencies positioning Paper 1 establishes at cell scope to the inter-Self FAI scope Paper 3 establishes, showing that the same architectural distinctions that distinguish CKS from its three nearest neighbors at cell scope distinguish FAI from those same neighbors at inter-Self scope.

---

## Abstract

Paper 1 of the CKS theory series positions the Coordination Knowledge Substrate architecture relative to three adjacent design objects with which it is most often conflated: retrieval-augmented generation (RAG), parametric (in-weight) memory, and external structured memory in the style of Knowledge Objects and OIDA. The distinctions Paper 1 draws are architectural commitments, not feature observations — they characterize a different design posture, not a different set of features on a shared posture. Paper 3 introduces Full Aspect Integration (FAI) as the canonical operation over a shared substrate that spans the perimeters of two or more CKS-governed Selves. This note applies Paper 1's three-adjacencies positioning to the inter-Self FAI scope: for each of the three adjacent approaches, the note identifies what that approach does at inter-Self scope, why FAI resembles it closely enough to invite conflation, how FAI is architecturally distinct, and why the distinction matters for prior-art positioning. The three-adjacencies framework is not new at inter-Self scope; it is the same framework from Paper 1 applied one rung higher on the substrate-mediator ladder. The same positioning that forecloses conflation at cell scope forecloses conflation at inter-Self scope.

---

## 1. Why the three-adjacencies framework extends to inter-Self scope

Paper 1 draws three architectural boundaries in compact form (§§1.2, 2.3) and develops them as load-bearing differentiations at §§3.1, 5.2, 6.1, 6.2, and 8.2. The derivation note *Three Adjacencies: Why CKS Is Not RAG, Not Parametric Memory, and Not External Structured Memory* (Li, April 2026) assembles those boundaries into a single operational reference. The distinctions are not peripheral to Paper 1's architecture; they are constitutive of it. The substrate's design posture — a persistent, human-governed coordination artifact over which AI acts as mediator, carrying decisions and rationale humans hold authority over — is precisely what separates CKS from the three adjacent objects. Remove any of the three distinctions and the architecture collapses into one of its neighbors.

Paper 3 extends substrate-mediated coordination across the inter-Self perimeter. The shared substrate through which two or more CKS-governed Selves coordinate is constructed for an interaction, spans the participating Selves' home governance perimeters, and carries all six Paper 1 commitments within scope. Full Aspect Integration is the canonical operation over this shared substrate: Selves contribute aspects (the structural exchange unit from Paper 2), the default is full merge of contributed aspects within the shared substrate, and whether full merge is performed and which aspects each Self contributes is governance-configured per event. The four-locus evolution-feed mechanism routes FAI outputs to each participating Self's home-perimeter Paper 2 evolution machinery after the event dissolves.

At inter-Self scope, the three adjacent approaches reappear. Cross-organizational RAG, federated learning and model weight exchange, and federated knowledge-base composition are all active design territories at the inter-Self boundary, and each resembles FAI closely enough to generate conflation risk. Adversaries may claim that Paper 3's inter-Self architecture falls within one of these categories rather than constituting a distinct architectural contribution. The three-adjacencies framework forecloses each characterization with the same structural logic Paper 1 deploys at cell scope: the distinctions are not incremental on top of the adjacent approaches; they are commitments the adjacent approaches do not make.

---

## 2. FAI is not inter-Self RAG

**What RAG does at inter-Self scope.** At the inter-Self boundary, the RAG pattern extends naturally to cross-organizational retrieval: Self A queries an index built over Self B's document corpus (or Self B's at inference time), retrieves source material relevant to a generation task, and uses that material as additional context. The design object at inter-Self scope is a cross-organizational corpus-plus-index pair — retrieval infrastructure connecting the document stores of participating Selves. The primary design goal remains retrieval quality: getting the right source content from one Self's corpus into another Self's LLM context at inference time.

**Why FAI resembles it.** FAI involves content crossing the inter-Self perimeter. When Self A and Self B participate in an FAI event, content from Self A's substrate becomes part of the shared substrate Self B's AI mediator also operates over. From a distance, this looks like one Self making content from another Self available for use — which is what cross-organizational RAG also does. The resemblance is strong enough that a reader familiar only with RAG might reach for the cross-organizational RAG frame to describe what FAI does.

**How FAI is architecturally distinct.** The content FAI exchanges is not source material retrieved for inference-time grounding. The unit of exchange is the *aspect* — a governed coordination unit grouping cells, carrying DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, lived experience). This content is substrate content: decisions, rationale, conflict state, and governance semantics that humans hold authority over. It is not a corpus of source documents indexed for similarity retrieval. The shared substrate into which contributed aspects merge is not a retrieval index; it is a perimeter-spanning coordination artifact under joint human authority, carrying all six Paper 1 commitments including conflict preservation and AI-as-substrate-mediator. The AI's role within an FAI event is substrate mediator — helping human-authorized participants operate over the shared substrate under jointly authored orchestration rules — not inference-time retrieval client querying a corpus for source content.

**Prior-art significance.** The characterization "this is just cross-organizational RAG" would collapse the shared substrate into a retrieval index and governance under joint authority into retrieval policy. It would lose the entire coordination-and-decision-layer move that makes inter-Self FAI an architectural contribution distinct from cross-organizational document retrieval. The same one-sentence test Paper 1 establishes carries directly: if the mechanism's primary function is to retrieve source material from one party's corpus into another party's LLM context at inference time, it is RAG; if the primary function is to carry governed substrate content — decisions, rationale, and conflict state — across organizational perimeters into a human-governed shared artifact, it is FAI.

---

## 3. FAI is not inter-Self parametric memory exchange

**What parametric memory exchange does at inter-Self scope.** At the inter-Self boundary, parametric memory exchange is the territory of federated learning, model merging, and weight-space alignment: two or more organizationally distinct models updating their weights through some form of cross-organizational gradient aggregation, weight averaging, or model merging procedure. Knowledge moves between Selves by flowing through the weight-update mechanism — gradient updates, merged parameter vectors, distilled weight snapshots. The content is in the weights; the exchange moves weight-encoded knowledge.

**Why FAI resembles it.** FAI's four-locus evolution-feed mechanism routes FAI outputs to each participating Self's home-perimeter evolution machinery after an event dissolves. DNA-layer content from the FAI event feeds DNA evolution; action-layer content feeds action-feedback evolution. The result is that each Self's architecture is changed by participating in an FAI event — the home substrate absorbs new content the Self did not have before. This looks like Selves learning from each other, which is also what federated learning and model merging accomplish. An observer familiar with weight-space cross-organizational knowledge transfer might describe FAI as a substrate-layer variant of the same general pattern.

**How FAI is architecturally distinct.** FAI's evolution feed operates exclusively over substrate content. DNA-layer content and action-layer content are reasoning-layer artifacts under Paper 2's instinct/reasoning separation. The instinct layer — LLM weights — takes no FAI input by architectural commitment. This is the instinct/reasoning separation extended at the inter-Self boundary as an architectural commitment at FAI mechanism level, not a deployment configuration. FAI does not transfer, average, or otherwise modify the participating Selves' model weights. What travels through the shared substrate and into each home substrate after dissolution is human-governed, addressable, inspectable content — substrate content each Self's governance perimeter holds authority over before and after ingestion. The cost model is database-like and linear in content additions; parametric expansion is superlinear and frontier-dependent. These cost models are structurally incompatible: importing the parametric cost curve into FAI produces unintelligible predictions about the architecture's scaling behavior.

**Prior-art significance.** The characterization "this is just federated learning over substrate content" would import the parametric expansion cost model and erase the instinct/reasoning separation boundary as a design commitment. It would reframe the evolution-feed mechanism as a weight-update procedure rather than as a governed substrate-content ingestion procedure under home-perimeter human authority. The same test Paper 1 establishes carries directly: if cross-organizational knowledge exchange requires modifying model weights through any training procedure, the mechanism is parametric; if exchange happens through writes to addressable governed substrate content under human authority at each perimeter, it is not.

---

## 4. FAI is not inter-Self external structured memory composition

**What external structured memory composition does at inter-Self scope.** External structured memory — the family represented by Knowledge Objects (KO) and OIDA — locates coordination-grade knowledge in typed structured units in an external store. At the inter-Self boundary, this family extends to cross-organizational knowledge base composition: federating structured knowledge stores across organizational perimeters, exchanging typed objects with provenance, merging knowledge graphs, and synchronizing epistemic-class-carrying knowledge units across organizations. KO's hash-addressed objects with provenance metadata and OIDA's Knowledge Objects carrying epistemic class, signed contradiction edges, and deterministic maintenance logic are well-suited to cross-organizational composition — the structure and typing make objects exchangeable without losing semantic content. The shared commitment across the family is that coordination-grade knowledge is a schema-level object with typed structure and maintained state.

**Why FAI resembles it.** FAI's unit of exchange is the aspect, which surfaces typed structured content: DNA-layer and action-layer substrate content with provenance, epistemic structure, and conflict state. The shared substrate is a typed structured artifact whose content carries provenance across organizational boundaries. FAI preserves conflicts as first-class substrate state — a commitment the OIDA family also makes through signed contradiction edges. An observer familiar with cross-organizational KO or OIDA composition might describe FAI as a governed variant of the same structured-exchange pattern.

**How FAI is architecturally distinct.** The three distinguishing axes Paper 1 establishes at cell scope carry intact to inter-Self scope, and a fourth axis — where disambiguation work lives — compounds the distinction.

*First*, human governance. FAI's shared substrate operates under joint human authority: the governance perimeter spanning participating Selves is itself substrate content under human control; which aspects each Self contributes, whether full merge is performed, and what persists after dissolution are all human-governed and configurable per event. KO's hash-addressed maintenance and OIDA's Knowledge Gravity Engine operate over the substrate deterministically; neither locates authority in any particular human actor or makes human authority over the merged state a first-class architectural commitment. Cross-organizational KO or OIDA composition inherits this posture: the composition mechanics operate over the structured store, and governance (if present) is layered separately rather than being constitutive of the composition mechanism.

*Second*, role and authority schema. Each participating Self brings to an FAI event not only structured content but the role and authority semantics encoded in its cells' orchestration rules. These semantics — who may decide what, on what evidence, under which rules — travel with the contributed aspects and remain in the shared substrate under joint authority. KO's `provenance_metadata` field and OIDA's epistemic class do not encode institutional provenance in this role/authority sense. Cross-organizational KO or OIDA composition does not, by architectural commitment, surface whose authority governs which content or under what orchestration rules that content was produced.

*Third*, AI's architectural role. In FAI, each participating Self's AI operates as substrate mediator within the shared substrate — executing operations under jointly authored orchestration rules, helping human-authorized participants read, write, and interpret shared substrate content. The AI does not consume the shared substrate as a client to answer queries. In KO and OIDA, AI is a substrate client: it reads structured memory to ground responses. Cross-organizational KO or OIDA composition preserves this client posture across the inter-Self boundary.

*Fourth*, where disambiguation work lives. FAI surfaces conflicts as first-class preserve-tier state in the shared substrate — the three-tier conflict-handling mechanism (preserve by default per Paper 1 inheritance; resolve via jointly authored orchestration rules as inspectable substrate content; escalate to humans across joint authority) encodes conflict handling as human-governed substrate content. KO disambiguates computationally at retrieval time; OIDA's Knowledge Gravity Engine resolves contradictions through deterministic maintenance over the substrate. Cross-organizational composition in either family inherits these computational disambiguation postures. FAI encodes conflict handling in human-authored orchestration rules, not in retrieval algorithms or maintenance engines.

**Prior-art significance.** The characterizations "this is just federated KO" or "this is cross-organizational OIDA composition" would each collapse the shared substrate into a cross-organizational typed knowledge store and lose one or more of the four distinguishing axes. "Federated KO" loses human governance and role/authority schema and reduces AI to substrate client. "Cross-organizational OIDA" loses human governance of the merged state and the AI-as-mediator commitment. The same test Paper 1 establishes carries directly: if the mechanism treats AI as a client consuming typed structured memory across organizational perimeters, with no first-class commitment to joint human authority over the merged state or to role/authority schema within it, it is external structured memory composition; if the shared artifact is human-governed by architectural commitment, carries role and authority semantics under jointly authored orchestration rules, and treats AI as substrate mediator rather than client, it is FAI.

---

## 5. The inheritance: same framework, extended scope

The three-adjacencies positioning at inter-Self scope is not a new architectural claim. It is Paper 1's positioning applied one rung higher on the substrate-mediator ladder. Paper 1 establishes the substrate as the medium of coordination within a cell and draws three boundaries at that scope. Paper 3 establishes the shared substrate as the medium across the inter-Self perimeter and inherits those boundaries at the new scope. The structural form of each distinction is identical at both scopes: the adjacent approach does at inter-Self scope what it does at cell scope, scaled to the inter-organizational boundary; FAI resembles it for the same reason CKS resembles it at cell scope; and FAI is distinct for the same architectural reasons CKS is distinct at cell scope.

This inheritance pattern is architecturally significant for two reasons. First, it demonstrates that the CKS trilogy's architectural commitments are consistent across scales — the same design posture that distinguishes CKS from its neighbors within a cell also distinguishes inter-Self FAI from those same neighbors at the inter-organizational boundary. The trilogy does not introduce new design philosophy at inter-Self scope; it extends prior philosophy to a new scope without contradiction. Second, the inheritance defeats the adversarial move of treating the inter-Self extension as an escape from the cell-scope distinctions — arguing that although CKS is architecturally distinct from RAG at cell scope, inter-Self FAI "is really" cross-organizational RAG. The distinctions hold at inter-Self scope for the same reasons they hold at cell scope; the scope change does not change the design posture.

The three-adjacencies framework is defined once, in Paper 1. This note extends it. Downstream work engaging with FAI at the inter-Self boundary can rely on the same three-adjacencies reference that cell-scope CKS work relies on, with the extension this note formalizes.

---

## 6. Operational test

For any inter-Self AI coordination mechanism, the following test determines whether it falls within the FAI architecture or within one of the three adjacent categories.

**Test for inter-Self RAG.** Ask: is the mechanism's primary function to retrieve source material from one participating party's document corpus into another party's LLM context at inference time? If yes, the mechanism is cross-organizational RAG, not FAI. If the mechanism's primary function is to carry governed substrate content — decisions, rationale, role/authority semantics, and conflict state — across organizational perimeters into a perimeter-spanning shared artifact under joint human authority, it is FAI.

**Test for inter-Self parametric memory exchange.** Ask: does the mechanism modify the model weights of any participating Self through any gradient-based or weight-merging procedure as a result of the inter-Self interaction? If yes, the mechanism operates on parametric memory, not on the governed substrate FAI operates over. If inter-Self exchange is bounded to substrate content (DNA-layer and action-layer reasoning-layer content), with instinct-layer content excluded by architectural commitment, the mechanism is consistent with FAI.

**Test for inter-Self external structured memory composition.** Ask three questions. First: does the mechanism locate joint human authority over the merged state as a first-class architectural commitment, or does it rely on deterministic maintenance over a typed store with governance layered separately? Second: does the mechanism carry role and authority semantics as substrate content under jointly authored orchestration rules, or does it carry only epistemic class and provenance metadata? Third: does the mechanism treat AI as substrate mediator under jointly authored orchestration rules, or as a substrate client consuming merged typed content to answer queries? If the answer to all three questions falls on the left side (joint human authority; role/authority schema; AI-as-mediator), the mechanism is consistent with FAI. If any answer falls on the right side (deterministic maintenance; epistemic class only; AI-as-client), the mechanism falls within the external structured memory family, not FAI.

An inter-Self coordination mechanism that passes all three tests — content is governed substrate content not retrieval target; exchange is bounded to reasoning-layer substrate content not weights; shared artifact is human-governed by commitment with role/authority schema and AI-as-mediator — is consistent with the FAI architecture Paper 3 establishes.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## Related notes in this series

Li, W. (2026). *Three Adjacencies: Why CKS Is Not RAG, Not Parametric Memory, and Not External Structured Memory.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and the Three-Adjacencies Framework.* May 15, 2026. ORCID: 0009-0004-8065-3235. Note 569 (D2.74), CKS Derivation Note Series.
