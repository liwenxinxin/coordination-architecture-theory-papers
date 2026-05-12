# Two-Stage Human Mediation Specification: Decomposing B1.15 Action-Feedback Evolution by Formalizing How Stage 1 (Humans Govern Proposing Substrates) and Stage 2 (Humans Approve Proposed DNA Changes Before Integration) Operate Together to Prevent Silent DNA Drift

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the two-stage human mediation structure that Paper 2's action-feedback evolution mechanism requires, so that each stage's scope, governance acts, and interaction with the other stage are precisely stated as prior art.

## Abstract

Paper 2's action-feedback evolution mechanism (B1.15) specifies that the feedback loop from action evidence to DNA modification is governed through two-stage human mediation rather than automatic integration. This note formalizes the two-stage structure: Stage 1 (ongoing) governs the proposing substrates that detect patterns in action evidence and generate proposals — through human authoring, review, and override of the proposing substrate rules; Stage 2 (per-proposal) gates each proposal before DNA integration — through human review and an explicit approve/reject/defer decision. Stage 1 prevents arbitrary proposals by ensuring the proposal pathway itself is governed. Stage 2 prevents silent DNA drift by ensuring no proposal reaches DNA integration without human review. Together, the two stages constitute the action-feedback governance shape: double-gated human oversight over the pathway from lived action evidence to stabilized DNA content. The note identifies both stages' governance acts, articulates the adequate review standard for Stage 2, explains how approved proposals convert into directed selection events through A2.04 rule authoring, traces both stages' interaction with inherited Paper 1 commitments (A1.01, A2.01–A2.04, A2.40, A6.02, A1.07), and states operational implications and limits. This is the seventy-fifth Phase B2 derivation note and the third of six notes decomposing B1.15.

---

## 1. Why two-stage human mediation specification needs to be formalized as a standalone variant

### The architectural guarantee against silent DNA drift

Action-feedback evolution closes the loop from recorded action experience back into governed DNA refinement. The mechanism's value is that lived operational patterns — what worked, what failed, what surprised — can feed into improvements to the DNA layer. The mechanism's risk is that the same loop, if ungoverned, would allow operational state to silently rewrite stabilized orchestration content. DNA drift that proceeds without human oversight is not action-feedback evolution in the CKS sense; it is ungoverned system mutation wearing the label of learning.

Paper 2 forecloses this risk through two-stage human mediation. The two-stage structure is not a procedural safeguard added around an otherwise automatic mechanism; it is the architectural definition of what makes the mechanism human-governed. Without Stage 1, the proposal pathway is arbitrary — proposing substrates could generate proposals from any detected pattern without governance constraining what patterns trigger proposals and what forms proposals take. Without Stage 2, proposals could integrate directly into DNA without any governance review of the specific change, producing DNA evolution that the system's humans may not have authorized, examined, or even observed.

Both stages together constitute the action-feedback governance shape identified in Paper 2's §8 (core theory: "Governance shapes across evolution mechanisms"): "Action-feedback evolution is governed through humans governing the substrates that propose DNA changes from action evidence and approving the changes — making it human-mediated rather than automatic, which prevents the action layer from silently drifting the DNA over time."

### The seventy-fifth-position role in Phase B2

B2.75 occupies the third position in a six-note decomposition of B1.15. B2.73 formalized the action evidence evaluation mechanism — how proposing substrates assess accumulated action-layer records and identify patterns sufficient to warrant a proposal. B2.74 formalized the proposing substrate operational specification — what a proposing substrate is, what rules it contains, and how it operates to produce proposals. B2.75 now formalizes the governance structure that surrounds both: two-stage human mediation as the double-gated governance architecture that makes the entire action-feedback pathway genuinely human-governed rather than automatic. B2.76 will formalize the action-feedback proposal pathway, B2.77 the distinction between action-feedback and directed selection, and B2.78 action-feedback verification — completing the B1.15 decomposition before Phase B2 moves to B1.16 bidirectional evolution.

