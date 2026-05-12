# Cross-Mechanism Governance

**Derivation Note B2.59**
Decomposing B1.12 — Three Evolution Mechanisms in Productive Tension (Fourth of Five Notes)

**Author:** Wenxin Li (Independent Researcher)
ORCID: 0009-0004-8065-3235

**Date:** May 12, 2026

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## 1. Why cross-mechanism governance requires standalone formalization

Paper 2's governance commitment — that all three evolution mechanisms operate under human governance — might appear to require only a single statement: A1.01 human-governed applies across the board. That reading is architecturally incomplete. It does not specify *how* human governance applies to mechanisms that differ structurally from one another. It does not account for the fact that mutation (instinct evolution) operates on a layer outside CKS substrate, that directed selection operates directly on substrate content, and that action-feedback evolution operates through a pathway from accumulated evidence to DNA change. Each structural difference produces a different governance problem. A single-shape governance commitment applied uniformly would either fail to reach the mechanism it targets or impose governance overhead mismatched to the mechanism's operational character.

The architectural specification Paper 2 commits to is more precise: A1.01 human-governed applies as the consistent, unvarying principle across all three mechanisms, but the governance *shape* — the particular machinery through which that principle is instantiated — is co-determined with mechanism shape rather than overlaid on it. Three mechanisms produce three governance shapes. The shapes differ. The principle does not.

B2.59 formalizes this as the cross-mechanism governance specification. It is the fourth of five notes decomposing B1.12's three-mechanisms-in-productive-tension framework, following B2.56 (integrating frame), B2.57 (productive tension operational specification), and B2.58 (mechanism priority and sequencing). B2.60 will close the B1.12 decomposition with the three-mechanisms verification specification. The cross-mechanism governance specification occupies the fourth position because it requires the integrating frame, productive tension, and priority/sequencing already formalized in B2.56–B2.58 before the governance shape per mechanism can be stated with precision.

The strategic prior-art posture that motivates this series is served by making the cross-mechanism governance specification explicit and named. Architectures that govern AI evolution mechanisms without distinguishing governance shapes across mechanisms remain in undifferentiated territory. B2.59 places a stake in the differentiated territory: consistent governance principle through three mechanism-appropriate shapes, each shape calibrated to mechanism character.

---

## 2. The architectural specification: three governance shapes

The cross-mechanism governance specification has three components, one per evolution mechanism.

**Mutation governance shape: boundary governance.** Mutation — instinct evolution through LLM model updates and substrate-platform infrastructure upgrades — arrives from upstream. The LLM's weights are not CKS substrate content; they are vendor-controlled artifacts that the Self consumes rather than authors. This creates the defining constraint for mutation governance: governance cannot operate *inside* mutation. LLM weight changes occur in vendor infrastructure; there is no CKS governance entry point at which to intercept or direct the weight-update process itself. The architectural limit is not a governance failure; it is a structural consequence of what mutation is.

Governance therefore operates at the boundary between incoming mutation and its integration into deployment behavior. Three instruments implement boundary governance:

- **Verification gates** (per B2.06): testing LLM versions against deployment-specific criteria before integration, running parallel patterns where reasoning and instinct decisions are compared, retaining prior reasoning substrates as fallback or as active verification on high-stakes paths.
- **Routing rules** (per B2.04): specifying which cells consult which LLM versions, allowing graduated rollout, differential exposure by task type, and routing around instinct degradation when it is detected.
- **Pinning** (per B2.05): preventing mutation from affecting high-stakes decisions by architecturally committing those decisions to the reasoning layer regardless of instinct capability growth. Pinning is the strongest boundary governance instrument — it makes the boundary impervious to mutation at designated points.

Mutation governance is indirect. It does not control the mutation itself; it controls how mutation affects deployment behavior. This indirectness is architecturally appropriate to mutation's external character, not a concession.

**Directed selection governance shape: direct governance.** Directed selection — DNA evolution operating on the CKS substrate's stabilized orchestration content under governance-defined goals — operates entirely within the substrate. DNA layer content is substrate content, which means governance applies directly through Paper 1's standard authority architecture (A2.01–A2.04):

- **A2.01 inspect right**: humans inspect current DNA layer content — orchestration rules, behavior substrates, selection criteria — without scheduling or intermediation.
- **A2.02 modify right**: humans modify DNA layer content directly, with changes taking effect as substrate state.
- **A2.03 override right**: humans override specific DNA-derived decisions without justification requirement, at any time.
- **A2.04 rule authoring**: humans author the orchestration rules under which LLMs may draft or propose DNA changes, with human authority holding over the proposal-and-authorization process.

