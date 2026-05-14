# Three-Tier Conflict Handling as Paper 3's Third Architectural Claim

**Series:** CKS Derivation Note Series — Phase D0 (Paper 3 Claim Anchors)
**Note ID:** D0.03 · **Series Number:** #462
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3's third architectural claim establishes the three-tier inter-Self conflict-handling mechanism — preserve, resolve via orchestration, escalate to humans — over the shared substrate. This derivation note anchors that claim, states each tier with its architectural content, and makes explicit the inheritance framing that is the prior-art core: the three-tier mechanism is not new architectural commitment. It is what Papers 1 and 2's conflict-handling principles produce when extended to the inter-Self scope. Tier 1 (preserve) inherits Paper 1 Claim 2's substrate-level conflict preservation and carries through to home-substrate annotations at dissolution. Tier 2 (resolve via orchestration) inherits Paper 1's cell-level orchestration-rule resolution as extended through Paper 2's intra-Self conflict handling. Tier 3 (escalate to humans) inherits Paper 1 Claim 3's human-governed final authority, with the cross-perimeter shape — escalation surfacing to the joint-governance arrangement of all participating Selves' home governance structures — as the genuinely fresh tier shape. The note maps the trilogy's conflict-handling progression, names the four failure modes the claim defends against, maps derived sub-commitments D1.13–D1.16, and provides an operational test.

---

## 1. Claim 3 Stated

Claim 3 of Paper 3 establishes the **three-tier inter-Self conflict-handling mechanism** operating within the shared substrate during Full Aspect Integration (FAI) events. The three tiers are:

- **Tier 1 — Preserve:** When the task does not require conflict resolution, conflicts surfaced during FAI are preserved within the shared substrate as first-class addressable state. Both sides of the conflict are retained. No auto-resolution occurs.
- **Tier 2 — Resolve via orchestration:** When prebuilt orchestration logic exists for the conflict class, the orchestration rules within the shared substrate determine the response. The rules are substrate content — human-authored under joint authority across participating Selves' governance, inspectable, and modifiable.
- **Tier 3 — Escalate to humans:** For conflicts that no orchestration logic resolves, the conflict surfaces to humans holding governance authority over the relevant participating Selves. This escalation crosses home perimeter boundaries: it is an inter-organizational governance event.

The tier-decision logic — the determination of which tier applies to a given conflict — operates through orchestration substrate that is itself substrate content under joint authority. Conflict tiers are not assigned by LLM inference; they are governed outcomes of authored rules. Actor-neutrality holds throughout: Selves do not "resolve conflicts," "negotiate," or "arbitrate" in the architectural register. Conflict resolution is the result of orchestration rules under joint authority, with LLMs operating as substrate mediators executing those rules.

---

## 2. Inheritance Framing: Not New Architecture

The prior-art core of this note is the inheritance framing. Paper 3 Claim 3 does not introduce new conflict-handling architecture. It states what Papers 1 and 2's conflict-handling principles produce when extended to the inter-Self scope. Every tier maps directly to prior commitments:

| Tier | Paper 3 form | Inheritance source |
|---|---|---|
| Tier 1 — Preserve | Conflicts in shared substrate preserved as first-class state | Paper 1 Claim 2: substrate-level conflict preservation as architectural default |
| Tier 2 — Resolve via orchestration | Orchestration rules within shared substrate as governed resolution | Paper 1 cell-level conflict resolution under human-authored orchestration rules; Paper 2 intra-Self conflict resolution at all three levels |
| Tier 3 — Escalate to humans | Unresolvable conflicts surface to governance of participating Selves | Paper 1 Claim 3: humans hold final authority; cross-perimeter shape is the one fresh element |

This mapping closes the adversary gap before it opens. An adversary claiming that the three-tier mechanism is novel relative to prior work faces the inheritance table above: tier 1 is Paper 1 Claim 2 applied at inter-Self scope; tier 2 is Paper 1's orchestration-rule resolution applied at inter-Self scope via Paper 2's recursive extension; tier 3 is Paper 1 Claim 3 applied at inter-Self scope with the cross-perimeter shape added. Fresh content is precisely localized to three loci: (a) the inter-Self specification of each tier, (b) the joint-authority shape of tier 3's escalation path, and (c) the substrate-content character of tier-decision logic at the shared-substrate level. Everything outside those three loci is inheritance that Claim 3 articulates rather than commitment that Claim 3 introduces.