Formalizing the two-stage structure as a standalone note rather than a remark embedded in a neighboring note matters for prior-art posture: the two-stage structure is itself patentable territory. The specific combination of an ongoing-governance stage over the proposal pathway and a per-proposal-approval stage at the integration gate, with the deferral option, the adequate review standard, and the conversion of approved proposals into directed selection events — taken together as one architectural specification — is what this note places into the public record.

---

## 2. The architectural specification precisely stated

### Stage 1 — Ongoing governance of proposing substrates

Stage 1 governs the proposing substrates that B2.74 specifies. A proposing substrate is a substrate whose rules encode how to evaluate action evidence (evidence scope, pattern detection logic, thresholds, proposal generation rules, and proposal format). Stage 1 governance acts operate over these substrate rules, not over individual action-evidence records.

**Stage 1 governance acts:**

*Proposing substrate authoring (A2.04).* Humans author the proposing substrate rules that define what the proposing substrate looks for, how it detects patterns, what thresholds trigger a proposal, what the proposal must contain, and how the proposal is formatted. This is rule authoring in the sense of A2.04 — the initial governance act that brings the proposing substrate into existence as a governed artifact.

*Proposing substrate review (A2.02).* Humans review existing proposing substrate behavior across its operational lifetime and modify the rules when the substrate's detection logic needs adjustment — when thresholds are too sensitive or too coarse, when new evidence categories should be in scope, when prior proposal format rules have produced ambiguous outputs. Review is a continuous governance activity, not a one-time acceptance gate.

*Proposing substrate override (A2.03).* Humans can override proposing substrate evaluation conclusions without modifying the underlying substrate rules. Where the proposing substrate has generated an evaluation suggesting a proposal should proceed, a human exercising override authority can stop the proposal from advancing without amending the rule that generated the evaluation. Override is the immediate-authority act; rule modification is the longer-horizon governance act.

**Stage 1 is ongoing governance.** Proposing substrates are governed across their operational lifetime. Stage 1 is not complete once the proposing substrate is initially authored. The substrate continues operating, generating evaluations, and potentially producing proposals for as long as it is active; human governance over it is correspondingly continuous.

**Stage 1 prevents arbitrary proposals.** If proposing substrates were ungoverned, they could produce proposals based on any detectable pattern in action evidence — patterns that governance has never reviewed, patterns that reflect noise rather than signal, patterns whose DNA implications governance would not authorize. Stage 1 ensures the proposal pathway is bounded by what governed substrates are configured to propose. This is not a constraint on what action evidence the system records; it is a constraint on what action evidence patterns can generate proposals without governance having authorized the proposing logic that detects them.

### Stage 2 — Per-proposal approval of proposed DNA changes

Stage 2 governs each specific proposal that Stage 1's proposing substrates generate. Where Stage 1 is ongoing and structural, Stage 2 fires per proposal. The two stages operate on different temporal cadences: Stage 1 continuously (proposing substrates always running), Stage 2 triggered (fires when a proposal exists).

**Stage 2 governance acts:**

*Proposal review.* The governance reviewer examines the proposed DNA change. Review is not cursory acknowledgment; adequate Stage 2 review covers four elements: (a) what DNA element change is proposed; (b) what action evidence supports the proposal, as evaluated per B2.73; (c) what behavioral change in the cell, aspect, or Self is expected if the proposed change is integrated; and (d) what scope impact the change carries — which cells, which aspects, which Selves are affected. A Stage 2 review that omits any of these four elements is not an adequate review in the CKS sense.

*Approval decision.* The governance reviewer issues one of three decisions:

