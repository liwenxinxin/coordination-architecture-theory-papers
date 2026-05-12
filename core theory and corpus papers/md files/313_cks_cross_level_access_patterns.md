# Cross-Level Access Patterns: Operational Guidance for Governed Inter-Level Interaction in CKS Deployments

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It does not introduce new axioms. Its contribution is to formalize, from the cross-level access commitment established in B1.19, the operational patterns by which governed cross-level interaction is applied in CKS deployments. This is the ninety-sixth note in Phase B2 of Series B and the third of four notes decomposing the B1.19 cross-level access commitment, following B2.94 (cross-level access integrating frame) and B2.95 (cross-level access governance).

## Abstract

The Coordination Knowledge Substrate (CKS) architecture establishes cross-level access as a governed inter-level interaction mechanism: higher levels operate over lower levels as content domain, with access governed through access rules per B2.95 and authority distribution per A2.47. B1.19 specifies that cross-level access is available; B2.95 specifies how it is governed. What remains is the operational dimension: when governed cross-level access is used, which patterns does it take? This note formalizes seven cross-level access patterns as the primary operational approaches for inter-level interaction in CKS deployments. Four are downward-access patterns (Self governance over aspects; aspect coordination over cells; expression mechanism per B2.30; governance override per A2.03). Two are upward-access patterns (operational result reporting; vertical evolution upward per B1.16). One is a downward-propagation pattern for evolution (vertical evolution downward per B1.16). Cross-pattern combinations are common in mature deployments; pattern selection is governed by authority distribution per A2.47. The expression mechanism pattern (Pattern 3) is architecturally distinctive — it is a pre-architected governed downward access path from Self DNA to cell behavior with no equivalent in conventional multi-component AI architectures. The patterns are operational guidance, not architectural requirements; the same governance framework per B2.95 applies to all of them.

## 1. Why cross-level access patterns requires standalone formalization

The B1.19 cross-level access commitment establishes that higher levels access lower levels as content domain and that access patterns are not strictly hierarchical — the Self can access cells directly when purpose requires. B2.95 establishes the governance framework through which that access is authorized, recorded, and overridable. Both commitments are necessary. Neither, on its own, answers the operational question: when cross-level access is used in practice, what does it look like?

The operational question matters for two reasons. First, deployments that implement CKS cross-level access need more than a governance framework — they need to recognize which interaction approaches are architecturally coherent and which combinations are expected. Without named patterns, the variety of cross-level interaction approaches is implicit, undifferentiated, and difficult to govern consistently. Named patterns give governance something concrete to configure access rules around. Second, the expression mechanism pattern (Pattern 3) is architecturally distinctive enough to warrant explicit prior-art formalization in its own right. It is a pre-architected governed downward access path from Self DNA to cell behavior — a design commitment with no recognized equivalent in conventional AI multi-component systems. Naming it as a pattern establishes the prior-art record for that specific architectural move.

This note formalizes the seven primary patterns. Together with B2.94 (integrating frame) and B2.95 (governance framework), they complete the operational characterization of cross-level access. B2.97 (cross-level access verification) will close the B1.19 decomposition.

## 2. The seven patterns precisely stated

Cross-level access patterns are the operational approaches by which governed cross-level interaction is applied. All patterns use the governance framework established in B2.95; patterns do not modify that framework. All pattern use is subject to authority distribution per A2.47 — not all entities hold authority for all patterns. The seven primary patterns are grouped by direction.

### Downward access patterns

**Pattern 1 — Self governance over aspects.** The Self-level entity accesses aspects to perform governance operations over integration behavior. Governance acts that instantiate this pattern include: aspect configuration review; authorization of aspect DNA changes per the DNA evolution mechanism (B1.14); and aspect lifecycle decisions — aspect birth, aspect mating, and aspect death per the lifecycle primitives that apply at every level (Paper 2, §6). This pattern is the architectural mechanism by which Self-level authority over the structural arrangement of aspects is exercised in practice. The Self integration architecture (B2.21) specifies which governance operations the Self performs; Pattern 1 names the cross-level access modality through which those operations reach aspects.

**Pattern 2 — Aspect coordination over cells.** An aspect-level entity accesses cells to organize their operational behavior within the aspect's purpose domain. Coordination acts include: invoking cells in accordance with coordination rules (B2.16); integrating cell outputs into aspect-level results; and handling cell-level conflicts in accordance with the aspect's conflict rules. Because cells can participate in multiple aspects simultaneously through relational role membership (B2.14), aspect coordination accesses cells in the context of a specific aspect arrangement without modifying cell membership in other arrangements. Pattern 2 is the normal operational modality through which aspect-level purpose is achieved.

