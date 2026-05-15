# Cooperation and Competition as FAI Variant Configurations

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Derivation note D2.20 formalizes the operational distinction between the cooperation variant and the competition variant of Full Aspect Integration (FAI) events. Both variants operate over the same shared-substrate architecture: same exchange primitives, same three-tier conflict-handling mechanism, same three rights and joint authority, same evolution feed loci, same exchange bounding. The variant is located entirely in the orchestration rules governing how the shared substrate operates during an event — specifically in how conflicts are handled, what the coordination goal is, and how governance configures the evolution feed. The cooperation variant configures orchestration rules for joint task completion, biasing toward the resolve tier and mutual capability combination. The competition variant configures orchestration rules for comparative evaluation, biasing toward the preserve tier and targeted capability absorption. This note states the prior-art claim that follows: any system implementing cooperative AI coordination and any system implementing competitive AI evaluation are both implementations of the same shared-substrate architecture under different governance configurations. Neither variant constitutes novel architecture beyond what D1.01–D1.22 collectively establish.

---

## 1. Derivation position

D2.20 is the operational decomposition of D1.22 Dimension 4 (cooperation/competition variant as a governance-configured FAI parameter). D1.22 established that six dimensions of a FAI event are configurable under governance as substrate content: sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth, and multi-mediator coordination. For Dimension 4 specifically, D1.22 committed that the cooperation/competition distinction is a governance-configured parameter — the same shared-substrate primitive operates under different orchestration rule sets depending on which variant governance selects.

D2.20 formalizes what that commitment means operationally. The derivation question is: what does "different orchestration rule sets" mean in practice? The answer has three parts: what the cooperation variant's orchestration rules are oriented toward, what the competition variant's orchestration rules are oriented toward, and what remains identical across both. The prior-art significance depends on stating all three with precision.

---

## 2. The cooperation variant

In the cooperation variant, participating Selves use FAI to jointly produce an outcome that neither could produce alone. The coordination goal is explicit and joint: the event has a target output, and the orchestration rules are configured to serve that target.

**Conflict handling in the cooperation variant.** The resolve tier is more heavily used. When aspects contributed by different Selves surface conflicts in the shared substrate, the cooperation variant's orchestration rules are configured to resolve those conflicts into coherent joint outputs wherever possible. Resolution is substrate-level: the orchestration rules for resolution are themselves authored substrate content under joint authority across participating Selves' governance, inspectable and modifiable at any time. The preserve tier remains available and will be used when conflicts cannot be resolved without human judgment or when governance explicitly flags a conflict as requiring preservation despite the cooperation context. The escalation tier applies as in any FAI event — conflicts that require human decision cross the joint authority boundary. But the overall orientation of the conflict-handling configuration is toward producing a coherent result from the contributed aspects rather than maximizing the record of differences.

**Merge patterns in the cooperation variant.** Full-merge and selective-merge patterns are both common. Full-merge combines all contributed aspects into the shared substrate, producing the most comprehensive joint view; selective-merge contributes aspects relevant to a defined coordination scope. The default in both cases is that the merge is oriented toward producing something usable from the combined contributions, which reflects the cooperation variant's joint-output goal.

**Evolution feed in the cooperation variant.** Both action-feedback ingestion and DNA absorption may be authorized by governance. Because the cooperation variant is aimed at capability combination — participating Selves contributing complementary approaches to a shared task — governance is often willing to authorize broader DNA absorption. A Self that contributed a strong orchestration pattern for a domain it knows well may authorize the other participating Selves to absorb that pattern through DNA evolution at home. The cooperation variant's evolution feed reflects the premise that both Selves benefit from the other's capabilities when the task is shared.

**The coordination goal.** The cooperation variant event is configured with an explicit joint coordination goal: what is this event trying to produce? That goal is itself substrate content under joint authority. Governance authors it before the event begins; it governs how orchestration rules handle conflicts, how merge patterns are selected, and how the event's dissolution is timed.

---

## 3. The competition variant

In the competition variant, participating Selves use FAI to compare governance approaches — each contributing its best architecture for a domain, with the event revealing where approaches agree and where they diverge. The coordination goal is comparative evaluation, not joint production.

**Conflict handling in the competition variant.** The preserve tier is more heavily used. This is the central operational distinction. In the competition variant, conflicts within the shared substrate are the primary output. Where two Selves' contributed aspects surface a conflict, the conflict annotation records that the approaches differ and how they differ. Resolving the conflict would erase the difference — and erasing differences defeats the purpose of a competition event. The orchestration rules in the competition variant are therefore configured to preserve conflicts as first-class substrate state rather than to resolve them. Full-merge with heavy conflict registration is the common pattern: both aspects are present in the shared substrate, and every conflict between them is registered with its provenance, its character, and the two positions it records.

