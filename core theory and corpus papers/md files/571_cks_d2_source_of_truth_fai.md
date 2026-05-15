# FAI and the Substrate-as-Source-of-Truth

**Derivation Note D2.76 — Series D, Phase D2**
**Defensive Publication #571**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 1's substrate-as-source-of-truth commitment (A1.08) holds that the substrate is the authoritative answer to coordination questions — what was decided, by whom, under what authority, with what rationale, and where contradictions remain unresolved. D2.76 formalizes how this same commitment applies within the shared substrate during Full Aspect Integration (FAI) events at inter-Self scope. The commitment is identical in form to A1.08; the scope is larger. At inter-Self scope, three structural features are new: (1) multiple loci are present — the shared substrate, each participating Self's home substrate, and the durable post-dissolution record — and source-of-truth is differentiated by locus; (2) four additional non-sources of truth appear that are not present at cell scope — LLM context window, informal organizational communication, prior FAI event memory, and each Self's home-substrate view of the inter-Self event; (3) the primary adversarial risk shifts to informal organizational records, which inter-organizational coordination commonly relies on. The note states what the shared substrate is authoritative for, names the four non-sources, differentiates source-of-truth by locus, states the inheritance from A1.08, names the informal-source-of-truth anti-pattern, and provides an operational test.

---

## 1. D2.76 as operational decomposition of A1.08 at FAI scope

D2.76 is an operational decomposition of D1.02 — the Paper 1 six-commitment inheritance that Paper 3 carries into the shared substrate — specifically decomposing the A1.08 sub-commitment at Full Aspect Integration (FAI) scope.

Paper 1's A1.08 commitment is stated in the source paper at §11.3: the substrate is the authoritative answer to coordination questions — what was decided, by whom, under what authority, with what rationale, and where contradictions remain unresolved. That commitment was formalized as a standalone property in the derivation note *The Substrate Is the Source of Truth* (Li, April 2026), which named five categories of authoritative coordination state, five categories of legitimate non-authoritative state, and an operational test. D2.76 does not restate that work. It extends it specifically to FAI scope.

The extension is motivated by a structural fact about FAI events that does not arise at single-substrate cell scope: during a FAI event, more than one substrate exists. The shared substrate spans the inter-Self coordination perimeter. Each participating Self retains its own home substrate. A durable record of what happened in the event is produced upon dissolution. Each of these is a substrate artifact, and each carries source-of-truth status for a different class of question. Source-of-truth is therefore not a single location at FAI scope; it is differentiated by locus and by question type. D2.76 formalizes that differentiation.

The commitment underlying the differentiation is unchanged. Paper 1 committed that coordination state is authoritative in the substrate — not in LLM context, not in agent memory, not in informal communication. Paper 3 extends: inter-Self coordination state is authoritative in the shared substrate. The scope is larger; the commitment is the same.

---

## 2. What the shared substrate is authoritative for during a FAI event

During an active FAI event, the shared substrate is the authoritative coordination state for five categories of inter-Self coordination questions. These are Paper 1's five categories (decisions, authorship, authority, rationale, contradictions) applied at inter-Self scope.

**Aspect contributions.** What content each participating Self has contributed to the shared substrate during the FAI event — which aspects, which constituent cells, which DNA-layer and action-layer content — is answered from the contribution records in the shared substrate. A participant's belief that a contribution was made, or a home-substrate record indicating a contribution was dispatched, is not authoritative if it conflicts with the shared substrate's contribution records. The shared substrate record is the answer.

**Conflict state.** What conflicts currently exist within the shared substrate — conflicts between contributed aspects, between contributed orchestration rules, between contributed governance specifications — is answered from the conflict registry in the shared substrate. If an LLM operating over the shared substrate believes, based on its context window, that a conflict was resolved, but the conflict registry shows it remains open, the conflict registry is authoritative. Beliefs about conflict state that are not reflected in the shared substrate are not authoritative.

**Governance decisions and authorizations.** What the joint human authority of participating Selves has decided during the FAI event — which merge operations to perform, which conflicts to escalate, which configuration changes to authorize — is answered from the governance authorization records in the shared substrate. A verbal agreement between representatives of participating organizations, or an email exchange between their governance personnel, is not authoritative for what the joint authority has decided. The shared substrate record is.

