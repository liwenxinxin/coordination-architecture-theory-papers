# Rule-Mediated AI Governance: The Composition of Human-Governed and AI-as-Substrate-Mediator in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural property that emerges when two of the source paper's foundational commitments — human-governed and AI-as-substrate-mediator — compose: namely, **rule-mediated AI governance**, the architectural pattern by which humans govern AI behavior through orchestration rules rather than through modification of the AI itself.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's six architectural commitments include human-governed (an authority architecture over substrate content and orchestration rules) and AI-as-substrate-mediator (a five-property role specifying how the LLM operates over the substrate). Each is independently formalized in adjacent derivation notes. Neither commitment, in isolation, fixes the architectural pattern by which humans govern AI behavior in a CKS deployment. Human-governed could be satisfied by deployments in which AI is governed through fine-tuning, prompt engineering, training-data curation, or vendor-provided governance affordances. AI-as-substrate-mediator could be satisfied by deployments in which the LLM operates as mediator under rules whose authorship is implementation-defined or vendor-managed. The composition of the two commitments produces what neither yields alone: humans author and modify rules, the rules govern cells, and cells operate the AI as mediator. This note formalizes that emergent property as **rule-mediated AI governance**, states its four operational components, identifies what the composition forces beyond either commitment alone, distinguishes anti-patterns that violate the composition specifically (including governance-through-fine-tuning and prompt-engineering-as-governance, neither of which violates either foundational commitment in isolation), names four adjacent patterns the composition is not, and provides an operational test with three sharpening properties.

## 1. Why the composition pair needs to be formalized as standalone

The human-governed and AI-as-substrate-mediator commitments each carry independent operational content. Each has been formalized as a standalone architectural commitment in an adjacent note. Neither formalization, taken alone, fixes the architectural pattern by which humans govern AI behavior in a CKS deployment.

The asymmetry is what makes the standalone treatment necessary. Human-governed can be satisfied by deployments that grant humans full authority over a substrate without committing to any particular mechanism for governing the AI itself. A deployment in which humans hold authority over substrate content and separately fine-tune the AI to change its behavior satisfies human-governed individually. AI-as-substrate-mediator can be satisfied by deployments in which the LLM operates as mediator under rules whose authorship is implementation-defined, framework-default, or vendor-managed. A deployment in which the LLM operates over a substrate under externally supplied rules satisfies AI-as-substrate-mediator individually.

Neither such system instantiates what the CKS pattern commits to at the AI-governance layer. The pattern's distinctive move is to anchor AI governance to rule authoring under human authority — rules that are themselves substrate content, that govern cells, and under which cells operate the AI as mediator. The lever humans pull to change AI behavior is rule modification, not AI modification. This pattern is what the composition produces, and is not produced by either commitment alone.

The composition's standalone treatment is operationally consequential. In 2024–2026 AI deployments, "governing AI" is dominantly approached through fine-tuning model weights, prompt engineering as the governance lever, training-data curation, vendor-specific governance APIs, or configuration-management changes. None is rule-mediated AI governance in the CKS sense. The composition forces a different architectural pattern, and naming the pattern as standalone makes the difference architecturally describable rather than implicit.

The source paper's §4.4 describes how cells operate the AI under rules within the orchestration layer; this note formalizes that description as a standalone architectural property. A sibling Phase A4 note formalizes the human-governed × substrate-as-source-of-truth composition (governance-against-authoritative-content). Together the two cover how human-governed composes with the two foundational commitments most directly relevant to its operation — the one fixing *what* governance lands on, and the one fixing *how* AI behavior is governed.

## 2. The emergent property, defined precisely

When human-governed and AI-as-substrate-mediator compose, they produce an architectural property — **rule-mediated AI governance** — with four operational components. A deployment instantiates the composition if and only if all four hold at all times during the deployment's existence.

**(a) Humans govern AI behavior through rules, not through AI modification.** Rule authoring is the canonical architectural mechanism by which humans determine what the AI does. Humans do not govern AI behavior by fine-tuning the model, by curating training data, by engineering prompts as the governance lever, or by operating vendor-specific governance APIs. They govern by authoring orchestration rules — human-authored substrate content under which cells execute over substrate.

