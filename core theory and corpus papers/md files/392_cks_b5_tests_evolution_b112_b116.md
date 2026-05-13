# Operational Tests for Evolution Mechanisms (B1.12–B1.16): Five Deployment-Facing Tests Including Three Mechanisms Presence, Mutation Governance Instruments, Directed Selection Governance, Action-Feedback Pathway Integrity, and Bidirectional Evolution Configuration, Each With Question, Mechanism, Pass, Fail, and Remediation Signal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to derive, from the evolution mechanism commitments of the source paper (§7, §8), five deployment-facing operational tests that a practitioner can apply to verify whether a CKS Self's evolution cluster (B1.12–B1.16) is correctly instantiated.

---

## Abstract

The CKS source paper (Paper 2, Li, April 2026) commits to three evolution mechanisms operating in productive tension (§7.2): instinct evolution as undirected mutation, DNA evolution as directed selection, and action-feedback evolution as the loop closing action experience back into governed DNA refinement. These mechanisms do not operate in isolation — they require governance infrastructure (§8) and operate across horizontal and vertical axes (§7.4). Verifying that a deployment correctly instantiates the evolution cluster (covering B1.12 through B1.16) requires tests that probe each layer of this infrastructure.

This note formalizes five such tests. Test 1 (B2.60) asks whether all three mechanisms are present and have been exercised since deployment. Test 2 (B2.66) asks whether the three mutation governance instruments — verification gates, routing rules, and high-stakes pinning — are configured and operational. Test 3 (B2.72) asks whether all DNA modifications are authorized, recorded, and retroactivity-compliant. Test 4 (B2.78) asks whether the complete action-feedback pathway from Action layer evidence through proposal generation to Stage 2 approval to DNA change is operational and has not been bypassed. Test 5 (B2.83) asks whether horizontal and vertical evolution governance pathways are configured and have been exercised.

All five tests must pass for the composite result to pass. Anti-patterns detected across the five tests include Single-Mechanism Evolution (B3.13), Ungoverned Mutation (B3.14), Ungoverned DNA Modification (B3.15), Silent DNA Drift (B3.16), Unidirectional Evolution (B3.17), Evolution Stasis (B3.24), Evidence Blindness (B3.28), and Specification Integrity Collapse (B3.30).

---

## 1. Why evolution governance requires operational tests

The evolution cluster (B1.12–B1.16) is architecturally dense: it requires three distinct mechanisms (B1.12: action-feedback evolution; B1.10–B1.11: instinct evolution and DNA evolution), each with its own governance instruments; multi-level simultaneous operation (B1.13); and horizontal and vertical axes (B1.14) under multi-shaped human governance (B1.15), with the instinct/reasoning boundary itself as governed substrate content (B1.16). No single indicator captures whether this cluster is functioning correctly.

The failure modes are also asymmetric. A deployment might have all three mechanisms nominally present but fail to govern any of them — producing Ungoverned Mutation (B3.14), Ungoverned DNA Modification (B3.15), and Silent DNA Drift (B3.16) simultaneously. It might govern instinct evolution correctly while allowing action-feedback proposals to auto-integrate without Stage 2 approval — producing Silent DNA Drift silently, without any visible architectural break. It might exercise only one evolution direction (upward but not downward, or horizontal but not vertical), producing Unidirectional Evolution (B3.17) without recognizing it as a deployment gap.

Operational tests create explicit detection points for each failure mode. The five tests in this note correspond to five verification entry points in the evolution governance layer: presence of all three mechanisms (B2.60), mutation instrument completeness (B2.66), directed selection authorization integrity (B2.72), action-feedback pathway integrity with anti-silent-drift check (B2.78), and bidirectional evolution configuration (B2.83). A deployment that passes all five has demonstrated not just that the mechanisms are nominally configured, but that they have been exercised under governance.

---

## 2. The evolution mechanism cluster: B1.12–B1.16

