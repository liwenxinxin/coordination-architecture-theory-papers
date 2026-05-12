# Proposing Substrate Operational Specification: Formalizing the Evidence-to-Proposal Artifact in Action-Feedback Evolution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to articulate, in operational form, the precise architectural specification of the *proposing substrate* — the governed substrate artifact through which action-feedback evolution per B1.15 operationalizes the evidence-to-proposal function — so that downstream work can adopt or argue against the specification without ambiguity.

## Abstract

Action-feedback evolution (B1.15) closes the loop from recorded operational experience back into governed DNA refinement. Paper 2 specifies that this loop operates through substrates that propose DNA changes from action evidence. This note formalizes the proposing substrate as the architectural artifact that performs that function. A proposing substrate is substrate-resident authoritative content per A2.46 Category 4, authored per A2.04, and subject to Stage 1 human governance per B1.15. Its content specification covers five elements: evidence scope, pattern detection logic, threshold specification, proposal generation rules, and proposal format. Its operational sequence comprises five steps: evidence ingestion, pattern matching, threshold evaluation, proposal generation, and proposal recording per A2.40. LLMs per A1.12 may execute any of these operations as allocated labor; governance over the substrate artifact remains human throughout. Proposing substrates exist at every structural level — cell, aspect, Self — per B1.20 recursive inheritance. The architectural distinctiveness of the specification is that it makes the feedback mechanism an explicit governed artifact subject to the same authority framework as all other substrate content, rather than implicit automated infrastructure outside governance reach. A deployment without proposing substrates cannot instantiate action-feedback evolution; the proposing substrate is necessary, not optional. This is the seventy-fourth note in Phase B2 of Series B, the second of six notes decomposing B1.15.

---

## 1. Why Proposing-Substrate Operational Specification Merits Standalone Formalization

Action-feedback evolution per B1.15 commits to a specific architectural claim: the loop from action evidence to DNA change is governed and human-mediated rather than autonomous. Paper 2's "Governance shapes across evolution mechanisms" section states this directly — action-feedback is governed through humans governing the substrates that propose DNA changes from action evidence and approving the changes. The architectural claim contains two parts: (a) there are substrates that propose DNA changes from action evidence, and (b) humans govern those substrates. Part (b) is the governance commitment inherited from Paper 1 per A1.01. Part (a) names a specific artifact: the proposing substrate. What that artifact is, what it contains, how it operates, and what governs it are not incidental details. They are the substance that makes action-feedback evolution architecturally real rather than programmatic declaration.

Formalizing the proposing substrate as a standalone operational variant serves two purposes in the Phase B2 program. First, it makes the artifact explicit in the prior-art record. Any party that implements governed feedback substrates — substrate-resident artifacts that read action evidence, apply authored evaluation logic, and generate DNA change proposals for human approval — is operating within territory this note establishes as prior art. Second, it sets the foundation for the five subsequent notes decomposing B1.15: two-stage human mediation per B2.75 and the proposal pathway, action-feedback vs. directed selection distinction, and verification per B2.76–B2.78 all presuppose that a proposing substrate exists with the specification this note establishes.

The note sits at position seventy-four within Phase B2 and second within the six-note B1.15 decomposition, following B2.73's formalization of the action evidence evaluation mechanism that feeds proposing substrate ingestion.

---

## 2. The Proposing Substrate: Architectural Specification

### 2.1 Definitional properties

A proposing substrate is defined by four co-present architectural properties.

**Substrate-resident per A1.08.** The proposing substrate is content within the CKS substrate, not external code, configuration file, or middleware outside governance reach. Substrate residency means the proposing substrate is subject to the same persistent structured state properties, human read/write access requirements, and LLM access specifications that A1.08 establishes for all substrate content. It exists as a first-class substrate artifact, not as background infrastructure.

**Authoritative content per A2.46 Category 4.** Proposing substrates fall within Category 4 of A2.46's authoritative content classification — content that specifies "what rules apply." A proposing substrate specifies what patterns in action evidence are significant, what threshold strength triggers a proposal, and what DNA changes a detected pattern should produce. These are rule specifications governing a class of substrate operations. They are authoritative in the same sense orchestration rules are authoritative: they determine how the system behaves across every execution that follows from them.

