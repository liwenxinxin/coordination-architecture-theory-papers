# Composition Pair Tests 21–30

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note presents ten binary governance tests — Tests 21 through 30 — covering the highest-priority composition pair requirements from Phase D4 of the CKS derivation series. Each test specifies the governance records to examine, poses a binary question answerable from those records alone, and identifies what a PASS indicates about compliant governance and what a FAIL signals about governance gaps. The ten tests map to the foundational composition pairs most likely to be missed in practice: pre-authorization for time-sensitive coordination, N-ary governance completeness, competition-variant conflict routing, exit-dissolution sequencing, parent-agreement hierarchy, emergency evolution feed pre-authorization, withdrawn-side conflict registry maintenance, absorption-before-restructuring sequencing, human authorization chains for automated governance actions, and knowledge transfer non-obligation. Each FAIL interpretation connects to the anti-pattern taxonomy from Phase D3. The tests are governance-record-based throughout; none requires access to technical implementation internals.

---

## 1. Purpose

Phase D5 produces operational tests for Paper 3's inter-Self coordination governance requirements. Each test operationalizes a composition pair commitment from Phase D4 — a commitment that arises when two specific architectural concepts are applied together and that is not visible in either concept examined in isolation. D5.01 covers Tests 11–20 (foundational event-lifecycle and substrate properties). This note covers Tests 21–30, the composition pair tests: ten tests drawn from the D4 pairs most likely to be missed because each requires both halves of a pair to be present simultaneously.

A governance test in this series has one property that distinguishes it from an implementation audit: it is answerable entirely from governance records. Records here means any persistent substrate content carrying governance authority — event configurations, standing configurations, cross-organizational agreements, timestamps on decision records, conflict registry entries, authorization chain records. A reviewer who can read those records can determine PASS or FAIL without any access to source code, runtime logs, or system internals. This constraint is not a limitation; it is the property that makes the test useful to governance practitioners, auditors, and counterparty reviewers who do not have implementation access.

---

## 2. Test Format

Every test follows the same five-part structure:

1. **Test number and name** — identifies the test within the D5 library and the composition pair it operationalizes.
2. **Records to examine** — the specific governance artifacts a reviewer must locate and read.
3. **Binary question** — the yes/no question answerable from those records alone.
4. **PASS indicates** — what compliant governance looks like when the answer is YES.
5. **FAIL indicates** — the governance gap or anti-pattern the failure signals when the answer is NO.

---

## 3. Tests 21–30

---

### Test 21 — Pre-Authorization for Time-Sensitive Events

**Composition pair:** Floor governance + Time-sensitive coordination (D4.02)

**Records to examine:** FAI event configuration, construction record, standing configuration if present.

**Binary question:** For a time-sensitive FAI event, is the event governed by a pre-authorized standing configuration or pre-authorized rules — rather than by governance configurations authored at event start?

**PASS indicates:** The construction record references a standing configuration or a set of pre-authorized rules that were in place before the event began. Governance was authored ahead of time and carried into the event by reference. The time pressure of the event itself did not drive governance authoring decisions.

**FAIL indicates:** The configuration was authored at event start under time pressure, or no configuration record exists at all. This is the co-occurrence of two anti-patterns: the governance floor was absent (AP-6) and governance was reactive rather than pre-authorized (AP-19). In combination, time-sensitive events without pre-authorization create conditions where substantive governance decisions are made under exactly the conditions least suited to careful human governance authoring. The gap is not that the event was time-sensitive; it is that the governance architecture did not prepare for that condition in advance.

---

### Test 22 — N-Ary Governance Completeness

**Composition pair:** Standing configurations + Multi-Self events (D4.03)

**Records to examine:** FAI event configuration, standing configuration(s), joint authorization records.

**Binary question:** For an FAI event with more than two participating Selves, does governance specify three-way or higher joint authorization and cross-pair conflict routing — either through a multilateral configuration or through bilateral configurations supplemented by an N-specific governance document?

**PASS indicates:** N-ary joint authorization is explicitly present, naming all participating Selves and specifying how joint authority is exercised across the full group. Cross-pair conflict routing — the rules for how conflicts between non-adjacent pairs in the event are handled — is also explicitly present. Governance records address the event at its actual cardinality, not at a two-Self default.

**FAIL indicates:** Only bilateral authorization records are present. Each pair of Selves may have been authorized individually, but the three-way or N-way governance that the event's cardinality requires is not covered. This is the N-blind configuration anti-pattern (AP-17): governance was authored as if the event were bilateral even though more parties participated. The practical consequence is that conflicts arising between non-adjacent pairs have no routing rule, and authority questions about the full group have no resolution path. Bilateral completeness does not compose into N-ary completeness automatically.

---

### Test 23 — Competition Pair Consistency

**Composition pair:** Competition variant + Preserve tier (D4.04)

**Records to examine:** FAI event configuration (specifically Dimension 4, the variant selection), conflict routing rules.