B1.12 (Action-feedback evolution) closes the loop from Action layer recorded experience back into DNA layer refinement — it is the only mechanism that lets a Self learn from its own operation rather than only from external upgrades or human design decisions. B1.13 (Multi-level simultaneous evolution) commits to all three mechanisms applying concurrently at cell, aspect, and Self levels, on different timescales, under different human authority scopes. B1.14 (Horizontal and vertical evolution) commits to two orthogonal axes: horizontal evolution propagates improvements laterally among peers at the same architectural level; vertical evolution moves refinements upward (from lower-level action evidence to higher-level DNA changes) and downward (from higher-level DNA changes into cell behavior through expression). B1.15 (Multi-shaped human governance across evolution mechanisms) commits to governance taking different forms across the three mechanisms — verification for instinct, the standard authority architecture for DNA, human-mediated approval for action-feedback. B1.16 (The instinct/reasoning boundary as governed substrate content) commits to the boundary between instinct and reasoning being itself substrate content that humans can tune.

The five tests probe this cluster as an operational whole. Tests 1–3 cover mechanism presence and governance instrumentation. Test 4 is the primary integrity check for the action-feedback pathway, including the anti-silent-drift check. Test 5 covers the bidirectional evolution configuration that B1.13 and B1.14 require.

---

## 3. Test 1 — Three Mechanisms Presence Test (B2.60)

**TEST QUESTION:** Are all three evolution mechanisms — instinct evolution (mutation governance), DNA evolution (directed selection), and action-feedback evolution — configured and operational in the deployment, per B1.12?

**TEST MECHANISM:** B2.60 three mechanisms verification proceeds by checking each mechanism independently.

For *instinct evolution (mutation)*: verify that verification gates exist per cell type for LLM integration (per B2.06), that routing rules for LLM version deployment are present (per B2.04), and that high-stakes decision pinning to the reasoning layer is configured (per B2.05).

For *DNA evolution (directed selection)*: verify that the DNA version chain (per B2.69) shows at least one directed modification since deployment. The mechanism requires evidence of exercise, not just configuration; a version chain that has not changed since deployment means directed selection has not operated.

For *action-feedback evolution*: verify that governed proposing substrates (per B2.74) are present with authored specifications, and that Stage 1 and Stage 2 governance review events (per B2.75) have occurred since deployment.

**PASS CONDITION:** All three mechanisms are present (configured with their respective instruments) and have been exercised since deployment. The DNA version chain shows directed modifications; Stage 1 and Stage 2 review events are recorded; mutation governance instruments are configured and have processed at least one LLM version event.

**FAIL CONDITION:** One or more mechanisms are absent in configuration; no directed selection events appear in the DNA version chain since deployment; no governed proposing substrates are present; no Stage 1 or Stage 2 review events have occurred; mutation governance instruments are not configured.

**REMEDIATION SIGNAL:** Single-Mechanism Evolution (B3.13) if one or two mechanisms are absent or have never been exercised — the deployment is not benefiting from the productive tension the source paper's §7.2 requires. Evolution Stasis (B3.24) if all active evolution mechanisms are absent or dormant — the deployment is not evolving through any governed pathway at operational timescales.

---

## 4. Test 2 — Mutation Governance Instruments Test (B2.66)

**TEST QUESTION:** Are all three mutation governance instruments — verification gates, routing rules, and high-stakes pinning — configured, operational, and exercised for LLM version changes?

**TEST MECHANISM:** B2.66 mutation governance verification checks each instrument against deployment records.

*Verification gates*: verify that verification suites exist per cell type and are run on LLM version updates, per B2.06. A verification gate that exists in configuration but is not run on updates does not satisfy the instrument requirement — presence and execution are both required.

*Routing rules*: verify that routing rules per B2.04 are present and specify LLM version routing — including which cells receive which model version and under what conditions fallback or staged deployment occurs. Routing rules that do not address LLM versions specifically do not satisfy this check.

*High-stakes pinning*: verify that high-stakes decisions are identified per B2.05 and that cells handling them have pinning rules in their DNA, preserving reasoning-layer governance regardless of how capable instinct becomes. Identification without pinning rules in DNA does not satisfy the instrument requirement.

