# Anti-Pattern: External Tool State Treated as Authoritative — Standalone Formalization of the Failure Mode Where State in External Integrated Systems Operates as Authoritative for Coordination Questions, Violating Substrate-as-Source-of-Truth and Hybrid Composition Architecture in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize a standalone anti-pattern — *external tool state treated as authoritative* — as the failure mode in which state held in external integrated systems (third-party SaaS applications, external databases, integration platforms, external API services, external knowledge stores, external vector databases) operates as the authoritative source for coordination questions, instead of substrate. The note is the seventeenth in a Phase A3 series and the fourth of five anti-patterns in the cluster that addresses violations of substrate-as-source-of-truth (A1.08).

## Abstract

CKS commits to substrate as the source of truth for coordination (A1.08, decomposed across five categories at A2.42–A2.48) and to a closed set of three legitimate composition patterns by which substrates compose with adjacent AI components (A1.16, decomposed at A2.91–A2.95). Real deployments routinely integrate with existing operational systems — CRMs, ticketing, project management, integration platforms, external databases, vector stores, knowledge bases. The architecture permits this through Pattern A consultation (A2.92) and Pattern C separate concern (A2.94), but only when substrate remains the authoritative record. The anti-pattern is the configuration where the integrated tool's state instead becomes the authoritative source. This note specifies the anti-pattern through four operational components, identifies the commitments it violates (A1.08 and A1.16 simultaneously, with A1.05's tool-agnosticism uniquely extended-violated through vendor coupling, and cascade implications across A1.07, A1.10, A1.04, A1.01, and A1.13's Requirement E), traces the failure mode, specifies the correction through cell-mediated mirroring under rules, distinguishes four adjacent legitimate patterns, and provides an operational test with three sharpening properties.

## 1. Why the anti-pattern needs standalone formalization

A1.08 commits to substrate as authoritative across the five source-of-truth categories per A2.42–A2.48. A1.16 commits to three legitimate composition patterns — Pattern A consultation (A2.92), Pattern B derived view (A2.93), Pattern C separate concern (A2.94) — and rules out everything else as the composition anti-patterns named at A2.95. The two commitments are mutually reinforcing: hybrid composition is exactly how external tools enter a CKS deployment without breaking substrate's authoritative role.

The failure mode formalized here is the configuration where that mutual reinforcement breaks at a specific architectural seam. A deployment integrates with an external tool — entirely legitimate under A1.16 — but treats the tool's state as operationally authoritative for coordination questions. The intended Pattern A consultation, in which a cell consults the tool and writes the processed result into substrate, is replaced by direct downstream consultation of the tool. The intended Pattern C separate concern is replaced by operational coupling through which the tool's state effectively answers coordination questions. Substrate may continue to exist; for the affected categories, it is no longer the consulted source.

Standalone formalization is needed for three reasons. First, the configuration is operationally common in 2024–2026 AI deployments because integration with existing business systems is the dominant deployment posture; the anti-pattern can drift in by default. Second, A3.17 is the fourth in the A1.08 cluster (A3.14 agent memory, A3.15 LLM context, A3.16 hidden cell state, A3.18 caches); the siblings cover migration to inside-deployment locations, while A3.17 covers migration to external-to-deployment locations and carries unique risks the inside-deployment cases do not — asynchronous external state changes, service unavailability, API deprecation, vendor lock-in, multi-tenancy and access-control mismatches. Third, integration-architecture territory is more defensibly contested as prior art when the anti-pattern is publicly named.

## 2. The anti-pattern, defined precisely

A deployment exhibits *external-tool-state-treated-as-authoritative* if all four of the following operational components are present.

**Component 1 — External tool state holds coordination-scope content per A2.42–A2.48.** One or more external integrated systems hold state whose content falls into one or more of the five source-of-truth categories: "what is the case" (A2.43), "what is current" (A2.44), "what is in conflict" (A2.45), "what rules apply" (A2.46), "who has what authority" (A2.47). Operationally common forms include CRM customer records as "what is the case," ticketing state as "what is current," project-management task state as "what is current" or "what is in conflict," external knowledge store content and vector database retrievals as "what is the case," integration platform configuration as "what rules apply," and external identity systems as "who has what authority."