**Binary question:** For an FAI event configured as a competition variant, do the conflict routing rules explicitly route approach-difference conflicts to the preserve tier?

**PASS indicates:** The competition variant is selected in the configuration, and the conflict routing rules contain an explicit entry specifying that approach-difference conflicts are routed to preserve. The two halves of the pair are consistent: the variant choice is reflected in the routing rules, not just in the dimension field.

**FAIL indicates:** The competition variant was selected but the routing rules were not updated correspondingly. Approach-difference conflicts that arise during the event have no routing rule pointing them to preserve, meaning they may be incorrectly routed to resolution tiers where competitive intelligence exposure could occur. This is AP-14: competitive intelligence misrouting. The governance gap is not that competition was chosen; it is that the variant selection was not propagated to the part of the configuration that governs conflict handling. These two records must be consistent; the test checks that consistency directly.

---

### Test 24 — Exit-Dissolution Sequencing

**Composition pair:** Exit rights + Active events (D4.05)

**Records to examine:** Exit declaration record, emergency dissolution records for active events, their timestamps.

**Binary question:** Does the exit declaration record carry a timestamp that precedes the timestamps on the emergency dissolution records for active events?

**PASS indicates:** The exit declaration came first. Emergency dissolution of the active events followed from the declared exit, in the governance-correct order. Authority to exit was exercised before the dissolution operations ran.

**FAIL indicates:** Either the dissolution records precede the exit declaration — meaning active events were dissolved before exit was formally declared, reversing the correct governance sequence — or dissolution records for active events are absent entirely, meaning the events were not formally dissolved at all. Absent dissolution records are the ungoverned dissolution pattern (AP-2): events that were operationally ended without corresponding governance records. The test is purely timestamp-based; no interpretation of substance is required. Sequencing errors are governance race conditions; absent records are governance gaps.

---

### Test 25 — Parent-Child Agreement Hierarchy

**Composition pair:** Cross-organizational agreements + Standing configurations (D4.13)

**Records to examine:** Standing configurations, cross-organizational agreements they are intended to operate under.

**Binary question:** Does each standing configuration contain an explicit reference to its parent cross-organizational agreement?

**PASS indicates:** Every standing configuration carries a field or section identifying the cross-organizational agreement it operates under. The governance hierarchy is navigable: from a standing configuration, a reviewer can identify its parent agreement and confirm that the configuration's scope, authorization, and constraints are consistent with that agreement.

**FAIL indicates:** One or more standing configurations have no parent agreement reference. These are orphaned standing configurations — they authorize repeated coordination activity without being anchored in any cross-organizational governance frame. The governance gap is structural: the standing configuration may have been authored for one agreement but there is no record linking them, or it may have been authored without any agreement in view. In either case, a reviewer cannot determine whether the standing configuration's terms are within the scope of any cross-organizational authorization.

---

### Test 26 — Emergency Evolution Feed Pre-Authorization

**Composition pair:** Emergency dissolution + Evolution feed (D4.14)

**Records to examine:** Emergency dissolution record, evolution feed eligibility configuration, evolution feed outputs.

**Binary question:** Did the evolution feed that ran at emergency dissolution proceed under a pre-authorized eligibility configuration — one that existed in the FAI event configuration before dissolution began — rather than under ad-hoc governance decisions made during the dissolution process?

**PASS indicates:** The evolution feed outputs reference a pre-configured eligibility scope from the FAI event configuration. The scope of what each participating Self was eligible to absorb from the event's outputs was determined before the dissolution event and carried through it by reference. Emergency conditions did not drive eligibility authoring.

**FAIL indicates:** No pre-authorized eligibility scope exists; the evolution feed ran without a pre-configured scope, or it ran under scope decisions made during the dissolution itself. The governance gap is that emergency dissolution — an already high-stakes operation — was compounded by ungoverned evolution feed routing. Eligibility for DNA absorption and action-feedback ingestion from a dissolved event is a governance decision that must be made in advance; ad-hoc eligibility decisions under dissolution conditions are the governance analog of the AP-24 pattern at the evolution feed layer.

---

### Test 27 — Withdrawn-Side Conflict Registry Update

**Composition pair:** Partial withdrawal + Conflict registry (D4.15)

**Records to examine:** Partial withdrawal record, conflict registry entries for aspects involved in the withdrawal.

**Binary question:** Do conflict registry entries for aspects that were withdrawn carry WITHDRAWN-SIDE status and a routing decision record, with timestamps following the withdrawal record?

**PASS indicates:** After the partial withdrawal was recorded, the conflict registry was updated. Each entry involving a withdrawn aspect now shows WITHDRAWN-SIDE status, and a routing decision record documents how the conflict was handled given the withdrawal. The registry reflects the current governance state of the event, not the pre-withdrawal state.