*Mutation event records*: verify that LLM version changes since deployment have been recorded as mutation events per A2.40 (provenance metadata), consistent with B2.61. Unrecorded LLM version changes indicate the mutation governance pipeline was bypassed.

**PASS CONDITION:** All three instruments are present; LLM version changes are recorded as mutation events with provenance metadata; verification gates are executed on updates; routing rules specify deployment management across LLM versions; high-stakes decisions are identified and pinned in cell DNA.

**FAIL CONDITION:** Any instrument is absent; LLM updates have occurred without mutation event records; verification gates are configured but not run on updates; routing rules exist without specifying LLM version routing; no high-stakes decisions are identified or cells lack pinning rules.

**REMEDIATION SIGNAL:** Ungoverned Mutation (B3.14). Identify the specific form: Form 1 (verification-skipped) if gates exist but are not run on updates; Form 2 (unrouted) if routing rules are absent or do not cover LLM versions; Form 3 (unpinned) if high-stakes decisions lack pinning rules in DNA. Multiple forms may co-occur and each requires distinct remediation.

---

## 5. Test 3 — Directed Selection Governance Test (B2.72)

**TEST QUESTION:** Are all DNA modifications in the version chain authorized per A2.47, recorded per A2.40, and compliant with retroactivity requirements, with no internally contradictory rules accumulating in current DNA?

**TEST MECHANISM:** B2.72 directed selection verification audits the DNA version chain (per B2.69) systematically.

*DNA version audit*: for each DNA version in the chain, verify that a modification record exists per A2.40 with governance authorization identifying the modifier and the authority level at which the modification was made. A version entry without a modification record indicates an untracked change.

*Authorization verification*: verify that the modifier held A2.47 authority at the scope modified — cell-level changes require cell-level authority; aspect-level or Self-level changes require authority at those respective scopes. Cross-scope modifications require explicit authorization at the higher scope.

*Retroactivity compliance* per B2.70: verify that DNA version timestamps precede the operations they governed. A DNA version that post-dates the operations it purports to have governed fails the retroactivity requirement — this indicates the version record was created after the fact rather than being in place when operations executed.

*Coherence check*: scan the current DNA for internally contradictory rules. Accumulating contradictions are the early signal for Specification Integrity Collapse (B3.30) before the collapse becomes operationally visible; detecting them early through the coherence check allows remediation before cell behavior becomes incoherent.

**PASS CONDITION:** All DNA modifications have authorization records, provenance metadata, and retroactivity compliance; the modifier's authority scope is confirmed at the appropriate level for each modification; no internal contradictions in current DNA.

**FAIL CONDITION:** Modifications without authorization records; modifications without provenance metadata; modification timestamps post-dating the governed operations; contradictory rules accumulating in current DNA.

**REMEDIATION SIGNAL:** Ungoverned DNA Modification (B3.15) for unauthorized or unrecorded modifications — the directed selection pathway has operated outside governance. Specification Integrity Collapse (B3.30) as early warning for accumulating contradictions — this is a blocking signal that should trigger immediate contradiction resolution before operational coherence is lost.

---

## 6. Test 4 — Action-Feedback Pathway Test (B2.78)

**TEST QUESTION:** Is the complete action-feedback pathway operational from Action layer evidence through proposal generation to Stage 2 approval to DNA change — and has any proposal been integrated without Stage 2 approval?

**TEST MECHANISM:** B2.78 action-feedback pathway integrity check proceeds through five sub-checks.

*Proposing substrates*: verify that governed proposing substrates per B2.74 are present with authored specifications establishing what evidence they consume, what kind of DNA change proposals they produce, and under whose authority they operate. Ungoverned or unspecified proposing substrates cannot participate in the Stage 1/Stage 2 pathway.

*Stage 1 governance*: verify that Stage 1 review events per B2.75 have occurred — proposing substrate outputs have been reviewed by humans with appropriate authority before proceeding to proposal stage. Stage 1 review is the first governance checkpoint in the action-feedback loop; its absence means proposals have been generated without any human review of the evidence they rest on.

