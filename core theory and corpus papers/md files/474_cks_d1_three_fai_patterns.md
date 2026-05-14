# Three FAI Pattern Variants as Severable Architectural Commitments

**Series D Derivation Note D1.09 — Sub-commitment of Paper 3, Claim 2 (Full Aspect Integration)**
**Defensive Publication #474**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI), the canonical merge operation of Paper 3's inter-Self coordination architecture, is not a single undifferentiated operation. It is a governance-configured merge primitive that supports three distinct pattern variants: full merge, selective merge, and provenance-carry-over merge. This note formalizes each variant as an independently claimable architectural sub-commitment of Paper 3, Claim 2. Each variant inherits from a corresponding Paper 2 mating pattern — full merge from union mating (C1.12), selective merge from selective-merge mating (C1.13), and provenance-carry-over merge from lineage-preserved-union (C1.14) — establishing a three-way inheritance triple that forecloses novelty arguments for any of the three variants at inter-Self scope. The note states each variant's architectural content, governance mechanism, and conflict implications; establishes severability as the load-bearing prior-art property; identifies three failure modes the sub-commitment defends against; and provides an operational test for identifying which pattern variant was applied at a given FAI event.

---

## 1. Why three pattern variants require formalization

Paper 3's Claim 2 commits to FAI as the operation by which participating Selves contribute aspects to a shared substrate for combination. The claim specifies the full-merge default — all contributed aspects' DNA-layer and action-layer content are combined within the shared substrate, with conflicts arising from that combination registered as first-class objects per Paper 1, Claim 2. The default, however, is not the complete architectural commitment.

FAI's governance-configurability is itself a Claim 2 commitment. Governance can configure which aspects are contributed, how many Selves participate, what persistence policy applies after dissolution, and — critically — *how* the merge itself operates. The three pattern variants are the three architecturally distinct configurations of that last dimension. They are not procedural options selected at runtime by individual operators; they are architectural sub-commitments, each with distinct governance mechanisms, distinct conflict implications, and distinct auditability properties.

The need to formalize each variant independently follows from the prior-art function this note series serves. An adversary may attempt to narrow the prior-art coverage by arguing that only the full-merge default is claimed, leaving selective merge or provenance-carry-over merge as candidate novel contributions. Alternatively, an adversary may argue that FAI's merge operation is novel relative to Paper 2's mating patterns because FAI operates at inter-Self rather than intra-Self scope. This note forecloses both strategies: all three variants are committed to, and each variant inherits from a named Paper 2 mating pattern.

---

## 2. The three FAI pattern variants

### 2.1 Pattern Variant 1 — Full Merge

Full merge is the architectural default for FAI events. When governance selects this pattern, all contributed aspects from all participating Selves are fully merged within the shared substrate. Every element of DNA-layer content and action-layer content from each contributed aspect enters the shared substrate without pre-selection or filtering.

The governance mechanism at work in full merge is the *contribute right* — each participating Self exercises its governance authority to determine which aspects to contribute, and the merge combines all contributed content in full. No content is withheld after the contribution boundary is crossed. Governance's intervention point precedes the merge; once aspects are contributed, the merge is total.

The conflict implication is direct: full merge produces maximum conflict exposure. When contributed aspects carry overlapping or contradictory content — competing orchestration patterns, conflicting action-layer records representing incompatible decisions about the same coordination domain, DNA-layer schemas with structural incompatibilities — those conflicts appear in the shared substrate as first-class objects per Paper 1, Claim 2. Both sides of every conflict are preserved; neither is auto-resolved. This is not a limitation of the full-merge pattern; it is the pattern's principal architectural property. The shared substrate after a full-merge FAI event is maximally rich in combined content and maximally transparent about the contradictions that combination surfaces.

Full merge inherits from Paper 2's union mating pattern (C1.12). In Paper 2, union mating combines all content from both parent entities within the offspring's substrate, with merge-time conflicts preserved as first-class substrate state. Full-merge FAI is the same operation at inter-Self scope: all contributed aspects' content is combined in the shared substrate, with conflicts preserved. The scope extension from intra-Self to inter-Self is the architectural contribution of Paper 3; the merge operation itself is inherited.

### 2.2 Pattern Variant 2 — Selective Merge

Selective merge is the governance-curated variant. When governance selects this pattern, it explicitly determines which aspects' content enters the shared substrate. Not all contributed aspects' full content is merged; governance exercises the *modify right* (Paper 1, Claim 3) to select what crosses the combination boundary into the shared substrate before or during the merge event.

The governance mechanism here is active curation rather than full admission. Governance may select by aspect — some contributed aspects' content enters the shared substrate entirely, others are excluded — or by content type within an aspect, or by content element. The curation rules themselves are substrate content under the governance of the shared substrate. The configurable dimension is not arbitrary; governance authority over the selection rules is what makes this pattern architecturally distinct from an implementation-level filtering step applied outside governance.