**What competition conflict density means.** A well-run competition variant event accumulates substantial conflict density. This is expected and informative. The conflict map produced by the event is the mechanism by which each participating Self learns where its governance approach agrees with others' and where it genuinely diverges. Conflicts at high density mean the event successfully captured real differences. A competition event that produced few conflicts would indicate either that the participating Selves' approaches are closely aligned (a substantive finding) or that the orchestration rules were misconfigured to resolve differences that should have been preserved (a governance failure in the opposite direction from what is commonly assumed).

**Merge patterns in the competition variant.** Full-merge with comprehensive conflict registration is the standard pattern. Selective-merge may be used when governance scopes the comparison to specific domains or aspects. In both cases, the merge operation's purpose is to produce a comprehensive record of where the approaches intersect and where they diverge — the conflict registry is the deliverable, not a residual byproduct.

**Evolution feed in the competition variant.** Action-feedback ingestion and DNA absorption are both available, as they are in the cooperation variant. The difference is governance selectivity. In the competition variant, the goal is comparative learning: a Self exits the event with a better understanding of how its governance compares to others'. DNA absorption is more selective as a result — governance absorbs aspects of a competitor's approach only where it judges those aspects genuinely superior to its own, not as a general combination exercise. The governance judgment about what to absorb is informed by the conflict map the event produced. A conflict where the other Self's approach is clearly more effective in the recorded execution evidence is a candidate for selective absorption; a conflict where the two approaches reflect different legitimate priorities is a place to maintain the divergence.

**The coordination goal.** The competition variant event is configured with a comparative coordination goal: what domain is being compared, which aspects are in scope, and what governance will do with the conflict registry at dissolution. The goal is also authored substrate content under joint authority, as in the cooperation variant. The difference is that the goal specifies comparison and evaluation rather than joint production.

---

## 4. What is the same in both variants

The variant lives entirely in the orchestration rules. Every other element of the FAI architecture is identical across cooperation and competition events.

**Shared-substrate architecture.** Both variants operate over the shared substrate established in D1.01–D1.05: the substrate is constructed temporarily for the event, spans the participating Selves' home governance perimeters, carries all six Paper 1 commitments within scope, and dissolves with configurable persistence policy.

**FAI operation.** Both variants use the same aspect contribution, merge patterns, and conflict registry established in D1.06–D1.12. Aspects are the unit of exchange in both. The exchange is bounded to substrate content — DNA-layer and action-layer content only; instinct-layer content, LLM weights, and model internals do not cross the event boundary in either variant. The three merge pattern variants (full-merge, selective-merge, incremental update) are all available in both.

**Three rights and joint authority.** Both variants operate under joint authority across participating Selves' governance. Each participating Self retains the right to inspect, modify, and override any substrate content or orchestration rule in the shared substrate at any time. The joint authority structure is not variant-specific.

**Three-tier conflict-handling mechanism.** Both variants use the same preserve / resolve / escalate three-tier mechanism from D1.13–D1.16. The variant affects the configuration of tier-selection rules — which tier is more heavily used — not the availability or architecture of the tiers themselves.

**Evolution feed loci.** Both variants use the same four-locus evolution feed structure from D1.17–D1.21: hand-off at FAI dissolution, per-mechanism feed structure, three-case layer-routing rule, asymmetric ingestion across participating Selves. The variant affects governance's selectivity in configuring what to absorb; it does not change the loci or the routing rules.

**Home perimeter integrity.** In both variants, each participating Self's home perimeter remains intact throughout the event. Governance-configured ingestion at home perimeter boundaries governs what enters each Self's home substrate at dissolution. The event does not breach either Self's home governance.

---

## 5. The variant is in the orchestration rules

The core prior-art claim is this: cooperation and competition are not different architectures. They are the same architecture under different governance configurations of the orchestration rules.

An orchestration rule set is a set of authored governance instructions that determine how the shared substrate operates during an event: how conflicts are tiered, what the coordination goal is, how evolution feed is configured, how merge patterns are selected. These rules are themselves substrate content under joint authority — authored before the event, inspectable during and after, modifiable under governance. Switching from a cooperation variant to a competition variant means authoring different orchestration rules, not building a different system.

This has direct consequences for prior-art scope. Any party that builds a system for competitive AI-to-AI evaluation — in which multiple AI systems contribute their governance approaches to a shared space, conflicts between approaches are recorded, and each system learns from the comparison — has built an implementation of the shared-substrate architecture described in Paper 3 and formalized across D1.01–D1.22. The competition-specific orchestration rule configuration (preserve-biased conflict handling, comparison-oriented coordination goal, selective evolution feed) does not constitute novel architecture beyond what D1.22 Dimension 4 already commits to.

Similarly, any party that builds a system for cooperative AI-to-AI joint production — in which multiple AI systems contribute complementary capabilities to a shared task, conflicts are resolved to produce a coherent joint output, and each system absorbs the other's capabilities through governed evolution — has built an implementation of the same architecture under the cooperation variant's orchestration rule configuration.

The architecture is one. The configurations are two. Neither configuration is novel relative to the other; both are instances of the same governance-configured FAI parameter D1.22 Dimension 4 commits to.

---

## 6. Prior-art significance

Formalizing both variants as prior art closes two otherwise distinct claim territories.

