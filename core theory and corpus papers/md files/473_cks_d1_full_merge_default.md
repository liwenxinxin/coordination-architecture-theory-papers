# Full-Merge as the FAI Architectural Default

**Derivation Note D1.08 — Series D, Phase D1 (Note #473)**
**Sub-commitment of Paper 3 Claim 2**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 Claim 2 establishes Full Aspect Integration (FAI) as the canonical operation over the shared substrate, and commits to full merge of contributed aspects as FAI's architectural default. This note formalizes that default commitment as sub-commitment D1.08. It states precisely what full merge means at the architectural level: all aspects contributed by all participating Selves are fully merged within the shared substrate, with their DNA-layer and action-layer content accessible as a combined whole and no content selectively excluded by the architecture absent governance configuration. It explains why the commitment is a *default* rather than a *mandate*: governance can configure alternative merge patterns, including selective merge, but the architecture presumes full combination absent restriction. It identifies the three architectural consequences of choosing full merge as the default: maximum information availability within the shared substrate, conflict preservation applied to all merge-generated conflicts, and human governance as the operative restriction mechanism. It positions the full-merge default as the inter-Self analog of Paper 2's union mating pattern at intra-Self scope, following the T1.05 disambiguation in the CKS trilogy ambiguity map. It names four failure modes the sub-commitment defends against, and provides an operational test for verifying full-merge default behavior in a deployed FAI event.

---

## 1. Background and Position in the Derivation Series

D1.08 is the eighth note in Phase D1 of the Series D derivation note program. Series D formalizes sub-commitments of Paper 3, and Phase D1 formalizes sub-commitments of Paper 3 Claim 2 specifically, which establishes FAI as the canonical operation over the shared substrate.

D1.08 derives from D0.02 (the Paper 3 Claim 2 registration note) and occupies a specific position within the Claim 2 architecture. Prior Phase D1 notes have established: FAI as the canonical inter-Self coordination primitive (D1.01), conflict preservation as the response to merge conflicts arising during FAI (D1.02), the aspect as the unit of exchange in FAI events (D1.03), the exchange boundary at the reasoning layer (D1.04), cardinality flexibility in FAI events (D1.05), the shared substrate as the temporary medium of inter-Self integration (D1.06), and governance configuration as the mechanism for controlling FAI event parameters (D1.07).

D1.08 formalizes a commitment that ties several of these together: that the default merge operation within an FAI event is *full* merge — the complete combination of all contributed aspects from all participating Selves within the shared substrate. The full-merge default is not incidental to FAI's architecture; it is a positive architectural commitment with prior-art significance.

---

## 2. Statement of D1.08

**D1.08 — Full-Merge as FAI Architectural Default:**

When participating Selves contribute aspects to the shared substrate during an FAI event, the default operation is full merge: all aspects contributed by all participating Selves are fully merged within the shared substrate. The DNA-layer and action-layer content of all contributed aspects is accessible within the shared substrate as a combined whole. No content is selectively excluded from the merge by the architecture absent governance configuration specifying an alternative merge pattern.

This default is an architectural commitment, not a procedural convenience. It reflects a positive design choice: absent governance reasons to restrict, full combination maximizes the coordination value of the FAI event. The architecture encodes that presumption in its default, placing the burden on governance to configure restriction rather than placing the burden on governance to authorize any combination.

Full merge as the default does not mean full merge is mandatory. Governance configuration can specify:

- **Which aspects each Self contributes** (sharing scope): a participating Self need not contribute all of its aspects to the shared substrate; governance determines the contribution set.
- **How contributed aspects are merged** (merge pattern): governance can configure selective merge or other available pattern variants rather than full merge of the contributed set.

Neither alternative is prohibited. Both are governance choices. What the architecture commits to is the starting point: absent governance configuration specifying otherwise, full merge of the contributed aspects is the operation that occurs.

---

## 3. What Full Merge Means at the Architectural Level

Full merge, as the FAI architectural default, is defined over the content that participating Selves have contributed to the shared substrate. Its content is precise.

**Scope of full merge.** Full merge operates over the contributed aspects, not over each participating Self's entire home substrate. What a Self contributes is governance-configured (per D1.07 and Paper 3 Claim 5 on sharing-scope configuration). Once contribution has occurred — once the governance-configured set of aspects has entered the shared substrate — full merge combines the *contributed* set in its entirety. The sharing-scope decision and the merge-pattern decision are analytically distinct: sharing scope determines what enters the shared substrate; merge pattern determines how what has entered is combined.

**Content accessed in full merge.** When an aspect is contributed to the shared substrate, it surfaces its constituent cells' DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, operational evidence) for exchange. Full merge makes this content from all contributed aspects accessible within the shared substrate as a combined whole. No DNA-layer or action-layer content from any contributed aspect is selectively withheld from the merge by the architecture.

**What full merge does not combine.** FAI exchanges only reasoning-layer content — DNA-layer and action-layer content per Paper 2's instinct/reasoning separation (D1.04). LLM weights and instinct-layer content do not exchange through the shared substrate. Full merge is full within the scope of what FAI exchanges; it is not full across content classes that FAI's layer boundary excludes.

**Result of full merge.** The shared substrate, after full merge, contains the combined DNA-layer and action-layer content of all contributed aspects from all participating Selves. This combined content is the substrate over which the FAI event's coordination activity proceeds. Any conflicts arising from full combination — where contributed content from different Selves or different aspects of the same Self is in tension — are preserved as first-class substrate state by inheritance from Paper 1 Claim 2 (conflict preservation), formalized at FAI scope in D1.02.

---

## 4. Why Default Rather Than Mandatory

The commitment is to a *default*, not a *mandate*. The distinction is architecturally significant and the word "default" is precise.

A mandatory full-merge architecture would require full combination regardless of governance judgment. It would remove governance's ability to configure selective merge or other patterns. FAI's architecture does not do this. Governance retains the authority to configure alternative merge patterns (Paper 3 Claim 5 on governance-configured merge patterns; D1.07 on governance configuration scope). The architecture makes full merge the starting point; it does not remove governance's authority to depart from it.

The reason for choosing full merge as the default, rather than some other starting point, is coordination-value maximization. The purpose of an FAI event is inter-Self coordination — the combination of contributed knowledge and experience across Selves to produce coordination value that neither Self could produce alone. Full merge maximizes the content available within the shared substrate for that coordination activity. Defaulting to any less-than-full combination would mean coordination value is systematically left on the table absent an affirmative governance decision to claim it. The architecture encodes the opposite presumption: combination is the objective; restriction is the departure that requires governance authorization.

This default structure contrasts with architectures that default to no-merge or restricted-merge, requiring explicit authorization for any content combination. No-merge-default architectures place the coordination-value burden on governance to affirmatively authorize each combination, rather than placing the restriction burden on governance to affirmatively configure each limit. FAI's default expresses a design philosophy: the shared substrate exists to enable coordination; the default should serve that purpose.

Governance can always restrict. The three rights — inspect, modify, override — that characterize human governance in the CKS architecture apply to the merge configuration as they apply to all substrate content and orchestration rules. A deployment in which governance has determined that selective merge is appropriate for a particular FAI event, or a particular class of FAI events, operates a governance-configured alternative to the default. The architecture permits and supports this. The default is the starting point for governance deliberation, not a wall against governance authority.

---

## 5. Full Merge as Architectural Commitment: Three Consequences

Choosing full merge as the architectural default is not merely a procedural choice. It carries three architectural consequences that are themselves prior-art commitments.

**Consequence 1: Maximum information availability within the shared substrate absent governance restriction.** The full-merge default means that, absent governance configuration specifying otherwise, the shared substrate contains the full combined content of all contributed aspects. Coordination activity within the shared substrate operates with maximum informational breadth. This is the direct purpose of the default choice. Any alternative default (selective merge, no-merge) would systematically reduce available information without governance involvement. The full-merge default makes governance the mechanism for reduction, not the architecture.

**Consequence 2: Conflict preservation applies to all conflicts arising from full merge.** Because full merge combines all contributed content without pre-filtering for compatibility, full merge may produce conflicts — cases where contributed content from different Selves, or different aspects of the same Self, is in tension within the shared substrate. The architecture's response is not to prevent full merge in order to avoid conflicts. The response is conflict preservation: conflicts arising from the full merge are preserved as first-class substrate state (D1.02; Paper 1 Claim 2 by inheritance through Paper 3 Claim 1 and §4). This is a design choice with prior-art significance. It would have been architecturally coherent to adopt a restricted-merge default specifically to minimize conflict incidence. FAI's architecture adopts the opposite posture: prefer full combination; handle conflicts as first-class objects rather than preventing them by restricting combination. Conflict preservation is the enabling mechanism that makes full-merge-as-default architecturally viable.

**Consequence 3: Human governance is the mechanism for restricting merge scope.** Because the default is full merge and alternatives require governance configuration, governance is the operative restriction mechanism. The architecture does not automatically restrict based on content type, contributor identity, or inferred compatibility. Whatever restriction occurs is governance-authored. This preserves the CKS authority architecture at the merge-configuration level: humans hold the authority over which content combines, expressed through governance-configured merge patterns, and the architecture does not usurp that authority by pre-determining restrictions.

---

## 6. Inter-Self Analog of Paper 2's Union Mating Pattern

The CKS trilogy ambiguity map (T1.05) establishes the precise relationship between Paper 2's mating operation (intra-Self scope) and FAI (inter-Self scope). D1.08's full-merge default is the inter-Self analog of the union mating pattern at intra-Self scope, and naming this inheritance explicitly is necessary to close the adversarial gap.

**Paper 2's union mating pattern.** Paper 2 establishes mating as a governed lifecycle operation combining two or more parent entities' DNA specifications to produce offspring. Three pattern variants are available: union (all parent DNA combined), selective merge (governance selects which rules to include), and lineage-preserved union (all combined with explicit cross-lineage references). The union pattern keeps everything from both parents and preserves all conflicts as first-class substrate state in the offspring, inheriting Paper 1 Claim 2's conflict preservation directly. Among the three pattern variants, Paper 2 does not name a default; all three are available under orchestration-configured selection.

**FAI's full-merge default as the inter-Self analog.** FAI's full merge — full combination of all contributed aspects within the shared substrate — is the inter-Self analog of Paper 2's union mating pattern. Both operations produce maximum content combination from participating entities: union mating combines all parent DNA; FAI full merge combines all contributed aspects. Both rely on conflict preservation (Paper 1 Claim 2) to handle the conflicts that full combination may produce. The three pattern variants available in Paper 2 mating carry through to FAI at inter-Self scope: full merge ≈ union; governance-configured selective merge ≈ selective merge; with explicit provenance carry-over ≈ lineage-preserved union. The T1.05 disambiguation establishes this as the same merge primitive at different coordination scopes.

**What is new at inter-Self scope.** The T1.05 prior-art closure establishes that FAI's merge operation is inherited, not novel, relative to Paper 2. But one specific commitment is fresh at inter-Self scope: Paper 2 does not name a default among its three pattern variants at intra-Self scope; FAI names full merge as the default at inter-Self scope. The architectural-default commitment specifically — not the merge primitive, not the three pattern variants, not the conflict preservation — is new at Claim 2. This locates the prior-art contribution precisely and closes both adversarial gaps simultaneously.

**Closing the adversarial gaps.** Two adversarial readings target this relationship. The first claims that FAI's full merge is novel relative to Paper 2's union mating pattern. T1.05 prior-art closure answers: the merge operation is the same primitive at different scopes; inheritance runs from Paper 2 union pattern to FAI full merge; the operation is not novel. The second claims that mating and FAI are the same operation and that Paper 3 therefore adds nothing. T1.05 also closes this: FAI is the merge primitive at inter-Self scope, where it carries two structural differences — (a) FAI produces evolution outputs absorbed into each Self's home substrate rather than producing new offspring entities; (b) FAI names full merge as the default at inter-Self scope, a commitment Paper 2 does not make at intra-Self scope. The merger-primitive inheritance is real; the extension is also real.

---

## 7. Failure Modes D1.08 Defends Against

D1.08 defends against four failure modes that could compromise the prior-art scope of the full-merge default commitment.

**Failure Mode 1: Mandatory-full-merge misreading.** An adversary might characterize FAI as committing to mandatory full merge — a fixed architectural requirement that admits no alternative. D1.08 forecloses this reading. Full merge is the default, not the mandate. Governance can configure selective merge or other patterns. The commitment is to the starting point and to the structural direction of the burden of proof (governance must configure restriction; the architecture does not impose it automatically). Mandatory full merge would be a different and stronger commitment than what D1.08 establishes.

**Failure Mode 2: No-merge-default architectures.** Architectures that default to no merging — requiring explicit governance authorization for any content combination — occupy a different position in the design space than FAI. FAI's full-merge default commits to the opposite starting point: combination is presumed; restriction requires governance configuration. D1.08 establishes this asymmetry explicitly, so that no-merge-default architectures are not read as equivalent to FAI on this axis.

**Failure Mode 3: Infrastructure-determined merge.** An adversary might claim that FAI's merge pattern is determined by the communication infrastructure (the protocols and tools through which aspects are contributed to the shared substrate) rather than by governance. D1.08 forecloses this reading. The merge pattern is governance-configured. The default is an architectural commitment authored into the governance structure of the FAI mechanism; it is not an artifact of infrastructure behavior. Infrastructure can implement full merge as the default; infrastructure does not define what the default is. The definition lives in the architecture's governance layer.

**Failure Mode 4: Full-merge at inter-Self scope as novel.** An adversary might claim that full-merge-with-conflict-preservation at inter-Self scope is a novel operation unrelated to any prior CKS commitment. T1.05 prior-art closure (see §6 above) answers this directly. Full merge at inter-Self scope is the analog of Paper 2's union mating pattern at intra-Self scope. The merge primitive, the three pattern variants, and the conflict preservation response all inherit from Paper 2 carrying through Paper 3's inter-Self extension. The specific fresh commitment at inter-Self scope — the full-merge default — is locatable on the architecture's prior-art map; it is not architecturally free-floating.

---

## 8. Operational Test

For an FAI event in which no alternative merge configuration is specified, the following test verifies that D1.08's full-merge default is instantiated:

1. **Contribution verification.** Identify all aspects contributed to the shared substrate by all participating Selves during the FAI event, as specified by the governance-configured sharing scope for that event.

2. **Full-merge verification.** Confirm that the DNA-layer and action-layer content of all identified contributed aspects is accessible within the shared substrate as combined content. No contributed aspect's content should be absent from the shared substrate by virtue of a merge restriction that was not governance-configured for this event.

3. **No-configuration-required verification.** Confirm that no explicit merge-pattern configuration was required to trigger full merge. Full merge should be the operation that occurred absent configuration specifying otherwise.

4. **Conflict preservation verification.** Identify any conflicts arising within the shared substrate from the full merge — cases where contributed content from different Selves or different aspects is in tension. Confirm that those conflicts are preserved as first-class substrate state rather than silently resolved, discarded, or used to block the merge. Conflict registration as first-class objects (D1.02; Paper 1 Claim 2) applies to all conflicts arising from the full merge.

A system that passes all four checks instantiates D1.08's full-merge default. A system that fails check 2 has selectively restricted the merge without governance configuration, violating the default. A system that fails check 4 has suppressed conflicts that the architecture requires to be preserved, violating the conflict preservation commitment that makes full-merge-as-default architecturally viable.

---

## 9. Relationship to Other D1 Notes

D1.08 is architecturally adjacent to several prior D1 notes and to the Paper 3 governance configuration notes (Claim 5).

**D1.02 (Conflict Preservation at FAI Scope).** D1.08 and D1.02 are complementary: full merge produces the conflicts that conflict preservation handles. The design is intentional — full merge is made viable as an architectural default precisely because conflict preservation handles its outputs. Neither commitment makes sense in isolation at the operational level: full merge without conflict preservation would be architecturally reckless (conflicts would be suppressed or blocking); conflict preservation without full merge would be underused (the primary conflict-generation mechanism would be restricted by default).

**D1.03 (Aspect as the Unit of Exchange).** Full merge operates over aspects. The content that is fully merged — the DNA-layer and action-layer content that is combined within the shared substrate — is surfaced by aspects. D1.08 inherits D1.03's commitment to aspect-level granularity: full merge is full at aspect granularity, not at cell granularity (too small) or at whole-Self granularity (architecturally incoherent given Selves are governance-distinct entities).

**D1.07 (Governance Configuration Scope).** The governance configuration capability that D1.07 establishes is the mechanism through which the full-merge default can be overridden. Sharing-scope configuration determines what enters the shared substrate; merge-pattern configuration determines how what has entered is combined. D1.08's default is the starting point for D1.07's governance deliberation.

**Paper 3 Claim 5 (Sharing-Scope and Merge-Pattern Configuration).** The governance configuration authority that enables alternative merge patterns is formalized in Claim 5 and its D-series notes. D1.08 is the default commitment against which Claim 5's configurability is exercised.

---

## 10. Summary

D1.08 formalizes the full-merge default as an architectural commitment within FAI's operation over the shared substrate. Full merge — the complete combination of all contributed aspects' DNA-layer and action-layer content within the shared substrate — is the operation that occurs absent governance configuration specifying an alternative merge pattern. The default is a positive design choice, not a residual; it encodes the presumption that combination serves the coordination objective and that restriction requires governance authorization.

The default is not a mandate. Governance retains full authority to configure sharing scope (which aspects are contributed) and merge pattern (how contributed aspects are combined). Neither full merge nor alternatives are prohibited; the architecture establishes full merge as the starting point from which governance may depart.

Three architectural consequences follow from the full-merge default: maximum information availability within the shared substrate, conflict preservation as the mechanism handling all merge-generated conflicts, and human governance as the operative restriction authority. All three are prior-art commitments with significance in the CKS architecture.

Full merge as the FAI default is the inter-Self analog of Paper 2's union mating pattern at intra-Self scope. The T1.05 disambiguation establishes the precise inheritance: same merge primitive, same three pattern variants, same conflict preservation response, extended to inter-Self scope. The specific commitment that is fresh at inter-Self scope is the naming of full merge as the default — a commitment Paper 2 does not make among its three pattern variants at intra-Self scope.

D1.08 defends against four failure modes: mandatory-full-merge misreading, no-merge-default architectures, infrastructure-determined merge, and full-merge-as-novel at inter-Self scope. The operational test provides four verifiable conditions for confirming that D1.08 is instantiated in a deployed FAI event.

---

*End of Derivation Note D1.08.*
