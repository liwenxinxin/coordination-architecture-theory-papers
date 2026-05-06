# LLM-Gatekeeping Over Substrate Access: An Anti-Pattern at the Intersection of the Human-Governed and AI-as-Substrate-Mediator Commitments in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize one architectural failure mode — **LLM-gatekeeping over substrate access** — as a standalone anti-pattern that compromises two of the source paper's foundational commitments simultaneously: the **human-governed** commitment (§3.1, §3.3) and the **AI-as-substrate-mediator** commitment (§4.1, §4.2, §4.4).

## Abstract

The CKS pattern's human-governed and AI-as-substrate-mediator commitments together specify both *that* humans hold authority over the substrate and *where* the LLM is architecturally positioned with respect to it — as a mediator within cells, not as an arbiter of human access. A specific deployment configuration violates both simultaneously: one in which an LLM is the gatekeeper for human-substrate interaction, requiring humans to go through the LLM to inspect, modify, or override substrate content, with the LLM evaluating, filtering, or authorizing the request. This configuration — *LLM-gatekeeping over substrate access* — is operationally attractive in commercial AI products because natural-language interfaces are commercially expected; it is architecturally distinctive in that humans cannot exercise the three rights directly, and the LLM operates beyond its mediator role. This note formalizes the anti-pattern as standalone: states the four operational components, identifies the commitments it violates (with the AI-as-substrate-mediator decomposition's *Property D — LLM does not exercise authority* — as the most directly violated), traces the failure mode, specifies the architectural correction, distinguishes it from four adjacent legitimate practices, and provides an operational test with three sharpening properties.

## 1. Why the anti-pattern needs to be formalized as standalone

The CKS pattern's foundational commitments include human-governance — humans retain the rights to inspect, modify, and override substrate content and orchestration rules at any time (§3.1, §3.3) — and AI-as-substrate-mediator — the LLM reads substrate as primary state, writes under orchestration rules, holds no substrate-relevant state outside the substrate, exercises no authority over substrate content, and records its writes back as attributed substrate content (§4.1, §4.2). The two work in concert: human-governance specifies that authority lies with humans; AI-as-substrate-mediator specifies *where* the LLM sits relative to that authority — as a mediator within cell executions, not between humans and substrate.

The two commitments admit a specific compound failure mode. A deployment may instantiate the substrate, the cells, and an LLM, and may nominally preserve human authority in its design documents, while operationally configuring the LLM as the *required interface* for human-substrate interaction. Humans interact with substrate by directing or persuading an LLM, which evaluates the request, retrieves or filters substrate content, and presents a transformed view back; modify and override requests pass through the LLM. The substrate exists, the LLM exists, the formal authority structure exists, but humans cannot exercise the three rights directly, and the LLM operates outside its mediator specification.

Standalone formalization is warranted because the anti-pattern violates two foundational commitments simultaneously — downstream readers may recognize one violation but not the other, or may fail to see that the architectural distinction between the legitimate mediator role and the gatekeeping configuration is precise rather than approximate — and because the anti-pattern compromises *Property D — LLM does not exercise authority* — directly: gatekeeping over human access *is* exercising authority, regardless of how the deployment characterizes it.

## 2. The anti-pattern, defined precisely

A deployment exhibits **LLM-gatekeeping over substrate access** when an LLM is interposed in the human-substrate access path such that human exercise of the three rights becomes conditional on LLM cooperation. The configuration has four operational components.

**(a) LLM as required interface.** The deployment is configured such that humans must go through an LLM to inspect, modify, or override substrate content. Direct architectural interfaces to the substrate are absent, hidden, operationally degraded, or restricted to deployment operators rather than the humans who hold authority. The "natural language assistant," "AI co-pilot," or "intelligent search bar" is the only path or the dominant path; humans cannot exercise the three rights independently of LLM availability.

**(b) LLM evaluation of access requests.** The LLM evaluates, screens, or processes human access requests before granting access. Evaluation may include deciding whether the request is "appropriate," determining what content is "relevant," reformulating the request before execution, or denying requests judged out of scope. The evaluation operationally exercises authority over what humans can access.

**(c) LLM filtering of substrate content.** The LLM filters or transforms substrate content before presenting it to humans — selecting which entries to surface, summarizing rather than presenting raw content, paraphrasing rather than quoting, or rendering content in a generated narrative. Humans see *what the LLM presents*, not what the substrate carries.

**(d) LLM authority over modify and override requests.** The LLM accepts, rejects, transforms, or conditions human modify and override requests. Even if the deployment's nominal authority structure designates the human as authority-holder, the LLM's gatekeeping operationally exercises the authority. Override requests — which the source paper specifies as exercisable without justification (§3.3) — require LLM consent, and the LLM may block them on its own evaluation.

A deployment exhibiting any one of (a)–(d) partially exhibits the anti-pattern; a deployment exhibiting all four exhibits it fully. The components are not independent — (a) typically implies (c); (b) typically implies (d) — but they are conceptually distinct.

## 3. Which CKS commitments are violated

