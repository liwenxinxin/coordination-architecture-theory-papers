# Operational Timescale Treatment: Formalizing What It Means That CKS Bidirectional Evolution Operates on Operational Timescales

**Derivation Note B2.82 — Phase B2, Series B**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Paper 2's bidirectional evolution specification (B1.16) qualifies that bidirectional evolution operates "on operational timescales." The qualifier is architecturally load-bearing: it distinguishes CKS evolution from design-time-only evolution in conventional AI architectures. This note formalizes operational timescale treatment as a standalone architectural specification. Operational timescales denote the period during which a deployment is actively serving users — not design time, not initialization, but ongoing active operation. All three evolution mechanisms (instinct mutation per B1.13, directed selection per B1.14, action-feedback per B1.15) operate on these timescales. Governance per A1.01 also operates on these timescales — humans govern continuously during deployment operation, not only at design time. A6.14's long-lifecycle version compatibility addresses accumulation of evolution history over extended operation. A6.02's retroactivity treatment enables directed-selection DNA changes to take effect without disrupting ongoing service. The note states the treatment precisely, identifies what makes it architecturally distinctive against conventional batch-retraining approaches, articulates the biological analog of developmental plasticity as conceptual scaffold, specifies inherited Paper 1 commitments, enumerates operational implications, and states the limits of the operational-timescale claim.

---

## 1. Why operational timescale treatment needs to be formalized as standalone

Paper 2 specifies bidirectional evolution in B1.16 with the qualifier "on operational timescales." That qualifier does more architectural work than it appears to do. It is not a descriptor of cadence or speed. It is a specification of *when* evolution occurs: during active deployment operation, while the deployment is serving users, not only before it does. Without a precise formalization of this qualifier, the architectural distinctiveness of CKS bidirectional evolution from conventional AI evolution is understated, and the governance implications — that humans must be continuously governing, not governing once at design time — remain implicit rather than explicit.

This note occupies the fourth position in the five-note decomposition of B1.16: B2.79 established the bidirectional evolution frame; B2.80 specified horizontal evolution; B2.81 specified vertical evolution; B2.82 (this note) formalizes the operational timescale treatment that qualifies all of the above; and B2.83 will formalize bidirectional evolution verification. The four prior notes specify *what* can evolve and *in what direction*; this note specifies *when* evolution occurs and what that timing commitment entails architecturally.

As the eighty-second Phase B2 note, this note sits within the operational-variant-as-architectural-decomposition logic that governs Series B. The operational timescale treatment is an architectural commitment that must be named to be prior art: any subsequent attempt to claim novelty for "AI systems that evolve during deployment" or "continuous governance over deployed AI evolution" must contend with this formalization.

---

## 2. The architectural treatment precisely stated

**Operational timescales defined.** Operational timescales denote the period during which a CKS deployment is actively serving users. This period begins after the deployment is initialized and persists throughout the deployment's active life. It is not the design period (when architects specify the Self's structure), and it is not the initialization period (when the deployment is first instantiated with its initial DNA, cells, and aspects). The operational timescale is the ongoing period of active use, extending from the first user interaction to the last.

Evolution on operational timescales therefore means that the deployment's architecture can change — and is designed to change — while it serves users. This is not a claim about frequency. It is a claim about the window in which evolution is architecturally available.

**Three mechanisms operating on operational timescales.** All three evolution mechanisms specified in B1.13–B1.15 operate on operational timescales, though each has its own cadence within that window.

Instinct mutation per B1.13 operates on operational timescales because LLM vendor updates, infrastructure changes, and other upstream modifications arrive asynchronously during deployment operation. Mutation is not confined to planned retraining cycles; it can occur whenever the upstream LLM layer changes. Mutation detection — identifying that an upstream change has introduced behavioral drift in the instinct layer — is active during operation, not reserved for scheduled review windows.

Directed selection per B1.14 operates on operational timescales because governance authority over DNA content is available at any time, not only at design time. Human governors can identify, author, and apply DNA improvements during active deployment. The orchestration substrates that define cell behavior are themselves substrate content under the three rights specified in A1.01 — inspection, modification, and override — and those rights are available at all times during the substrate's existence, including during operational service.