**Authored per A2.04.** Humans author proposing substrates. Authoring specifies the evaluation logic, evidence patterns, threshold parameters, and proposal generation rules the substrate will apply. This is not configuration of a third-party tool; it is the exercise of rule-authoring authority that A2.04 establishes as foundational. As with orchestration rules, LLM-drafted proposing substrate content subject to human authority before taking effect is admissible; content committed outside human authority is not.

**Subject to Stage 1 governance per B1.15.** Stage 1 governance is the human governance of the substrates that propose DNA changes — as distinct from Stage 2 governance, which is human approval of specific proposals those substrates generate. Humans governing the proposing substrate directly determine what the substrate examines, how it evaluates evidence, what patterns it treats as significant, and what proposals it generates. Stage 1 governance is not a checkpoint at proposal review time; it is ongoing authority over the substrate artifact that produces proposals.

### 2.2 Content specification

A proposing substrate contains five elements.

**Evidence scope specification.** The proposing substrate specifies which cells' Action layer records are examined, what time window those records span, and what record types are included. Evidence scope is authored: it is not automatically determined by the substrate's structural position but by the human authors who specify what operational experience is relevant to the evaluation purpose this proposing substrate serves.

**Pattern detection logic.** The proposing substrate contains authored rules specifying what patterns in ingested Action evidence are significant. A pattern might describe a class of outcomes (repeated failures of a particular rule application, consistent latency above threshold, unexpected conflict frequency) that the substrate is designed to detect. Pattern detection logic is categorical authored content, not emergent analysis — it encodes what human governance has determined warrants a proposal.

**Threshold specification.** The proposing substrate specifies what evidence pattern strength triggers proposal generation. Threshold specification prevents noise from generating unnecessary proposals: not every detected pattern produces a proposal, only patterns meeting the authored threshold criteria. Thresholds are substrate content subject to governance modification as operational understanding develops.

**Proposal generation rules.** The proposing substrate specifies how to convert a detected pattern meeting threshold criteria into a DNA change proposal. Proposal generation rules specify what DNA elements to target, what the proposed change should be, and how to frame the proposal for human governance review. These rules operationalize the evidence-to-proposal function in the concrete form human governance will evaluate at Stage 2.

**Proposal format specification.** The proposing substrate specifies how proposals are structured for Stage 2 governance review per B2.75. Format specification ensures that proposals produced by the substrate are legible to the human governance process that must evaluate them. Format is substrate content — it is authored and goverable, not fixed by system implementation.

### 2.3 Operational sequence

A proposing substrate performs five operations.

**Evidence ingestion.** The proposing substrate reads from Action layer records per its evidence scope specification. Ingestion is bounded by the authored scope: the substrate reads what its specification designates, not the full Action layer indiscriminately.

**Pattern matching.** The proposing substrate applies its pattern detection logic to ingested evidence. Pattern matching may be computationally simple (rule-based matching against authored pattern templates) or may involve complex recognition over large evidence sets. LLMs per A1.12 are available as labor for complex pattern matching where authored logic alone is insufficient.

**Threshold evaluation.** The proposing substrate evaluates whether matched patterns meet the authored threshold criteria. Patterns meeting threshold proceed to proposal generation; patterns below threshold do not. The threshold evaluation step is auditable — it applies authored criteria to detected patterns and produces a traceable determination.

**Proposal generation.** The proposing substrate produces DNA change proposals from patterns meeting threshold criteria, applying its proposal generation rules. Each proposal specifies the DNA change proposed, the evidence that triggered the proposal, and the pattern logic that connected them. LLMs per A1.12 may perform proposal generation for proposals requiring complex articulation.

**Proposal recording.** The proposing substrate records generated proposals per A2.40's six provenance metadata fields: what was proposed, who (or what substrate) proposed it, under what authority, with what rationale, at what time, with what evidence basis. Provenance recording makes proposals traceable through the Stage 2 governance process and auditable after the fact.

### 2.4 LLM operations and the labor/governance distinction

LLMs per A1.12 may perform any of the five operations described above — evidence ingestion, pattern matching, threshold evaluation, proposal generation, and proposal recording — as allocated labor under human direction. The availability of LLM labor for complex pattern recognition is architecturally important: Action layer evidence at scale may exhibit patterns that authored rule-matching alone cannot efficiently detect. LLM-performed pattern matching under authored proposing substrate direction is consistent with the architecture.