**Pattern 3 — Expression mechanism downward per B2.30.** Self DNA affects cell behavior through the expression mechanism. This is the most architecturally specific downward access pattern: Self DNA activates and deactivates cell DNA elements through harness substrate configuration, determining which sub-substrates are active for current cell activity. The harness substrate is itself human-governed, fully inspectable, modifiable, and overridable. Pattern 3 is governed through Self DNA rules and recorded through the provenance mechanisms per A2.40. The pattern's distinguishing property is its directedness: it is not ad hoc downward influence but a pre-architected governed channel from Self DNA to cell behavior. §3 of this note returns to what makes Pattern 3 architecturally distinctive relative to conventional systems.

**Pattern 4 — Governance override downward per A2.03.** Higher-level entities exercise override rights over lower-level decisions. The Self may override aspect coordination decisions; aspects may override cell operational decisions. Override is a right preserved at all times per the human-governed commitment (A1.01) and the authority architecture that A2.03 establishes. Override pattern events are governed and recorded per A2.40. Pattern 4 is distinct from Pattern 1 (Self governance over aspects) in that override is an intervention into an already-operating lower-level process, not a governance act over aspect structure. Override may be triggered by inspection of upward reporting (Pattern 5); the combination is addressed in §2.5.

### Upward access patterns

**Pattern 5 — Operational result reporting upward.** Cells report operational results to aspects; aspects report operational outcomes to Selves. Reporting enables aspect-level and Self-level visibility into lower-level operations without requiring the higher-level entity to inspect lower-level substrate directly. Reporting is part of the normal operational flow: cells complete tasks, results flow upward, and aspects integrate them into purpose-level outputs that flow to the Self. The reporting mechanism is the primary channel through which the Self and aspects maintain operational situational awareness.

**Pattern 6 — Vertical evolution upward per B1.16.** Cell-level improvements inform aspect evolution; cell action-layer evidence informs aspect action-feedback proposing substrates per B1.15. This pattern carries improvement information from lower to higher levels through cross-level access. It is the upward dimension of the bidirectional vertical evolution commitment (B1.16): structural reorganization does not flow only from above; evidence and capability developments at lower levels propagate upward and inform governed decisions about higher-level structure. Cross-level access is the operational substrate through which that propagation occurs.

**Pattern 7 — Vertical evolution downward per B1.16.** Self and aspect evolution propagates downward to cell level. Self DNA changes affect cell behavior through the expression mechanism (Pattern 3 combined with evolutionary change). Aspect coordination rule changes affect cell participation within the aspect. This pattern is the downward dimension of bidirectional vertical evolution: when the Self or an aspect evolves its structural arrangement or DNA content, the effects reach cells through governed downward access. Pattern 7 and Pattern 6 jointly constitute the operational substrate for bidirectional evolution per B1.16.

### Cross-pattern interactions

Patterns may and frequently do combine in practice. Governance override (Pattern 4) typically follows inspection of upward reporting (Pattern 5): the Self or aspect receives an operational report, assesses it, and exercises an override if appropriate. Vertical evolution (Patterns 6 and 7) uses both reporting (Pattern 5) to carry evidence upward and expression (Pattern 3) to propagate structural changes downward. Mature deployments that are actively evolving will have Patterns 5, 6, and 7 operating concurrently as a coordinated vertical evolution cycle, with Patterns 1 and 2 operating as the governance and coordination background against which evolution proceeds.

### Pattern selection and authority distribution

Pattern selection in a deployment follows authority distribution per A2.47. Authority for Pattern 1 rests with the Self; authority for Pattern 2 rests with aspects; authority for Pattern 3 is governed through Self DNA rules; authority for Pattern 4 is distributed per the override authority architecture of A2.03; authority for Pattern 5 is distributed to the reporting entities (cells upward to aspects, aspects upward to the Self); authority for Patterns 6 and 7 is governed as part of vertical evolution governance per B1.16. Cross-partner access patterns in multi-Self deployments require cross-partner authority specification per A2.47.

## 3. What makes cross-level access patterns architecturally distinctive

Conventional AI multi-component architectures have inter-component communication — agents call tools, orchestrators route to agents, components pass messages or share state. In these architectures, inter-component communication patterns are implicit: they follow from the routing logic, the API contracts, or the message-passing infrastructure, but they are not named as a governed set of patterns with authority conditions and provenance requirements.