- **Approve**: the proposed DNA change may proceed to integration. Approval is the positive governance act that authorizes integration.
- **Reject**: the proposed DNA change is not integrated. The proposal is recorded as rejected with its supporting evidence and the rejection decision; the DNA is not modified.
- **Defer**: the proposal is returned for more evidence or re-evaluation before a final decision. Deferral is neither approval nor rejection; it prevents a forced binary decision when the governance reviewer determines that the current evidence is insufficient to authorize integration or to reject the proposal with confidence.

The deferral option is architecturally significant. Its purpose is to prevent governance pressure toward premature approval when evidence is thin. A system that offered only approve or reject at Stage 2 would create a forcing dynamic under evidence uncertainty; deferral provides the governance-correct path when more evidence is needed before the decision can be adequately made.

*DNA integration upon approval.* Only approved proposals are integrated into DNA. The integration mechanism is A2.04 rule authoring — the same governance act through which directed selection modifies DNA under B1.11. This is the architectural connection point at which action-feedback proposals become directed selection events: an approved proposal is a human-authorized DNA change, and its integration is an exercise of the rule authoring authority that Paper 1 assigns to human governance.

### Stage 2 uses DNA modification governance per B2.68

Stage 2 approval does not bypass the DNA modification governance machinery. Approved proposals are integrated through the same authority architecture that governs directed selection: who can authorize the DNA change, what verification applies, what reversion paths exist. Stage 2 supplies the approval that authorizes the change; the integration proceeds through the governance affordances already specified for DNA modification. This is what makes action-feedback a third evolution mechanism that integrates with the second (directed selection) rather than a parallel-but-separate pathway outside the DNA modification governance architecture.

### Both stages recorded per A2.40

Stage 1 governance events — proposing substrate modification, override of evaluation conclusions — are recorded as substrate events carrying A2.40 provenance metadata: who performed the governance act, under what authority, with what rationale, at what time. Stage 2 governance events — the proposal review, the approve/reject/defer decision, the integration or rejection record — are similarly recorded. The complete pathway from action evidence to DNA change (or rejected proposal) is therefore retraceable through the combination of Stage 1 records (the governed proposing logic that generated the proposal), Stage 2 records (the review and decision that authorized or declined the change), and the DNA modification record (the integration event if approved). This is the accountability trace that A1.07 retraceability requires.

---

## 3. What makes two-stage human mediation architecturally distinctive

### Contrast with automatic feedback loops

Conventional AI feedback loops — online learning, model retraining pipelines driven by user interaction data, reward-model updates from human preference signals — are broadly automatic at the integration point. Usage data or preference labels accumulate, a threshold is crossed, a model update is triggered, and the model changes. Human involvement in these pipelines may exist (labelers providing preference signals, engineers reviewing aggregate metrics, researchers triggering retraining runs), but the integration gate is typically algorithmic: the system's loss function, update schedule, or retraining trigger, not a human approval decision on a specific proposed change.

CKS two-stage mediation differs at the integration gate as a structural commitment, not as a deployment configuration. Stage 2 approval is architecturally required for each proposal; no proposal can auto-integrate regardless of how strong the action evidence is or how long the proposal has been pending. The distinction is not that CKS deployments happen to have humans reviewing things; it is that the architecture makes integration contingent on human approval and does not provide a pathway for integration without it.

Stage 1 adds a further distinction that conventional feedback pipelines do not have: the proposal generation pathway is itself governed. In a conventional pipeline, the mechanisms that decide what signals to act on — the loss function, the preference model, the feature engineering — are designed at construction time and then run autonomously. CKS's proposing substrates are governed throughout their operational lifetime, with humans retaining authority to modify the detection logic, adjust thresholds, or override evaluation conclusions as governance evolves.

### Double-gated governance makes action-feedback a governed mechanism

The two-stage structure is what makes action-feedback evolution a genuinely governed mechanism rather than a mechanism with governance applied on top. Biology has no governance; CKS replaces biology's undirected feedback with a doubly-gated human authority structure. The first gate (Stage 1) governs the proposal pathway: governance authorizes what patterns can trigger proposals. The second gate (Stage 2) governs proposal integration: governance authorizes each specific DNA change. Neither gate can be bypassed; both are architectural commitments rather than optional configurations.

