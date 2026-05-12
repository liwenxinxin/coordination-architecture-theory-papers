# Ungoverned Mutation: The Anti-Pattern That Arises When LLM Version Changes Are Integrated Without the Three Mutation Governance Instruments per B1.13

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Instinct evolution — the mechanism by which LLM version changes sharpen what a cell can do at the instinct layer — is undirected from the Self's perspective: capability may improve or degrade in any specific case. The CKS commitment B1.13 holds that mutation is not left unmanaged; it is governed through three instruments that together convert undirected change into controlled integration. Those instruments are verification gates (confirming behavioral compatibility with cell DNA specifications before new LLM versions reach production), routing patterns (enabling gradual or partial deployment so that problems surface in bounded scope), and pinning (protecting high-stakes decisions from instinct-layer behavioral variation regardless of what LLM version changes arrive). Ungoverned Mutation is the anti-pattern that emerges when one or more of these instruments is absent. It takes three recognizable forms corresponding to the three missing instruments: Verification-Skipped Mutation, where new LLM versions are deployed without behavioral testing; Unrouted Mutation, where all cells simultaneously consume new LLM versions with no controlled rollout; and Unpinned Mutation, where governance-critical decisions are exposed to instinct-layer change without architectural protection. This note names and formalizes each form, traces the emergence conditions and operational consequences, and specifies detection through the B2.66 mutation governance verification together with per-instrument checks, with remediation through configuring all three instruments under the authority architecture B1.13 requires.

---

## 1. The Commitment: B1.13 Mutation Governed Through Verification, Routing, and Pinning

B1.13 establishes that instinct evolution — the mutation-like mechanism in the CKS evolutionary architecture — is not simply accepted as an upstream dependency upgrade. When an LLM provider releases a new model version, what arrives at the cell boundary is a behavioral change whose specific effects on any given cell's DNA-governed behavior are unknown until tested. The LLM provider may have improved general capability; it may have changed reasoning patterns in ways that interact with a cell's DNA rules; it may have introduced regressions on the specific task profiles a cell handles. None of this is knowable in advance from the version release notes alone.

B1.13 holds that the appropriate response to this uncertainty is not to block instinct evolution — doing so would sacrifice the capability gains that make mutation-like evolution valuable alongside the directed mechanisms — but to govern it. The governing instruments B1.13 commits to are three.

The first is verification gates, specified at the operational level by B2.06. A verification gate is a behavioral test suite that a new LLM version must pass before it is deployed to production cells. The gate evaluates the new LLM's outputs against the DNA rules that govern each cell type, confirming that the behavioral changes the new version introduces are compatible with the specifications the cell is committed to meeting. Without a verification gate, the deploying architecture has no basis other than vendor assurance for confidence that the new version is safe to integrate.

The second is routing patterns, specified by B2.04. A routing pattern governs which cells use which LLM version at any given moment during a mutation event. Rather than switching all cells simultaneously to the new version, routing enables partial deployment — some cells receive the new version while others continue on the prior version — so that behavioral changes surface in bounded scope where they can be detected and reversed without affecting the full system. Routing also enables the specific recovery pattern of routing around bad instinct: when a new LLM version produces problematic behavior in a cell, routing rules allow that cell to fall back to the prior version without system-wide rollback.

The third is pinning, governed through high-stakes identification per B2.05. Pinning is the architectural decision to protect specific decisions — those carrying high governance consequence, regulatory weight, or irreversibility risk — from instinct-layer behavioral variation. A pinned decision is handled through the reasoning layer regardless of what the instinct layer would produce, and regardless of what LLM version changes arrive. Pinning is configured through DNA rule authoring: the cell's DNA specifies that this category of decision bypasses instinct-layer processing. Without pinning, the highest-stakes decisions a Self handles are exposed to exactly the behavioral uncertainty that makes mutation governance necessary.

Together these three instruments implement what B1.13 names as governed instinct evolution: capability gains arrive, but they arrive under human-controlled conditions. B2.61 specifies an LLM model update as a mutation event that triggers the governance machinery. B2.62 addresses mutation detection as the prerequisite for governance — the event must be recognized before the instruments can be applied. B2.66 provides mutation governance verification as the check that confirms all three instruments are configured and operational after a mutation integration.

---

## 2. The Anti-Pattern: Ungoverned Mutation

