# The AI Training-Data Inclusion Boundary: A Standalone Architectural Treatment for Vendor Training-Data Policies in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize a single boundary case — the AI training-data inclusion scenario — as a standalone architectural treatment that articulates how the CKS pattern handles AI vendor training-data policies affecting substrate content while preserving the source paper's commitments.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern places an LLM in the AI-as-substrate-mediator role (§4.2 of the source paper): the LLM helps humans read, write, interpret, and compose substrate content while the substrate remains the authoritative artifact. When the LLM is provided by a third-party vendor whose data-handling practices include training future models on data passed through their service, retaining data for safety review, using data for model improvement, or sharing data with third-party evaluators, substrate content is exposed to vendor training inclusion as a side effect of cell execution. This note formalizes the resulting boundary case as a standalone architectural treatment: it identifies the architectural commitments stressed, articulates the integrated treatment that resolves the boundary while preserving substrate authoritativeness per A1.08 and A2.21 Property C, enumerates anti-pattern treatments that would violate the architecture, and names the operational implications and limits of the treatment.

## 1. Why the AI training-data inclusion boundary needs to be formalized as standalone

AI vendor training-data policies are operationally consequential and architecturally distinctive in the 2024–2026 deployment landscape. The major commercial LLM vendors publish data-handling policies that vary in material respects: some retain input data for fixed periods for safety review; some train next-generation models on data passed through default API endpoints while excluding data passed through enterprise endpoints; some share data with third-party evaluators under specific safety regimes; some change these policies between versions of their published terms. Each behavior affects what happens to substrate content when a cell in a CKS-coherent deployment consults the vendor's LLM in its A1.04 mediator role.

The architectural distinction between vendor training inclusion and substrate authoritativeness is non-obvious. A reader may suppose that data incorporated into a vendor's training corpus has, by that fact, become authoritative for the vendor's future model outputs in a way that competes with the deployment's substrate. A reader may equally suppose that vendor training inclusion violates A2.21 Property C (LLM does not hold substrate-relevant state outside substrate) because the vendor's weights now incorporate gradients computed over substrate-derived data. Both readings collapse important distinctions, and standalone formalization is what keeps the distinctions visible.

The boundary case also has strategic prior-art weight. "AI data privacy" and "AI training-data control" are highly active concerns in 2024–2026 commercial discourse, and proprietary frameworks for governing data flow to AI vendors are proliferating. Formalizing the CKS-coherent treatment as derived from already-defended commitments establishes the pattern's response as architectural and pre-stated rather than novel and bolt-on. The load-bearing source-paper sections are §4.2 (AI-as-substrate-mediator role), §4.5 (hybrid system composition), §11.3 (substrate as source of truth), and §11.4 (the architectural test of authority).

## 2. The boundary case scenario and what makes it non-obvious

The scenario is concrete. A CKS-coherent deployment instantiates one or more cells whose execution involves consulting an LLM in the A1.04 mediator role. The LLM is provided by a third-party vendor whose published policy states that data passed through the service is retained, used for training future model versions, used for safety review, used for model improvement, or shared with third parties for evaluation, in some combination. As cells execute, substrate content — content the deployment treats as authoritative — passes through the vendor's API and becomes subject to the vendor's policy. The deployment must continue operating with substrate authoritativeness preserved per A1.08 and with the architectural commitments of the source paper intact.

What makes the scenario non-obvious is that the vendor's training inclusion is genuinely consequential — it affects the vendor's future model outputs, has legal and contractual implications, and is the kind of operational fact operators must reason about — yet it is also architecturally orthogonal to several of the commitments it appears to threaten. Vendor training does not transform vendor-side weights into authoritative state about the deployment's specific substrate; it does not give the vendor governance authority over substrate content that originated under A1.01; and it does not displace the substrate as the deployment's source of truth. Each of these architectural facts is true and each is non-obvious; naming the boundary as standalone is what makes the architectural reading visible against the operational one.

