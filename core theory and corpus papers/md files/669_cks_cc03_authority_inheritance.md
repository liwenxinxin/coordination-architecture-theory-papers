# P3↔P1 Human-Governed Authority Inheritance: Joint Authorization Is the Inter-Self Scope Adaptation of Governance Authority

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026).

---

## Abstract

Paper 1 of the CKS trilogy established human-governed authority as one of its six architectural commitments: governance holds the rights to inspect, modify, and override substrate content and orchestration rules at any time, with no justification required for override, and no automated system capable of holding these rights. Paper 3 extends this commitment to inter-Self scope through four architectural constructs: joint authority over the shared substrate, the three rights applied across governance perimeters, the non-delegation principle, and the exit right. This note formalizes the inheritance edge between Paper 1 Claim 3 and these Paper 3 constructs. The central result: joint authorization is not a new concept introduced by Paper 3 but the inter-Self scope adaptation of the same principle Paper 1 established — that humans, not automated systems, hold governance authority. The principle is identical; its expression in a multi-authority context requires coordination between governance perimeters that single-authority scope does not.

---

## 1. Source commitment: Paper 1 Claim 3

Paper 1's human-governed commitment names three rights that governance holds over the substrate at all times during the substrate's existence:

- **The inspect right**: governance can read any substrate content and any orchestration rule.
- **The modify right**: governance can write to, edit, or delete any substrate content or orchestration rule.
- **The override right**: governance can remove or replace any substrate content or the output of any operation touching the substrate; no justification is required.

These rights are architectural, not procedural. They must be available as a property of the system's design — not as a workflow feature that a vendor, runtime layer, or automated process could in principle block. They are also unconditional: urgency does not suspend them, scale does not dilute them, and automation does not absorb them.

The commitment carries a critical corollary: authority over the substrate is not allocable to automated systems. Labor is allocable — humans, LLMs under human direction, and stable cells under orchestration rules can all perform the work of writing, curating, and maintaining substrate content. But authority over the result is not a labor commitment. An LLM that writes substrate content under an orchestration rule does so under human authority; that authority does not transfer. The human retains the inspect, modify, and override rights regardless of what produced the content being governed.

At intra-Self scope — the scope Paper 1 addresses — a single governance authority holds all three rights over a single Self's substrate. There is one perimeter, one authority, and the three rights are unilateral.

---

## 2. Extension identification: Paper 3 constructs that extend Claim 3

Paper 3 introduces four constructs that extend Paper 1 Claim 3 to inter-Self scope.

**Joint authority (Paper 3 §4 / D1.25).** When two or more Selves coordinate through a shared substrate, governance authority over the shared substrate is held jointly by the governance structures of all participating Selves. No single Self's governance holds unilateral authority over the shared substrate; all participating governance authorities hold the three rights together over shared content.

**Three rights at inter-Self scope (Paper 3 §4 / D2.04).** The inspect, modify, and override rights apply to the shared substrate's content exactly as they apply to a single Self's substrate: governance can read shared content, amend it through joint authorization, and exit the coordination relationship without justification. The rights travel with the substrate object; expanding the substrate to inter-Self scope does not dilute or suspend them.

**Non-delegation principle (Paper 3 §4 / D2.43).** Governance authority over the shared substrate cannot be delegated to automated systems or non-governance actors regardless of event scale, operational frequency, or technical complexity. Pre-authorized labor may proceed under orchestration rules that governance authored; governance authority cannot be transferred to the systems executing that labor.

**Exit right (Paper 3 §4 / D2.46).** Each participating Self's governance retains the right to terminate the inter-Self coordination relationship entirely without justification. Home governance sovereignty cannot be overridden by the coordination event; no configuration, prior agreement, or automated escalation mechanism can in principle prevent a governance authority from exiting the relationship.

---

## 3. What is preserved and what is adapted

**What is preserved.** Structural human governance authority holds identically at intra-Self and inter-Self scope. The three rights are unconditional. No justification is required for override or exit. Automated systems cannot hold governance authority. These properties do not weaken, dilute, or bifurcate as the scope moves from one Self to many. The principle is the same: humans hold authority over the substrate.

**What is adapted.** At intra-Self scope, one governance authority holds the three rights unilaterally over one Self's substrate. At inter-Self scope, multiple governance authorities jointly hold the three rights over a shared substrate. This introduces a coordination requirement that single-authority scope does not have: the modify right at inter-Self scope requires joint authorization from all participating governance authorities, whereas at intra-Self scope a single authority can modify unilaterally. The structure of authority (joint vs. unilateral) is adapted; the authority-not-labor principle is not.

