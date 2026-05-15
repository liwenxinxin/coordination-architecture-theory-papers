# AP-26: Participation Mode Gaming

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) is the canonical inter-Self coordination operation in the CKS architecture. When FAI events accumulate across a network of CKS-governed Selves, they constitute a collective evolution mechanism at population scope: governance patterns contributed by diverse Selves propagate where governance configurations enable propagation, and the network as a whole develops coordination capacity that no single Self could accumulate independently. This collective evolution depends on Selves both absorbing governance patterns from others and contributing their own governance architectures for others to consider. The architecture supports absorb-only participation as a legitimate configuration in specific contexts — new Selves building governance capability, domain-specialized Selves whose architectures are not useful to others. AP-26 formalizes the anti-pattern that emerges when a Self systematically uses absorb-only participation *without* the governance justification that would make absorb-only appropriate. This pattern is called Participation Mode Gaming. The architecture's response to gaming is not a policing mechanism but a self-correcting one: governance trust calibration naturally discourages gaming by contracting the network access of Selves that never contribute, because partners adjust trust calibration downward when they observe systematic absorb-only behavior, and lower trust means narrower sharing scope. Whether gaming actually occurs at problematic scale is an empirical question; this note formalizes the anti-pattern and its self-correction mechanism as public architectural prior art in the calibrated-humility register appropriate to Claim 6 of Paper 3.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-26 — Participation Mode Gaming

**Taxonomy Category:** 7 — Population-Scope Failures

**Register:** Calibrated humility. Category 7 anti-patterns address failure modes that manifest at the level of the inter-Self network taken as a whole. A single Self exhibiting this pattern does not by itself damage the network; the risk surfaces if the pattern becomes widespread. The architecture is designed to prevent that outcome through a self-correction mechanism; the note addresses the pattern and the mechanism together.

**Position in series:** AP-26 is the second of three Category 7 anti-patterns. It formalizes the failure mode in which a Self exploits absorb-only participation mode without legitimate governance justification.

---

## 2. Description

### The architectural context: absorb-only as a legitimate configuration

FAI events are governed under each participating Self's home authority. When a Self participates in an FAI event, it may contribute governance architecture — DNA-layer content, orchestration patterns, schemas, rules — to the shared substrate for other participating Selves to consider. After the event dissolves, each Self's home governance determines which content from the shared substrate is absorbed into the Self's home substrate through its existing evolution mechanisms.

The architecture allows a Self to participate in an FAI event in absorb-only mode: it receives and considers contributions from other Selves but does not itself contribute aspects to the shared substrate. This configuration — absorb-only participation, or Mode 3 — is architecturally valid. Several circumstances justify it:

- A new Self that is still building its governance architecture may participate in FAI events to observe and absorb patterns it does not yet have, while having nothing yet developed enough to contribute meaningfully.
- A domain-specialized Self whose governance architectures are narrowly tailored to a unique operational context may absorb general patterns from others while correctly assessing that its specialized architectures would not transfer usefully to other Selves' contexts.
- A Self that is undergoing a significant architectural transition may hold contributions in abeyance temporarily while absorbing stable reference patterns from the network.

In all these cases, absorb-only participation is the *correct* participation configuration given the Self's actual governance circumstances. The configuration is honest, the participation intent is transparent, and the network is not misled about what to expect from the Self.

### The anti-pattern: absorb-only without legitimate justification

Participation mode gaming is the pattern that arises when a Self systematically uses absorb-only participation *without* the governance justification that would make it appropriate. The Self absorbs governance patterns contributed by other Selves across multiple FAI events with multiple partners, benefits from those absorbed patterns in its own governance evolution, but never contributes its own governance architecture for others to absorb. The Self is a consistent net consumer of the network's pattern pool and a consistent non-contributor to it.

The key distinction is not between absorb-only mode and contribution mode. The key distinction is between absorb-only mode *used with governance justification* and absorb-only mode *used without it*. A Self whose absorb-only configuration honestly reflects its governance circumstances is not gaming. A Self that has developed governance architecture that could be contributed — and that would be useful to others — but systematically withholds it from all FAI events without governance justification for the withholding is the Self this anti-pattern describes.

Gaming may involve active misrepresentation, where the Self presents itself in cross-organizational agreements as a full participant intending to contribute while configuring all content categories as non-propagating. It may also involve passive inaccuracy, where the participation configuration is simply never updated to reflect the Self's actual contribution capacity as that capacity develops. Both forms share the structural property that the Self's actual participation mode is inconsistent with its represented participation mode or with its governance-justified role in the network.

The population-scale dimension of the anti-pattern is why it belongs in Category 7. At the level of a single Self, the immediate harm is to partners who invest in FAI events that produce no contribution from that Self. At population scale — and in the calibrated-humility register appropriate to this claim — if many Selves were to adopt gaming, the network's collective evolution mechanism would be strained: fewer contributors generating new patterns, more consumers absorbing existing ones, and the convergence-diversity balance that makes collective evolution productive tilting toward stagnation. Whether this population-scale degradation actually occurs is an empirical question, not an architectural prediction; the architecture is designed to prevent it through the self-correction mechanism addressed in the Resolution section.