The calibration register Paper 3 names for Claim 3 is **principles-extending**: the claim extends established principles to a new scope rather than defending fresh mechanism or completing the trilogy. This register guards against two implicit failure modes. The under-claim treats Claim 3 as nothing more than re-citation of Paper 1 §5.3 at bigger scope, with inter-Self specification dissolving into bookkeeping. The over-claim treats Claim 3 as free-standing conflict-handling architecture competing with Paper 1 §5.3. The inheritance framing navigates between them: the extension is real (inter-Self scope is new), and it is not a new architectural commitment (the extension is fully derivable from what Papers 1 and 2 commit to).

---

## 3. The Trilogy's Conflict-Handling Progression

Conflict handling across the trilogy is one architectural commitment — preserve conflicts as first-class state, govern their resolution under human-authored rules — extended to progressively larger coordination scopes:

**Paper 1 — Two-level (within-cell):** Conflict-as-first-class (Claim 2) establishes substrate-level conflict preservation as the architectural default within a cell. Both sides of any conflict are retained as addressable substrate state; no auto-resolution collapses the conflict. Resolution, when it occurs, operates at cell level under orchestration rules that humans author. The "humans decide resolution logic, not the LLM" axis is the governing commitment at this scope.

**Paper 2 — Recursive application at three levels (within-Self):** Paper 2 extends Paper 1's two-level conflict structure to all three levels within a Self — cell scope, aspect scope (cross-cell conflicts), and Self scope (cross-aspect conflicts). The A1.03 conflict registry applies at every level. The extension is recursive: the same preserve-then-resolve-under-rules architecture repeats at each level of composition within the Self.

**Paper 3 — Three-tier at the inter-Self boundary:** Claim 3 extends conflict handling across the inter-Self perimeter. The shared substrate is the locus. FAI events surface conflicts across participating Selves' contributed aspects. The three tiers are the inter-Self form of the same architectural commitment — preserve as default, govern resolution by authored rules, surface to human authority where rules do not resolve. The third tier adds the cross-perimeter escalation shape that the inter-Self scope requires.

The trilogy-level pattern that cks_trilogy_ambiguity_map.md T1.06 names is: same commitment, larger scope at each paper. The unifying claim is that conflict handling across the trilogy is one architecture, not three. Paper 3 Claim 3 is the third term in a series whose first two terms Papers 1 and 2 already establish.

---

## 4. Tier 1 — Preserve: Architectural Content and Carry-Through

The preserve tier is the architectural default. When a conflict surfaces during an FAI event, the default response is preservation — not resolution, not filtering, not deferral to LLM judgment. Both sides of the conflict become first-class addressable substrate objects within the shared substrate, with the divergence point identified and provenance attached.

Preservation is not passive holding. The conflict object carries enough information for a human or an orchestration rule to act on it: both contributing positions, their provenance (which Self contributed which side), and the nature of the divergence. The preserved conflict is inspectable, modifiable, and subject to the three governance rights — inspect, modify, override — that Paper 1 Claim 3 commits to at every level of the architecture.