**(b) AI capability and AI behavior are architecturally separated.** AI capability — what the AI is able to do, given its training, parameters, and vendor-provided features — is treated as vendor-managed, not as a direct governance object at the architectural layer. AI behavior — what the AI does in this deployment, in which operations, with what outputs, under what transformations — is human-governed through rules. The two are architecturally distinct objects of governance. The separation is what makes vendor-provided AI architecturally acceptable in CKS: humans need not govern capability (the vendor manages it), because behavior is governed at the rule layer above.

**(c) All AI-affecting-substrate operations are rule-governed.** Every operation in which the AI affects substrate state is governed by a human-authored orchestration rule. There are no AI-affecting-substrate operations outside rule-governance. This is the operational expression, at the AI-output layer, of AI-as-substrate-mediator's property that the LLM writes to substrate only under orchestration rules; the composition with human-governed adds that those rules are themselves authored under human authority.

**(d) AI behavior changes occur through rule modification, not through AI modification.** The architectural mechanism by which a human changes AI behavior is rule modification — adding, editing, or replacing orchestration rules under the modify right. To change what the AI does, the human modifies the rule; the human does not modify the AI.

The four components are jointly necessary. A deployment satisfying (a)–(c) but failing (d) — in which rules govern most operations but AI behavior changes are made by fine-tuning rather than by rule modification — instantiates the foundational commitments individually but fails the composition. A deployment satisfying (a), (b), and (d) but failing (c) — in which rule modification is the AI-behavior-modification mechanism for governed operations but a class of AI-affecting-substrate operations sits outside rule-governance — likewise fails the composition.

## 3. What the composition forces beyond either commitment alone

The composition is operationally consequential because it forces architectural decisions neither foundational commitment forces alone.

*Governance cannot be through fine-tuning.* Human-governed in isolation can be satisfied by humans fine-tuning the model. The composition forces governance through rule authoring under human authority, not through model weight modification.

*Governance cannot be through prompt engineering as the governance lever.* Human-governed in isolation can be satisfied by humans engineering prompts to change AI behavior. The composition forces governance through orchestration rules. Prompt construction within cells, under rules, remains admissible as part of rule-governed cell execution; what the composition prohibits is prompt engineering *as* the governance mechanism in lieu of rule authoring.

*Governance cannot be through training-data curation.* Human-governed in isolation can be satisfied by humans curating the data the AI was trained on. The composition forces governance over what the AI does in the deployment, not over what the AI learned.

*The AI cannot operate without explicit rule-mediation.* AI-as-substrate-mediator in isolation can be satisfied by an LLM operating as mediator under rules whose authorship is implementation-defined or vendor-managed. The composition forces explicit rule-governance under human authority.

*Rules must be human-authored.* The composition forces orchestration rules to be authored by humans through architectural mechanism. LLM-drafted rules subject to human authority before they take effect remain admissible under the human-governed commitment's labor-allocability framing; rules generated by AI or vendor systems and committed outside human authority do not.

*Capability and behavior must be architecturally distinct.* Architectures that conflate AI capability with AI behavior — by making behavior changes architecturally indistinguishable from capability changes, or by treating vendor-managed capability changes as governance moments — violate the composition.

*Vendor changes must not break governance.* Because the composition anchors governance to substrate-resident rules, governance operates at a layer independent of vendor-specific affordances. Migrating to a different AI vendor, or accepting a vendor model update, must not require re-architecting the deployment's governance.

## 4. Anti-patterns specifically violating the composition

The composition admits a sharper anti-pattern set than either foundational commitment alone, in three classes.

The first class is anti-patterns at the AI-as-substrate-mediator layer that prevent the composition from operating. *LLM-as-autonomous-agent*, in which the LLM holds goals, plans, and intermediate state across multiple steps and exercises judgment about what actions to take, violates the composition because rule-mediation cannot operate over an LLM that directs its own behavior; rules become advisory rather than governing. *LLM-as-terminal-producer*, in which LLM outputs flow directly to substrate state without rule-governed transformation, violates the composition because rule-governance is bypassed at the output layer. *LLM-as-source-of-truth*, in which the LLM exercises authority over substrate content (silent overwrite, collapse of preserved contradictions, modification of orchestration rules), violates the composition because rule-governance is bypassed at the authority layer.