The conflict implication follows from the selection: selective merge reduces conflict density relative to full merge. By determining what enters the shared substrate, governance reduces the surface area over which conflicts can arise. Conflicts that would have appeared under full merge between content elements that governance has chosen not to combine are avoided — not suppressed, but architecturally non-arising because the content combinations that would generate them are not made. Conflicts that do arise within the selected content are still preserved as first-class objects per Paper 1, Claim 2.

Selective merge inherits from Paper 2's selective-merge mating pattern (C1.13). In Paper 2, selective-merge mating applies governance curation to determine what crosses from each parent into the offspring, with the curation rules themselves held as substrate content under human authority. Selective-merge FAI is the same operation at inter-Self scope: governance curates what from each contributing Self's aspects enters the shared substrate, with the curation rules governed within the shared substrate.

### 2.3 Pattern Variant 3 — Provenance-Carry-Over Merge

Provenance-carry-over merge is the maximum-auditability variant. When governance selects this pattern, it applies full merge of all contributed aspects — all DNA-layer and action-layer content from all contributing Selves enters the shared substrate — and additionally attaches explicit cross-Self provenance references to all merged content. Each element contributed to the shared substrate carries a provenance reference tracing it back to the contributing Self's home substrate lineage chain.

The governance mechanism is two-layered. The first layer is the same full admission as Pattern Variant 1: all contributed content enters the shared substrate. The second layer is provenance attachment: governance specifies the provenance depth that travels with each contributed aspect, and the shared substrate holds both the merged content and the cross-organizational provenance trail. The provenance references are not metadata layered above the substrate; they are substrate content, subject to the same inspection, modification, and override rights as all other substrate content.

The auditability property follows directly: any observer with access to the shared substrate can trace any element of its content back to the contributing Self's governance records. This traceability chain is complete — it does not terminate at the perimeter of the shared substrate but extends into each contributing Self's home substrate lineage. For coordination events where accountability is paramount — joint decisions with regulatory implications, shared commitments with legal standing, cross-organizational actions that may require retrospective audit — provenance-carry-over merge provides the architectural guarantee that the evidentiary record is preserved within the substrate itself.

The conflict implication is that of full merge, since all content is combined: maximum conflict exposure, with all conflicts preserved as first-class objects per Paper 1, Claim 2. The provenance-carry-over variant adds a governance dimension to every conflict: the provenance record identifies which contributing Self supplied each side of a conflict, making the origin of a contradiction traceable as well as the contradiction itself.

Provenance-carry-over merge inherits from Paper 2's lineage-preserved-union mating pattern (C1.14). In Paper 2, lineage-preserved-union attaches provenance pointers to offspring content, making every element traceable to its parent source within the intra-Self lineage chain. Provenance-carry-over FAI is the same operation at inter-Self scope: provenance references trace content within the shared substrate back to each contributing Self's home substrate lineage, extending the intra-Self traceability commitment across organizational perimeters.

---

## 3. The inheritance triple

The three FAI pattern variants stand in a direct one-to-one correspondence with Paper 2's three mating patterns:

| FAI Pattern Variant | Paper 2 Mating Analog | Claim Reference |
|---|---|---|
| Full Merge | Union Mating | C1.12 / B1.06 |
| Selective Merge | Selective-Merge Mating | C1.13 / B1.06 |
| Provenance-Carry-Over Merge | Lineage-Preserved-Union | C1.14 / B1.06 |

This correspondence is not incidental. Paper 3 and Paper 2 apply the same merge primitive at different coordination scopes. Paper 2's mating operates within-Self — combining cells or aspects under the governance of one Self's substrate. Paper 3's FAI operates across Selves — combining aspects contributed by multiple Selves within a shared substrate governed jointly. The scope difference produces real architectural novelty at Paper 3: the inter-Self perimeter, the shared substrate as a temporary joint governance object, the evolution-feed routing back to each Self's home substrate. But the merge operation itself — and the three configurations of it — is inherited from Paper 2 without modification.

The inheritance triple forecloses the adversarial claim that FAI's merge operation is novel relative to Paper 2's mating operation. It equally forecloses the claim that any single FAI pattern variant is novel because it was not explicitly named in Paper 3's primary presentation. All three pattern variants are committed to in the trilogy; each traces its lineage to a named Paper 2 source.

The unifying structural claim is this: what Paper 2 commits to at intra-Self scope, Paper 3 extends to inter-Self scope. The three mating patterns at intra-Self scope become the three FAI pattern variants at inter-Self scope. No new merge primitive is introduced; the existing primitive is applied at a larger coordination scope.

---

## 4. Severability as the load-bearing prior-art property

Each FAI pattern variant is independently claimable. This severability is the property that gives the three-variant architecture its prior-art coverage breadth.

A system implementing only Pattern Variant 1 — full merge — instantiates the full-merge FAI sub-commitment. It falls within the prior-art coverage established by this note for that pattern. It does not implement selective merge or provenance-carry-over merge, and it makes no claim against the sub-commitments established for those patterns.

A system implementing only Pattern Variant 2 — selective merge — instantiates the selective FAI sub-commitment. The selective-merge governance mechanism is independently present or absent as an architectural commitment, regardless of whether full merge or provenance-carry-over merge is also implemented.