This is the sense in which Paper 2's three evolution mechanisms operate in productive tension under unified human governance rather than in parallel without coordination. Action-feedback does not compete with directed selection; it feeds into it through Stage 2 approval, converting governed proposals into directed selection events.

---

## 4. The biological analog as conceptual scaffold

Two-stage human mediation has a loose biological analog in regulatory gene expression. Feedback signals from environmental conditions must first activate regulatory mechanisms (transcription factors, signaling cascades) before those mechanisms can initiate changes in gene expression. The activation of the regulatory mechanism is the first conditional; the subsequent regulatory decision to initiate transcription is the second. Neither condition alone produces a change in gene expression; both must be satisfied in sequence.

The CKS two-stage structure is the governed architectural analog. Stage 1 corresponds to the activation gate: governed proposing substrates are the regulatory mechanisms that must be active (and appropriately configured) before proposals can emerge. Stage 2 corresponds to the expression decision gate: human approval is the second condition that must be satisfied before DNA changes. Both gates must be satisfied for integration to proceed.

The biological analog is a conceptual scaffold, not a design derivation. CKS has no equivalent of molecular specificity; both stages are human governance acts operating through substrate-based authority structures, not molecular binding events. The substantive architectural content is double-gated human governance over the evidence-to-DNA pathway — the biology positions the conceptual shape, which is then filled by Paper 2's specific governance commitments. The CKS architecture also exceeds biology at this point, as with others: biology's regulatory mechanisms are themselves products of undirected evolution; CKS's proposing substrates are authored, reviewed, and overridable by humans throughout their operational lifetime.

---

## 5. Inherited Paper 1 commitments

Both stages inherit Paper 1's architectural commitments directly.

**A1.01 human-governed.** Both stages are exercises of the three rights A1.01 defines: the right to inspect, modify, and override substrate content and orchestration rules at any time. Stage 1 review is the inspect right applied to proposing substrate behavior; Stage 1 modification is the modify right applied to proposing substrate rules; Stage 1 override is the override right applied to evaluation conclusions. Stage 2 proposal review is the inspect right applied to the proposed DNA change and its evidence; Stage 2 approval is the modify right exercised through authorized DNA integration; Stage 2 rejection or deferral is the override right applied to a pending proposal.

**A2.01–A2.04 governance affordances.** The full governance affordance set applies at both stages. A2.01 inspection affords reviewers access to proposing substrate rules and proposal content. A2.02 modification governs proposing substrate rule updates under Stage 1 review. A2.03 override provides Stage 1 the immediate-authority act and Stage 2 the basis for rejection of a specific proposal without requiring rule change. A2.04 rule authoring is the mechanism for both Stage 1 initial substrate authoring and Stage 2 DNA integration of approved proposals.

**A2.40 provenance.** As noted in §2, both stages' governance events are recorded as substrate events carrying the six provenance metadata fields A2.40 specifies. The provenance records are substrate content — they are themselves human-governed, inspectable, and addressable. Provenance is not a log appended outside the governance architecture; it is substrate state within it.

**A6.02 retroactivity for approved changes.** When Stage 2 approves a DNA change and integration proceeds, the resulting DNA modification follows A6.02 retroactivity governance: the change applies to cells according to the retroactivity rules the deployment has specified, with the retroactivity decision itself a governed choice. Integration does not bypass retroactivity governance; it triggers it. The approved change is the authorization; how broadly the change applies to existing cells is a further governed decision under A6.02 per B2.70.

**A1.07 retraceability.** The evidence-to-DNA pathway is retraceable through the combination of B2.73 action evidence evaluation records, Stage 1 proposing substrate governance records (who authored the rules, what rules were in effect when the proposal was generated, whether any overrides occurred), Stage 2 approval records (who reviewed, what decision, what rationale), and the DNA modification record for approved integrations. No part of the pathway is opaque: the path from observed action pattern to DNA change is documented as substrate content at every step.