Ungoverned Mutation names the failure mode that results when a mutation event per B2.61 is integrated without one or more of the three B1.13 governance instruments. The anti-pattern has three distinct forms. Each form corresponds to the absence of exactly one instrument; a deployment can exhibit one, two, or all three forms simultaneously.

The distinction from B3.13 (Single-Mechanism Evolution) matters here. B3.13 addressed the broader failure where the evolutionary architecture lacks all three evolution mechanisms — instinct evolution, directed selection, and action-feedback — reducing to a single mechanism. Ungoverned Mutation operates at a narrower scope: within instinct evolution specifically, it addresses the absence of the per-instrument governance machinery that B1.13 requires. A deployment could have all three evolution mechanisms present while still exhibiting Ungoverned Mutation if the mutation governance instruments for instinct evolution are absent.

---

## 3. Recognizable Forms

### Form 1: Verification-Skipped Mutation

Verification-Skipped Mutation is the form in which a new LLM version per B2.61 is integrated without running verification gates per B2.06. The new LLM version is deployed directly to production cells without behavioral testing against the DNA specifications those cells carry. The integration event proceeds as a dependency upgrade — the software artifact is updated, the new version becomes active — without any governance gate interposing between version change and production deployment.

Recognition signals are specific. No verification event records per A2.40 appear in the substrate preceding the LLM version change: the governance record that would document what was tested and what passed is absent. B2.66 mutation governance verification, when run, identifies the verification instrument as unconfigured: there are no verification suites associated with the cell types affected by the mutation event. After the LLM update, cell behaviors change in ways observable through substrate outputs, but no prior behavioral testing established what changes were expected or acceptable. The divergence between expected and actual behavior — if it is detected at all — surfaces through operational failures rather than through governance machinery.

The causal structure is important to state precisely. The verification gate's function is not to certify that the new LLM version is superior in general; it is to confirm that the new version is compatible with the DNA specifications this specific cell is committed to meeting. A new LLM version that improves general capability may simultaneously degrade a cell's specialized performance on the task profiles its DNA rules govern. Vendor testing covers neither the cell's specific task profile nor the cell's DNA rules; it covers the vendor's own evaluation criteria. Verification-Skipped Mutation outsources the compatibility question to the vendor and accepts the answer implicitly by deploying without testing.

### Form 2: Unrouted Mutation

Unrouted Mutation is the form in which a new LLM version is integrated and immediately all cells route to it, with no routing adaptation per B2.04. There is no partial deployment, no canary-style introduction to a subset of cells, no period during which the prior LLM version remains available as a fallback. The mutation event is instantaneous from the architecture's perspective: at one moment all cells use the old version, and at the next all cells use the new version.

Recognition signals are specific. Routing rules per B2.04 are absent or uniformly configured to always use the current LLM version regardless of verification status. B2.66 mutation governance verification, when run, identifies the routing instrument as unconfigured: there are no routing rules that differentiate cells by verification status, deployment stage, or LLM version assignment. Behavioral changes from the LLM update affect all cells simultaneously. If the new version produces problematic outputs in any cell, there is no architectural mechanism to restore that cell to prior-version behavior without reverting the entire LLM deployment — which affects all cells, including those where the new version was performing acceptably.

The routing instrument is what makes mutation reversible in practice. Verification gates answer whether the new version is safe to deploy; routing answers how it is deployed so that recovery remains possible if verification was wrong or incomplete. An architecture without routing has implicitly committed to all-or-nothing mutation integration: success or failure is system-wide, not cell-bounded.

### Form 3: Unpinned Mutation

Unpinned Mutation is the form in which LLM version changes affect high-stakes decisions because pinning per B2.05 is not configured. The cells handling high-stakes decisions have no DNA rules that route those decisions through the reasoning layer regardless of instinct-layer outputs. Governance-critical decisions — those carrying regulatory consequence, irreversibility risk, or authority-boundary significance — are processed through the instinct layer and are therefore exposed to whatever behavioral changes arrive with LLM version updates.

Recognition signals are specific. B2.05 high-stakes identification is absent from the architecture: no process has classified decisions by governance consequence and established which decision categories require architectural protection. Cells handling high-stakes decisions have no pinning rules in their DNA per B2.25. B2.66 mutation governance verification, when run, identifies the pinning instrument as unconfigured: high-stakes decision types are not classified and not protected. When LLM version changes arrive, the behavioral outputs for high-stakes decision categories change in ways that governance has not reviewed and may not detect.