*Stage 2 governance*: verify that Stage 2 approval events have occurred — proposals have been approved by humans with authority to authorize directed selection, and those approvals have been translated into actual DNA changes recorded in the version chain. A Stage 2 approval that does not produce a corresponding DNA version entry indicates the approval-to-change translation pathway is broken.

*Anti-silent-drift check per B2.78*: this is the test's most critical sub-check and the primary deployment-facing detector for Silent DNA Drift (B3.16). Verify that no action-feedback proposals have been integrated into DNA without a recorded Stage 2 approval event. This check is a *blocking* check: any single integration without Stage 2 approval is a failure, not a trend to be monitored. Silent integration — where the Action layer effectively edits the DNA layer without governance authorization — is self-concealing: the DNA continues to appear governed while drifting toward operational patterns that no human authorized. The source paper's §8 commitment that action-feedback evolution is "human-mediated rather than automatic" specifically prevents this pathway from becoming automatic; the anti-silent-drift check verifies that commitment at the deployment level.

*Action layer completeness*: verify that Action layer records per B2.26 are complete enough per A5.08 to serve as quality evidence for proposing substrates. Incomplete Action layer records deprive the feedback pathway of its empirical foundation — proposals generated from thin or incomplete evidence cannot accurately represent the Self's operational experience.

**PASS CONDITION:** Governed proposing substrates exist with authored specifications; Stage 1 review events are recorded; Stage 2 approval events are recorded; no proposals have been integrated without Stage 2 approval (anti-silent-drift check passes); Action layer records are complete enough to serve as quality evidence.

**FAIL CONDITION:** Proposing substrates absent or ungoverned; no Stage 1 review events; no Stage 2 approval events; any proposal has been auto-integrated without Stage 2 approval; Action layer records are incomplete.

**REMEDIATION SIGNAL:** Evidence Blindness (B3.28) if the action-feedback pathway is absent or disconnected — the Self cannot learn from its own operation because there is no governed pathway from evidence to DNA change. Silent DNA Drift (B3.16) if the anti-silent-drift check fails — the DNA layer has drifted from what humans authorized, and the extent of drift must be assessed by auditing all unauthorized integrations against the current DNA state. Silent DNA Drift remediation requires reconstructing what the DNA would contain under proper governance and reconciling the unauthorized changes explicitly.

---

## 7. Test 5 — Bidirectional Evolution Test (B2.83)

**TEST QUESTION:** Are horizontal and vertical evolution governance pathways configured and have they been exercised per B1.14 and B1.16?

**TEST MECHANISM:** B2.83 bidirectional evolution verification checks each directional pathway independently.

*Horizontal evolution*: verify that improvements identified in one peer cell or peer aspect have been reviewed for applicability to other entities at the same architectural level. Governance reviews must be configured to assess peer improvement applicability as a standing process — not just in redesign phases. A deployment in which cells evolve without any review of whether their evolution is applicable to peers is operating with horizontal evolution disconnected.

*Vertical evolution — upward*: verify that action-feedback proposals originating at lower levels (cell-level evidence producing aspect-level or Self-level DNA changes) have occurred and produced DNA version chain entries at the higher scope. The upward pathway closes the loop from operational cell experience to structural-level governance; its absence means lower-level learning never propagates to where it can govern the whole.

*Vertical evolution — downward*: verify that Self-level or aspect-level DNA changes have propagated to cell behavior through the expression mechanism per B1.07, establishing that the downward pathway from governance-level directed selection to operational cell execution is functional. DNA changes that do not reach cells through expression are governance decisions that have not taken effect operationally.

*Operational timescale*: verify that evolution governance is operating continuously rather than only at deployment redesign events. B1.13's multi-level simultaneous evolution commitment is an operational commitment — the mechanisms apply at cell, aspect, and Self levels on ongoing operational timescales, not only when the system is being redesigned. Governance that is only active at redesign is not instantiating the multi-level simultaneous evolution commitment.