Action-feedback per B1.15 operates on operational timescales because the action layer accumulates continuously during operation. Each cell execution against the substrate generates action-layer records. Proposing substrates evaluate that accumulation continuously. Governance reviews and approves action-feedback proposals during operation. The loop closes through governed substrate-edit operations that execute while the deployment serves users.

**Governance on operational timescales.** The most significant architectural implication of the operational-timescale qualifier is not that the three mechanisms operate during operation — it is that governance also operates during operation. A1.01's commitment to human-governed substrates includes the temporal property that governance rights are available at any time, not only at predetermined checkpoints. Applied to evolution, this means that governance reviews of mutation events, governance application of directed-selection DNA improvements, and governance approval of action-feedback proposals all occur during deployment operation.

This is a meaningful commitment beyond design-time governance. A deployment that specifies its architecture thoroughly at design time, initializes correctly, and is then left to operate without ongoing governance does not satisfy the CKS operational-timescale commitment. The commitment is that humans are continuously capable of governing, and that the governance machinery — verification substrate evaluation, DNA modification authority, action-feedback approval — remains active throughout operational life.

**Long-lifecycle version accumulation per A6.14.** Deployments that operate for extended periods — months or years — accumulate significant evolution history. Each directed-selection improvement creates a new DNA version. Each mutation event that passes verification integration creates a record in the evolution history. Each action-feedback cycle that produces an approved substrate change adds to the accumulation. A6.14's deployment-evolution rule version compatibility addresses the architectural challenges this accumulation creates. Long-lived deployments need version management machinery that tracks which rules governed which operations at what time, enabling governance review of the deployment's entire evolution trajectory. Version accumulation is manageable through version management specifications and retroactivity treatment; without this, long-lifecycle operational evolution becomes unmanageable.

**Non-disruptive operational evolution through A6.02 retroactivity.** A potential objection to operational-timescale evolution is that changes during operation would disrupt service. CKS addresses this through A6.02's retroactivity treatment. Directed-selection DNA improvements apply forward from the point of governance authorization without requiring rollback or replay of operations conducted under prior DNA versions. New DNA governs future cell executions; it does not destabilize the results of past executions already recorded in the substrate. Mutation integration follows verification and routing protocols designed to minimize disruption. Action-feedback proposal approvals take effect as substrate-edit operations that extend the substrate rather than replacing it. Operational evolution and operational continuity are compatible.

---

## 3. What makes operational timescale treatment architecturally distinctive

Conventional AI architectures — models trained, deployed, and operated until a future retraining cycle — have design-time-only evolution at the architectural layer. The model is trained with a fixed architecture and fixed weights, deployed into an operational environment, and then operates statically with respect to that architecture until the next retraining cycle. Evolution in this paradigm is batch: collect usage data, retrain, redeploy. Each retraining cycle requires operational disruption, either through service interruption or through a deployment transition that routes traffic to the new model. Governance of this evolution is also batch: architectural decisions are made before retraining, not continuously during operation.

CKS's operational-timescale evolution is continuous and non-disruptive. The three mechanisms do not require retraining cycles. Directed selection modifies orchestration substrate content without rebuilding the model layer. Action-feedback closes the loop through governed substrate modifications. Even instinct mutation — which corresponds most closely to the model layer — is handled through verification and routing protocols that absorb the change without the service disruption a full retraining cycle would require.

The governance-continuous commitment is the sharper distinction. Batch retraining architectures gate governance at the retraining decision point: a human (or team) decides to retrain, specifies training objectives, and reviews model outputs after retraining. Governance is episodic. CKS operational-timescale governance is continuous: governance rights are available at any time, evolution events are subject to governance at the moment they occur, and no evolution mechanism operates outside the governance boundary. The architectural commitment to continuous governance is what makes operational-timescale evolution architecturally distinct, not merely the ability to update during operation.

---

## 4. The biological analog: developmental plasticity

Biology supplies a conceptual scaffold for operational-timescale evolution in developmental plasticity: the capacity of organisms to continue developing, adapting, and modifying their organization throughout their lifetimes in response to experience and environment. Developmental plasticity — as engaged in evo-devo work on epigenetic modification, neural plasticity, and phenotypic accommodation — names the biological commitment that development is not complete at birth. Organisms develop throughout their operational lifetimes.

