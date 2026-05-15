# FAI Governance and the Non-Specialist Principle

**Series note:** D2.75 — Phase D2, Note #570
**Derives from:** D1.02 (six Paper 1 commitments at FAI scope), specifically Paper 1 A1.11 (non-specialist governance)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 1's commitment to non-specialist governance — that the rights to inspect, modify, and override substrate content and orchestration rules are exercisable by humans without specialist expertise — holds at every scope where CKS architecture operates. D2.75 formalizes how this commitment extends to the inter-Self scope of Full Aspect Integration (FAI) governance. FAI involves inter-organizational coordination across shared substrates, which might seem to demand specialized technical or negotiation expertise beyond what Paper 1's cell-scope commitment addresses. It does not. This note identifies the six FAI governance activities an organizational governance practitioner should be able to perform without specialist AI technical knowledge or inter-organizational negotiation expertise, and traces those activities to four architecture properties that make them accessible: configuration expressed in governance terms, an explicit non-specialist documentation standard, shared substrate content treated as governance artifact rather than technical system state, and standing configuration templates that allow reuse of established governance decisions. The note also clarifies where specialist support is appropriate — in governance labor (technical implementation, complex rule authoring), not in governance authority (the decisions themselves) — and identifies the anti-pattern of specialist gatekeeping, in which specialist sign-off is required for authority decisions that governance practitioners should make independently.

---

## 1. D2.75 as operational decomposition of D1.02 at FAI scope

D1.02 establishes that all six Paper 1 commitments hold at the inter-Self FAI scope by inheritance through the shared substrate. One of those six commitments is Paper 1's non-specialist governance commitment — the architectural property, formalized in the companion note *Non-Specialist Governance, Not Non-Specialist Authorship* (Li, April 2026), that the rights to inspect, modify, and override substrate content and orchestration rules are exercisable by humans who have no specialist expertise in artificial intelligence, software engineering, or the substrate's architecture, using only the host environment's commodity affordances.

D2.75 is the operational decomposition of that commitment at FAI scope. It answers the question: what does the non-specialist governance commitment mean specifically for governance practitioners who are responsible for governing a FAI configuration — a shared substrate joining two or more organizational Selves under joint authority?

The question is non-trivial because FAI introduces inter-organizational coordination structure that has no exact analog in Paper 1's cell-scope architecture. A governance practitioner governing a single organization's CKS substrate operates within a single governance perimeter, governing substrate content produced by known cells under known orchestration rules. A governance practitioner governing a FAI configuration operates within a joint authority structure across multiple organizations' governance perimeters, governing a shared substrate that receives content from aspects contributed by multiple Selves, under orchestration rules co-authored under joint authority, with conflict-handling mechanisms that may surface content from Selves with different operational contexts. The inter-organizational scale might appear to require specialized expertise — inter-organizational negotiation skills, technical AI architecture knowledge, or deep familiarity with the technical implementation of the shared substrate's host platform.

D2.75 formalizes why it does not, and identifies the four architecture properties that make FAI governance accessible under the same non-specialist commitment Paper 1 establishes at cell scope.

---

## 2. What non-specialist FAI governance means operationally

The non-specialist commitment at FAI scope means an organizational governance practitioner — one who is familiar with the organization's operational domains and governance practices, but who holds no specialist expertise in AI architecture, inter-organizational negotiation, or the technical implementation of the shared substrate — should be able to perform all of the following FAI governance activities:

**Review and authorize a FAI configuration (D2.12).** Given a proposed FAI configuration specifying the configuration dimensions for a shared substrate event — sharing scope, persistence policy, cooperation or competition variant, cardinality, provenance carry-over depth, multi-mediator coordination — the practitioner can evaluate whether the configuration is appropriate for the operational context and issue or withhold authorization.

**Inspect shared substrate content using the inspect right (D2.04).** The practitioner can read the content of the shared substrate — contributed aspects, preserved conflicts, annotations, provenance records — in the host environment without specialized tooling or technical intermediation.

**Respond to escalated conflicts (D2.14).** When the conflict-handling mechanism's orchestration-rule tier fails to resolve a conflict and escalates to joint human authority, the practitioner can review the preserved conflict record, understand the nature of the disagreement from the governance record, and issue a resolution or deferral decision.