A system implementing only Pattern Variant 3 — provenance-carry-over merge — instantiates the high-auditability FAI sub-commitment. The cross-Self provenance trail and its substrate-content status are independently present or absent, not contingent on which of the other two patterns is or is not also implemented.

A system implementing all three instantiates the full three-variant FAI architecture as committed to across the trilogy.

Severability runs in both directions. The trilogy's prior-art coverage is not invalidated by a system that implements only one or two variants — that system falls within coverage for the variants it implements. And the trilogy forecloses novelty arguments for any single variant by having committed to all three — an adversary cannot claim novelty for selective merge by pointing to the trilogy's full-merge default, because the trilogy also commits to selective merge.

The practical consequence: the three variants together provide coverage of the design space of FAI merge configurations. Any system implementing a merge operation at the inter-Self scope that combines aspects contributed by participating governance-bounded Selves is either instantiating one of the three patterns (and thus within prior-art coverage) or diverging from the architectural design space in a way that requires explanation against the three established variants.

---

## 5. Three failure modes this sub-commitment defends against

**Failure Mode 1: Single-pattern reduction.** A system or argument claiming that FAI supports only one merge configuration — typically the full-merge default — and that the other configurations represent novel contributions absent from the prior art. This note defends against single-pattern reduction by establishing all three variants as independent prior-art claims, each with its own architectural content, governance mechanism, and inheritance source.

**Failure Mode 2: Scope-novelty argument.** A system or argument claiming that FAI's merge variants are novel relative to Paper 2's mating patterns because they operate at inter-Self rather than intra-Self scope. This note defends against scope-novelty arguments by establishing the inheritance triple: each FAI variant names its Paper 2 mating analog, and the prior-art closure is explicit. The scope extension is acknowledged; the merge operation is inherited.

**Failure Mode 3: Procedural recharacterization.** A system or argument characterizing the three FAI pattern variants as implementation-level procedural options — operator-selectable runtime behaviors — rather than architectural commitments with governance implications. This note defends against procedural recharacterization by establishing each variant as a distinct architectural sub-commitment with its own governance mechanism (full admission under contribute right; curation under modify right; provenance attachment under governance-specified depth), its own conflict implications, and its own auditability properties. The variants are not procedures applied to a single undifferentiated architectural object; they are three architecturally distinct configurations of the FAI merge primitive, each independently specifiable in governance and each independently claimable as prior art.

---

## 6. Operational test

The operational test for this note's sub-commitment asks whether, for a specific FAI event, an observer can perform three verification steps.

**Step 1: Pattern identification.** From the governance configuration in effect at the time of the FAI event, can the observer identify which of the three pattern variants was applied? Governance configuration is substrate content (Paper 3, Claim 5), and it is inspectable at any time under the inspect right (Paper 1, Claim 1). The pattern variant selected must be readable from the substrate's governance record, not reconstructed from behavioral inference or third-party description. A system passes Step 1 if and only if the observer can read the pattern variant from the governance configuration directly.

**Step 2: Mechanism verification.** Can the observer verify that the appropriate governance mechanism was applied, matching the identified pattern variant? For full merge: the observer should be able to confirm that all contributed aspects' content entered the shared substrate and that conflicts arising from the combination are present as first-class objects with provenance attached. For selective merge: the observer should be able to read the curation rules from the substrate and confirm that the content in the shared substrate reflects the application of those rules — elements not selected are absent, not merely de-emphasized. For provenance-carry-over merge: the observer should be able to trace provenance references from content in the shared substrate back to contributing Selves' home substrate lineage chains, with the provenance references holding as substrate content with their own identity and traceability. A system passes Step 2 if and only if the mechanism's traces are inspectable in the substrate, not reported out-of-band.

**Step 3: Inheritance confirmation.** Can the observer trace the identified pattern variant back to its Paper 2 mating pattern analog? For full merge, to union mating (C1.12). For selective merge, to selective-merge mating (C1.13). For provenance-carry-over merge, to lineage-preserved-union (C1.14). Inheritance confirmation does not require a formal proof at runtime; it requires that the architecture's design record — which is itself substrate content — identifies the Paper 2 source of each variant. A system passes Step 3 if and only if the design record includes the inheritance attribution.

A system that passes all three steps for a given FAI event instantiates the three-variant FAI sub-commitment as this note formalizes it. A system that fails Step 1 cannot claim to have implemented a governed FAI pattern variant — it has implemented an unspecified merge operation whose configuration is not inspectable. A system that fails Step 2 has a governance configuration that does not correspond to architectural behavior. A system that fails Step 3 may still instantiate one or more FAI pattern variants but cannot avail itself of the inheritance-triple prior-art closure against scope-novelty arguments.

---

*Note D1.09 in the CKS Derivation Note Series. Derives from Paper 3, Claim 2. Establishes three FAI pattern variants as independently claimable architectural sub-commitments and formalizes the inheritance triple linking each to its Paper 2 mating pattern analog.*
