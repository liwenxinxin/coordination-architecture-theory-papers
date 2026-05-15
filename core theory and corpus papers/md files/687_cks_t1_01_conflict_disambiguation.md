# Disambiguating "Conflict" Across the Trilogy

**Series T — Trilogy-Wide Ambiguity Reduction | Note T1.01 | Note #687**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in precise operational form, the scope-specific meanings of the term *conflict* as used across all three papers, to establish that the same architectural concept underlies all three usages, and to foreclose adversarial attempts to treat any one paper's usage as independently novel.

---

## Abstract

The term "conflict" appears in all three papers of the CKS trilogy as a core governance concept. Across those three appearances, the word carries one constant architectural commitment — governance specification incompatibility is a first-class state that must be preserved, not silently resolved — and three different scope applications: intra-cell rule incompatibility in Paper 1, intra-Self mating incompatibility in Paper 2, and inter-Self approach incompatibility in Paper 3. The resolution mechanisms differ across the three papers because the governance authority structure differs, not because the underlying concept of conflict differs. This note states the concept identification, maps the scope-specific usages across all three papers, makes the disambiguation precise, and specifies the prior-art coverage the disambiguation provides.

---

## 1. Concept Identification

**Term:** "Conflict" / "governance conflict"

**Status:** Core governance concept used in all three papers with a consistent underlying principle and three scope-specific applications.

**The constant:** At every scope, conflict names a state in which two or more governance specifications are incompatible with each other. The architectural response is constant: conflicts are preserved as first-class substrate state; neither side is automatically discarded; resolution occurs under human-governed orchestration rules.

**What varies:** The type of incompatibility (rule-level versus approach-level), the number of governance authorities involved (one versus two or more), and the resolution mechanism available (directed selection versus multi-tier escalation). None of these variations changes the concept itself.

---

## 2. Paper 1 Usage — Intra-Cell Rule Incompatibility

In Paper 1, "conflict" refers to intra-cell conflicts: cases where two or more orchestration rules within a single cell's substrate produce incompatible outputs for the same governance situation.

Paper 1 Claim 2 establishes conflict as a **first-class governance state**. Both sides of the conflict are preserved as substrate content; neither side is automatically discarded or silently resolved. This is the architectural move that distinguishes the CKS pattern from detect-resolve-forget architectures, in which conflicts are resolved immediately and no persistent record of the conflict itself is retained.

Conflict detection at Paper 1 scope is part of the cell's ongoing governance monitoring. Resolution occurs through **directed selection**: governance reviews the conflict, decides which rule to modify or which interpretation to authorize, and records the resolution in the substrate. The resolution is itself substrate content, subject to the three governance rights (inspect, modify, override). One governance authority is involved — the human governance of the cell.

The scope constraint is precise: Paper 1 conflict is internal to one cell, under one governance authority, within one substrate. This is the foundational scope from which Papers 2 and 3 extend.

---

## 3. Paper 2 Usage — Intra-Self Mating Incompatibility and Cross-Tier Conflicts

Paper 2 retains Paper 1's first-class preservation principle in full and extends conflict to two additional scopes within a single Self.

**Scope (a) — Intra-Self mating conflicts.** When two aspects participate in a mating event, their content-domains may overlap in incompatible ways. Merge-time conflicts between aspects are handled under the mating governance architecture, with Paper 1's preservation principle holding: the conflict is substrate content, both sides are retained, and resolution occurs under human-authored orchestration rules for the mating operation. This is still one governance authority — the Self's governance — but now two aspects interacting rather than two rules within one cell.

**Scope (b) — Cross-tier conflicts.** When cell-level governance and aspect-level governance, or aspect-level and Self-level governance, produce incompatible specifications for the same content domain, the vertical governance hierarchy must resolve or preserve the cross-tier conflict. Paper 2 explicitly applies the conflict-as-first-class principle at all three levels — cell, aspect, Self — treating the conflict registry as recursive across levels rather than applicable only at the cell level.

Paper 2 therefore expands conflict scope from cell-internal to include aspect-mating merge time and vertical cross-tier governance incompatibility, all within one Self's governance perimeter. The preservation principle does not change. What changes is the structural distance between the conflicting specifications: they may now originate from different levels of the same governance hierarchy rather than from two rules within one cell.

---

## 4. Paper 3 Usage — Inter-Self Approach Incompatibility

Paper 3 retains the preservation principle from Papers 1 and 2 and extends conflict to the inter-Self scope: cases where two contributing Selves' aspects carry different governance approaches for the same content domain within a shared substrate.

These inter-Self conflicts are structurally different from the conflicts in Papers 1 and 2. In Papers 1 and 2, the conflicting specifications originate from within one governance architecture — the same human authority governs both sides of the conflict. In Paper 3, the conflicting specifications originate from **two independent governance architectures**: the home governance structures of two distinct Selves. This is not a rule-level incompatibility within one substrate; it is an approach-level difference between two governance architectures that are meeting for the first time within a shared substrate constructed for the FAI event.