The second class is the canonical composition violation. *LLM-gatekeeping*, in which an LLM is interposed between humans and the substrate where rules live, violates the composition distinctively. The deployment may individually satisfy human-governed (humans formally hold rights) and individually satisfy AI-as-substrate-mediator (the LLM operates as mediator nominally), but the composition fails because rule authoring under human authority cannot operate when the LLM gates the human's access to rules. The sibling Phase A4 note treats LLM-gatekeeping as the canonical violation of governance-against-authoritative-content; the present composition treats it as a violation of governance-of-AI-through-rules — the same anti-pattern violates both compositions, in different operational respects.

The third class is the operationally significant one — anti-patterns that violate the composition without violating either foundational commitment individually. *Governance-through-fine-tuning* satisfies human-governed individually (humans hold authority over the AI through the right to fine-tune) and may satisfy AI-as-substrate-mediator individually (the LLM operates as mediator with fine-tuned weights), but fails the composition because governance lands at the AI layer rather than at the rule layer. *Prompt-engineering-as-governance* satisfies AI-as-substrate-mediator individually (the LLM is mediator) and may satisfy human-governed individually (humans control the prompts), but fails the composition because governance lands at the prompt-construction layer rather than at the rule-authoring layer. *Training-data-curation-as-governance* fails analogously to fine-tuning: governance lands at the data layer, not the rule layer. *Vendor-API-governance*, in which humans govern AI through vendor-provided affordances (content policies, moderation settings, "responsible AI" features), fails the composition because governance is vendor-mediated rather than architecturally rule-mediated; the rules under which the AI operates are not human-authored substrate content. *Configuration-management-as-governance*, in which humans modify deployment configurations to govern AI behavior, fails the composition because configurations outside the substrate are not orchestration rules in the architectural sense — the source paper commits orchestration rules to live as substrate content, not as deployment-environment state.

This third class identifies systems that look governable on a per-commitment review and yet are not architecturally governable in the CKS sense.

## 5. Operational decisions the composition forces

A deployment satisfying the composition makes specific architectural decisions, jointly necessary.

All AI-affecting-substrate operations are rule-governed: every operation in which the AI affects substrate state is governed by a rule, with no exceptions or pre-rule paths through which AI outputs reach substrate state. Rules are substrate-resident: orchestration rules live as substrate content, governed by the same authority architecture as other substrate content; rules outside the substrate (in deployment configurations, vendor APIs, framework defaults) are not rules in the architectural sense. Rule modification is the AI-behavior-modification mechanism: when humans need to change AI behavior, the architectural mechanism is rule modification — exercising the modify right over orchestration rules — and the deployment does not provide alternative architectural paths (fine-tuning interfaces, prompt-template editors operating outside rule authoring, vendor-policy dashboards) as the governance mechanism. AI capability is vendor-provided and architecturally separated: capability is not a governance object at the architectural layer, which is what enables vendor changes, model updates, and vendor migrations to occur without re-authoring of the governance pattern. Cells operate the AI under rules: every cell that uses the AI operates the AI under its orchestration rule, reading substrate content as primary state, invoking the AI within the rule's bounds, writing to substrate under the rule, with the write recorded with attribution. The AI does not exercise authority: AI-as-substrate-mediator's non-authority property is preserved by the composition, with rule-mediation specifically preventing AI authority exercise. Governance is permanent across AI capability changes: the temporal property of the human-governed commitment — that authority is exercisable at any time — extends through the composition to AI behavior, which remains governable through rule modification across model updates, vendor migrations, and capability changes.

## 6. What the composition is NOT

Stating what the composition is not, precisely, prevents drift toward four adjacent patterns it is commonly conflated with.

*Not governance-through-AI-modification.* Architectures in which humans govern AI behavior through fine-tuning, retraining, weight modification, or other AI-internal changes do not satisfy the composition. Fine-tuning may be a vendor-side capability the deployment uses; it is not the architectural governance mechanism.

*Not prompt-engineering-as-AI-control.* Architectures in which humans govern AI behavior through prompt engineering — even sophisticated, structured, version-controlled prompt engineering — do not satisfy the composition. Prompt construction within cells, under rules, is admissible; the anti-pattern is prompt engineering as the governance mechanism.

*Not vendor-API-governance.* Architectures in which humans govern AI through vendor-specific governance APIs do not satisfy the composition. Vendor governance affordances may serve as adjacent inputs to cells; the anti-pattern is vendor governance as the architectural mechanism in lieu of rule authoring.