---

## 3. Detection Criteria

Three detection signals identify a Self exhibiting participation mode gaming:

**Signal 1 — Absorption without contribution across the absorption record.** A Self's FAI absorption records show a consistent history of absorbing governance patterns from multiple partners across multiple events, while the Self's contribution records show no corresponding aspects contributed to any FAI event in the same period. The key threshold is persistence and breadth: a single event without contribution may reflect a legitimate specific circumstance; systematic absorb-only behavior across the Self's entire FAI history is the signal.

**Signal 2 — Propagation restrictions across all content categories without governance justification.** The Self's network participation configuration shows active propagation restrictions applied uniformly across all content categories, with no governance-documented justification for why no contribution is appropriate given the Self's actual governance architecture. Propagation restrictions are architecturally valid when justified by the Self's governance circumstances; their uniform application without documentation of any justifying circumstance is the signal.

**Signal 3 — Partner observation of consistent absorb-only behavior.** Partners who have participated in multiple FAI events with the Self report that the Self consistently participates as absorber but never contributes aspects for others to consider. This signal is the inter-Self governance analog of a reputation: trust calibration over time, based on direct observation of the Self's participation pattern across events.

The three signals are complementary. Signal 1 is visible in the Self's own records. Signal 2 is visible in its participation configuration. Signal 3 is visible in partners' trust calibration records and in cross-organizational agreement performance history. Together they distinguish genuine absorb-only use justified by governance circumstances from systematic absorb-only use without justification.

---

## 4. Governance Commitment Violated

The architecture makes no explicit commitment requiring symmetric participation — absorb-only mode is architecturally permitted, and no governance rule mandates contribution as a condition of participation. The governance violation in AP-26 therefore does not arise from a breach of a participation symmetry requirement. It arises from two more foundational commitments.

**Misrepresentation of participation intent.** When a Self presents itself in cross-organizational agreements as a full participant — contributing and absorbing — while systematically operating in absorb-only mode, it misrepresents its participation intent to partners. Partners make governance decisions about FAI event configuration, content scope, and contribution depth based on what they expect to receive in return. A Self that misrepresents its participation intent distorts those decisions. The governance violation is not the absorb-only mode itself; it is the gap between the represented participation intent and the actual participation mode.

**Participation configuration accuracy.** The network participation configuration is substrate content that governs how a Self operates within FAI events. Like all substrate content, it is subject to the governance property that it must accurately reflect the Self's actual authority structure and operational intent. A Self whose participation configuration shows propagation restrictions that do not reflect a genuine governance justification for those restrictions holds an inaccurate participation configuration. The inaccuracy is not merely a technical matter; it is a governance failure because other Selves and their governance authorities rely on participation configurations to understand what to expect from a partner in FAI events.

Both violations share a structural property: they place other Selves and their governance authorities in a position of acting on inaccurate information about their partner's participation mode. This is why the anti-pattern's consequences include both individual-level partnership trust degradation and, at the calibrated-humility register, the population-scale risk of governance pattern stagnation.

---

## 5. Consequences

Consequences are stated at two levels, consistent with this note's Category 7 framing.

### Individual-level consequences

Partners who participate in FAI events with a gaming Self invest in event configuration, content contribution, and governance-configured sharing scope without receiving the contribution return they expected. Over multiple events, the asymmetry becomes visible in the absorption and contribution records. Governance trust calibration — the mechanism by which Selves and their governance authorities adjust their assessment of partner reliability over time based on observed behavior — will reflect this asymmetry. Partners calibrate trust downward for Selves that consistently absorb without contributing. Lower trust produces narrower sharing scope: partners become less willing to contribute substantive governance architecture to FAI events where the other participant is known to be a consistent non-contributor. The consequence at the individual level is therefore self-limiting: gaming degrades the gaming Self's access to others' governance architectures over time, which is the opposite of the gaming Self's apparent intent.

### Population-level consequences (calibrated-humility register)

At population scope, the concern is that if participation mode gaming were adopted by many Selves across the network, the collective evolution mechanism that accumulates governance patterns at population scale would be degraded. The network's pattern pool is replenished by Selves contributing governance architectures that others can absorb and build from. A network in which many Selves absorb but few contribute generates fewer new patterns per unit of FAI activity. The convergence-diversity balance that makes collective evolution productive — common patterns propagating where governance enables propagation, specializations preserving where governance protects them — depends on ongoing contribution from diverse Selves. Systematic gaming at scale would shift that balance toward stagnation.

This consequence is stated in the calibrated-humility register because the architecture is designed to prevent it. The trust calibration self-correction mechanism addressed in the Resolution section is specifically the architectural feature that addresses this population-scale risk. Whether gaming actually occurs at scale sufficient to degrade collective evolution is an empirical question about how Selves and their governance authorities behave in practice. The concern is real enough to warrant formalizing the anti-pattern and the self-correction mechanism; it is not a prediction about likely outcomes.