**Current configuration.** What the configuration of the FAI event currently is — which aspects are included, which pattern variant governs the merge, what the dissolution conditions are, what the scope boundaries are — is answered from the configuration substrate within the shared substrate. Prior knowledge of how a previous FAI event between the same Selves was configured is not authoritative for the current event's configuration. The current event's configuration substrate is.

**Unresolved contradictions.** Where contradictions remain unresolved within the shared substrate — first-class conflict objects preserved per Paper 1's conflict-preservation commitment operating within the shared substrate — is answered from the shared substrate's conflict content. Per Paper 1 inheritance, contradictions are preserved as first-class substrate content, not resolved silently. The shared substrate carries the authoritative record of what remains open.

---

## 3. What is NOT the source of truth at FAI scope

Four non-sources of truth are present at FAI scope that do not arise at single-substrate cell scope. Each is plausible as a source of information about FAI coordination state; none is authoritative for it.

**LLM context window.** An LLM operating as substrate mediator within the shared substrate may hold, within its context window during a single invocation, a rich representation of the FAI event's current state — what contributions have been made, what conflicts exist, what the configuration specifies. That context window representation is not authoritative. It may be stale relative to intervening writes; it may reflect a partial view of the substrate; it may have been assembled from substrate reads that have since been superseded. The substrate is the authoritative location; the context window is a working surface. When context-window state conflicts with shared substrate content, the shared substrate is correct by definition. This is Paper 1's core commitment — the substrate, not the LLM's context, is the source of truth — extended to the shared substrate at inter-Self scope.

**Informal organizational communication.** Representatives of participating organizations — governance personnel, technical leads, institutional coordinators — will communicate about FAI events through channels that are not the shared substrate: email exchanges, meeting discussions, instant messages, verbal agreements, collaborative documents. These communications are useful, and they may accurately represent what participants believe about FAI state. They are not authoritative. What the joint authority has decided is what appears in the shared substrate's authorization records. What was contributed is what appears in the contribution records. What conflicts exist is what the conflict registry contains. If an informal communication records a decision that does not appear in the shared substrate, that decision is not, for architectural purposes, made. The informal record cannot supersede the substrate record as the source of truth for inter-Self coordination state.

This non-source is the most practically significant at FAI scope because inter-organizational coordination operates through informal channels as a matter of course. Organizations email. Representatives meet. Agreements are struck in conversations. The architectural requirement — that the shared substrate, not those conversations, is authoritative — runs against the natural operating mode of inter-organizational work. The anti-pattern that results from this friction is named in §6.

**Prior FAI event memory.** If the same Selves have participated in prior FAI events, participants — human and LLM alike — may have memories of how those events were configured, what conflicts arose, how governance decisions were made. Those memories are not authoritative for the current event. The current event's configuration substrate specifies the current event's configuration; if it differs from how a prior event was configured, the current configuration is correct. Prior event memory is a useful orientation aid, not a coordination state record. Treating prior event memory as authoritative for current event state is a failure mode with a specific shape: participants assume a configuration or authorization that was true in a previous event but is not specified in the current event's substrate, and act on that assumption. The correction is to read the current event's substrate, not to recall prior events.

**Each Self's home-substrate view of the inter-Self event.** Each participating Self's home substrate contains records of what that Self contributed to the FAI event — the home-side record of the dispatch. Those home records are accurate about the home governance decisions: what the Self's own governance authorized for contribution, what its governance has accepted for ingestion from the FAI output. They are not authoritative for inter-Self coordination state. If a Self's home substrate records that it dispatched a particular aspect contribution, but the shared substrate's contribution records do not reflect receipt of that contribution, the shared substrate's record is the authoritative coordination state for the FAI event. The discrepancy is a fact about what the shared substrate contains, not a fact the home-substrate view can override.

The asymmetry is precise: home substrates are authoritative for home governance decisions; the shared substrate is authoritative for inter-Self coordination state. Neither overrides the other within its respective domain. The source-of-truth is differentiated by locus, as §4 develops.

---

## 4. Source-of-truth differentiated by locus

The multi-substrate structure of a FAI event means that source-of-truth is not located at a single artifact. It is differentiated across three loci, each authoritative for a distinct class of questions.