## 3. Architectural commitments that are stressed

Six commitments are stressed by the boundary, and articulating each stress precisely is what positions the architectural treatment in §4.

**A1.04 (AI-as-substrate-mediator) with A2.21 Property C.** Property C states that the LLM does not hold substrate-relevant state outside the substrate across cell executions. Vendor training appears to violate Property C because gradients computed over data passed through the vendor's service are now in some sense "held" by the vendor's trained weights. The stress is that "held in weights as a transformation of training data" and "held outside the substrate as authoritative state for this deployment" must not be conflated.

**A1.08 (substrate as source of truth) with A2.42–A2.47.** Substrate-as-source-of-truth states that the substrate is the deployment's authoritative artifact for the five categories §11.3 names. The stress is that vendor training may, after the fact, produce vendor model outputs that mention or reflect substrate-derived patterns; if such outputs are then treated as authoritative, the substrate's authority has been displaced.

**A1.05 (tool-agnosticism).** Tool-agnosticism states that the substrate's commitments are realizable across hosts and LLMs that satisfy the three minimal requirements (§7.1). The stress is that vendor selection may need to incorporate training-data policy as a selection criterion when deployments handle data whose flow is constrained by regulation, contract, or rule.

**A1.01 (human-governed) with A2.04 (orchestration rule authoring).** Human governance says the three rights apply at all times to substrate content and to orchestration rules. The stress is that "what data may flow to which AI vendor" is itself a governance question, and the rules that answer it must be authored under A2.04 by humans rather than determined by a vendor, an external compliance framework, or the LLM itself.

**A1.07 (path retraceability) with A2.40 (six provenance metadata fields).** Path retraceability says any substrate-affecting operation is reconstructible end to end from substrate content alone. The stress is that vendor consultation now has external consequences — the data is also in the vendor's pipeline — and provenance must record what was consulted via which vendor with which data so that the consequences are auditable.

## 4. The architectural treatment

The treatment combines six commitments already defended in the source paper. None of the moves below is new; what is new is the integration that names how the commitments together address the AI training-data inclusion case.

**Substrate authoritativeness is unaffected by vendor training inclusion.** Per A1.08 and the architectural test of authority (§11.4), the substrate remains authoritative for the deployment's coordination state regardless of what a vendor does with copies of data passing through its service in cell execution. A vendor's trained model is a transformation of its training data — a statistical artifact distributed across weights — not a competing source of truth about the deployment. Vendor model outputs flowing back through the mediator role are inputs that the substrate, under orchestration rules, may incorporate or reject; the vendor's training history does not bear on the question of authority. A4.10 names the same property from the composition direction: substrate-resident authoritative content is vendor-independent.

**Vendor training-data policy is an external signal handled per A6.09.** Vendor data-handling policy generally is the domain of the boundary case A6.09 articulates. Training-data policy is a sub-case A6.09's machinery already handles: the vendor's policy is informational input that humans evaluate when deciding what data may flow to which vendor under what rule. Policy changes by the vendor are events under A6.09, not architectural reconfigurations.

**Rules per A2.04 specify what data may flow to which AI vendor.** The locus where the data-flow question is answered is the orchestration-rule layer authored by humans. Rules categorize substrate content by sensitivity, regulatory classification, contractual constraint, or other criteria the deployment determines, and specify which categories may flow through which vendors. The categorization is itself substrate content under A2.46 (Category 4: substrate authoritative for "what rules apply"); the rules are authored, modified, and overridden under the three A1.01 rights. A cell consulting an AI vendor operates under the rule's specification: it does not pass content prohibited by rule even if functionally available, because cell behavior is rule-determined, not capability-determined.

**Provenance per A2.40 records what data went to which vendor.** The six provenance metadata fields A1.07 specifies and A2.40 enumerates already carry the information needed to make vendor consultation auditable. Field 5 (mechanism) identifies the specific vendor, model, and endpoint consulted; field 6 (cell-execution-id) identifies the cell execution under which the consultation occurred. Audit reconstruction per A2.36–A2.39 can answer "what substrate content was exposed to which vendor at what time under which rule" entirely from substrate content.