CKS cross-level access patterns are explicit, enumerated, and governance-governed. Each pattern has a named directionality, a named authority condition (which level or entity holds authority for the pattern), and a named recording requirement per A2.40. The enumeration is not exhaustive — deployments may use patterns not listed here — but the named patterns are architecturally grounded in Paper 2's commitments and constitute prior art for the specific interaction approaches they describe.

Pattern 3 is particularly distinctive. The expression mechanism — Self DNA activating and deactivating cell DNA elements through harness substrate configuration — is a pre-architected governed downward access channel from Self DNA to cell behavior. No conventional multi-component AI architecture has an equivalent: the standard downward influence mechanism in such architectures is prompt engineering or configuration injection, neither of which is a governed substrate-content channel with full provenance. Pattern 3 names a specific architectural commitment — governed behavioral influence from a higher-level substrate to a lower-level substrate — that has no clean analog in the contemporary field.

## 4. The biological analog as conceptual scaffold

The seven patterns parallel the different types of biological inter-level signaling. Hormonal signals provide broad downward influence from a systemic level to distributed cellular behavior — the Pattern 3 analog, where Self DNA affects cell behavior through a governed broadcast mechanism. Cell-to-tissue signaling carries operational results from cellular activity upward to tissue-level coordination — the Pattern 5 analog. Tissue-level developmental governance organizes cell populations for purpose-defined morphological goals — the Pattern 1 and 2 analog. Evolutionary information flows both upward (cellular adaptation informing organismal fitness) and downward (developmental programs encoding evolutionary history into cell behavior) — the Pattern 6 and 7 analog.

CKS patterns are more explicit and governed than their biological counterparts. Biological inter-level signaling is the product of evolutionary selection; its authority architecture is implicit in molecular machinery and developmental programs. CKS patterns are deliberately architected, explicitly named, and governed through the access rule framework per B2.95. The biological analog functions as conceptual scaffold — it explains why multiple distinct patterns are needed (different inter-level interaction purposes require different directional and temporal properties) — not as architectural specification. The architectural substance is the seven governed operational patterns, not the biological parallel.

## 5. Inherited Paper 1 commitments

Cross-level access patterns inherit all Paper 1 commitments through the recursive levels principle: Paper 1's commitments hold at each level — cell, aspect, Self — without modification.

**A1.01 (human-governed)** is the foundation: all seven patterns are governed, and the human authority to inspect, modify, and override any cross-level access event is preserved at all times. Governance is an authority architecture (A1.01), not a review workflow; patterns do not change what governance means.

**A2.47 (authority distribution)** governs pattern selection: which entities hold authority for which patterns determines which patterns are operationally available to which actors in a deployment. Cross-partner authority for multi-Self deployments is specified per A2.47.

**A2.40 (provenance)** requires that pattern events be recorded: cross-level access events, override acts, reporting flows, and evolution propagations all generate provenance records traceable through the substrate.

**B2.30 (expression mechanism)** is directly instantiated by Pattern 3: the harness substrate as expression governor is the architectural mechanism through which Pattern 3 operates.

**B1.16 (bidirectional evolution)** is directly instantiated by Patterns 6 and 7: vertical evolution in the CKS sense requires both upward information propagation from cells to higher levels and downward structural propagation from higher levels to cells; the patterns name the cross-level access modalities through which that bidirectionality is achieved.

**A2.03 (override right)** is directly instantiated by Pattern 4: the governance override downward pattern is the operational form of the override right A2.03 establishes.

## 6. Operational implications

Several implications follow from the seven-pattern enumeration for deployments implementing CKS cross-level access.

Deployments should recognize which patterns are in use and configure access rules accordingly per B2.95. A deployment in which aspects coordinate over cells (Pattern 2) but aspects do not report upward to the Self (Pattern 5) is architecturally coherent but has reduced Self-level operational visibility; the deployment should configure its governance accordingly. Pattern documentation within a deployment helps governance personnel understand the cross-level interaction design and exercise override rights appropriately.

Pattern combinations are common in mature deployments. A deployment actively evolving its structure will have Patterns 5, 6, and 7 operating as a vertical evolution cycle, with Pattern 1 governing structural changes at the Self-aspect boundary. Governance that understands these combinations can anticipate the cross-level access events that normal operations generate and distinguish them from anomalous access.