**PASS CONDITION:** Horizontal propagation has been reviewed for at least one peer improvement; the upward vertical pathway has been exercised (lower-level evidence has produced higher-level DNA changes); the downward vertical expression mechanism has propagated DNA changes to cell behavior; evolution governance has continuous operational presence, not only redesign-phase presence.

**FAIL CONDITION:** No horizontal propagation review events since deployment; action-feedback proposals have never produced DNA changes at higher levels than their origin; Self-level or aspect-level DNA changes have never reached cells through expression; governance activity is only present at deployment redesign with no operational-timescale evolution governance.

**REMEDIATION SIGNAL:** Unidirectional Evolution (B3.17) — identify the missing direction: horizontal absent; vertical-upward absent; vertical-downward absent. Multiple directions may be absent simultaneously. Evolution Stasis (B3.24) if all evolutionary pathways are inactive and governance is only at deployment redesign — the Self is not evolving through any governed pathway at operational timescales, regardless of how well-configured the mechanisms appear in static inspection.

---

## 8. Composite evolution test result and anti-pattern coverage

All five tests must pass for the composite evolution governance result to pass. A single failing test does not localize the fault to one mechanism only; the tests are designed to complement each other, and some anti-patterns are detectable only at the intersection of multiple tests. A deployment that passes Test 1 (all mechanisms present) but fails Test 4 (anti-silent-drift check) has mechanisms present but operating outside governance. A deployment that passes Tests 1–4 but fails Test 5 may have all three mechanisms governed correctly at one level while failing to propagate evolution across levels.

The eight anti-patterns covered across the five tests:

- **B3.13 (Single-Mechanism Evolution)** — detected by Test 1 when one or two mechanisms are absent or have never been exercised; the productive tension the source paper's §7.2 commits to is absent.
- **B3.14 (Ungoverned Mutation)** — detected by Test 2 in three distinct forms (verification-skipped, unrouted, unpinned), each requiring separate remediation.
- **B3.15 (Ungoverned DNA Modification)** — detected by Test 3 when authorization records or provenance metadata are absent from the DNA version chain.
- **B3.16 (Silent DNA Drift)** — detected by Test 4's anti-silent-drift check, which is the primary deployment-facing detector for this anti-pattern; any single unauthorized integration is a blocking failure.
- **B3.17 (Unidirectional Evolution)** — detected by Test 5 when horizontal propagation review, vertical-upward pathway, or vertical-downward expression pathway is absent.
- **B3.24 (Evolution Stasis)** — detected by Test 1 (all mechanisms dormant) and by Test 5 (governance only at redesign); a deployment may show stasis through either path.
- **B3.28 (Evidence Blindness)** — detected by Test 4 when the action-feedback pathway is absent or disconnected, preventing the Self from learning from its own operation.
- **B3.30 (Specification Integrity Collapse)** — detected as early warning by Test 3's coherence check; accumulating contradictions surface before operational coherence is lost if the check is applied periodically.

The composite test is not a single-point event. Evolution mechanisms operate on ongoing timescales, and the tests should be applied periodically throughout a deployment's life, not only at launch. A deployment that passes the composite test at launch may develop Evolution Stasis (B3.24) if governance activity drops. A deployment that passes Test 4 at launch may develop Silent DNA Drift (B3.16) if Stage 2 approval processes erode over time. The multi-level simultaneous evolution commitment of B1.13 implies that evolution governance must maintain continuous operational presence; the operational test structure formalizes what that continuous presence requires.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to cite this note

Li, W. (2026). *Operational Tests for Evolution Mechanisms (B1.12–B1.16): Five Deployment-Facing Tests Including Three Mechanisms Presence, Mutation Governance Instruments, Directed Selection Governance, Action-Feedback Pathway Integrity, and Bidirectional Evolution Configuration, Each With Question, Mechanism, Pass, Fail, and Remediation Signal.* May 13, 2026. ORCID: 0009-0004-8065-3235.