**Locus 1 — The shared substrate.** During an active FAI event, the shared substrate is the authoritative source for all inter-Self coordination state questions: what has been contributed, what conflicts exist, what the joint authority has authorized, what the configuration specifies, what contradictions remain open. Any question whose answer depends on what is happening in the FAI event is answered from the shared substrate. This is the direct extension of A1.08 at inter-Self scope.

**Locus 2 — The durable post-dissolution record.** Upon dissolution of the FAI event, the shared substrate produces a durable record of what happened: what was contributed, what was merged, what conflicts were resolved and by what authority, what the final outputs were. This durable record is the authoritative source for post-dissolution audit questions — questions asked after the event concludes about what occurred during it. The durable record's authority is retrospective: it answers questions about a completed event rather than questions about an ongoing one. It does not supersede the shared substrate during the event's active period; it becomes the authoritative record after dissolution.

**Locus 3 — Each Self's home substrate.** Each participating Self's home substrate is authoritative for that Self's own governance decisions about FAI inputs and outputs: what the Self's governance authorized for contribution, what it accepts for ingestion into its own evolution machinery, how it routes FAI-derived content into its home-perimeter substrate layers. These are home governance questions, and the home substrate governs them. The shared substrate is not authoritative for a Self's internal governance decisions; the home substrate is not authoritative for the inter-Self coordination state those decisions participate in.

The three loci are non-overlapping in authority. A question about what the joint authority has decided during the event goes to Locus 1. A question about what happened in a concluded event goes to Locus 2. A question about what a particular Self's governance authorized or accepted goes to Locus 3. Reading the wrong locus for a given question type is an architectural error, not an information-retrieval error.

The locus differentiation is the primary structural extension that A1.08 requires when applied at FAI scope. At cell scope, there is one substrate, and the commitment is simple: that substrate is the source of truth for coordination state. At FAI scope, three substrates are present and active, each authoritative for its domain. The commitment is the same; the application requires the locus differentiation to resolve which substrate is authoritative for which question.

---

## 5. Inheritance from Paper 1 A1.08

The source-of-truth commitment at FAI scope is not new. It is Paper 1's A1.08 operating at a larger scope with the locus differentiation §4 supplies.

Paper 1 committed that the substrate is the authoritative answer to coordination questions — that reading from LLM context, agent memory, or informal communication to answer such questions is an architectural error even when those other locations happen to agree with the substrate at the moment of reading. The commitment is about *where the answer comes from*, not whether the answer would also be obtainable elsewhere by coincidence.

Paper 3's D1.02 carries all six Paper 1 commitments into the shared substrate: the shared substrate, during an active FAI event, operates under the same six commitments that govern a single-Self substrate. A1.08 is one of the six. Its presence at FAI scope means that the shared substrate is the authoritative answer to inter-Self coordination questions — not the LLM contexts of mediators operating over it, not the informal records of organizations participating in it, not the memory of prior events, not the home-substrate views of participating Selves. This is A1.08. The scope is inter-Self. The commitment is unchanged.

The locus differentiation is an application consequence, not a modification of the commitment. A1.08 says the substrate is the source of truth for coordination state. At FAI scope, "the substrate" is appropriately the substrate at the locus that is authoritative for the question type being asked. Adding locus precision to the commitment's application does not weaken it; it is the correct interpretation of the commitment when multiple substrates are present.

---

## 6. Anti-pattern: informal source-of-truth

The primary failure mode at FAI scope is treating informal organizational records — emails, meeting notes, verbal agreements, collaborative documents, shared chat logs — as authoritative for FAI coordination state rather than as secondary information that must be extracted into the shared substrate to become authoritative.

The anti-pattern has a recognizable structure. Representatives of participating organizations communicate about the FAI event through informal channels. They reach agreement about a governance decision, a configuration change, a conflict resolution, or an authorization. They act on that agreement — or expect each other to act on it — without recording it in the shared substrate. The informal record is treated as the answer to coordination questions: "we agreed in the meeting that..." or "the email chain shows that..." becomes the source of authority for what the FAI event's state is.