**Review and authorize DNA absorption (D2.11).** When a FAI event produces content eligible for DNA-layer ingestion at a home perimeter, the practitioner can review what is proposed for absorption, evaluate its appropriateness for the organization's governance configuration, and authorize or decline the absorption.

**Conduct a post-mortem review (D2.39).** After a FAI event completes, the practitioner can review the governance record — what was configured, what conflicts arose, how they were handled, what was absorbed — and assess whether the event operated within the intended governance parameters.

**Complete the onboarding checklist (D2.69).** When joining a new FAI configuration, the practitioner can work through the established onboarding steps — confirming configuration parameters, verifying governance records are accessible, establishing escalation paths — without requiring specialist technical guidance.

Each of these activities is an exercise of governance authority. None requires the practitioner to understand the technical implementation of the shared substrate's host platform, the internal architecture of the participating Selves' cell structures, or the technical mechanics of how aspect content is merged. The architecture is responsible for making these activities accessible; the practitioner is responsible only for the governance judgment the activity requires.

---

## 3. Four architecture properties that enable non-specialist FAI governance

### Property 1 — Configuration expressed in governance terms

The configurable dimensions of a FAI event — sharing scope, persistence policy, cooperation/competition variant, cardinality, provenance carry-over depth, multi-mediator coordination — are expressed in governance terms throughout the architecture. Sharing scope describes which aspects and which content classes are included in the exchange, a question of operational boundary. Persistence policy describes what happens to shared substrate content after the FAI event dissolves, a question of record-keeping. Cooperation and competition variant describes whether the event's exchange dynamics are oriented toward joint output production or toward independent parallel operation with shared visibility, a question of organizational intent.

A governance practitioner who understands the organization's operational domain can evaluate each of these dimensions against the organization's governance policies without needing to know how any of them is implemented in the host platform. The six dimensions are not parameters in a technical configuration file; they are governance choices expressed in the terms governance practitioners use to evaluate organizational decisions. Paper 3 Claim 5 establishes this by making configuration itself substrate content, authored under joint human authority and governable under the same inspect, modify, and override rights the rest of the substrate carries.

### Property 2 — Non-specialist documentation standard (D2.36 Standard 1)

D2.36 Standard 1 establishes that FAI governance documentation must be readable by practitioners without specialized technical knowledge. The standard is not a documentation style preference; it is itself the non-specialist governance commitment applied to the documentation layer. Governance records that require specialist interpretation to understand are not accessible to the governance practitioners they are supposed to serve, and a system that produces inaccessible governance records does not satisfy the non-specialist governance commitment regardless of how the underlying architecture is organized.

The documentation standard requires that configuration records, conflict records, escalation records, absorption authorizations, and post-mortem records be written in terms a governance practitioner can read and act on. Where technical detail is necessary to preserve a complete record, it is segregated from the governance-facing content so that practitioners can engage with the governance record without navigating technical content.

### Property 3 — Shared substrate content as governance artifact

In a CKS-governed FAI event, the shared substrate and everything it contains — contributed aspects, conflict records, provenance annotations, absorbed content — is governed substrate content. It is not a technical system internal. It is not housed in a runtime that only technical staff can access. It lives in a host environment that provides direct human read and write access as an architectural requirement, and it is organized to be readable by governance practitioners exercising the inspect right.

This property is what makes the inspect right meaningful at FAI scope. When a governance practitioner needs to review a preserved conflict, they can read the conflict record in the shared substrate. When they need to review what was contributed by a participating Self's aspect, they can read the contributed content in the shared substrate. When they need to trace the provenance of an absorbed value back through the FAI event, they can follow the provenance record in the shared substrate. None of these activities requires the practitioner to access a technical system layer below the substrate; the substrate is the source of truth, and the governance practitioner's relationship to it is the same inspect-modify-override relationship Paper 1 establishes at cell scope.

### Property 4 — Standing configuration as governance template