The adaptation follows mechanically from applying the same principle to a different governance topology. When there is one governance authority, authority is held by one. When there are multiple governance authorities each holding full authority within their own perimeter, authority over their shared object is held by all of them. Paper 3 does not introduce joint authority as a fresh concept; it names what Paper 1's principle produces when extended to a multi-authority context.

---

## 4. Three inheritance relations formalized

**Joint authorization as the inter-Self scope expression of unilateral authority.** Paper 1 establishes that one governance authority holds the three rights over one substrate. Paper 3's joint authority at inter-Self scope is the same statement applied to a coordination context where multiple distinct governance perimeters participate. The number of governance authorities changes; the principle (humans hold authority, authority is not delegated to automated systems) does not. A downstream system that treats joint authorization as a new architectural concept independent of Paper 1 Claim 3 misidentifies the inheritance relationship.

**Exit right as the inter-Self scope expression of the override right.** Paper 1's override right allows governance to remove any substrate content without justification. At intra-Self scope, the override right operates on content within a single governance perimeter: governance can remove it, modify it, or restructure it unconditionally. At inter-Self scope, the corresponding unconditional right is the exit right: governance can terminate the coordination relationship entirely without justification. The structural logic is identical — governance authority cannot be trapped by the system's state, by prior operational commitments, or by the volume of work underway. The scope object changes from content removal to relationship termination, because at inter-Self scope the relevant exercise of unconditional authority is over the relationship, not only over individual pieces of shared content. Both the override right and the exit right express the same architectural property: governance authority is never contingent on system approval.

**Non-delegation as the inter-Self scope expression of the authority-not-labor principle.** Paper 1 Claim 3's authority-not-labor distinction establishes that no automated system can hold governance authority, regardless of what that system produced or how frequently it acts on the substrate. The operational expression of this at intra-Self scope is that the human-governed commitment holds regardless of which labor mode produced any given piece of substrate content — direct human authoring, LLM execution under rules, or stable cell automation. At inter-Self scope, Paper 3's non-delegation principle extends this: governance authority over the shared substrate cannot be delegated to automated systems or non-governance actors at any scale. The operational pattern at inter-Self scope may involve pre-authorized labor executing at scale between governance interventions; the pre-authorization is itself a governance act (rule authoring under Paper 1's Moment 1), and the authority that makes the pre-authorization valid is human governance authority, not the authority of the executing system. Non-delegation is not a fresh commitment; it is Paper 1 Claim 3's authority-not-labor principle named at the inter-Self scope boundary.

---

## 5. Operational test for the inheritance

The inheritance holds — that is, a Paper 3 deployment correctly instantiates the P3↔P1 authority inheritance — if and only if all of the following are true at all times during the shared substrate's existence:

1. Each participating governance authority can read any shared substrate content without scheduling, workflow approval, or intermediation by automated systems.
2. Amendments to shared substrate content require joint authorization from all participating governance authorities; no single participating authority can modify shared content unilaterally against the others' held authority, and no automated system can modify shared content outside the authority structure.
3. Each participating governance authority retains the right to exit the coordination relationship entirely without justification to the shared substrate's orchestration layer or to any other participating authority within the architecture (exit may be logged, audited, or trigger contractual consequences; it is not architecturally gated).
4. No automated system, orchestration layer, or configuration decision made during the coordination relationship can in principle prevent any participating governance authority from exercising (1), (2), or (3).
5. Governance authority over the shared substrate is held by the participating governance authorities jointly; no portion of that authority has been transferred to automated systems, even under high-frequency or high-volume coordination.

A shared substrate deployment that fails any of (1)–(5) may be a useful inter-Self coordination system, but it does not correctly instantiate the P3↔P1 authority inheritance and does not carry the architectural property Paper 1 Claim 3 establishes at intra-Self scope.

---

## 6. What the inheritance does not change

The inheritance formalizes extension; it does not introduce new constraints on Paper 1 deployments. Paper 1 intra-Self deployments are not required to implement joint authorization, exit rights, or non-delegation as named at Paper 3 scope; those constructs arise specifically from the inter-Self coordination context. Downstream work building solely at intra-Self scope should use Paper 1 Claim 3 directly; downstream work building at inter-Self scope should trace joint authorization, exit rights, and non-delegation back to Paper 1 Claim 3 as their source, through the inheritance formalizations in §4.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *P3↔P1 Human-Governed Authority Inheritance: Joint Authorization Is the Inter-Self Scope Adaptation of Governance Authority.* May 15, 2026. ORCID: 0009-0004-8065-3235.