Unpinned Mutation has a distinctive property that separates it from the other two forms: it is not merely about the risk that a mutation event goes wrong. It is about the structural condition in which the highest-consequence decisions the Self handles are permanently subject to instinct-layer variation, regardless of whether verification and routing are otherwise functional. Even a well-verified, carefully routed LLM update changes instinct-layer behavior. Pinning is the commitment that certain decisions will not be governed by instinct-layer variation at all, whatever the verification result confirms.

---

## 4. Emergence Conditions

Three conditions produce Ungoverned Mutation in practice. They are distinct, can operate independently, and each is sufficient to produce at least one form of the anti-pattern.

**Simplicity preference.** Mutation governance instruments require architecture investment before they yield protection. Verification suites must be authored per cell type; routing rules must be designed and tested; high-stakes decision classification must be performed and encoded in DNA. These costs are paid before any mutation event occurs. When architects are under time or resource pressure, or when the organization treats AI infrastructure as a productivity tool rather than a governed system, the investment in mutation governance instruments is deferred. The LLM update is treated as a dependency upgrade analogous to a library version bump: apply the change, trust the vendor's release notes, and monitor for obvious failures. This simplicity preference produces all three forms simultaneously by treating governance as optional overhead rather than as architectural commitment.

**Vendor trust.** Commercial LLM providers run extensive evaluation programs before releasing new model versions. Architects who are aware of this testing may conclude that their own verification gates are redundant — that the provider's quality assurance is sufficient to confirm the new version is safe for their cells. The error in this reasoning is the scope mismatch described above: vendor testing evaluates general capability against vendor-defined criteria; it does not evaluate behavioral compatibility with the specific DNA rules governing each cell. Vendor trust produces Verification-Skipped Mutation specifically, because the rationale targets the verification instrument while leaving routing and pinning underspecified.

**Absent high-stakes oversight.** Unpinned Mutation requires a distinct emergence condition: the organization has not performed the classification work that identifies which decisions are governance-critical. High-stakes oversight requires someone with governance authority to ask which decisions, if their behavioral outputs changed unexpectedly, would produce regulatory exposure, operational irreversibility, or authority-boundary violations. If no one has asked this question — or if the answer has not been translated into DNA rule authoring — the pinning instrument has no substrate content to operate on. Absent high-stakes oversight is not the same as simplicity preference: an organization may invest in verification and routing while still failing to classify decisions by governance consequence, leaving the pinning instrument configured for no decision category.

---

## 5. Operational Consequences

**Silent behavioral drift.** Without verification gates, LLM updates change cell behavior in ways that may violate DNA specifications without producing immediately detectable operational failures. A cell whose DNA rules require specific output structures, specific reasoning patterns, or specific decision criteria may produce outputs that look superficially correct while subtly diverging from what the rules require. The divergence is silent because no governance machinery is testing for it. It surfaces — if it surfaces — through downstream operational failures, user complaints, or audit findings, at which point the causal connection to an LLM version change may be difficult to reconstruct.

**High-stakes exposure.** Without pinning, governance-critical decisions are exposed to instinct-layer behavioral changes with each mutation event. Regulated decisions may produce different outputs after an LLM update without governance awareness. In some regulatory contexts, this means that the architecture is making compliance representations it cannot support: if a regulator asks whether the decision logic applied to a specific governance-critical determination is stable, documented, and human-reviewed, the honest answer in an unpinned architecture is that the decision logic changes whenever the LLM version changes, that this is not recorded as a governance event, and that no human reviewed the decision-logic change before it took effect.

**Rollback incapacity.** Without routing rules, there is no architectural mechanism to route individual cells back to the prior LLM version if the new version produces problems. All cells are simultaneously affected by the mutation event, and all cells must simultaneously revert if rollback is needed. This makes the cost of discovering a post-deployment problem very high: rollback affects not only the cells where the problem was found but every cell using the LLM, including those where the new version was performing correctly. The architecture has no scalpel; it has only a system-wide switch.

**Audit failure.** Without mutation governance records, compliance auditors cannot determine what behavioral changes LLM updates introduced and when. The substrate does not carry the verification event records that would document which behaviors were tested, what the test results were, and what governance decision authorized the mutation event to proceed. When audit requires the organization to demonstrate that its AI-assisted decisions were produced by systems operating within governed parameters, an ungoverned mutation architecture cannot satisfy the requirement because the governance events that would establish the parameters did not occur.

---

## 6. Detection