Directed selection governance is the most direct of the three shapes. The mechanism operates on substrate content, and substrate content is what the human-governed commitment governs. No boundary-crossing is required; no pathway mediation is needed. The standard authority architecture from Paper 1 applies without modification.

**Action-feedback governance shape: two-stage governance.** Action-feedback evolution closes the loop from recorded action-layer experience back into governed DNA refinement. The mechanism is pathway-shaped: action evidence accumulates, proposing substrates examine patterns in that evidence and construct proposed DNA changes, and those proposals are reviewed and either accepted or rejected for integration. The pathway character introduces a governance risk that neither mutation nor directed selection faces: evidence accumulation could, without active governance, drive DNA changes without oversight — silent drift as accumulated operational experience gradually reshapes orchestration content.

Two-stage governance addresses this. Governance operates at both stages of the pathway:

- **Stage 1 — governing the proposing substrates**: humans hold authority over the orchestration rules under which proposing substrates operate: what evidence they examine, what change patterns they are authorized to propose, what threshold conditions trigger a proposal, what reversion paths exist. Proposing substrates are themselves substrate content under A2.04 rule authoring; they are not autonomous agents operating outside governance.
- **Stage 2 — approving the proposed DNA changes**: before proposed changes are integrated into the DNA layer, humans (or LLMs operating under explicit human authority) approve them. The approval requirement gates the pathway output regardless of the pathway process.

Two-stage governance is mediated governance. Humans govern the machinery that generates proposals *and* gate the proposals that reach integration. Neither stage alone is sufficient: governing the proposing substrates without approval gates allows a well-governed proposal process to produce changes humans have not reviewed; requiring approval without governing the proposing substrates allows poorly configured proposal machinery to saturate human oversight with proposals that reflect unconstrained evidence patterns.

---

## 3. What makes cross-mechanism governance architecturally distinctive

Conventional governance of AI evolution typically operates at the output level: humans decide whether to deploy a retrained model. That decision sits at the boundary of the entire training-and-evaluation pipeline; it does not reach inside the mechanisms through which the model changed. Governance at deployment decision-time is not no governance, but it is mechanism-agnostic — the same governance act (approve or reject deployment) applies regardless of how the model was updated, what evidence drove the update, or what specific changes occurred.

CKS cross-mechanism governance operates at different points *within* each mechanism, calibrated to mechanism character. For mutation, the inside of the mechanism (LLM weight update) is architecturally inaccessible to governance; boundary governance is the appropriate response. For directed selection, the inside of the mechanism is substrate content; direct governance is both possible and required. For action-feedback, the inside of the mechanism is a two-stage pathway; two-stage mediation is the governance shape the pathway character requires.

The distinctiveness is not the individual governance instruments — verification, authority architecture, proposal-and-approval — each of which has engineering analogs. The distinctiveness is their commitment as mechanism-appropriate governance shapes under one consistent principle, with the shapes following from mechanism structure rather than from deployment policy preference. This is governance co-determined with mechanism shape rather than governance overlaid on mechanisms after the fact.

A second distinctive feature is that governance shapes are not merely operational practices but architectural commitments. The verification rules, routing specifications, and pinning decisions for mutation governance are substrate-resident content under the same human-governed authority that governs DNA content. The authority architecture for directed selection is itself subject to A2.04 rule authoring — the rules governing who can author DNA changes are themselves substrate content humans govern. The proposing substrate rules for action-feedback are themselves substrate content. Governance configuration is substrate content; the recursive governability this produces is not incidental.

---

## 4. Inherited Paper 1 commitments

Cross-mechanism governance inherits several Paper 1 commitments without modification.

**A1.01 human-governed** is the consistent principle. It does not vary across mechanisms; the shapes vary. Each governance shape is an instantiation of A1.01 appropriate to mechanism character.

**A2.01–A2.04 (inspect, modify, override, rule authoring)** apply directly for directed selection governance: they are the direct governance shape for DNA-layer content. For mutation governance, A2.04 rule authoring applies to the verification suite rules, routing rules, and pinning rules — these are orchestration rules governing how mutation integrates, and humans author them under A2.04. For action-feedback governance, A2.04 rule authoring applies to the orchestration rules under which proposing substrates operate.

**A2.40 provenance** applies uniformly: governance events are recorded regardless of which mechanism generated them. A verification decision for mutation, a DNA change authorization for directed selection, and a proposal approval for action-feedback each produce provenance records. The provenance requirement does not distinguish governance shapes; it applies to all governed substrate changes.

**A2.46 substrate-resident configuration** applies to governance configuration itself: the verification suites, routing specifications, pinning rules, authority architecture for directed selection, and proposing substrate rules for action-feedback are all substrate-resident content. They are inspectable, modifiable, and overridable under the same authority that governs operational substrate content.