Paper 3 handles inter-Self conflicts through a **three-tier mechanism**: (1) preserve — conflicts within the shared substrate are retained as first-class state, by direct inheritance from Paper 1; (2) resolve via orchestration — when prebuilt orchestration rules within the shared substrate address the conflict class, those rules determine the response under joint governance authority; (3) escalate to humans — when no automated resolution is appropriate, the conflict surfaces to the governance authorities of the participating Selves.

The three-tier mechanism is not a new concept of conflict. It is what Paper 1's two-level structure (substrate-level preservation plus cell-level resolution under orchestration rules) produces when those principles are applied at inter-Self scope, where a third tier — cross-perimeter escalation to joint human authority — is required because no single governance authority can resolve the conflict unilaterally.

**Competitive intelligence value.** Paper 3 introduces one genuinely new *use* of conflict preservation that does not appear in Papers 1 or 2: in competition-variant FAI events, preserved conflicts are not merely governance bookkeeping — they are the primary output. The preserved conflict record shows precisely where two Selves' governance approaches diverge, and that divergence is the comparative intelligence the event was constructed to produce. This expanded use of conflict preservation is a Paper 3 addition; it is not a new concept of conflict. The underlying commitment — preserve incompatibility as first-class state rather than resolving it away — is the same commitment Paper 1 makes. Paper 3 recognizes an additional reason to value that commitment at inter-Self scope.

---

## 5. The Disambiguation

"Conflict" across the trilogy names **one architectural concept**: governance specification incompatibility that must be preserved as first-class substrate state and resolved under human-authored orchestration rules. The concept is constant. Three scope-specific properties vary:

| Property | Paper 1 | Paper 2 | Paper 3 |
|---|---|---|---|
| **Type of incompatibility** | Rule-level, within one cell | Rule-level across aspects/levels within one Self | Approach-level between two independent governance architectures |
| **Governance authority structure** | One authority, one substrate | One authority, multi-level substrate | Two or more authorities, shared substrate |
| **Resolution mechanism** | Directed selection by governing human(s) | Recursive directed selection at the applicable level | Three-tier: preserve / resolve via orchestration / escalate to joint authority |
| **Preservation principle** | First-class state, both sides retained | First-class state at every level | First-class state across the inter-Self perimeter |

The resolution mechanism changes because the governance authority structure changes, not because the concept of conflict changes. A single governance authority can apply directed selection because it holds authority over both sides of the conflict. A joint governance arrangement across two Selves cannot apply directed selection unilaterally; it requires the three-tier structure to accommodate the case where no single authority governs the resolution. The mechanism is the governance authority structure's adaptation to conflict, not a redefinition of what conflict is.

The competitive intelligence value Paper 3 introduces does not alter this picture. It is an expanded *application* of the preservation commitment at inter-Self scope, not a revision of what preservation means or what conflict names.

---

## 6. Prior-Art Disambiguation Claim

"Conflict" throughout the CKS trilogy refers to the same concept — governance specification incompatibility with first-class preservation — at three progressively larger scopes. The concept is established in Paper 1 as Claim 2 (conflict-as-first-class governance state). Paper 2 extends the scope of application to multi-level intra-Self governance. Paper 3 extends the scope of application to inter-Self governance across independent governance authorities.

Any adversarial claim that the conflict concept introduced in Paper 2 or Paper 3 is novel relative to the earlier papers must address the following:

- Paper 1 Claim 2 establishes the foundational architectural commitment: preserve incompatibility as first-class state, resolve under orchestration rules.
- Paper 2 applies that commitment recursively at all three levels of the Self's governance hierarchy and at merge-time within mating operations. The commitment is not new; only the scope of application is extended.
- Paper 3 applies the same commitment at inter-Self scope and develops the three-tier mechanism as what the Paper 1 commitment produces when extended to a multi-authority governance arrangement. The three-tier mechanism is not free-standing architecture; it is the Paper 1 two-level structure with a cross-perimeter escalation tier added for the cases where joint authority is required.
- The competitive intelligence value Paper 3 identifies does not constitute a new concept of conflict. It is a new downstream use of the preservation commitment at inter-Self scope.

Conversely, any adversarial claim that Paper 3's three-tier mechanism is merely a restatement of Paper 1 Claim 2 must address the following:

- The inter-Self scope requires a joint-authority escalation tier with no equivalent in Paper 1's single-authority structure. This is fresh content at Paper 3 scope.
- The approach-level incompatibility between two independent governance architectures is structurally different from the rule-level incompatibility within one governance architecture. The distinction is relevant to the escalation tier design.
- The competitive intelligence use of preserved conflicts is absent from Papers 1 and 2. This is a Paper 3 contribution.

The disambiguation forecloses simultaneous claims that (a) the Papers 2 and 3 conflict concept is novel and independent and (b) the Papers 1 and 2 conflict concept already covers what Paper 3 does. Both claims fail. The concept is one; the scope applications are three; the inheritance is direct and acknowledged.

---

## Source Papers

Li, W. (2026a). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Disambiguating "Conflict" Across the Trilogy.* Series T, Note T1.01 (#687). May 15, 2026. ORCID: 0009-0004-8065-3235.