**Vendor selection per A4.18 considers training-data policies.** Tool-agnosticism does not require indifference among hosts; it requires that the substrate's commitments hold across hosts that satisfy the three minimal requirements. Vendor selection, exercised under human authority, may legitimately incorporate training-data policy as a selection criterion when the deployment's data-flow rules so require. The selection is human-authored per A2.04; the alternation of vendors over time is governed per A1.05.

**A2.21 Property C is preserved by distinguishing training inclusion from state retention.** The architecture distinguishes two scenarios that are operationally adjacent and architecturally separate. "The LLM was trained on data, including substrate-derived data" — the trained model is a statistical transformation of training data and is not authoritative for any specific deployment's state. "The LLM maintains 'what is currently the case' for this specific deployment across cell executions" — this would constitute holding substrate-relevant state outside the substrate, and Property C prohibits it. Vendor training inclusion is the first scenario, not the second; Property C is preserved.

## 5. Anti-pattern treatments that would violate the architecture

Eight anti-patterns name treatments that would, by their structure, violate the architectural commitments named in §3.

**Vendor-training-as-authoritative.** Treating vendor model outputs as authoritative because the vendor's training corpus included substrate-derived data. An instantiation of the A3.13 LLM-as-source-of-truth anti-pattern; the substrate's A1.08 authority is violated.

**Auto-allow-all-data-to-LLM.** Any substrate content may be passed to any consulted LLM without rule-specified data-flow constraints. The decision about what flows to which vendor is abdicated to runtime convenience rather than authored per A2.04.

**LLM-mediated-data-classification.** The LLM itself decides what data is appropriate to send to the LLM — e.g., an upstream LLM call that classifies substrate content for sensitivity and routes accordingly. The data-flow rule, which is governance content per A2.46, has been delegated to LLM judgment. Another A3.13 instantiation.

**Compliance-framework-determines-data-flow.** An external compliance framework imposes data-flow rules outside the A2.04 rule-authoring locus. Encoding external requirements as A2.04 rules is admissible; the anti-pattern is when the framework bypasses A2.04 and operates as a parallel authority. The A1.01 unitary-authority architecture is violated.

**Vendor-training-overrides-substrate-authority.** Post-training vendor outputs are treated as more authoritative than pre-training substrate content because the vendor "knows more now." The temporal variant of vendor-training-as-authoritative; violates the §11.4 architectural test of authority.

**Silent-vendor-training-without-provenance.** Vendor consultation that does not record vendor identity, model, endpoint, or call context in A2.40 provenance — making audit of "what was exposed to which vendor when" impossible after the fact. The A1.07 retraceability commitment is violated.

**Vendor-claims-data-ownership.** Treating a vendor's training-data policy as conferring ownership of substrate content the vendor's model was trained on. Substrate ownership is a function of A1.01 governance, fixed by deployment authorship and not transferable through API consumption.

**Training-data-exemption-from-A2.21.** Allowing the LLM to be authoritative for specific deployment state across cell executions on the grounds that "the LLM was trained on this deployment's data, so it knows the state." This collapses the §4 distinction between "trained on data" and "maintains specific deployment state" and exempts the LLM from Property C on training-history grounds. The exemption is unsupported.

## 6. Operational implications

Four operational implications follow from §4. Deployments that handle regulated, contractually constrained, or otherwise controlled data author rules per A2.04 that categorize substrate content along the relevant axes and specify which categories may flow to which vendors; the categorization is substrate content under A2.46 and is governed under A1.01. Vendor selection per A4.18 incorporates training-data policy where the rule requires — a deployment with non-sensitive data may select among vendors freely, while a deployment with sensitive data may select only vendors whose policies satisfy the rule's constraints. Provenance enables audit of vendor exposure: because A2.40 records vendor identity, model, endpoint, and call context, an auditor exercising the A1.01 inspect right can reconstruct, from substrate content alone, what substrate content has been exposed to which vendor across the deployment's history; this is what makes the boundary operationally tractable in regulated environments. Finally, A6.09 governs the response to vendor policy changes — when a vendor announces a change to its training-data policy, humans evaluate the change against the deployment's data-flow rules, revise rules per A2.04 if needed, and either continue with the vendor or migrate to an alternate vendor per A1.05.