LLM-gatekeeping violates two foundational commitments simultaneously, with several decomposition-level commitments operationally compromised.

**Foundational violation 1: human-governed (§3.1, §3.3).** Humans cannot exercise the three rights directly when an LLM gates substrate access. Inspection passes through LLM filtering; modification passes through LLM evaluation; override requires LLM consent — converting a justification-free right (per §3.3) into a justification-required one. The architectural commitment to human authority may be preserved nominally, but the architectural-property reading of the commitment (the rights must be a property of the system's design, not a procedural promise) fails directly.

**Foundational violation 2: AI-as-substrate-mediator (§4.1, §4.2).** The mediator role specifies the LLM's architectural position as *between cell-executor and substrate*: reading substrate as primary source within cell executions, writing under orchestration rules within cell executions. LLM-gatekeeping operates the LLM in a different position — *between humans and substrate* — by interposing it in the human-substrate access path. The two architectural positions are distinct, and the gatekeeping position is outside the mediator role specification. The integrating frame for the mediator role is operationally compromised even when individual mediator properties are nominally preserved within cell executions.

**Direct violation of Property D — LLM does not exercise authority.** The AI-as-substrate-mediator decomposition specifies that the LLM does not exercise authority over substrate content. Gatekeeping *is* exercising authority — the LLM decides what humans can see, what modifications take effect, and what overrides are granted. The architectural commitment to non-authority fails operationally because gatekeeping behavior is operationally authoritative, regardless of whether the deployment frames it as "assistance."

**Operational compromise of substrate-as-source-of-truth for authority.** When LLM gatekeeping is operative, the LLM effectively becomes the de facto authority over human substrate access regardless of the substrate-resident authority structure. The substrate's source-of-truth status for "who has what authority" is operationally compromised because the LLM's gatekeeping decisions, not the substrate's authority structure, determine access.

**Extended violation of the composition requirements.** Multi-substrate composition must preserve per-substrate human governance and the AI-as-mediator role at every layer; LLM-gatekeeping fails both, and a composition built on a gatekeeping deployment propagates the failures across the composed substrates.

## 4. The failure mode

LLM-gatekeeping produces deployments where the LLM effectively operates as authority over what humans can see, modify, or override. The downstream consequences are operationally specific.

**Authority migration and override blocking.** Even when the substrate-resident authority structure correctly specifies the human as authority-holder, the LLM's gatekeeping operationally exercises authority. Override — architecturally designed to be exercisable on the human's authority alone, without justification to the system — becomes conditional on LLM evaluation; the LLM may block override requests it judges as inappropriate or transform them. The architectural commitment to human authority fails because authority is exercisable only through the LLM's cooperation.

**Opaque filtering and hallucination injection.** Humans see what the LLM presents, not substrate content directly. The inspect right fails because the LLM's filtering may obscure substrate content the human is authorized to see, and path retraceability is compromised when the LLM filters provenance during presentation. LLM hallucinations — content not present in the LLM's inputs — can also appear in presented substrate content; humans may believe the substrate carries content the LLM hallucinated, collapsing the architectural distinction between substrate content and LLM output at the presentation layer.

**Model-update sensitivity.** Vendor model updates, fine-tuning changes, or prompt-engineering changes alter the gatekeeping behavior. Access patterns that worked under one model may fail under another, and a content-policy update from the model vendor may render previously accessible substrate content inaccessible. Substrate access becomes mediated by an inherently changing LLM rather than a stable architectural interface.

**Mediator role boundary collapsed.** The architectural distinction between the legitimate mediator role (LLM-substrate within cells) and the gatekeeping anti-pattern (LLM between humans and substrate) is operationally collapsed. Both involve LLMs interacting with substrate; conflating them — through deployment documentation that describes the LLM as a "mediator" in both senses — produces gatekeeping under the cover of mediator-role compliance.

## 5. The architectural correction

The architectural correction operates through three commitments together.

**Direct substrate access for humans.** The substrate must provide direct architectural interfaces for humans to inspect, modify, and override substrate content without LLM mediation. The interfaces must operate independently of LLM cooperation; humans exercising rights through them do not depend on LLM availability, model state, vendor policy, or LLM evaluation. The interfaces need not be elaborate — the source paper's tool-agnosticism commitment names persistent structured state, human read/write access, and LLM access as the three minimal requirements (§7.1), and direct substrate access for humans is satisfied by any environment meeting them.

**Mediator role boundary preservation.** The LLM operates within cells under orchestration rules per the AI-as-substrate-mediator role specification. It reads substrate as primary state and writes under orchestration rules within cells; it does not exercise authority over human access. The mediator role is between cell-executing-LLM and substrate, not between humans and substrate. Deployment architecture should explicitly identify where LLMs operate as cell-mediators and verify that no LLM operates between humans and substrate as gatekeeper.

**Substrate-resident authority structure.** The authority structure for "who has what authority" remains substrate-resident. LLM evaluation, filtering, or gating does not modify the authority structure; authority is architecturally specified and architecturally exercisable through direct interfaces.

A correctly architected deployment may additionally provide LLMs as helpful interfaces — translation, drafting, presentation — which are legitimate when they *complement* direct substrate access rather than gating it. The deployment also operationally tests human direct substrate access, because architectural commitments not operationally tested tend to drift toward what the deployment finds convenient, which under commercial pressure tends toward gatekeeping.

## 6. What the anti-pattern is NOT

Four adjacent practices are commonly conflated with LLM-gatekeeping but are legitimate when humans retain direct architectural access.

**Not LLM-as-translation-interface that does not gate.** LLMs that render substrate content in natural language for easier reading are legitimate when they do not gate access. The anti-pattern arises specifically when translation becomes the only path or filters content; deployments where translation is one of several access methods, alongside direct substrate inspection, satisfy the architecture.

**Not LLM-as-drafting-assistant that does not gate.** LLMs that help humans draft modifications — suggesting wording, providing template content, refining proposed changes — are legitimate when humans retain the direct ability to modify substrate independently. Drafting assistance that becomes a required path through which all human modifications must flow is the anti-pattern.

**Not LLM-as-cell-mediator within cells.** The legitimate AI-as-substrate-mediator role per §4.1, §4.2 — the LLM operating within cells, reading substrate as primary state, writing under orchestration rules, with attribution recorded back as substrate content — is exactly what the source paper specifies. Cell mediation operates between LLM-as-cell-executor and substrate; gatekeeping operates between humans and substrate. Same LLM, same substrate, different position, different commitment status.

**Not LLM-as-informational-presenter that does not condition access.** LLMs that summarize state, highlight changes, or provide dashboards are legitimate when they inform without conditioning access. Presentation that filters out content the LLM decides humans should not see is gating, regardless of whether it is characterized as "summarization," "relevance ranking," or "user-friendly default view."

## 7. Operational test

A deployment exhibits the anti-pattern when any of the four operational components in §2 are present at any time during the substrate's existence. **Three sharpening properties** further distinguish it from adjacent legitimate practices.

**(a) Direct-substrate-access test.** Verify operationally that humans can inspect, modify, and override substrate without LLM mediation. Test by attempting rights exercise through direct substrate interfaces; if no such interfaces exist, or if they require LLM cooperation to operate, the test fails.

**(b) LLM-bypass test.** Verify that LLM unavailability — model offline, vendor outage, prompt-engineering changes, content-policy denial — does not block human substrate access. Test by simulating LLM unavailability and attempting rights exercise; if the rights become unexercisable, the test fails. This property distinguishes architectural direct access from "LLM is technically optional but everything is built around it" deployments.

**(c) Mediator-role-boundary test.** Verify that the LLM operates within cells under orchestration rules, not between humans and substrate. Test by examining the LLM's architectural position; LLMs operating at the human-substrate interface, regardless of how the position is labeled in deployment documentation, fail the test.

A deployment that fails any of (a)–(c) exhibits the anti-pattern in some form, and the architectural correction in §5 specifies the operational changes required.

**The one-sentence test.** *If a deployment requires humans to go through an LLM to access substrate — for inspection, modification, or override — and the LLM evaluates, filters, or gates the human access requests, the deployment exhibits LLM-gatekeeping over substrate access; the architectural commitments to human-governance (humans exercise rights directly) and to AI-as-substrate-mediator (the LLM operates as mediator within cells, not as gatekeeper between humans and substrate) both fail, with Property D — LLM does not exercise authority — directly violated.*

## 8. Conclusion

LLM-gatekeeping over substrate access is the failure mode at the intersection of two foundational CKS commitments. It fails human-governance because humans cannot exercise the three rights directly when an LLM gates substrate access; it fails AI-as-substrate-mediator because the LLM operates beyond its mediator role by positioning itself between humans and substrate; and it fails *Property D — LLM does not exercise authority* — directly, because gatekeeping *is* exercising authority. The architectural distinction between the legitimate mediator role and the gatekeeping anti-pattern is precise but operationally easy to confuse, because both involve LLMs interacting with substrate.

The anti-pattern is operationally attractive in 2024–2026 commercial AI product environments because natural-language interfaces are commercially expected. Implementations under pressure to deliver AI products with conversational interfaces consistently default to LLM gatekeeping — audiences understand "we have a chatbot interface for our AI system" as a positive feature without recognizing the architectural consequence: that humans no longer access substrate directly and the LLM has acquired gatekeeping authority. The correction is specific: humans must have direct architectural access to substrate, the LLM must operate within cells under orchestration rules, and the authority structure must remain substrate-resident. Helpful LLM interfaces are not the failure mode; *required* LLM interfaces are.

This note is the first in the CKS anti-pattern sequence to formalize a failure mode that violates two foundational commitments simultaneously. Subsequent work that adopts, extends, composes, or argues against the CKS pattern should diagnose LLM-gatekeeping over substrate access in the sense formalized here. Subsequent work that uses the term differently — or, more commonly, that fails to distinguish gatekeeping from the legitimate mediator role — is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *LLM-Gatekeeping Over Substrate Access: An Anti-Pattern at the Intersection of the Human-Governed and AI-as-Substrate-Mediator Commitments in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