What LLM performance of these operations does not change is governance. The proposing substrate itself — its evidence scope specification, its pattern detection logic, its threshold specification, its proposal generation rules, its format specification — is authored by humans and subject to Stage 1 human governance. LLMs operate within the substrate's authored specification; they do not govern the substrate. The labor/governance distinction established across the Series B decomposition notes holds fully here: LLMs perform operations, humans govern the artifacts that structure those operations.

### 2.5 Recursive deployment per B1.20

Proposing substrates exist at every structural level per B1.20's recursive inheritance commitment. Cell-level proposing substrates examine cell DNA and cell Action records and propose cell DNA changes. Aspect-level proposing substrates examine aspect-level orchestration content and propose aspect DNA changes. Self-level proposing substrates examine Self-level structure and propose Self DNA changes. Each level's proposing substrate is authored and governed at that level by the humans with authority at that scope. The specification in §2.1–2.4 applies at every level; what varies is the scope of evidence, the DNA elements targeted, and the human governance authority exercised.

---

## 3. Architectural Distinctiveness: Governed Artifact vs. Implicit Automation

The proposing substrate's architectural distinctiveness becomes clear against the alternative. Conventional AI feedback mechanisms — the pathway from system usage to model or configuration improvement — typically operate as implicit automated infrastructure. Usage data flows through processing pipelines; patterns are detected by analytics systems; training signals are generated by automated processes; model parameters update through automated cycles. At no point in this conventional pathway does there exist a "proposing substrate" as a first-class artifact: authored content specifying what patterns matter, what thresholds trigger action, and how patterns become proposals. The feedback mechanism is architectural background, not governed foreground.

CKS makes the feedback mechanism explicit and governed. The proposing substrate is a substrate artifact, subject to the same governance framework — the same A2.01 inspect, A2.02 modify, A2.03 override, A2.04 rule-authoring affordances — as any other substrate content. The feedback loop exists in the substrate, not around it. This means that what the feedback loop considers evidence, what it detects as significant, what it proposes as DNA change, and how it formats those proposals for governance review are all under the same governance authority that governs the substrate's other content.

The implication extends beyond individual proposal cycles. Because proposing substrates are substrate content, they are themselves subject to modification and evolution. As operational experience accumulates and understanding of which evidence patterns predict DNA improvement develops, humans modify the proposing substrate — updating its pattern detection logic, adjusting its thresholds, refining its proposal generation rules. This meta-evolution is governed directed selection operating on the substrate that governs evidence-to-proposal cycles. The governed artifact is not static infrastructure; it is a governed artifact that evolves under the same governance framework it instantiates.

---

## 4. The Biological Analog as Conceptual Scaffold

Paper 2 positions action-feedback evolution against West-Eberhard's plasticity-first framing from evolutionary biology: phenotypes leading genotypes via environmental induction, with subsequent genetic accommodation. The structural shape — operational state shaping what is later stabilized — is close to what CKS action-feedback evolution commits to.

Within this framing, the proposing substrate has a biological analog in molecular regulatory mechanisms. Specific molecules — transcription factors, signaling proteins, regulatory RNA — sense environmental and cellular conditions and initiate cascades that affect gene expression, and in some cases initiate processes that influence heritable genetic change over generational time. These regulatory mechanisms are the biological analog of the proposing substrate: they translate operational (environmental, cellular) conditions into signals that interface with genetic material.

The analog functions as conceptual scaffold, not architectural derivation. Two properties of CKS proposing substrates exceed what biology has:

First, biological regulatory mechanisms are not governed artifacts. They evolved; they are not authored. They cannot be modified by an authority that specifies what they detect or what they propose. CKS proposing substrates are authored content, subject to modification, override, and refinement under human governance authority. The governance layer is the architectural addition that makes the analog productive without making it exact.

Second, biological genetic accommodation operates through selection over populations over generations. CKS proposing substrates generate proposals that humans approve or reject in discrete governed cycles. The loop is discrete and auditable rather than statistical and multi-generational. The proposing substrate's proposal recording per A2.40 makes each cycle traceable; biology has no equivalent.

The architectural substance of the proposing substrate is the governed substrate artifact that mediates between accumulated operational experience and DNA evolution — with authorship, governance, and provenance properties that biology does not provide.

---

## 5. Inherited Paper 1 Commitments