**Component 2 — External tool consulted as authoritative for coordination questions.** Coordination questions are routed to the external tool as the consulted source. Downstream operations — cells, orchestration logic, audit consumers, human-facing reads — query the external tool for authoritative answers. Substrate may exist nominally, but it is not the consulted source for the affected categories.

**Component 3 — External tool state wins over substrate when conflicts arise.** When external tool state and substrate state disagree, the external tool wins operationally. The deployment trusts the external tool by default and treats discrepancies as "substrate stale, tool fresh." The architectural commitment that substrate is the authoritative record per A1.08 fails specifically at the moment of conflict.

**Component 4 — External tool treated as the deployment's "system of record" for coordination.** The deployment positions the external tool as the authoritative record for coordination content — through architecture documentation, data-flow diagrams, governance policies, or operational practice. "System of record" is a positive enterprise-architecture concept, and its application to external tools for coordination content masks architectural failure as architectural alignment.

A deployment exhibiting all four components fully exhibits the anti-pattern; a strict subset is a warning condition that the operational test in §7 should resolve to either full exhibition or correction.

## 3. Which CKS commitments are violated

The anti-pattern violates A1.08 and A1.16 directly and simultaneously, with the remaining implications cascading from those two foundational failures.

**A1.08 (substrate is the source of truth) — directly violated.** The commitment that substrate is authoritative across the five categories per A2.42–A2.48 fails when external tool state is the consulted source. Whichever of A2.43 ("what is the case"), A2.44 ("what is current"), A2.45 ("what is in conflict"), A2.46 ("what rules apply"), and A2.47 ("who has what authority") the external tool holds, that category's substrate-authoritative commitment fails operationally.

**A1.16 (hybrid systems composition) — directly violated.** A2.92's Pattern A consultation requires that consultation outputs are processed by the consulting cell and written into substrate as the authoritative record (Property B per A2.20); A3.17 has consultation outputs operating as authoritative directly. A2.94's Pattern C separate concern requires that the external tool has no coordination-state coupling; A3.17 has coordination-state coupling. A2.95's composition anti-patterns are accordingly implicated.

**A1.05 (tool-agnosticism) — extended-violated.** Authority over coordination content depending on specific external vendor systems creates lock-in directly: API deprecation forces re-architecture, vendor migration requires re-architecting authority, and substitution of one vendor for another is no longer architecturally neutral. This violation is unique to A3.17 and distinguishes it from the inside-deployment siblings A3.14–A3.16.

**A1.13's Requirement E per A2.80 (human-selective composition) — extended-violated.** External tools operationally exercise authority outside whatever composition humans selected, because operational authority migrates to the tool independently of the selected composition pattern.

**A1.07 (path retraceability), A1.10 (determinism contract), A1.04 (AI-as-substrate-mediator), A1.01 (human-governed) — extended-implicated.** External state changes occurring asynchronously may not be retraceable through substrate per A2.40; the deterministic-substrate commitment per A1.10 fails outside the allowed categories of non-determinism per A2.62; LLMs treating tool state as authoritative inputs without substrate-mediated processing relax A1.04's substrate-locality constraint; and the inspect right per A2.01 applies to substrate, while authoritative content held in external tools sits under those tools' own access controls and governance models, operationally compromising the architectural mechanism of governance-through-substrate per A2.01–A2.04.

The dual A1.08+A1.16 violation is load-bearing: A3.17 requires correction at both the source-of-truth and composition layers because the same operational mechanism violates both.

## 4. The failure mode

External-tool-state-as-authoritative produces deployments where coordination authority depends on external systems the deployment does not architecturally control. The downstream consequences are largely unique to the external-locus character of the anti-pattern.

*Asynchronous external state changes producing substrate drift.* External tools change state without notifying the deployment. Substrate becomes out of sync with content the deployment treats as authoritative; the deployment runs with mismatched authoritative content invisibly, because downstream consumers read whichever source the architecture routes them to.

*Service unavailability, API deprecation, and vendor lock-in.* External tools may be down, slow, or rate-limited; coordination operations fail when the consulted source is unavailable. External services deprecate APIs over time; migration to a different vendor requires re-architecting authority. The architectural property that substrate is always-available authority — the property that lets cells operate and humans inspect under A2.01 regardless of external conditions — is lost, and coordination authority is contingent on a vendor's API roadmap. A1.05 is broken at the architectural layer where it is most consequential.