*Not policy-document-AI-control.* Architectures in which humans author policy documents that the AI interprets and applies do not satisfy the composition. Rules must be substrate-resident orchestration content authored under human authority — not external documents the AI reads, interprets, and applies at its own discretion. Policy documents authored as input material to rule authoring are admissible; policy-document interpretation as the governance mechanism is not.

## 7. Operational test

A deployment satisfies the composition of human-governed and AI-as-substrate-mediator if and only if all of the following hold at all times during the deployment's existence.

1. Humans govern AI behavior through orchestration rules — by authoring, modifying, and overriding rules. They do not govern AI behavior through model fine-tuning, training-data curation, prompt engineering as the governance lever, vendor-API governance, or configuration-management changes treated as governance moments.

2. AI capability and AI behavior are architecturally separated. Capability is vendor-provided and not a direct governance object at the architectural layer; behavior is human-governed through rules.

3. All operations in which the AI affects substrate state are governed by a human-authored orchestration rule.

4. AI behavior changes occur through rule modification. Where the deployment provides a path to change AI behavior other than rule modification, that path is either capability-layer (vendor-managed and architecturally separated) or violates the composition.

The test sharpens through three operational properties.

**Rule-governance-of-AI-behavior test.** Trace the AI-affecting-substrate operations in the deployment. Each must be governed by a rule. Operations that affect substrate state without rule-governance indicate composition failure.

**AI-modification-versus-rule-modification test.** Identify the deployment's mechanism for changing AI behavior. The mechanism must be rule modification. AI behavior changes made by fine-tuning, by editing prompts as the governance lever, by changing training data, or by operating vendor-governance APIs indicate composition failure.

**Capability-behavior-separation test.** Examine whether vendor-provided AI capability could be replaced — for example, by migrating to a different AI vendor — without re-architecting the deployment's governance. Inability to migrate without re-architecting indicates composition failure.

A one-sentence test for analysts classifying a deployment quickly: *if a deployment governs AI behavior through orchestration rules — not through fine-tuning, training-data curation, prompt engineering as governance, or vendor-API governance — with AI capability and behavior architecturally separated and all AI-affecting-substrate operations rule-governed, then the deployment satisfies the human-governed × AI-as-substrate-mediator composition.* The four-component definition in §2 plus the operational test above provide the full architectural specification for cases requiring detailed analysis.

## 8. Why naming this composition matters

The composition of human-governed and AI-as-substrate-mediator is what makes the CKS pattern architecturally distinctive at the AI-governance layer. Without publishing it as standalone, the rule-mediated AI governance pattern is implicit in the foundational commitments rather than architecturally specified. Implementations that satisfy human-governed individually or AI-as-substrate-mediator individually but fail the composition produce systems that look governable on a per-commitment review and are not architecturally governable in the CKS sense — governance operates at the AI layer (fine-tuning, prompt engineering) rather than at the rule layer; capability and behavior are conflated; rule modification does not change AI behavior. The composition specifically prevents these failure modes.

Naming the composition as standalone gives downstream readers a precise specification of CKS's rule-mediated AI governance pattern and its operational requirements. It makes the boundaries between rule-mediated AI governance and adjacent governance patterns architecturally describable rather than implicit. And it produces an independently citable target for the architectural pattern that is operationally distinctive at the AI-governance layer in 2024–2026 — a layer where governance approaches dominantly rest on AI modification, prompt engineering, training-data curation, or vendor APIs.

This note follows a sibling Phase A4 note formalizing the human-governed × substrate-as-source-of-truth composition. Together, the two cover how the human-governed commitment composes with the two foundational commitments most directly relevant to its operation. Subsequent composition-pair notes will formalize additional architecturally significant pairs from the larger set the foundational commitments admit.

Subsequent work that adopts, extends, composes, or argues against the CKS pattern at the AI-governance layer should use *rule-mediated AI governance* in the sense formalized here. Subsequent work that governs AI through model modification, prompt engineering as the governance lever, training-data curation, or vendor-managed governance — without rule authoring under human authority being the architectural mechanism — is using a different governance pattern, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Rule-Mediated AI Governance: The Composition of Human-Governed and AI-as-Substrate-Mediator in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