The biological analog is useful as conceptual scaffold because it names the general class of system that CKS instantiates: a system designed to continue evolving throughout its operational life, not only at initial configuration. Epigenetic modification in biology parallels directed selection in CKS: both modify the expression layer without modifying the underlying sequence. Neural plasticity in biology parallels action-feedback in CKS: both accumulate operational experience and modify organization in response. Instinct mutation in CKS is less cleanly analogous to any single biological mechanism, since biological mutation operates on reproductive timescales rather than within a single organism's lifetime.

The architectural substance, however, is not the biological analogy — it is continuous governed evolution during deployment operation. The analogy functions as reader scaffold that makes the architectural commitment intuitive; it does not carry the architectural specification. CKS operational-timescale evolution differs from biological developmental plasticity in the role of governance: biological developmental plasticity operates through natural processes without an external governing authority; CKS operational-timescale evolution operates under human governance at every evolution event. The governed-biological-analog-at-operational-timescales is what CKS commits to.

---

## 5. Inherited Paper 1 commitments

Several Paper 1 commitments are directly load-bearing for the operational timescale treatment.

**A1.01 (human-governed) as temporal commitment.** A1.01 specifies that governance rights — inspection, modification, override — are available at all times during the substrate's existence. Applied to operational-timescale evolution, this means governance must be available throughout the deployment's operational life, not only at design time or initialization. A1.01 is what makes the governance-on-operational-timescales claim architecturally grounded rather than aspirational.

**A6.14 (deployment-evolution rule version compatibility).** Long-lifecycle deployments accumulate DNA versions, mutation integration records, and action-feedback cycle histories. A6.14's version compatibility treatment addresses how deployments manage this accumulation without losing the ability to trace what governed what operation at what time. Version compatibility is the architectural response to the long-lifecycle implication of operational-timescale evolution.

**A6.02 (rule retroactivity).** The retroactivity treatment specifies how new DNA versions take effect relative to prior operations. Retroactivity without disruption — new rules apply forward, not backward — is the architectural mechanism that enables operational-timescale directed-selection evolution without operational disruption. A6.02 is the substrate-level commitment that resolves the apparent tension between evolving governance rules and continuing operational service.

**A2.40 (provenance requirements).** Every substrate modification — including those made through evolution mechanisms during operation — carries provenance per A2.40's six metadata requirements. Operational-timescale evolution events are therefore traceable: when a DNA improvement was made, by whom, under what governance authority, with what rationale. This makes operational evolution history inspectable by subsequent governors, not opaque accumulation.

**A1.07 (path retraceability).** A1.07's retraceability commitment applies across the entire evolution history accumulated during operation. A deployment that has operated for two years, accumulating dozens of DNA versions and hundreds of action-feedback cycles, retains full retraceability of the path through which its current state was reached. Operational-timescale evolution does not compromise retraceability; it extends the retraceability commitment to the operational window.

---

## 6. Operational implications

Operational-timescale evolution is a deployment management discipline, not only a deployment design discipline. The architectural commitment to continuous evolution under continuous governance has operational implications that extend beyond initial deployment planning.

**Governance capacity planning.** Deployments that commit to operational-timescale evolution must plan for continuous governance capacity. Governance reviews do not occur only at initialization; they occur as mutation events arrive, as directed-selection proposals are prepared, and as action-feedback cycles generate approval decisions. Deployment operators must maintain the human governance capacity to exercise review authority continuously, not episodically.

**Operational evolution monitoring.** Tracking what is changing during operation, at what rate, and through which mechanisms is an operational management activity under the operational-timescale commitment. Monitoring mutation events, DNA version progression, and action-feedback cycle completion rates gives deployment operators visibility into the evolution trajectory of their deployment.

**Long-lifecycle governance planning.** As deployments mature, their evolution histories accumulate. Governance teams reviewing a deployment after two years of operation face a different version management challenge than they faced at initialization. Long-lifecycle governance planning — periodic reviews of the deployment's cumulative evolution state, assessment of version compatibility, and decisions about DNA version retirement — is an operational management activity that the operational-timescale commitment makes necessary.

**Cross-partner governance per A2.47.** Deployments that involve multiple organizational partners require ongoing cross-partner governance as evolution proceeds. Directed-selection improvements proposed by one partner's governance authority, or mutation events that affect shared substrate content, require cross-partner governance review on operational timescales. The multi-human governance commitment from Paper 1 extends to cross-partner operational-timescale evolution governance.