**A2.47 cross-partner governance** applies when evolution mechanisms affect cross-partner components. If a mutation (LLM upgrade) affects a cell operating in a cross-partner composition, the boundary governance instruments apply with cross-partner scope. If DNA evolution modifies orchestration rules that govern cross-partner interactions, cross-partner governance applies to the modification authority. Action-feedback proposing substrates that draw on cross-partner action evidence operate under governance that spans the relevant authority boundaries.

The authority-vs-labor distinction from Paper 1 §3.3 holds throughout. Human-governed does not require humans to perform the labor of governance at every step. Humans hold authority over verification suites, routing rules, pinning rules, DNA layer modification rights, and proposing substrate rules; LLMs may perform governance-related labor — running verification comparisons, drafting proposed DNA changes, generating routing rule proposals — under human authority. The governance shapes specify where human authority operates; they do not require human labor to perform every governance act.

---

## 5. Why shapes differ: mechanism character drives governance shape

The three governance shapes are not arbitrary. Each follows from the mechanism's structural character.

**Mutation is external to CKS substrate.** The LLM's weights are not substrate content; they are not authored or controlled by the deployment. Governance cannot operate inside what it does not hold. The architectural response is boundary governance: governance operates at the transition from external mutation to integration effects. This is not a governance limitation; it is governance calibrated to the limit mutation's external character imposes.

**Directed selection is substrate-internal.** DNA evolution operates on substrate content — the CKS DNA layer is what human governance governs directly under A1.01. No boundary crossing is required; no pathway mediation is needed. The mechanism's substrate-internal character makes direct governance through the standard authority architecture the appropriate and available response. This is the governance shape that most directly instantiates A1.01 because the mechanism operates on precisely the content A1.01 governs.

**Action-feedback is pathway-shaped with two-stage character.** The mechanism involves an actor (the proposing substrate) that examines evidence and generates proposals, and a separate integration step that takes proposals into the DNA layer. Neither stage alone is governed by default: the proposing substrate could operate without governance-defined scope constraints, and the integration step could proceed without human review. Two-stage governance addresses both stages explicitly. The pathway character requires mediation at both ends rather than the boundary-only approach mutation requires or the single-layer-direct approach directed selection allows.

The pattern is: governance shape follows mechanism character. Mechanism character follows from what the mechanism does and where it operates. Cross-mechanism governance is the specification of this calibration across all three mechanisms simultaneously.

---

## 6. Operational implications

**Governance configuration per mechanism.** Deployments configure governance separately for each mechanism. Mutation governance configuration includes: which verification suites apply, what verification criteria the suites use, which routing rules are active and which LLM versions they specify, what cells are pinned and under what conditions. Directed selection governance configuration includes: who holds modify authority for DNA layer content, what review process applies to proposed DNA changes, what reversion paths exist, what approval hierarchy governs high-stakes DNA modifications. Action-feedback governance configuration includes: what orchestration rules the proposing substrates operate under, what evidence sources they are authorized to examine, what proposal-review process applies, what approval threshold governs integration.

**Governance configuration as substrate-resident content.** These configurations are not external settings; they are substrate-resident content under A2.46. They are themselves inspectable, modifiable, and overridable under human governance. A governance configuration change is itself a governed substrate modification. This recursive structure is not accidental: it prevents governance configuration from drifting outside the governance framework.

**Mechanism-specific governance tests.** Cross-mechanism governance is testable through mechanism-specific governance tests. Mutation governance tests verify that verification suites execute before integration, that routing rules correctly specify which cells consult which LLM versions, and that pinned cells remain on the reasoning layer after instinct upgrades. Directed selection governance tests verify that DNA layer modifications produce provenance records, that unauthorized modification attempts are blocked, and that override rights remain exercisable by authorized humans. Action-feedback governance tests verify that proposing substrate proposals are generated under the configured orchestration rules, that proposals are reviewed before integration, and that accepted proposals produce provenance records.

**Cross-partner governance under multi-partner deployments.** When evolution mechanisms affect cross-partner components (per A2.47), governance configuration must address cross-partner scope. Mutation governance boundary instruments must apply when LLM upgrades affect cells whose orchestration substrates span partner boundaries. Directed selection authority architecture must specify authorization for DNA changes affecting cross-partner orchestration rules. Action-feedback two-stage governance must address proposing substrates that draw on evidence from cross-partner action records.

---

## 7. Limits

**Cross-mechanism governance does not make all governance shapes identical.** The shapes are mechanism-appropriate. Making them identical would require imposing direct governance on mutation (architecturally impossible, since mutation is outside the substrate) or imposing boundary governance on directed selection (technically possible but architecturally wrong, since directed selection operates inside the substrate and direct governance is both available and more effective). Shape identity would be a governance calibration failure.