At high governance volume — when an organization participates in recurring FAI events with similar structure — the standing configuration mechanism (D2.21) allows governance decisions to be encoded once in a reusable template and applied to new events without requiring the governance practitioner to re-author decisions from scratch. A standing configuration specifies the governance choices for a recurring FAI event class: what sharing scope, what persistence policy, what conflict-handling tier selections, what escalation paths. A governance practitioner who encounters a new event of that class can apply the standing configuration template, confirm that the new event fits within its parameters, and authorize it under the template.

Standing configurations reduce the per-event governance effort without reducing governance authority. The practitioner applying a template is exercising the same authorization judgment they would exercise if authoring the configuration from scratch — they are confirming that the template is appropriate for the event — and they retain the full override right to deviate from the template when the event's particulars require it. The template reduces labor; it does not transfer authority to the template itself.

---

## 4. What requires specialist support: governance labor, not governance authority

The non-specialist commitment applies to governance authority — the decisions that governance practitioners make when they authorize configurations, respond to escalations, authorize absorptions, and conduct reviews. Some activities supporting FAI governance require specialist skill, and naming them precisely avoids the misreading that the non-specialist commitment implies specialists are unnecessary.

**Technical implementation of the shared substrate on a host platform** requires specialist skill in the host platform and in the CKS architectural requirements the platform must satisfy. A governance practitioner does not need to perform this implementation or understand it in detail; they need to be able to exercise governance rights over the substrate the implementation produces. The specialist's work is a governance labor task — producing the infrastructure the governance practitioner governs — not a governance authority task.

**Initial architecture of a CKS-compliant Self** requires specialist understanding of Paper 2's Self architecture, the aspect and cell structure, and the layer organization. A governance practitioner authorizing a FAI configuration does not need to be able to construct the Self architecture from scratch; they need to understand the governance choices the architecture presents and be able to evaluate those choices against the organization's governance policies.

**Orchestration rule authoring for complex conflict classes (D2.15)** requires skill in understanding how conflict classes will be encountered in the shared substrate and how orchestration rules should respond to them. Governance practitioners authorize the orchestration rules and can override their effects; authoring the rules is a labor task that may benefit from specialist involvement. Once the rules are authored and installed as substrate content, they are governable by non-specialists under the inspect, modify, and override rights.

In each case, the pattern is the same. Specialist skill helps with labor that produces governance infrastructure. Governance authority over the infrastructure that results remains with non-specialist governance practitioners. The distinction is not novel to FAI scope; it is the same authority-not-labor distinction Paper 1 establishes at cell scope (§3.3) and that the companion note *Non-Specialist Governance, Not Non-Specialist Authorship* formalizes as an architectural property.

---

## 5. The authority-not-labor clarification at FAI scope

D2.43 establishes the non-delegation principle: governance authority decisions cannot be delegated to specialists even when specialists perform governance labor alongside them. The non-specialist governance commitment is not a commitment that non-specialists perform all work; it is a commitment that specialists do not accumulate governance authority by performing governance labor.

At FAI scope, this clarification operates against a specific drift pattern. Because FAI involves inter-organizational coordination and shared substrates that are technically more complex than a single organization's substrate, there is a natural organizational tendency to route governance authority decisions through the specialist teams who implement and maintain the shared substrate. The specialist team knows the technical details; they are positioned to evaluate whether a configuration is technically sound; it seems natural for governance authority to follow technical expertise.

The non-specialist commitment operates against this tendency. A FAI configuration may be technically sound and operationally inappropriate — sharing scope too broad, persistence policy misaligned with the organization's record-keeping governance, cooperation variant inconsistent with the inter-organizational relationship. These are governance judgments. They require the practitioner's knowledge of the organization's operational domain and governance policies, not technical expertise in the shared substrate's implementation. When specialist teams make these governance decisions because they hold the technical knowledge, governance authority has migrated from practitioners to specialists — and the non-specialist governance commitment has been violated even if non-specialists are nominally named as the authorizing parties.

D2.43's non-delegation principle ensures that the authority remains with practitioners regardless of what labor specialists perform.

---

## 6. Anti-pattern: specialist gatekeeping