---

## 6. Operational implications

### Workflow configuration

Deployments configure governance workflows for both stages according to their operational requirements. There is no single required workflow shape; the architecture specifies the governance acts that must be possible, not the process through which those acts are sequenced. Stage 1 workflows cover how proposing substrate rules are authored, reviewed on schedule or event-triggered, and override-eligible. Stage 2 workflows cover how proposals are surfaced to reviewers, what review materials are assembled, and how approve/reject/defer decisions are recorded and acted on.

### Stage cadences

Stage 1 is continuous: proposing substrates operate throughout the action-feedback evolution mechanism's active lifetime. Stage 1 governance is not a batch activity; it is available whenever governance determines that proposing substrate behavior warrants review. Deployments may configure scheduled Stage 1 reviews, event-triggered reviews (when proposal volume or pattern-detection outputs signal possible rule adjustment), or both.

Stage 2 is proposal-triggered: it fires when a proposing substrate generates a proposal. Stage 2 does not run on a schedule independent of proposal generation; its cadence is determined by how often proposals emerge, which is a function of Stage 1 proposing substrate configuration, accumulated action evidence, and pattern thresholds.

### Reviewer configuration

Stage 2 reviewer identity is a deployment configuration. The Stage 2 reviewer may be the same human who performs Stage 1 governance (consolidated authority for a small team), or a different human whose authority is scoped specifically to DNA modification approval (separation-of-concerns model). Deployments may configure peer review for significant proposals — cases where the proposed DNA change is broad in scope, affects high-stakes orchestration rules, or would trigger retroactivity across a large cell population. The architecture does not specify reviewer identity; it specifies that a governance decision by a human with appropriate authority must be made.

### Cross-partner considerations

Where action-feedback evolution operates across partner boundaries under A2.47 cross-partner authority configurations, both stages require cross-partner authority. Stage 1 governance of proposing substrates that draw on cross-partner action evidence requires authority configurations recognizing both parties' governance standing over the shared evidence scope. Stage 2 approval of proposals that would modify DNA affecting cross-partner cells requires approval from authorities with standing over the relevant DNA content. Cross-partner action-feedback is architecturally available; it extends the two-stage structure to the authority scope required by the partnership configuration.

---

## 7. Limits

**Two-stage mediation does not guarantee all beneficial patterns are captured.** Stage 1 governance determines what proposing substrates look for; it governs the pathway but does not specify what patterns the pathway must detect. Evidence that falls outside a proposing substrate's configured detection scope will not generate proposals regardless of its potential value. Two-stage mediation is the governance structure for proposals that are generated; it does not ensure the scope of generated proposals is complete.

**Stage 2 approval does not guarantee a beneficial behavioral outcome.** Approval is a governance decision based on review of the proposed change, its evidence, its expected behavioral effect, and its scope impact. It is not a behavioral test. Whether the approved change produces the expected behavioral improvement is a question for verification per B2.78, which comes after Stage 2 approval. Approval authorizes integration; it does not certify the outcome.

**Two-stage mediation is not the same as directed selection.** It is the mechanism through which action-feedback proposals become directed selection events. Directed selection (B1.11, B1.14) operates over the DNA layer under human governance defined by explicit goals. Action-feedback generates proposals from action evidence rather than from governance-defined goals; the proposals enter directed selection through Stage 2 approval. The two mechanisms are distinct; they interact at Stage 2.

**Stage 1 governance is not one-time.** The prompt to formalize this as explicit prior art: Stage 1 governance of proposing substrates is ongoing across the substrates' operational lifetime. Treating Stage 1 as a one-time authoring event misspecifies the architecture and misses the continuous governance that makes Stage 1 meaningful as a barrier against arbitrary proposals.