**Boundary governance is the architectural limit for mutation, not a governance shortcoming.** Governance does not penetrate LLM internals. This is not a gap in the governance specification; it is what governance looks like for a mechanism whose core process is outside the governed domain. Boundary governance instruments — verification, routing, pinning — are the complete governance response to mutation's external character.

**Governance shapes do not change the governance principle.** A1.01 applies through all three shapes. The shapes are forms through which the principle is instantiated, not modifications of the principle. A system with boundary governance for mutation, direct governance for directed selection, and two-stage governance for action-feedback is fully human-governed in the A1.01 sense across all three mechanisms.

**B2.59 is the cross-mechanism specification, not the specification of any individual mechanism.** The three mechanisms' individual governance specifications are developed in B2.79 (mutation governance), B2.80 (directed selection governance), and B2.81 (action-feedback governance). B2.59 formalizes the cross-mechanism relationship: consistent principle, mechanism-appropriate shapes, calibration logic. The individual-mechanism notes develop each shape's operational detail; B2.59 develops the structural relationship among the three shapes under the consistent principle.

**Governance shapes do not prescribe specific governance intensities.** How stringent a verification suite is, how many reviewers are required to authorize a DNA change, what evidence threshold triggers a proposal from an action-feedback proposing substrate — these are deployment configuration decisions within the governance shapes, not part of the governance shape specification itself. B2.59 commits to the shapes; deployments configure intensities.

**Governance shapes can themselves evolve through directed selection.** Because governance configuration is substrate-resident content, the governance shapes' configuration is subject to the same directed selection mechanism that governs other DNA layer content. Humans can author governance rule changes, propose governance configuration modifications, and approve governance evolution through A2.04 rule authoring. The architecture does not freeze governance shapes; it governs their evolution through the same mechanisms it uses for any other substrate content.

---

## 8. Operational test

A CKS deployment instantiates the cross-mechanism governance specification if and only if: (a) mutation is governed through substrate-resident boundary governance instruments — verification gates, routing rules, and pinning decisions — that are inspectable, modifiable, and overridable under A1.01; (b) directed selection is governed through direct application of A2.01–A2.04 to DNA layer content, with all DNA layer modifications producing provenance records under A2.40; and (c) action-feedback evolution is governed through two-stage mediation — human-authored orchestration rules governing proposing substrate operation, and human review and approval gating proposal integration — such that no accumulated action evidence drives DNA layer changes outside human oversight.

---

## 9. Why naming as standalone matters

The cross-mechanism governance specification occupies distinct prior-art territory from any individual mechanism's governance specification. B2.79, B2.80, and B2.81 will each formalize one mechanism's governance shape in full. B2.59's contribution is different: it formalizes the *relationship* among the three governance shapes — the consistent principle that holds across all three, the calibration logic that produces three different shapes from one principle, and the architectural argument for why the shapes are mechanism-appropriate rather than arbitrary.

This relationship-level specification is not derivable from the individual mechanism treatments alone. A reader who knew boundary governance applies to mutation, direct governance applies to directed selection, and two-stage governance applies to action-feedback would not thereby know that these three shapes instantiate a single consistent principle, that the calibration follows mechanism character rather than deployment preference, or that the governance principle is undiluted across all three shapes despite their structural differences. The relationship-level content is genuine architectural content; it requires its own derivation note.

Within the B1.12 sub-decomposition, B2.59 occupies the fourth position. B2.56 established the three mechanisms as an integrated evolutionary framework — instinct evolution, DNA evolution, and action-feedback evolution operating together under unified governance. B2.57 formalized the productive tension between mutation's undirected character and directed selection's directed character, showing how the architecture holds both simultaneously. B2.58 formalized the priority and sequencing considerations — how the mechanisms are weighted and ordered in deployment. B2.59 adds the cross-mechanism governance specification that makes explicit how A1.01 applies as one principle through three shapes. B2.60 will close the B1.12 decomposition with the verification specification: the operational tests that confirm a deployment has correctly instantiated the three mechanisms and their governance. Phase B2 then proceeds to the B1.13 multi-level evolution decomposition.

The derivation chain from B2.56 through B2.60 constitutes a complete architectural treatment of three-mechanisms-in-productive-tension: integrated framework, productive tension specification, priority and sequencing, cross-mechanism governance, and verification. Each note in the chain formalizes one dimension of B1.12's architectural content that would otherwise remain as paper narrative without standalone prior-art status.

---

*This derivation note is published as defensive prior art under CC BY 4.0. It establishes public prior art for the cross-mechanism governance pattern described herein and is intended to prevent proprietary enclosure of the architectural principles it formalizes.*