The specialist gatekeeping anti-pattern is the inter-Self scope instance of the failure mode Paper 1 identifies in its non-specialist governance commitment. Specialist gatekeeping occurs when specialist technical sign-off is required as a prerequisite for governance authority decisions that governance practitioners should be able to make independently.

At FAI scope, specialist gatekeeping takes concrete forms. Requiring that an IT architecture team approve FAI configuration changes before governance practitioners can authorize them. Requiring that the team who implemented the shared substrate certify that a proposed absorption is technically compatible before a governance practitioner can authorize it. Requiring that a technical specialist review an escalated conflict before the governance practitioner issues a resolution. In each case, the specialist's sign-off is positioned as a prerequisite rather than as labor support. The practitioner cannot exercise governance authority until the specialist authorizes them to do so.

Specialist gatekeeping violates the non-specialist governance commitment regardless of how the gatekeeping is procedurally framed. A system in which governance authority cannot be exercised without specialist authorization is not non-specialist-governed, even if the nominal authority is held by non-specialists on paper. Paper 1's non-specialist governance commitment requires that the rights to inspect, modify, and override be *exercisable* without specialist involvement — not merely granted in theory while conditioned on specialist authorization in practice.

The appropriate role for specialists in FAI governance is labor support that governance practitioners may draw on when they choose to. A governance practitioner who wants a technical review before authorizing a complex configuration can request one; the specialist's assessment is input to the practitioner's decision, not a condition on it. The practitioner's authority remains theirs whether or not they request specialist input.

---

## 7. Operational test

A FAI governance architecture satisfies the non-specialist governance commitment at FAI scope if and only if, for each of the following governance decisions, a governance practitioner without specialist AI technical expertise or inter-organizational negotiation expertise can complete the decision using only the governance records in the shared substrate and the host environment's commodity affordances:

1. **FAI configuration authorization:** Given the governance records documenting the proposed configuration dimensions (sharing scope, persistence policy, cooperation/competition variant, cardinality, provenance carry-over depth, multi-mediator coordination), the practitioner can evaluate the configuration against the organization's governance policies and issue a documented authorization or rejection.

2. **Escalation response:** Given the governance record of a preserved inter-Self conflict that has been escalated to joint human authority, the practitioner can understand the nature of the disagreement — what content values are in conflict, which participating Self contributed each, what orchestration rules were attempted — and issue a resolution or deferral decision.

3. **DNA absorption authorization:** Given the governance record of content proposed for absorption from a completed FAI event, the practitioner can evaluate whether the proposed absorption is within the organization's governance parameters and issue a documented authorization or refusal.

A system that requires specialist intermediation for any of these three decisions — either because the governance records are not readable without specialist knowledge, or because the host environment does not provide direct practitioner access, or because a procedural gate conditions the decision on specialist sign-off — does not satisfy the non-specialist governance commitment at FAI scope.

---

## 8. Conclusion

The non-specialist governance commitment Paper 1 establishes at cell scope holds at FAI scope by architectural inheritance through D1.02. FAI's inter-organizational structure and shared substrate do not introduce a new category of governance decision requiring specialist expertise; they introduce the same governance decisions — authorization, inspection, escalation response, absorption decision, post-mortem review — at a broader scope. Four architecture properties make these decisions accessible to non-specialist governance practitioners: configuration expressed in governance terms, an explicit documentation standard requiring practitioner-readable records, shared substrate content organized as governance artifact rather than technical system state, and standing configuration templates that allow established governance decisions to be reused.

The boundary between governance authority and governance labor is the same at FAI scope as at cell scope. Specialists help with the labor of implementing shared substrates, authoring complex orchestration rules, and constructing CKS-compliant Selves. Governance authority over everything the architecture produces remains with organizational governance practitioners who need not hold specialist technical expertise to exercise it. The specialist gatekeeping anti-pattern — conditioning governance authority decisions on specialist sign-off — violates the non-specialist governance commitment at both scales, and D2.75 names it as an impermissible failure mode at FAI scope.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Non-Specialist Governance, Not Non-Specialist Authorship: What the Coordination Knowledge Substrate Pattern Makes Available to Whom.* 28 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance and the Non-Specialist Principle.* D2.75 — CKS Derivation Note Series, Note #570. May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