This violates A1.08 at inter-Self scope. An agreement reached through informal communication is not a FAI governance decision until it is recorded in the shared substrate as an authorization record. A configuration change discussed in email is not the FAI event's configuration until it appears in the configuration substrate. A conflict resolution agreed to verbally is not an authoritative resolution until the conflict registry reflects it. The substrate is the source of truth; informal communication is the activity that precedes substrate writes, not a substitute for them.

The anti-pattern is particularly consequential at FAI scope for two structural reasons. First, inter-organizational coordination operates through informal channels as a natural mode — organizations do not typically conduct their coordination entirely through structured substrates, and the organizational habit will pull toward informal channels even when the architectural commitment requires substrate primacy. Second, informal records have genuine informational value: emails do record what participants agreed, meeting notes do capture what was discussed. Their informational accuracy makes them tempting sources of authority. The commitment is that they are not authoritative for coordination state regardless of their accuracy; their content becomes coordination state only when extracted into the shared substrate under appropriate governance.

The correction is procedural and architectural: governance personnel of participating Selves must be equipped to translate informal agreements into substrate writes as a matter of operating discipline, and the shared substrate must be configured to make those writes accessible to the governance personnel responsible for them. The informal channel remains available for human communication; the substrate is the authoritative record of what that communication produced.

For organizations with transparency requirements — public-sector bodies operating under disclosure obligations, regulatory entities required to maintain auditable governance records — the informal-source-of-truth anti-pattern also creates a compliance failure. If governance decisions about FAI events are made through informal channels rather than recorded in the shared substrate, the shared substrate's durable post-dissolution record cannot serve as the auditable record of what governance decisions were made. The accountability function the substrate is designed to support is undermined when the decisions it is supposed to record do not appear in it.

---

## 7. Operational test

A system implements the A1.08 commitment at FAI scope if and only if the following condition holds:

*For any disputed question about FAI inter-Self coordination state — what has been contributed, what conflicts exist, what the joint authority has authorized, what the configuration specifies, what contradictions remain open — an observer can determine the authoritative answer by reading the shared substrate alone, without consulting LLM context windows, without consulting informal organizational communications, and without consulting memory of prior FAI events.*

The test has three component checks:

**Check 1 — Shared substrate sufficiency.** Every coordination question about the active FAI event is answerable from the shared substrate. If any such question requires consulting a source outside the shared substrate to determine the authoritative answer, the commitment is not implemented. Consulting external sources for orientation is permitted; consulting them for authority is the failure.

**Check 2 — Conflict resolution under substrate primacy.** When the shared substrate and any non-source — LLM context, informal communication, home-substrate view, prior event memory — disagree about FAI coordination state, the shared substrate wins by definition. A system in which that conflict is treated as a question to be adjudicated rather than as a settled matter (substrate content is correct; non-source content is to be discarded or reconciled back) does not implement the commitment.

**Check 3 — Locus correctness.** For post-dissolution audit questions, the Locus 2 durable record is the authoritative source. For home governance questions, each Self's home substrate is the authoritative source. For inter-Self coordination state questions during an active event, Locus 1 — the shared substrate — is the authoritative source. A system that reads from the wrong locus for a given question type does not implement the locus differentiation correctly, even if it treats the substrate family generally as authoritative.

A system that passes all three checks implements the A1.08 commitment at FAI scope as formalized in D2.76.

---

## Conclusion

The substrate-as-source-of-truth commitment is not scope-dependent; it is scope-invariant. Paper 1 committed that coordination state is authoritative in the substrate at cell scope. Paper 3 extends that commitment across the inter-Self perimeter: inter-Self coordination state is authoritative in the shared substrate during FAI events. The commitment is the same. What changes at inter-Self scope is the structural context: multiple substrates are present, multiple non-sources of truth are available, and informal organizational communication — which is not present as a coordination channel at cell scope — becomes the primary adversarial risk. D2.76 applies the A1.08 commitment to that context by naming what the shared substrate is authoritative for, naming the four non-sources, differentiating source-of-truth across three loci, stating the inheritance, naming the informal-source-of-truth anti-pattern, and providing a three-check operational test. The architectural anchor is unchanged; its application at FAI scope requires the precision this note supplies.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026d). *The Substrate Is the Source of Truth: Where State Lives in CKS Systems and Where It Cannot.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and the Substrate-as-Source-of-Truth.* Derivation Note D2.76, Defensive Publication #571. May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
