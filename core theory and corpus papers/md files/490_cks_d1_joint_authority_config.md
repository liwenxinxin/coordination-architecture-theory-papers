# Joint Authority Over the FAI Configuration Substrate

**Derivation Note D1.25 — Series D, Phase D1 (#490)**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D1.25 formalizes the fourth sub-commitment of Paper 3 Claim 5: authority over the FAI configuration substrate is held *jointly* by all participating Selves' governance structures. The three rights established in Paper 1 — inspect, modify, override — apply to the FAI configuration substrate in joint form. No single Self holds unilateral configuration authority; no external party holds it. The specification of how joint authority is exercised is itself authored substrate content within the configuration substrate — the governance-configurable approval mechanics are a named example of this recursive property. Joint authority operates within the inter-Self perimeter only; it does not extend into any participating Self's home governance scope. This note states the commitment precisely, develops the approval-mechanics implication, states the perimeter boundary, traces inheritance from Papers 1 and 2, identifies four failure modes the commitment defends against, and provides an operational test. It closes the Claim 5 sub-commitment set (D1.22–D1.25) with a summary and notes that D1.26 opens the Claim 6 sub-commitments.

---

## 1. Statement of D1.25

Paper 3 Claim 5 commits to the FAI configuration substrate — the collection of substrate content specifying the six configurable FAI dimensions (D1.22) and their governance framework (D1.23) — as substrate content under joint authority. D1.25 formalizes what that joint authority means architecturally.

The commitment has three parts. First, authority over the FAI configuration substrate is held jointly by all participating Selves' governance structures. Neither any single participating Self nor any external party holds unilateral authority over what the FAI configuration specifies. Second, the three rights from Paper 1 Claim 3 — inspect, modify, override — apply to the configuration substrate in joint form, with the exercise of those rights governed by approval mechanics that are themselves substrate content. Third, this joint authority operates within the inter-Self perimeter: it governs the shared configuration substrate and nothing beyond it. Each participating Self's home governance retains exclusive authority within its own home perimeter.

---

## 2. The Three Rights Held Jointly

Paper 1 Claim 3 establishes that human governance over a substrate means holding three rights: the right to inspect any substrate content, the right to modify any substrate content, and the right to override any operation touching substrate content. These rights are structural — available as an architectural property of the system's design, not as a procedural promise dependent on workflow or deployment.

D1.25 applies these three rights to the FAI configuration substrate in joint form across all participating Selves' governance structures.

**The inspect right held jointly.** Any participating Self's governance structure may inspect the FAI configuration substrate. Configuration content — the specification of FAI dimensions, the approval process, the approval records — is visible to all governance structures that hold joint authority. Opacity over configuration content to any participating governance structure is an architectural violation, not a policy option.

**The modify right held jointly.** Modification of the FAI configuration substrate requires the approval of the governance structures holding joint authority, in accordance with whatever approval mechanics are themselves authored as substrate content within the configuration substrate. The modify right is not extinguished by joint holding; it is exercised under governance-configured approval. What governance configures is the shape of the approval process, not whether approval is required.

**The override right held jointly.** Emergency or corrective override of FAI configuration content requires joint governance action, or an emergency protocol that is itself authored as substrate content within the configuration substrate. A single Self's governance structure cannot unilaterally override a jointly authorized configuration — but all participating governance structures acting jointly may. The right is real and exercisable; its exercise is what the approval mechanics govern.

The joint holding of these three rights is not a weakening of the authority commitment from Paper 1. It is the inter-Self scope instantiation of the same structural authority: the same three rights, applied to a substrate object that spans multiple organizational governance perimeters.

---

## 3. Approval Mechanics as Governance-Configurable Substrate Content

The most operationally significant implication of D1.25 is that the specification of how joint authority is exercised is itself authored substrate content within the configuration substrate. This is the recursive property from D1.23 applied to the authority dimension: just as configuration-of-configuration is substrate content (D1.23), the configuration of joint-authority approval mechanics is substrate content.

The architecture prescribes that whatever approval mechanism governs the FAI configuration must be authored as substrate content within the configuration substrate, jointly authorized. The architecture does not prescribe which approval structure governs any particular deployment. That is a governance decision, authored by the participating Selves' governance structures, recorded as substrate content.

Four approval structures illustrate the space of what governance may configure:

**Consensus.** All participating Selves' governance structures must approve the FAI configuration before construction proceeds. No Self's governance structure may be bypassed. The configuration becomes authoritative only when all approvals are recorded. This structure maximizes governance participation at the cost of coordination overhead.

**Majority.** A governance-specified threshold of participating Selves' governance structures must approve the configuration. The majority threshold itself is authored substrate content. This structure balances breadth of governance participation with coordination efficiency, with the balance point set by the governance structures themselves.

**Initiating-Self with acceptance.** The initiating Self proposes the FAI configuration; other participating Selves' governance structures review and either accept participation or decline. The proposed configuration takes effect as between the accepting parties. Governance structures that decline do not participate in the FAI event. This structure permits coordination to proceed without requiring all-party sign-off, while preserving each governance structure's right to withhold participation from a configuration it does not accept.

**Delegated authority.** One participating Self's governance structure holds authority delegated from the others for configuration decisions of specified types. The delegation scope, duration, and revocation conditions are themselves authored substrate content. This structure allows governance efficiency where participating Selves have established durable trust relationships, without permanently surrendering any governance structure's underlying authority.

These four structures are examples, not an exhaustive classification. The architectural commitment is that *whatever* approval structure governs an FAI configuration is authored governance content — inspectable, modifiable, overridable under the joint authority it specifies. A deployment in which the approval mechanism is not substrate content, or in which it is determined by platform convention rather than by the participating governance structures, does not satisfy D1.25.

The approval mechanics apply at the moment the FAI configuration takes effect — before the FAI event is constructed. Governance over the configuration substrate is prospective, not only retrospective: the configuration must be approved before the event begins, with the approval records available as substrate content for subsequent inspection.

---

## 4. Joint Authority Ends at the Home Perimeter

The inter-Self perimeter (D1.03) is the governance boundary of the shared substrate. Joint authority over the FAI configuration substrate operates within that perimeter. It does not cross into any participating Self's home perimeter.

This boundary is the architectural sovereignty protection for each participating Self. Whatever the joint governance structures agree to configure for the FAI event, that agreement governs the shared substrate scope only. No participating Self's home governance is bound by the FAI configuration to alter its home substrate content, home governance rules, or home authority structures. After the hand-off boundary at FAI dissolution (D1.20), each Self's home governance is the sole authority over how the FAI evolution outputs are — or are not — absorbed into the home substrate.

The implication is that participating in FAI does not require any Self to surrender home governance authority. Each Self enters the shared coordination scope under the jointly authorized FAI configuration and exits it with its home governance intact. Joint authority governs the shared object; home authority governs the home object. Neither encroaches on the other.

This also means that joint authority cannot be used as a mechanism to impose substrate configurations on a participating Self's home governance. A configuration provision that purports to govern what a participating Self must do within its home substrate — with its home content, its home orchestration rules, or its home governance — is outside the scope of joint authority. The architecture does not support such provisions, and including them in a configuration substrate does not make them binding.

---

## 5. Inheritance from Papers 1 and 2

D1.25 inherits from two prior commitments and extends them to inter-Self scope.

**From Paper 1 Claim 3 (human-governed authority).** Paper 1 establishes that the three rights — inspect, modify, override — apply to all substrate content and orchestration rules. The authority commitment is structural and unconditional: a system in which any party can in principle prevent a human from exercising these rights over substrate content is not human-governed in the CKS sense. D1.25 is the inter-Self scope instantiation of this commitment. The three rights apply to the FAI configuration substrate in joint form; the joint form does not weaken them.

**From Paper 2 Claim 5 (multi-shaped governance as substrate content).** Paper 2 establishes that governance parameters — the shapes of authority across cell, aspect, and Self scopes — are themselves substrate content. Different entities within a Self may have different governance configurations; those configurations are authored as substrate content and are subject to the same three rights as other substrate content. D1.25 extends this to the inter-Self scope: joint governance parameters for the shared configuration substrate are themselves authored substrate content within that substrate, subject to the joint-authority version of the three rights.

The trilogy ambiguity map entries T1.09 (Authority Distribution) and T1.15 (Governance Authority Distribution) establish the unifying claim: authority in the trilogy is always human-held structural authority over the relevant substrate scope. The scope expands across papers — cell scope (Paper 1), Self scope (Paper 2), inter-Self scope (Paper 3) — without weakening the three rights or the authority-not-labor principle. D1.25 is the articulation of this expansion at the inter-Self scope for the configuration substrate specifically.

---

## 6. Failure Modes Defended Against

D1.25 defends against four failure modes in inter-Self coordination architectures.

**Unilateral configuration authority.** One participating Self's governance structure determines all FAI configurations without joint approval from the other participating Selves' governance structures. This failure mode violates the joint holding of the modify right. The initiating-Self-with-acceptance approval structure mitigates this by requiring that other governance structures affirmatively accept the proposed configuration; the consensus and majority structures exclude it architecturally. In any case, the approval mechanics must be authored substrate content that the other governance structures can inspect — unilateral configuration authority is not a governance-configured option within D1.25's scope.

**Non-substrate approval mechanics.** The process by which joint authority over the FAI configuration is exercised is determined by platform convention, contract terms, or informal agreement rather than being authored substrate content within the configuration substrate. This failure mode violates the recursive property of D1.25: the specification of how joint authority is exercised must itself be substrate content, inspectable and governable. Approval mechanics that live outside the substrate are not jointly authorized governance content; they are ungoverned procedural facts.

**External configuration authority.** A third-party platform, vendor, or infrastructure layer determines FAI configurations rather than the participating Selves' governance structures. The configuration substrate's content is authored by an entity outside the joint governance structure. This failure mode violates the joint-authority commitment entirely: neither the inspect right, the modify right, nor the override right over configuration content is held by the participating governance structures if the content is authored by an external party. Tool-agnosticism (a Paper 1 commitment inherited at inter-Self scope) permits any infrastructure to implement the shared substrate; it does not permit any infrastructure to determine the substrate's content.

**Joint authority over home substrates.** Joint authority is claimed to extend into participating Selves' home governance scopes — imposing configuration requirements on home substrates, altering home governance rules, or conditioning FAI participation on home substrate changes. This failure mode violates the inter-Self perimeter boundary. Joint authority governs the shared configuration substrate only; it ends at the home perimeter. Any architecture in which FAI participation requires a Self to surrender home governance authority misrepresents the scope of D1.25's commitment.

---

## 7. Operational Test

For a given FAI event, the following operational test determines whether D1.25 is instantiated:

**Test 1 — Joint-authority configuration as substrate content.** An observer with access to the FAI configuration substrate can locate authored substrate content specifying: (a) which governance structures hold joint authority over the FAI configuration for this event; (b) the approval mechanism that governed how the configuration took effect; and (c) the approval records showing that the configuration was approved in accordance with that mechanism before the FAI event was constructed. If any of these three elements is absent, undocumented, or located outside the substrate, D1.25 is not instantiated.

**Test 2 — No unilateral determination.** The approval records confirm that no single participating Self's governance structure unilaterally determined the complete FAI configuration. Either all governance structures approved (consensus), or a governance-specified threshold approved (majority), or other governance structures affirmatively accepted the initiating Self's proposal (initiating-Self with acceptance), or the approval records show the scope and conditions of any delegated authority that governed the event. A configuration record showing only one governance structure's authorization, with no mechanism by which other structures approved or accepted, fails this test.

**Test 3 — Approval mechanics as substrate content.** The approval mechanism that governed this event is itself authored substrate content within the configuration substrate — not a platform convention, not an informal agreement, not an implied default. The mechanism is inspectable, and its governance status (who authored it, under what authority) is traceable.

**Test 4 — Home perimeter integrity.** Nothing in the FAI configuration substrate purports to govern the content of any participating Self's home substrate, or requires any participating Self to alter its home governance rules as a condition of participation. The configuration substrate specifies only the shared coordination scope.

A system passes all four tests if and only if it instantiates D1.25.

---

## 8. Closing the Claim 5 Sub-Commitment Set

D1.22 through D1.25 together cover the four sub-commitments of Paper 3 Claim 5.

**D1.22 — Six configurable dimensions as substrate content.** The six FAI dimensions (aspect contribution scope, merge default and pattern variants, conflict-handling tier configuration, evolution-feed locus parameters, mediator coordination pattern, and recursive configuration depth) are themselves substrate content within the FAI configuration substrate, authored under joint authority and subject to the three rights.

**D1.23 — Configuration-of-configuration as substrate content.** The governance framework that governs the FAI configuration dimensions is itself substrate content — configuration of configuration is also substrate content, with the recursion bottoming at human-authored governance authority per Paper 1. There is no meta-governance layer outside the substrate; governance all the way down is the architectural property.

**D1.24 — Recursive applicability across claims.** The configuration-as-substrate-content commitment applies at the configuration level across Claims 1 through 4: the shared substrate construction policy (Claim 1), the FAI mechanism parameters (Claim 2), the conflict-handling tier configuration (Claim 3), and the evolution-feed locus parameters (Claim 4) are all governed as substrate content with recursive applicability. Claim 5 is the systematic articulation of this recursion across the prior claims.

**D1.25 (this note) — Joint authority over the FAI configuration substrate.** Authority over the configuration substrate is held jointly by all participating Selves' governance structures. The three rights apply in joint form. Approval mechanics are governance-configurable substrate content. Joint authority is bounded by the inter-Self perimeter.

The four sub-commitments together constitute the architectural content of Paper 3 Claim 5: what is configured (D1.22), how configuration of configuration works (D1.23), where the recursive commitment applies (D1.24), and who holds authority over the configuration substrate and on what terms (D1.25).

D1.26 opens the Claim 6 sub-commitment set. Claim 6 extends the architecture to population-scale collective evolution: the dynamics that arise when many governance-structured Selves accumulate FAI events under cross-population governance, with joint authority extending at population scope to population-level governance perimeters and the recursion bottoming at population-level human governance per Paper 1's authority commitment. D1.26 begins the five Claim 6 sub-commitments covering population-scale architecture, cross-event evolution dynamics under joint authority, and the architectural-commitment differentiation against capability-motivated population-scale coordination.

---

*End of D1.25 — Joint Authority Over the FAI Configuration Substrate.*