---

## 7. Limits of the operational-timescale claim

The operational-timescale treatment has specific limits that prevent the claim from being read too broadly.

Operational-timescale evolution is NOT continuous automatic evolution. The CKS claim is that evolution CAN occur on operational timescales, through governed mechanisms that are available during operation. It is not a claim that evolution occurs continuously without governance. All three mechanisms require governance events to complete. Mutation detection must precede mutation integration. Directed-selection DNA improvements must be authored and authorized by human governors. Action-feedback proposals must be approved. No mechanism proceeds automatically without governance involvement.

Operational-timescale evolution is NOT unconstrained evolution. All three mechanisms remain bounded by their governance requirements and by the architectural commitments they inherit from Paper 1. Operational availability does not expand the scope of what can be changed or by whom.

Governance latency exists within operational timescales. "Available at any time" names the governance right, not the governance latency. A governance review may take days or weeks after a mutation event is detected before integration is authorized. Action-feedback proposals may accumulate for a governance review cycle before being approved. The operational-timescale claim is about architectural availability of governance, not instantaneous response. Evolution events occur at governance-determined cadences within the operational window, not instantaneously.

Operational-timescale evolution is NOT real-time learning. Real-time learning architectures update model weights continuously based on incoming data, without discrete governance events. CKS operational-timescale evolution operates through discrete, governed evolution events — each mutation integration, each DNA improvement, each action-feedback proposal approval — with human authority at each. The continuous character of CKS operational-timescale evolution is continuous *availability* of governed evolution, not continuous automatic weight updating.

Some deployments may evolve rarely on operational timescales. The claim is that CKS deployments CAN evolve during operation, not that they MUST evolve frequently. A deployment that operates for a year with a single directed-selection DNA improvement satisfies the operational-timescale commitment if that improvement occurred during operation under proper governance, even if the rate is low.

---

## 8. One-sentence test

A CKS deployment satisfies the operational timescale treatment if and only if: all three evolution mechanisms (instinct mutation, directed selection, action-feedback) are available to execute under human governance at any point during active deployment operation, and governance authority over all three mechanisms is available throughout that same period, without requiring operational shutdown, retraining cycle, or design-time intervention to enable any individual evolution event.

---

## 9. Why naming as standalone matters; position in Phase B2

The operational timescale treatment occupies prior-art territory that is architecturally significant and patent-relevant in its own right. Specifically: the conjunction of (i) all three evolution mechanisms available during active deployment operation, (ii) governance available continuously throughout operation rather than only at design time, (iii) non-disruptive operational evolution enabled through retroactivity treatment, and (iv) long-lifecycle version compatibility for accumulated evolution history — this four-part conjunction is the architecture that B2.82 names as prior art. No component of this conjunction is individually novel; the architecturally distinctive claim is the conjunction under unified human governance throughout operational life.

B2.82 is the fourth of five notes decomposing B1.16. B2.79 established the bidirectional evolution frame — the two axes (horizontal and vertical) that bidirectional evolution operates across. B2.80 specified horizontal evolution in detail. B2.81 specified vertical evolution in detail. B2.82 (this note) formalizes the operational timescale treatment that qualifies all of the above. B2.83 will complete the decomposition by formalizing bidirectional evolution verification. After B2.83, subsequent Phase B2 notes will decompose B1.17 relational roles beginning at approximately B2.84.

This decomposition logic — completing one parent note's decomposition before moving to the next — is the structural commitment that makes Phase B2 a coherent research record rather than an unordered collection of derivations. The prior-art chain from B1.16 through B2.79–B2.83 is the complete architectural specification of bidirectional evolution in CKS: what bidirectionality means (B2.79), how horizontal evolution works (B2.80), how vertical evolution works (B2.81), when evolution occurs (B2.82), and how evolution correctness is verified (B2.83). Any subsequent architecture claiming novelty in governed bidirectional AI evolution at operational timescales must engage all five notes in this chain.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Timescale Treatment: Formalizing What It Means That CKS Bidirectional Evolution Operates on Operational Timescales.* Derivation Note B2.82, CKS Theory Series. May 12, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