The first territory is systems that present cooperative AI coordination as novel: multi-agent joint-production systems in which AI systems share reasoning artifacts, combine capabilities, and produce joint outputs under shared governance. The shared-substrate architecture from Paper 3, including the cooperation variant of FAI, is prior art for this territory. Any such system that uses a shared substrate to mediate the coordination, exchanges structured reasoning artifacts across home governance perimeters, handles conflicts in the shared substrate, and feeds evolution from the exchange is an implementation of this architecture.

The second territory is systems that present competitive AI evaluation as architecturally distinct from cooperative AI coordination — arguing that competitive evaluation requires novel mechanisms because it must preserve differences rather than resolve them, generate conflict maps rather than joint outputs, and support selective rather than comprehensive capability absorption. This argument does not survive D2.20's formalization. Competitive evaluation systems that preserve differences are using the same shared-substrate architecture with a preserve-biased tier-selection rule, which is an orchestration rule configuration. Generating conflict maps is what the conflict registry produces when the preserve tier is heavily used. Selective capability absorption is what governance-configured evolution feed selectivity produces at dissolution. None of these features require architecture beyond what D1.01–D1.22 establish.

Both claim territories are foreclosed. The prior-art chain runs from Paper 3's Claim 5 (configuration as substrate content) through D1.22 (cooperation/competition variant as Dimension 4) to D2.20 (operational specification of both variants).

---

## 7. Anti-pattern: conflating competition conflict density with governance failure

The anti-pattern to name explicitly is treating high conflict density in a competition variant event as a governance problem.

In the cooperation variant, high conflict density after a full-merge may indicate that the orchestration rules for conflict resolution are underspecified, that the aspects contributed by the two Selves are more incompatible than the coordination goal assumed, or that the event needs escalation to joint human authority before it can produce a useful output. These are genuine signals that something in the cooperation configuration needs attention.

In the competition variant, high conflict density after a full-merge is not a governance problem. It is the expected output of a well-run event. The conflict registry with many entries means the event successfully captured where the two Selves' governance approaches genuinely differ — which is exactly what a competition event is designed to reveal. A governance authority that responds to high conflict density in a competition event by reconfiguring the orchestration rules to resolve more conflicts has misdiagnosed the situation: the result is a competition event that erases the differences it was supposed to map.

The correct diagnostic question is not "how many conflicts were preserved?" but "is the conflict density consistent with the variant the event was configured to run?" A competition event with low conflict density may warrant investigation — the Selves' approaches may be genuinely aligned, or the contributing aspects may have been scoped too narrowly to surface real differences. A competition event with high conflict density is operating as designed.

This anti-pattern is architecturally grounded. The three-tier conflict-handling mechanism (D1.13–D1.16) makes conflict preservation, conflict resolution, and conflict escalation all first-class operations. The variant configuration governs which tier is the primary workhorse. The anti-pattern arises when a governance authority applies cooperation-variant diagnostics to a competition-variant event — treating preserve-tier output as something that should have been resolve-tier output. The operational distinction D2.20 establishes is what makes it possible to recognize and correct this misapplication.

---

## 8. Operational test

For a FAI event, an observer can determine from the orchestration rule configuration and the conflict registry patterns whether the event used the cooperation variant or the competition variant. The test has three components.

**Orchestration rule configuration.** Inspect the orchestration rules governing tier selection: what is the default tier when a conflict surfaces? What conditions trigger resolve versus preserve? What is the stated coordination goal? A cooperation variant event will have resolve-biased tier-selection rules and a joint production goal. A competition variant event will have preserve-biased tier-selection rules and a comparative evaluation goal. These are authored substrate content under joint authority, inspectable at any time.

**Conflict registry pattern.** Inspect the conflict registry at the end of the event: what proportion of surfaced conflicts are registered as preserved versus resolved? In a cooperation variant event, the resolved proportion should be higher — the event was trying to produce a coherent joint output from the contributed aspects. In a competition variant event, the preserved proportion should be higher — the event was trying to map differences. A competition event where the resolved proportion dominates warrants governance review of whether the orchestration rules were correctly configured for the stated variant.

**Evolution feed configuration.** Inspect the evolution feed configuration at each participating Self's home perimeter: what DNA absorption scope did governance authorize? A cooperation variant event will typically show broader authorization. A competition variant event will typically show more selective authorization, scoped to aspects the conflict registry identified as candidates for genuine improvement.

All three components are substrate content — authored, inspectable, and auditable per the shared substrate's governance. The test is executable without access to either Self's home substrate internals; it operates entirely on the shared substrate's content during and after the event.

---

*This derivation note (#515) is part of the CKS defensive publication series. It derives Phase D2.20 from D1.22 Dimension 4 (cooperation/competition variant as a governance-configured FAI parameter). The note establishes cooperation and competition as orchestration rule variants of the same shared-substrate architecture, not as distinct architectures, and forecloses novelty claims for both cooperative AI coordination systems and competitive AI evaluation systems relative to Paper 3's prior-art chain.*