Vertical evolution patterns (6 and 7) are particularly important for deployments in active structural evolution. These patterns make cross-level access the operational substrate for the bidirectional evolution B1.16 establishes. Deployments that do not configure cross-level access for vertical evolution patterns will find that structural evolution requires out-of-band mechanisms rather than governed substrate operations.

Cross-partner access patterns in multi-Self deployments require cross-partner authority specification per A2.47. The patterns enumerated here apply within a single Self's governance perimeter; the extension to inter-Self access is addressed in Paper 3's territory.

## 7. Limits

The seven patterns are operational guidance, not architectural requirements. Deployments may use patterns not listed; the enumeration is illustrative of the primary patterns that Paper 2's commitments generate and authorize, not a closed specification of every legitimate cross-level interaction approach. Pattern selection is deployment judgment, not architectural prescription.

Pattern enumeration does not change the underlying access governance per B2.95. All seven patterns use the same governance framework: access is governed, provenance is recorded, override rights are preserved. Naming a pattern does not make the access it describes automatic, ungoverned, or lower-cost — all access remains governed per B2.95 regardless of which pattern it instantiates.

The patterns are not mutually exclusive. Multiple patterns operate concurrently in a functioning deployment. Pattern 1 (Self governance over aspects) and Pattern 5 (operational result reporting upward) operate simultaneously as a matter of course; Pattern 2 (aspect coordination over cells) and Pattern 3 (expression mechanism downward) may operate simultaneously when aspect coordination invokes cells whose active DNA elements are determined by expression. Concurrency is normal; the patterns provide a vocabulary for naming what is happening, not a sequencing constraint on what can happen.

Finally, the biological analog is scaffolding, not specification. CKS inter-level signaling is more explicit, more governed, and more deliberately architected than biological inter-level signaling. The analog is useful for explaining why multiple directional patterns are needed; it does not impose any biological constraint on CKS architectural design.

## 8. Operational test

A CKS deployment instantiates cross-level access patterns if and only if all of the following are true:

1. Downward access by higher-level entities over lower-level content occurs through named, governance-authorized modalities — Self governance over aspects (Pattern 1), aspect coordination over cells (Pattern 2), or expression mechanism (Pattern 3) — and not through implicit routing that bypasses access governance per B2.95.
2. Governance override (Pattern 4) is available at any time to higher-level entities over lower-level decisions, with override events recorded per A2.40.
3. Cells and aspects produce operational result reports that flow upward to higher-level entities (Pattern 5), with reporting governed and accessible to humans exercising inspect rights per A1.01.
4. Vertical evolution information (Pattern 6) and structural propagation (Pattern 7) flow through cross-level access subject to the same governance framework as all other patterns — not through out-of-band mechanisms that bypass access governance.
5. Pattern selection follows authority distribution per A2.47: no entity exercises a pattern for which it does not hold authority.
6. The expression mechanism (Pattern 3) operates through harness substrate configuration that is human-governed, fully inspectable, modifiable, and overridable.

A deployment that routes inter-level interaction through implicit channels that bypass access governance, or that treats vertical evolution as an out-of-band structural operation rather than a governed cross-level access event, does not instantiate cross-level access patterns in the CKS sense.

## 9. Conclusion

Cross-level access in CKS is governed (per B2.95) and available across non-strictly-hierarchical level relationships (per B1.19). What this note adds is the operational layer: when governed cross-level access is used in practice, it takes one or more of seven named patterns. The patterns are grounded in Paper 2's architectural commitments, carry all Paper 1 governance properties through the recursive levels principle, and are subject to authority distribution per A2.47.

Naming the patterns as standalone prior art matters for three reasons. It establishes that the expression mechanism (Pattern 3) — a pre-architected governed downward channel from Self DNA to cell behavior — is a specific CKS architectural commitment, not an incidental implementation detail. It establishes that vertical evolution (Patterns 6 and 7) uses cross-level access as its operational substrate, so that bidirectional evolution per B1.16 is not merely a property of the architecture's intent but of its operational mechanics. And it provides deployments with a governance vocabulary for configuring, documenting, and auditing cross-level interactions.

This note is the third of four decompositions of B1.19 (B2.94 integrating frame; B2.95 access governance; B2.96 this note; B2.97 cross-level access verification). B2.97 will complete the B1.19 decomposition. Subsequent Phase B2 notes (B2.98 onward) will decompose the B1.20 recursive Paper 1 commitments, completing Phase B2.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Level Access Patterns: Operational Guidance for Governed Inter-Level Interaction in CKS Deployments.* May 12, 2026. ORCID: 0009-0004-8065-3235.