**FAIL indicates:** Conflict registry entries for withdrawn aspects still carry their pre-withdrawal status. The registry has not been updated to reflect the withdrawal. This is a governance consistency failure: the event's conflict state as represented in the registry diverges from the event's actual participation state. Downstream governance operations — including escalation decisions, preserve-tier routing, and evolution feed eligibility — that read the conflict registry will operate on stale information.

---

### Test 28 — Absorption Before Restructuring Sequencing

**Composition pair:** DNA absorption + Aspect restructuring (D4.08)

**Records to examine:** DNA absorption decision records, aspect restructuring records for the same aspects, their timestamps.

**Binary question:** For aspects that received both a DNA absorption decision and a subsequent restructuring, does the absorption decision record carry a timestamp that precedes the restructuring record's timestamp?

**PASS indicates:** Absorption was decided first. Restructuring followed from a governance-stable foundation: the DNA content from the absorbed material was in place before the aspect structure was reorganized around it. The two governance operations occurred in the correct order.

**FAIL indicates:** Restructuring preceded the absorption decision for one or more aspects. This is a governance race condition: the aspect was restructured before governance had determined what DNA content it would carry. Restructuring decisions made before absorption decisions cannot correctly account for the absorbed content's structural implications. The sequencing failure cannot be retroactively corrected by documentation; it indicates that the two governance operations were not coordinated within the same governance frame.

---

### Test 29 — Human Authorization Chain for Automated Governance Actions

**Composition pair:** Determinism contract + Non-delegation (D4.25)

**Records to examine:** Automated governance action records, pre-authorization records they reference.

**Binary question:** For each automated governance action, does a pre-authorization record exist that is traceable, through a navigable chain, to a human governance authorization?

**PASS indicates:** Each automated action carries a reference to a pre-authorization record. That pre-authorization record in turn references a human governance authorization — a record that a human with governance authority over the relevant Selves authored and signed. The chain is complete and navigable in both directions: from automated action back to human authorization, and from human authorization forward to the automated actions it covers.

**FAIL indicates:** One or more automated governance actions lack a pre-authorization reference, or the chain from pre-authorization to human authorization is broken. This is automated governance (AP-24): governance actions taken without traceable human authorization. The distinction the test enforces is architectural: automation is compatible with human governance when automation runs under pre-authorization that traces to human authority; automation is not compatible with human governance when automated actions stand alone, without any authorization chain. The test does not require that humans approve each automated action in real time; it requires that each automated action be covered by a pre-authorization that a human authored.

---

### Test 30 — Knowledge Transfer Non-Obligation Statement

**Composition pair:** Knowledge transfer + DNA absorption (D4.11)

**Records to examine:** Cross-organizational agreement governing the knowledge transfer event.

**Binary question:** Does the cross-organizational agreement explicitly state that DNA absorption is the learner Self's home governance decision and cannot be conditioned on by the contributor?

**PASS indicates:** An explicit non-obligation statement is present in the agreement. The contributor's contribution of aspects and DNA-layer content to the shared substrate creates no obligation on the receiving Self to absorb any of that content into its home substrate. Absorption decisions rest entirely with the receiving Self's home governance, and that boundary is explicitly stated in the governing agreement.

**FAIL indicates:** The non-obligation statement is absent. Without it, the absorption intent that a contributor naturally holds — the expectation that contributed content will be absorbed — may implicitly convert into a contractual obligation, either through later dispute interpretation or through subsequent agreement drafting that treats prior absorption as a precedent. The governance gap is not that absorption occurred; it is that the agreement's silence on the question leaves the receiving Self's governance sovereignty over absorption decisions formally unprotected.

---

## 4. Reading Across the Test Set

The ten tests form a coherent library because they address the five most consequential failure modes in inter-Self coordination governance: **sequencing failures** (Tests 24 and 28 check whether governance operations occurred in the correct order); **coverage gaps** (Tests 22, 25, and 29 check whether governance is complete at the scope the operation requires); **pre-authorization failures** (Tests 21 and 26 check whether governance was authored before it was needed, not during the operation it governs); **consistency failures** (Tests 23 and 27 check whether related governance records agree with each other); and **sovereignty protection** (Test 30 checks whether the receiving Self's governance authority is explicitly protected in the governing agreement).

A governance reviewer applying these tests sequentially will find that failures tend to cluster: an absent parent agreement reference (Test 25) often accompanies N-blind governance (Test 22), because both reflect the same pattern of governance scoped to a single relationship rather than to the full relational context of an event. Similarly, a pre-authorization failure (Test 21) often co-occurs with a missing human authorization chain (Test 29), because both reflect a governance culture in which time pressure or operational convenience was allowed to displace governance preparation. Where failures cluster, the underlying governance gap is structural rather than incidental.

The tests are independent in the sense that each tests one specific composition pair; a PASS on one does not imply a PASS on any other. They are interdependent in the sense that a complete governance review applies all ten, because the composition pair requirements they operationalize are each necessary conditions for compliant inter-Self coordination governance at the scope Paper 3 specifies.

---

*End of note.*