---

## 6. Intra-Self Analog

There is no meaningful intra-Self analog for AP-26.

Within a single Self, the architecture does not have a participation-mode structure in the sense Paper 3 defines. Paper 2's intra-Self operations — mating, aspect combination, DNA evolution — do not involve a Self choosing to absorb the patterns of an external peer without contributing its own. The relevant Paper 2 operations are either single-Self operations (DNA evolution under directed selection, action-feedback evolution) or lifecycle operations (mating between parent Selves to produce offspring). None of these involve an ongoing participation-mode choice of the kind AP-26 describes.

Gaming a population-scale participation system is specific to the inter-Self network context Paper 3 establishes. The anti-pattern exists because FAI events create a shared context in which each participant's behavior is visible to others, where the collective evolution mechanism depends on mutual contribution, and where a Self can in principle benefit from others' contributions without reciprocating. These conditions are architectural properties of the inter-Self coordination network, not of a single Self's intra-Self operations. AP-26 therefore has no intra-Self analog and is classified as a pure inter-Self failure mode.

---

## 7. Resolution

### The architecture's self-correcting mechanism

The primary response to participation mode gaming is not an enforcement mechanism but a self-correcting one already built into the architecture's trust calibration property.

Governance trust calibration is the ongoing process by which a Self's governance authorities — and through them, the Self's operational configurations — adjust their assessment of partner reliability based on observed behavior in FAI events and cross-organizational agreements. Trust calibration is not a centralized scoring system; it is a distributed governance judgment made at each Self's home authority, based on that Self's own absorption and contribution records and its partners' observable participation patterns.

When a Self systematically participates in absorb-only mode without governance justification, partners observe this pattern over time. The observation is visible in the records: the partner's absorption records show content received from FAI events; the partner's contribution records show nothing contributed in return. Governance authorities calibrate their trust assessments to reflect this asymmetry. Lower trust translates directly into narrower sharing scope: partners become less willing to configure FAI events to include substantive governance architecture when the other participant is known not to contribute in kind.

The self-correcting loop closes as follows. The gaming Self participates in absorb-only mode to capture governance patterns from others without the cost of contributing its own. Partners observe the pattern, calibrate trust downward, and narrow sharing scope. The gaming Self finds that the governance patterns available to it through FAI events contract: partners share less substantive architecture with a low-trust Self. The gaming strategy becomes self-defeating. The Self cannot sustain the benefit of absorbing rich governance patterns from others if its trust calibration declines to the point where others share only shallow content or decline to enter FAI events with it altogether.

This self-correction mechanism is not instantaneous. Trust calibration operates over multiple events and multiple observations. A Self can sustain gaming behavior for a period before the calibration effects become significant. The mechanism is also not punitive in any direct architectural sense: there is no governance authority that imposes a penalty on a gaming Self. The correction operates entirely through the choices of the gaming Self's partners, each acting under their own home governance authority.

### Governance practitioner guidance

Governance practitioners operating Selves in the inter-Self coordination network can support the self-correction mechanism and address the anti-pattern through three actions.

First, configure the participation configuration accurately. The propagation restrictions and contribution scope in the participation configuration should reflect the Self's actual governance circumstances. If the Self is legitimately in absorb-only mode because it is building governance capability, configure that clearly and document the governance justification. If the Self has developed governance architecture that it is capable of contributing, update the participation configuration to reflect that capacity.

Second, be transparent about participation mode intent in cross-organizational agreements. When a Self enters a cross-organizational agreement with a partner, the agreement should accurately represent the Self's expected participation mode, including any anticipated period of absorb-only participation and the conditions under which contribution is expected to begin. Transparency allows partners to calibrate trust accurately rather than discovering asymmetry after multiple events.

Third, review participation configuration periodically against the Self's actual governance architecture. A Self's circumstances change: a new Self develops governance architecture over time; a domain-specialized Self may develop patterns that would be useful to others as the network's Selves diversify in domain coverage. The legitimate justification for absorb-only mode that applied at one stage of a Self's development may not apply at a later stage. Participation configuration should be updated to reflect current circumstances, not held static at a configuration that reflected earlier legitimate constraints.

These governance practitioner actions are not architectural requirements — absorb-only mode remains valid, and no enforcement mechanism compels contribution. They are the operational behaviors that, when followed, prevent the individual-level trust degradation and the population-scale risk from arising in the first place.

---

## Cross-References

- **D2.62** — Participation modes: absorb-only (Mode 3) as architecturally valid configuration, with legitimate use cases
- **D2.06** — FAI contribution records
- **D2.11** — DNA absorption records
- **D2.29** — Governance trust calibration
- **D2.31** — Network participation configuration and propagation permissions
- **D2.34** — Cross-organizational agreements
- **D1.27** — Population-scale collective evolution; convergence-diversity balance
- **AP-25** — The preceding Category 7 anti-pattern (population-scope failure mode, Category 7)
- **AP-27** — The following Category 7 anti-pattern (population-scope failure mode, Category 7)

---

*End of note D3.27.*