Tier 1 carries a property that extends beyond the FAI event's duration. When the shared substrate dissolves at the close of an FAI event, preserved conflicts do not simply disappear. They propagate as **evolution-feed annotations** within each participating Self's home substrate, under governance-configured ingestion at the home perimeter (Paper 3 Claim 4's mechanism). Within each home substrate, the annotation flags a boundary that home governance must address under home authority during evolution-mechanism operation. Whether that home governance treats the boundary as a place to do further work, a place to leave the divergence in place, or a place to escalate within the Self's own governance structure is determined by home authority — not by the FAI event architecture.

This carry-through property is part of Tier 1's architectural content, not a downstream consequence belonging to a different claim. The preserved conflict travels: from shared substrate during FAI → to home substrate as annotation at dissolution → to home-governance agenda under home authority thereafter. The path is traceable, the annotation is substrate content, and the authority over it passes cleanly to home governance at the perimeter crossing.

---

## 5. Tier 2 — Resolve via Orchestration: Authored Rules as Substrate Content

The resolve tier applies when prebuilt orchestration logic exists for the conflict class. The orchestration rules within the shared substrate determine the response. Two properties of these rules are architecturally load-bearing.

First, the rules are **substrate content**. They are not compiled into the coordination infrastructure, not embedded in LLM inference, not stored in opaque middleware. They are authored as content within the shared substrate — inspectable, modifiable, and subject to the same three governance rights that apply to all other substrate content. An observer who can read the shared substrate can read the orchestration rules. The rules are not hidden.

Second, the rules are authored under **joint authority across participating Selves' governance**. Because the shared substrate spans the home governance perimeters of multiple Selves, the orchestration rules within it are not unilaterally authored by one Self. They are authored under the joint-authority arrangement that governs the shared substrate's content generally. This means that Tier 2 resolution is governed resolution — the authority over what the rules say is distributed across the organizations whose Selves participate. No single Self's governance unilaterally determines how inter-Self conflicts of a given class resolve.

The actor-neutrality discipline holds at this tier. Tier 2 does not make Selves capable of resolving conflicts. It makes *rules* capable of governing conflict resolution, with LLMs operating as substrate mediators executing those rules under human authority over the rules themselves.

---

## 6. Tier 3 — Escalate to Humans: The Cross-Perimeter Governance Event

The escalate tier applies when no orchestration logic resolves the conflict. The conflict surfaces to humans. Tier 3's form in Paper 3 differs from Paper 1's escalation pattern in one precisely delimited way: **the escalation crosses home perimeter boundaries**.

In Paper 1, escalation operates within a single Self's governance structure — a conflict that no cell-level rule resolves surfaces to the humans who govern that substrate. In Paper 3, the escalation involves at minimum two organizations: the conflict surfaces to the joint-governance arrangement of the participating Selves' home governance structures. The humans who receive the escalation hold governance authority over the participating Selves — not over one Self's substrate, but over the relationship between Selves as expressed through the shared substrate they jointly govern.

This cross-perimeter property has three architectural consequences. First, the escalation path must be pre-established within the shared substrate's joint-governance arrangement before the FAI event begins — the humans who hold escalation authority are identified in the configuration substrate, not discovered at escalation time. Second, the escalation event is itself a substrate-auditable occurrence: it is recorded within the shared substrate as a governance event with provenance, not simply a notification to external parties. Third, the resolution that follows the escalation — whatever the humans with joint authority determine — re-enters the substrate as authored content, maintaining the substrate-as-coordination-artifact commitment at the escalation tier.

Tier 3 inherits Paper 1 Claim 3 (humans hold final authority where no automated resolution is permitted) and extends that commitment to the inter-Self scope by adding the cross-perimeter escalation path. The inheritance is direct; the cross-perimeter shape is what the inter-Self scope requires and what is genuinely fresh at this tier.

---

## 7. Four Failure Modes the Claim Defends Against

Claim 3 defends against four named failure modes:

**1. Silent conflict resolution at inter-Self scope.** Conflicts arising during FAI are auto-resolved at the merge point — filtered, collapsed, or averaged — without first-class preservation. The conflict's information content is lost; neither the divergence point nor the contributing positions survive in the substrate. Claim 3 forecloses this by making preservation the architectural default at Tier 1, with both sides of any conflict retained as addressable substrate state.

**2. Ungoverned conflict resolution.** Orchestration logic exists for a conflict class, but the rules are not substrate content — they are embedded in LLM inference, compiled into middleware, or otherwise not accessible to the three governance rights. Claim 3 forecloses this by requiring that Tier 2 orchestration rules be authored substrate content under joint authority, inspectable and modifiable on the same terms as any other substrate content.

**3. Missing escalation path.** For conflicts beyond orchestration capacity, no defined path to human authority exists — the conflict stalls, is silently dropped, or is resolved by LLM inference in the absence of a governed path. Claim 3 forecloses this by requiring Tier 3 as an architectural commitment: the escalation path to humans holding governance authority over the participating Selves is pre-established, not improvised.

**4. Tier conflation.** Preserve and resolve are treated as the same operation — preservation is understood as "temporary holding pending resolution," with resolution as the eventual destination for all conflicts. Claim 3 forecloses this by specifying preservation as a terminal state for any conflict where the task does not require resolution. A conflict that the shared substrate carries through FAI dissolution and delivers to home substrates as an annotation has been fully handled by Tier 1; resolution is not a deferred requirement.

---

## 8. Derived Sub-Commitments D1.13–D1.16

Claim 3 generates four derived sub-commitments in the Phase D1 series:

**D1.13 — Preserve tier as substrate-level conflict preservation at inter-Self scope.** Conflicts surfaced during FAI events within the shared substrate are preserved as first-class addressable state by architectural default, with both contributing positions retained, divergence point identified, and provenance attached. This sub-commitment is the direct inter-Self application of Paper 1 Claim 2's conflict-as-first-class principle.

**D1.14 — Resolve-via-orchestration tier: orchestration rules within shared substrate as governed conflict resolution.** When prebuilt orchestration logic exists for a conflict class, the conflict is resolved by orchestration rules that are themselves substrate content authored under joint authority across participating Selves' governance. Inspectability and modifiability of the rules under the three governance rights are requirements, not options. This sub-commitment inherits Paper 1's cell-level conflict resolution and Paper 2's intra-Self multi-level extension.

**D1.15 — Escalate-to-humans tier: human-governance commitment at inter-Self scope as cross-perimeter governance event.** For conflicts no orchestration logic resolves, the escalation path surfaces to humans holding governance authority over the participating Selves, crossing organizational perimeter boundaries. The escalation-receiving humans are identified in joint-governance configuration before the FAI event begins. This sub-commitment inherits Paper 1 Claim 3 and extends it with the cross-perimeter shape.

**D1.16 — Conflict carry-through to home evolution.** Preserved conflicts travel from the shared substrate to each participating Self's home substrate as evolution-feed annotations at FAI dissolution, under governance-configured ingestion at the home perimeter. The annotations flag boundaries that home governance must address under home authority. This sub-commitment is part of Tier 1's architectural content, not a downstream consequence of a separate mechanism; it is the path by which the three-tier mechanism connects to each Self's ongoing governance work within its home substrate.

---

## 9. Operational Test

A shared substrate during an FAI event instantiates the three-tier conflict-handling mechanism if and only if all of the following are true:

1. **Tier determination is observable.** For any conflict in the shared substrate, an observer with read access can determine which tier applies — whether the conflict is being preserved (Tier 1), being resolved by orchestration rules (Tier 2), or has been escalated to human governance (Tier 3). The determination is not inferred from LLM output; it is readable substrate state.

2. **Tier 2 rules are locatable as substrate content.** For any conflict handled at Tier 2, the orchestration rules governing the resolution are locatable within the shared substrate as authored content — inspectable by any participant with read access, modifiable under joint authority, not embedded in middleware or LLM inference in a form inaccessible to the governance rights.

3. **Tier 3 escalation is traceable to joint human governance authorization.** For any conflict escalated at Tier 3, the escalation path is traceable to humans holding governance authority over the participating Selves, and the joint-authority arrangement that identifies those humans is pre-established within the shared substrate's configuration content — not determined at escalation time. The escalation event is recorded as auditable substrate content.

4. **Tier 1 carry-through is traceable to home substrate annotations.** For any conflict preserved at Tier 1 and carried through FAI dissolution, the annotation within each participating Self's home substrate is traceable to the original preserved conflict in the shared substrate, with provenance intact across the perimeter crossing.

5. **Preservation is the default, not an exception.** A conflict for which no Tier 2 orchestration rule exists and no Tier 3 escalation has been initiated is preserved at Tier 1, not silently resolved, filtered, or dropped. The default direction is toward preservation, not resolution.

A system that fails any of (1)–(5) may handle conflicts in some fashion, but does not instantiate Paper 3 Claim 3's three-tier mechanism.

---

## 10. Conclusion

Paper 3 Claim 3 extends the trilogy's conflict-handling architecture to the inter-Self boundary. The three tiers — preserve as first-class state, resolve by authored orchestration rules, escalate to humans holding joint governance authority — are the form that Papers 1 and 2's conflict-handling principles take at inter-Self scope. The inheritance is direct and complete at Tiers 1 and 2; Tier 3 adds only the cross-perimeter escalation shape that the inter-Self scope requires.

Three architectural properties distinguish Claim 3's conflict-handling from approaches its failure modes describe: preservation is the default (not resolution), orchestration rules are substrate content under joint authority (not hidden), and escalation is a pre-authorized cross-perimeter governance event (not improvised). Together, these properties make conflict handling at the inter-Self boundary as governed and auditable as conflict handling within a single Self.

Downstream derivation work proceeds from D1.13–D1.16 into Phase D2 operational variants. The anti-pattern formalizations for Claim 3 (silent conflict resolution at inter-Self scope; ungoverned orchestration rules; missing escalation path; tier conflation) proceed in Phase D3.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Three-Tier Conflict Handling as Paper 3's Third Architectural Claim.* CKS Derivation Note D0.03, Series #462. May 14, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