*Multi-tenancy and access-control mismatches.* External tools have their own access controls — user permissions, role-based access, tenant boundaries — that may differ from substrate's governance per A1.01. Who sees what authoritative content is determined by the external tool's ACLs rather than by the deployment's governance model; the inspect/modify/override rights apply to substrate, not to authoritative content held elsewhere under different rules.

*Mismatched authoritative content invisibly trusted.* When substrate says one thing and the external tool says another, the deployment trusts the external tool by Component 3; substrate becomes architecturally moot for the affected categories.

*Recovery from external tool errors operationally constrained.* When external authoritative content is identified as erroneous, recovery requires modifying the external tool — which may have its own change controls, audit requirements, or modification limits. The architectural commitment that the modify and override rights per A2.02 and A2.03 take effect as substrate state fails because the authoritative state is not substrate.

*Compounding with related anti-patterns.* When LLMs consult external tools and treat consultation outputs as authoritative, A3.17 compounds with A3.13 (LLM-as-source-of-truth); when cells embed external tool state internally, A3.17 compounds with A3.05 (cell-as-substrate). The compounding fragments authority across LLM context, cell internals, and external systems simultaneously.

*"System of record" framing masks the failure.* Deployment teams may resist correction because the external tool is positioned as a system of record — a positive enterprise-architecture concept. The architectural commitment is more specific: for *coordination* purposes, substrate is the system of record; external tools may be operational systems for other concerns, but coordination authority does not migrate to them.

## 5. The architectural correction

The correction operates through three foundational commitments together — A1.08, A1.16, and A2.04's rule-mediated cell processing — and is operationally tractable even for deployments with extensive external-tool dependencies.

**Substrate as single source of truth across the five categories.** The deployment commits to substrate as authoritative across A2.43–A2.47. Coordination questions are answered by consulting substrate, not external tools.

**Hybrid composition through A1.16's three patterns, with substrate-authoritative outputs.** External tools enter the architecture as Pattern A consultations per A2.92 or Pattern C separate concerns per A2.94. Pattern A consultation outputs become substrate state through cell processing per Property B per A2.20: the cell consults the external tool, processes the response under its orchestration rule per A2.04, records attribution per A2.40, and writes substrate state with the processed outcome. Pattern C separate concerns operate without coordination-state coupling.

**Cell-mediated mirroring of external tool state when reflection is needed.** When external state changes need to be reflected into substrate — for example, when CRM customer records change and the deployment's coordination depends on the change — cells perform mirroring operations under rules. The pattern is *external-tool-change → cell-mediated-mirroring → substrate-update*; substrate remains authoritative; the external tool is the upstream input, not the downstream authority. Mirroring may be triggered on demand or scheduled, but in both cases substrate is the consulted source for downstream operations.

**Coordination questions routed to substrate.** Downstream operations consult substrate as the authoritative source. Cells may consult external tools during their execution per Pattern A; the consultation result becomes substrate state through the cell's processing; consumers downstream of the cell consult substrate, not the tool.

**Operational distinction between operational systems and coordination authority.** External tools may remain operational systems for non-coordination concerns. A CRM may continue to be the operational system for customer relationship management; a ticketing system for ticket workflows. The correction does not require duplicating all external-tool state into substrate; it requires that for *coordination* questions, substrate is the consulted authority, with the necessary subset mirrored or processed into substrate by cells under rules. Because authority lives in substrate, vendor changes, API deprecations, and service migrations affect only the consulting and mirroring cells, not the authoritative state itself; A1.05 is preserved through the correction.

## 6. What external-tool-state-as-authoritative is NOT

The anti-pattern is commonly conflated with four adjacent legitimate patterns. The distinctions are precise.

*Not Pattern A consultation per A2.92 with substrate-authoritative outputs.* Pattern A has cells consulting external tools as adjacent components during execution, with the consultation rule-mediated, the cell processing the result, and substrate state written as the authoritative record. The anti-pattern arises specifically when consultation outputs become authoritative directly without cell-mediated processing into substrate.

*Not Pattern C separate concern per A2.94 with no coordination coupling.* Pattern C has external tools operating as separate concerns — for non-coordination purposes such as email sending, payment processing, notification delivery — without coordination-state coupling. The anti-pattern is the failure mode in which separation is broken by coordination-state coupling.