The proposing substrate's architectural specification inherits and applies the following Paper 1 commitments directly.

**A1.08 — Substrate is source of truth.** Proposing substrates are substrate content. The evidence scope, pattern logic, threshold specification, proposal rules, and format specification the substrate contains are authoritative substrate state, not external configuration.

**A2.46 — Two-axis extension structure; Category 4 authoritative content.** Proposing substrates are Category 4 content — they specify what rules apply for evidence evaluation and proposal generation. The authoritative content classification commits the proposing substrate to the full governance framework Category 4 content carries.

**A2.04 — Rule authoring.** Proposing substrates are authored by humans. Authoring is foundational: the evaluation logic, pattern detection rules, threshold parameters, and proposal generation rules are not generated by the system or emergent from operations; they are written by humans exercising rule-authoring authority.

**A2.40 — Six provenance metadata fields.** Proposals generated by a proposing substrate are recorded with all six metadata fields: what, who, under what authority, with what rationale, when, and with what evidence basis. Provenance recording makes the evidence-to-proposal chain traceable and the proposal's basis auditable.

**A2.01–A2.03 — Governance affordances.** Humans can inspect any proposing substrate configuration and its operational record (A2.01). Humans can modify any proposing substrate rule — evidence scope, pattern logic, thresholds, proposal generation rules (A2.02). Humans can override specific proposals a proposing substrate generates (A2.03). These affordances are available at any time, not only at scheduled review intervals.

**A1.12 — Labor allocation framework.** LLMs operate as allocated labor performing proposing substrate operations. The three-mode labor allocation (direct human, LLM under rule, stable-cell automation) applies to proposing substrate operations as to all substrate operations. Labor allocation is a deployment decision; governance authority is not.

**A1.01 — Human-governed.** The proposing substrate is human-governed in the precise sense A1.01 establishes: humans hold the rights to inspect, modify, and override at any time. The substrate is governed; operations executing within it are labor.

---

## 6. Operational Implications

**Configuration per structural level and cell type.** Deployments configure proposing substrates per the structural levels and cell types they serve. A deployment with multiple cell types operating under distinct DNA content and action record patterns will configure distinct proposing substrates reflecting the evidence patterns relevant to each. Configuration is deployment design, not architectural prescription.

**Multiple co-existing proposing substrates.** Multiple proposing substrates may exist within a single deployment — one per cell type, one per aspect, one at the Self level — each examining the evidence scope relevant to its level and targeting the DNA elements under its governance scope. Co-existence is the norm in deployments with structural complexity.

**Evolution through directed selection per B1.14.** As understanding of effective evidence patterns and proposal generation logic develops through operational experience, humans modify proposing substrate rules. This evolution operates through directed selection: humans evaluate proposing substrate performance, determine what rules to improve, author the improvements, and commit the changes under governance. The proposing substrate that governs action-feedback cycles is itself subject to action-feedback insights, creating a recursive improvement dynamic.

**Cross-partner proposing substrates per A2.47.** Proposing substrates that span cross-partner content per A2.47 require the cross-partner authority specified at that note. Single-authority proposing substrates operate under single-authority governance; cross-partner proposing substrates require the multi-party authority architecture that cross-partner content generally requires.

**Stage 2 governance feed per B2.75.** Proposals generated by the proposing substrate feed the Stage 2 governance process formalized in B2.75. The proposing substrate's output is the input to Stage 2: formatted proposals with provenance, ready for human approval or rejection under the authority architecture B2.75 specifies.

**LLM-operated proposing substrates for complex pattern recognition.** Deployments with large Action layer evidence sets, or where evidence patterns require semantic analysis rather than rule-based matching, will operate proposing substrates with LLM labor performing pattern matching and proposal generation. The authored specification governs LLM operations; the LLM executes within authored scope.

---

## 7. Limits

**Proposing substrates do not directly change DNA.** The proposing substrate's output is proposals, not enacted changes. Direct DNA modification requires Stage 2 human governance approval per B2.75. A proposing substrate that directly modified DNA — without proposal, without human approval — would violate the action-feedback governance commitment B1.15 establishes.