**B2.66 mutation governance verification.** The primary detection mechanism runs B2.66, which asks whether all three mutation governance instruments are configured. The verification query is structured around three sub-checks that correspond to the three B1.13 instruments. A finding that any instrument is absent confirms the anti-pattern in the form corresponding to that instrument.

**B2.06 verification gates check.** For each cell type affected by LLM mutation events, ask: does a verification suite exist that tests behavioral compatibility with that cell's DNA specifications? If not, Verification-Skipped Mutation is present or imminent. The check is structural — it examines substrate configuration, not deployment history — and can be run without waiting for a mutation event to occur.

**B2.04 routing rules check.** Ask: do routing rules exist that specify LLM version routing per cell, and do those rules provide for partial deployment and fallback to prior LLM versions? If routing rules are absent or uniformly configured to always use the current version, Unrouted Mutation is present or imminent. The check is again structural, examining whether the routing architecture is capable of differentiated deployment.

**B2.05 pinning configuration check.** Ask: has high-stakes decision classification been performed, and do the DNA rules of cells handling high-stakes decisions include pinning rules that route those decisions through the reasoning layer? If high-stakes identification is absent or if no pinning rules exist in the DNA of cells handling governance-critical decisions, Unpinned Mutation is present. This check requires examining both the classification record and the DNA rule content of the relevant cells.

A clean B2.66 result — confirming all three instruments are configured — does not guarantee that the instruments are correctly implemented, only that they are present. Where mutation governance is newly configured, additional validation through a simulated or low-stakes mutation event is warranted before relying on the instruments under a production mutation event.

---

## 7. Remediation

Remediation addresses each missing instrument in turn, following the authority architecture B1.13 requires.

**Configure verification gates per B2.06 through directed selection per B1.14.** For each cell type, develop a verification suite that tests behavioral compatibility with that cell's DNA rules. The suite should cover the specific output structures, decision criteria, and reasoning patterns the DNA rules govern. Verification suites are themselves substrate content — they are governed through the same authority architecture as other DNA content and can be updated as DNA rules change. Directed selection per B1.14 provides the governance mechanism for verifying that the verification suites themselves remain current with the DNA specifications they test.

**Establish routing rules per B2.04 for LLM version management.** Configure routing rules that specify which LLM version each cell uses during a mutation event. At minimum, routing rules should enable partial deployment (some cells receive new versions before others), fallback (cells can route back to prior LLM versions if verification-confirmed problems emerge post-deployment), and staged rollout (new versions expand to additional cells as confidence accumulates). Routing rules are DNA content and are governed through the standard authority architecture.

**Identify high-stakes decisions per B2.05 and implement pinning through DNA rule authoring.** Perform the governance classification work that identifies which decision categories, if their behavioral outputs changed, would produce regulatory exposure, irreversibility risk, or authority-boundary violations. For each classified category, author DNA rules in the cells handling those decisions that route the decision through the reasoning layer regardless of instinct-layer processing. Pinning rules are permanently active, not triggered by mutation events — they protect high-stakes decisions from instinct-layer variation continuously, not only during governance events.

**Run B2.66 mutation governance verification after configuration.** After all three instruments are configured, run B2.66 to confirm that the anti-pattern conditions are no longer present. Where the architecture is preparing for an upcoming mutation event, B2.66 should be run as a pre-event check before the LLM version change is applied, not after.

---

## Summary

Ungoverned Mutation is the anti-pattern that results from treating LLM version changes as dependency upgrades rather than as governance events per B2.61. B1.13 commits to governing mutation through three instruments: verification gates that confirm behavioral compatibility before deployment, routing patterns that enable controlled rollout and recovery, and pinning that protects high-stakes decisions from instinct-layer variation permanently. When any instrument is absent, the corresponding form of the anti-pattern is present: Verification-Skipped Mutation, Unrouted Mutation, or Unpinned Mutation. The consequences compound — silent behavioral drift, high-stakes exposure, rollback incapacity, and audit failure — in proportion to how many instruments are missing. Detection runs through B2.66 mutation governance verification together with per-instrument structural checks. Remediation configures all three instruments under the authority architecture that B1.13 requires, converting mutation from an ungoverned dependency change into a governed capability integration event.

---

*This derivation note is part of the CKS Derivation Notes series, a defensive publication program formalizing patentable architectural derivations from the CKS theory papers as public prior art. Each note is deposited to Zenodo under CC BY 4.0.*