*Not substrate-mirrored external state with substrate as the authoritative version.* Deployments may mirror external tool state into substrate (periodic sync, on-demand fetch, event-driven update) when substrate is the authoritative version for coordination purposes. Mirroring with substrate-authoritative is legitimate; not mirroring (treating the external tool as authoritative) is the failure.

*Not external tools as informational sources with cell-mediated processing.* External tools may be informational sources — reference databases, computation services, knowledge stores — when their content is consulted by cells under rules and processed into substrate state. The anti-pattern arises specifically when external tools provide authoritative answers directly, without cell-mediation.

## 7. Operational test

A deployment exhibits external-tool-state-treated-as-authoritative if any of (a)–(d) below are operationally true at any time during the deployment's existence, and any of the three sharpening tests (e.1)–(e.3) confirms the diagnosis.

(a) External tool state contains content in one or more of the five source-of-truth categories per A2.43–A2.47, and that content is treated as authoritative for coordination questions.

(b) Coordination questions are answered from external tool state rather than substrate; downstream operations consult external tools as authoritative.

(c) When external tool state and substrate disagree, external tool state wins operationally.

(d) The deployment positions external tools as systems of record for coordination content.

(e.1) *External-state-locus test.* Verify operationally where authoritative content for coordination questions resides. Inspect what downstream operations consult; direct consultation of an external tool for authoritative answers, without substrate-mediation through Pattern A processing, indicates the anti-pattern.

(e.2) *External-vs-substrate-conflict-resolution test.* Verify operationally what wins under conflict. Examine cases in which external tool state and substrate disagree, and inspect which content downstream operations treat as authoritative. External tool winning indicates the anti-pattern.

(e.3) *External-state-substrate-mirroring test.* Verify whether external tool state changes are mirrored into substrate through cell-mediated operations under rules. Absence of mirroring (with downstream operations consulting the tool directly under change) indicates the anti-pattern.

A deployment satisfying any of (a)–(d) and any of (e.1)–(e.3) exhibits the anti-pattern. The correction per §5 specifies the operational changes required.

The one-sentence test condenses the diagnosis: if a deployment treats state in external integrated systems as authoritative for coordination questions, with external tool state winning operationally over substrate when conflicts arise and the external tool positioned as the system of record for coordination, the deployment exhibits external-tool-state-treated-as-authoritative; A1.08 and A1.16 both fail through the same mechanism, A2.92's or A2.94's boundaries are violated, A2.95's composition anti-patterns are implicated, and A1.05's tool-agnosticism is extended-violated through vendor coupling.

## 8. Conclusion

External-tool-state-treated-as-authoritative is the configuration in which state held in external integrated systems operates as authoritative for coordination questions, replacing substrate's role as the consulted source. The configuration violates A1.08 and A1.16 simultaneously through one operational mechanism, with A1.05's tool-agnosticism uniquely extended-violated through vendor coupling and cascade implications across A1.07, A1.10, A1.04, A1.01, and A1.13's Requirement E. The unique-to-A3.17 character — external-to-deployment locus, with risks of asynchronous state changes, service unavailability, API deprecation, vendor lock-in, and multi-tenancy mismatches — distinguishes it from the inside-deployment sibling anti-patterns A3.14, A3.15, and A3.16.

The correction is specific and tractable: substrate is the source of truth across the five categories per A2.42–A2.48; external tools enter the architecture as Pattern A consultations or Pattern C separate concerns per A1.16; cell-mediated mirroring under rules per A2.04 reflects external state into substrate where reflection is needed; substrate is the consulted source for downstream operations. The correction does not require duplicating all external-tool state into substrate; it requires that for coordination questions, substrate is the authoritative record. A3.17 is the fourth of five A1.08 cluster anti-patterns; the fifth, A3.18 (caches treated as authoritative), formalizes the final source-of-truth-migration location and closes the cluster.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235. Load-bearing sections for this note: §11.3 (substrate as source of truth), §6.2 (cost-curve distinction; "context rot" failure mode), §4.1 (substrate authority over coordination), §4.5 (hybrid system composition with adjacent components).

## How to cite this note

Li, W. (2026). *Anti-Pattern: External Tool State Treated as Authoritative — Standalone Formalization of the Failure Mode Where State in External Integrated Systems Operates as Authoritative for Coordination Questions, Violating Substrate-as-Source-of-Truth and Hybrid Composition Architecture in CKS.* May 6, 2026. ORCID: 0009-0004-8065-3235.