**Proposing substrates are not the same as directed selection.** Directed selection per B1.14 is DNA evolution under explicit goals defined by human governance. Action-feedback evolution per B1.15 is DNA refinement driven by accumulated operational evidence. The proposing substrate is the artifact specific to action-feedback; it proposes. Directed selection is the mechanism through which humans decide — including decisions about whether to accept proposals. The two mechanisms are architecturally distinct. B2.77 formalizes this distinction.

**Proposing substrates are governed artifacts, not autonomous agents.** The proposing substrate operates within its authored specification under human governance. It does not autonomously expand its evidence scope, modify its own detection logic, or generate proposals outside its authored categories. Governance authority over the substrate is human; operations within the substrate may be LLM-performed labor.

**LLM performance of proposing substrate operations does not change governance.** That LLMs perform pattern matching, threshold evaluation, or proposal generation does not transfer governance over the proposing substrate to the LLM. The substrate's authored specification governs LLM operations. Humans retain the A2.01–A2.03 governance affordances over the substrate regardless of which labor mode executes its operations.

**Proposing substrates are not static.** The proposing substrate evolves through directed selection as evaluation understanding improves. A proposing substrate that cannot be modified — one where authored rules are locked and not subject to governance update — fails the A2.02 modify affordance. Proposing substrates are governed artifacts; governed artifacts are subject to governance modification.

**Proposing substrates are required for action-feedback evolution.** A deployment without proposing substrates cannot have action-feedback evolution. Action-feedback evolution requires that the loop from action evidence to DNA proposal passes through governed substrates. There is no architecturally consistent form of action-feedback evolution that bypasses the proposing substrate. The proposing substrate is necessary, not optional.

---

## 8. Operational Test

A system instantiates the proposing substrate specification if and only if all of the following are true:

1. There exists a substrate artifact — substrate-resident content per A1.08 — that specifies what action evidence is examined, what patterns are significant, what threshold strength triggers a proposal, how patterns convert to DNA change proposals, and how proposals are formatted for governance review.
2. The artifact is authored by humans per A2.04 and is subject to the three governance affordances per A2.01–A2.03: inspect, modify, override, at any time.
3. The artifact is Category 4 authoritative content per A2.46: it specifies what rules apply for evidence evaluation and proposal generation.
4. Proposals the artifact generates are recorded with full A2.40 provenance.
5. No operation performed by the artifact or by LLMs under the artifact's direction directly modifies DNA; all outputs are proposals requiring Stage 2 human approval per B2.75.
6. Proposing substrate rules can be modified through directed selection per B1.14 as governance determines refinement is needed.

A deployment that satisfies (1)–(6) has a proposing substrate per this specification. A deployment that accumulates action evidence and generates DNA change proposals through any pathway that bypasses (1)–(6) — including automated pipelines, external analytics systems, or LLM-generated changes without governed substrate specification — does not satisfy the specification and is not instantiating CKS action-feedback evolution.

---

## 9. Position in B1.15 Decomposition and Phase B2 Progression

B2.74 is the second of six notes decomposing B1.15 action-feedback evolution:

- **B2.73** (preceding): Action evidence evaluation mechanism — formalizes how Action layer records produce the evidence that proposing substrates ingest.
- **B2.74** (this note): Proposing substrate operational specification — formalizes the artifact that performs evidence-to-proposal.
- **B2.75** (next): Two-stage human mediation specification — formalizes Stage 1 (proposing substrate governance) and Stage 2 (proposal approval) as a unified human mediation architecture.
- **B2.76**: Action-feedback proposal pathway — formalizes the end-to-end path from action evidence through proposal to DNA change decision.
- **B2.77**: Action-feedback vs. directed selection distinction — establishes the architectural boundary between the two evolution mechanisms.
- **B2.78**: Action-feedback verification — formalizes the verification machinery applicable to action-feedback DNA changes.

After B2.78 closes the B1.15 decomposition, Phase B2 continues with B1.16 bidirectional evolution decomposition at B2.79 and beyond.

Naming the proposing substrate as a standalone formalized artifact — rather than leaving it as an implicit component within action-feedback evolution's general description — places it explicitly in the prior-art record with defined content, defined operations, defined governance properties, and defined limits. Subsequent work that implements, extends, or argues against the governed feedback-substrate pattern engages an artifact this note has named.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Proposing Substrate Operational Specification: Formalizing the Evidence-to-Proposal Artifact in Action-Feedback Evolution.* May 12, 2026. ORCID: 0009-0004-8065-3235.