## 7. Limits of the architectural treatment

The treatment is bounded in four respects.

**It applies to AI training-data inclusion specifically.** General vendor data-handling — retention windows, jurisdictional data residency, sub-processor chains, and similar — is the domain of A6.09 broadly. This note formalizes the training-data sub-case because that sub-case is architecturally distinctive (it brings A2.21 Property C into stress) and operationally consequential. Other sub-cases are handled by A6.09's general machinery.

**It does not address vendor unavailability.** The case where a vendor is unavailable, deprecates a model, or terminates a service is the domain of A6.03. Training-data inclusion is a question of governance over data flow under stable vendor availability; unavailability is a question of mediator continuity under vendor disruption.

**It does not address composition partner data sharing.** The case where a CKS-coherent deployment composes with a non-CKS partner system that itself shares data downstream is the domain of A4.16 (retraceability preservation across composition).

**It does not displace substantive legal or regulatory compliance.** Whether a particular deployment's data-flow rules satisfy a particular regulatory regime, contract, or jurisdiction is a substantive question the architecture supports addressing — by making rules authored, categorization explicit, and provenance auditable — but does not itself answer. The architecture provides the loci and the auditability; the substantive content of the rules is the deployment's to author.

## 8. Operational test

A CKS-coherent deployment handles AI training-data inclusion correctly if and only if all of the following hold at all times during the substrate's existence:

1. Substrate content authoritativeness per A1.08 is unaffected by vendor training inclusion — vendor model outputs are not treated as authoritative for the deployment on the basis of the vendor's training history.
2. Data flow to AI vendors is specified by orchestration rules authored under A2.04 — not by vendor judgment, LLM judgment, or external compliance frameworks operating outside the rule layer.
3. Vendor consultations are recorded in A2.40 provenance with sufficient resolution to reconstruct, from substrate content alone, what substrate content was exposed to which vendor at what time under which rule.
4. Vendor selection per A4.18 incorporates training-data policy where the deployment's rules require, with selection exercised under A1.01 human authority.
5. The LLM is not treated as maintaining specific deployment state across cell executions on training-history grounds — A2.21 Property C is preserved by the distinction between "trained on data" (admissible) and "maintains specific deployment state" (prohibited).

A treatment that fails any of (1)–(5) may be a useful treatment, may serve some other architectural purpose, but is not the CKS-coherent treatment of the boundary.

## 9. Conclusion

The AI training-data inclusion boundary is the case where AI vendor training-data policies affect substrate content because cells consulting the vendor's LLM in the A1.04 mediator role expose substrate content to vendor data handling. Naming this boundary as a standalone architectural treatment matters because the operational reality — vendors do train on data, retain data, share data — is non-obviously orthogonal to several of the commitments the case appears to threaten. Substrate authoritativeness per A1.08 is not displaced by vendor training; A2.21 Property C is not violated by gradients computed over training data; A1.05 tool-agnosticism is not undone by vendor selection's incorporation of training-data policy. The treatment combines existing commitments — substrate authority, rule authoring, provenance, vendor selection, and the A6.09 boundary mechanics — into an integrated handling. The anti-patterns ruled out are the readings that would collapse one or more of those commitments into vendor judgment.

A6.13 is the thirteenth of approximately fifteen Phase A6 boundary-case notes; A6.14 (deployment-evolution rule version compatibility) and A6.15 (schema evolution / substrate migration) close the phase.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The AI Training-Data Inclusion Boundary: A Standalone Architectural Treatment for Vendor Training-Data Policies in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