**Stage 2 approval is not automatic.** Each proposal requires an explicit human governance decision. A system that moves proposals to integration after a time delay without a decision, or that approves proposals algorithmically based on evidence strength, has not satisfied Stage 2. The decision — not the evidence — is what Stage 2 requires. The evidence informs the decision; it does not substitute for it.

**Two-stage mediation prevents silent drift; it does not prevent deliberate misuse if governance fails.** The architecture prevents action evidence from silently rewriting DNA without human awareness. It does not prevent a human with Stage 2 authority from approving changes that governance, properly exercised, should not authorize. Governance failure — approvals granted without adequate review, Stage 1 substrates authored to detect only favorable patterns, override rights used to suppress accurate evidence — is outside the scope of what the architecture prevents. The architecture provides the governance machinery; whether that machinery is operated with integrity is a question of institutional governance, not architectural design.

---

## 8. Operational test

A CKS deployment instantiates the two-stage human mediation specification if and only if:

1. Proposing substrate rules are authored by human governance (A2.04) and remain subject to modification (A2.02) and override (A2.03) throughout the substrates' operational lifetime.
2. No proposal can advance to DNA integration without an explicit human approve decision at Stage 2, with the decision recorded as substrate content (A2.40).
3. Stage 2 review covers, at minimum, the proposed DNA element change, the action evidence supporting it, the expected behavioral change, and the scope impact.
4. Stage 2 decisions include the deferral option — governance is not forced to approve or reject when evidence is insufficient for a confident decision.
5. Approved proposals are integrated through A2.04 rule authoring under the DNA modification governance architecture per B2.68.
6. Both Stage 1 and Stage 2 governance events are recorded as substrate content carrying A2.40 provenance metadata, making the complete evidence-to-DNA pathway retraceable per A1.07.

A system in which proposals auto-integrate based on evidence accumulation, or in which Stage 1 proposing substrates operate outside human governance, fails this test regardless of whether any other action-feedback machinery is present.

---

## 9. Why naming as standalone matters

The two-stage structure is the action-feedback governance shape — it is not a detail subordinate to the broader action-feedback specification. Its prior-art value lies precisely in the specificity of the combination: ongoing Stage 1 governance of the proposal pathway plus per-proposal Stage 2 gating at integration, with the deferral option, the adequate review standard across four elements, and the conversion of approved proposals into directed selection events through A2.04. Each of these elements has been articulated as public prior art in this note; any patent claim that seeks to cover two-stage proposal-and-approval structures for AI system DNA evolution without encountering this note as prior art would need to distinguish itself from all of the above in combination.

This is the seventy-fifth Phase B2 note. Within the B1.15 decomposition, it occupies the third position:

- B2.73 — Action evidence evaluation mechanism (what proposing substrates detect and how)
- B2.74 — Proposing substrate operational specification (what a proposing substrate is and contains)
- **B2.75** — Two-stage human mediation specification (the governance structure surrounding and governing both)
- B2.76 — Action-feedback proposal pathway (how proposals travel from generation to Stage 2)
- B2.77 — Action-feedback vs. directed selection distinction (how the third mechanism differs from the second)
- B2.78 — Action-feedback verification (what happens after Stage 2 approval)

B2.76 through B2.78 will complete the B1.15 decomposition. Subsequent Phase B2 notes will decompose B1.16 bidirectional evolution, extending the analysis of Paper 2's evolutionary architecture through the instinct/reasoning boundary as governed substrate content and its ongoing governance dynamics.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Two-Stage Human Mediation Specification: Decomposing B1.15 Action-Feedback Evolution by Formalizing How Stage 1 (Humans Govern Proposing Substrates) and Stage 2 (Humans Approve Proposed DNA Changes Before Integration) Operate Together to Prevent Silent DNA Drift.* May 12, 2026. ORCID: 0009-0004-8065-3235.
