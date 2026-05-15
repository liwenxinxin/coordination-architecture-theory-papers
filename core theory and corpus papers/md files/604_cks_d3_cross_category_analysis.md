# Cross-Category FAI Anti-Pattern Analysis

**Series note:** D3.29 — Derivation Note #604
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Notes D3.01 through D3.28 formalize twenty-seven anti-patterns across seven categories covering the failure modes of the Full Aspect Integration (FAI) architecture. This note, D3.29, synthesizes those twenty-seven anti-patterns as a cross-category analytical object rather than treating each in isolation. The note identifies four co-occurrence patterns in which one anti-pattern's presence makes one or more others statistically likely; identifies three particularly dangerous combinations in which the interaction between two anti-patterns produces failure more severe than either anti-pattern produces alone; presents a detection priority order for governance auditors who cannot inspect all twenty-seven simultaneously; and provides cross-category detection efficiency guidance that converts the taxonomy from a reference list into a practical diagnostic tool.

---

## 1. The Cross-Category Analytical Posture

D3.01 through D3.28 treat each anti-pattern in isolation: what the anti-pattern is, which architectural commitment it violates, what its operational signatures are, and how it differs from the correct pattern. Isolation is the right posture for formalization — it keeps each note's scope clean and makes each note useful as a standalone reference. But isolation is the wrong posture for governance auditing. Anti-patterns in FAI systems do not occur independently. They share causal structure: some anti-patterns produce conditions that make others likely. They cluster by lifecycle phase: anti-patterns that violate lifecycle governance (AP-1, AP-2) tend to appear together. And they interact: two anti-patterns present simultaneously can produce failure modes that neither would produce alone.

D3.29 provides the cross-category layer that the isolation posture cannot. Its output is not a summary of D3.01–D3.28 but a structural analysis of how those twenty-seven anti-patterns relate to one another and what that structure implies for efficient detection.

---

## 2. Four Key Co-Occurrence Patterns

A co-occurrence pattern names a set of anti-patterns that tend to appear together, along with the causal mechanism that links them. Identifying co-occurrence patterns allows a governance auditor who detects one member of the set to efficiently check for the others rather than treating each as an independent finding.

### Pattern 1 — The Implicit Configuration Cascade

**Chain:** AP-6 (Implicit Configuration) → AP-1 (Ungoverned Construction) → AP-22 (Black Box Shared Substrate) → AP-23 (Authorization Chain Gap)

When a FAI event has no authored configuration substrate — the condition AP-6 names — the absence is not merely a configuration gap. It is the root cause of a downstream cascade. Without an authored configuration, there is no governance record of the event's initiation, which is the condition AP-1 names. Without a construction authorization record, the shared substrate carries no governance basis for decisions made during the event, which is what AP-22 identifies as the black-box condition. Without governance basis for decisions, the authorization chain that should connect each decision to a human-authored authority has no origin point, producing the chain gap AP-23 names. Each downstream anti-pattern is a consequence of AP-6, not a separate failure. AP-6 is the root; the others are its branches.

This causal structure has a direct governance implication: finding AP-6 is like finding the root of a failure tree. Addressing AP-6 by introducing authored configuration substrate does not merely close AP-6; it removes the causal precondition for AP-1, AP-22, and AP-23. The four-anti-pattern cluster may collapse to zero with a single intervention at the root.

### Pattern 2 — The Conflict Governance Collapse

**Chain:** AP-12 (Informal Resolution Rules) → AP-22 (Black Box Shared Substrate) → AP-3 (Silent Conflict Collapse)

When conflict resolution logic is informal rather than specified as substrate-level rules — the condition AP-12 names — the shared substrate's conflict governance becomes opaque. A governance authority cannot inspect what rule was applied to which conflict, because no formal rule exists to inspect; this is the AP-22 black-box condition applied specifically to conflict governance. Informal rules, operating without inspectable specification, tend to systematically favor one contributing party's aspects over another's through implicit priority rather than explicit policy. Sustained, this systematic favoritism produces outcomes equivalent to AP-3: conflicts are not genuinely registered and preserved as first-class substrate state but are instead silently resolved in one direction. AP-3 is the outcome of AP-12 operating through AP-22; it may not appear as a distinct event but as the gradual erosion of conflict-preservation integrity.

### Pattern 3 — The Evolution Governance Chain Failure

**Chain:** AP-5 (Non-Attributed Ingestion) → AP-15 (Vertical Propagation Break) → AP-16 (Unconfigured Proposing Substrate)

When FAI-origin records are ingested into a home substrate without attribution markers — the condition AP-5 names — the record's origin as a FAI-derived input is lost at the point of ingestion. The four-locus evolution feed requires that FAI-origin content carry its attribution as it propagates vertically through the home substrate's evolution machinery. Without attribution, vertical propagation cannot carry FAI-origin markers; AP-15 (Vertical Propagation Break) is the direct consequence of AP-5 at the propagation layer. Without vertical propagation of FAI-origin markers, the proposing substrate that surfaces evolution proposals cannot be configured to distinguish FAI-origin proposals from other proposals; AP-16 (Unconfigured Proposing Substrate) results. The three anti-patterns form a single propagation failure: attribution loss at ingestion cascades upward through the evolution chain.

### Pattern 4 — The Lifecycle Governance Void

**Cluster:** AP-1 (Ungoverned Construction) + AP-2 (Ungoverned Dissolution)

AP-1 and AP-2 together do not form a cascade in the causal sense — neither causes the other. They form a void. When a FAI event has no construction authorization record (AP-1) and no dissolution record (AP-2), every governance decision made during the event's lifecycle lacks both a foundation (no construction record establishes the event's authorized purpose and scope) and a closure (no dissolution record provides a governed endpoint or evolution hand-off). The event is a governance void throughout its duration: each decision made during it floats without anchoring to a construction authorization and without resolving into a dissolution record. The void is not localized — it extends across the entire event lifecycle and undermines every governance artifact the event was supposed to produce.

---

## 3. Three Most Dangerous Combinations

Co-occurrence patterns describe probability and causal structure. The most dangerous combinations describe something distinct: anti-pattern pairs whose *interaction* produces failure modes more severe than either anti-pattern alone would produce, because the two anti-patterns remove complementary safeguards.

### Most Dangerous: AP-6 + AP-24 — Implicit Configuration and Automated Governance

AP-6 alone is severe: a FAI event without authored configuration has no governance foundation. A human auditor or governance authority who becomes aware of the gap can, however, intervene — human authority is still present and exercisable even when the configuration substrate is absent. AP-24 alone is also severe: governance decisions made by automated systems rather than human-authored rules displace human authority from individual decisions. But a FAI event governed by automated systems may still have an authored configuration that constrains the automation's decision space.

When AP-6 and AP-24 are present simultaneously, the two safeguards that individually limit each anti-pattern's damage disappear together. There is no authored configuration to constrain what the automated governance system may decide, and there is no human authority actively governing the decisions the automation is making. The FAI event is, in every operational respect, an ungoverned inter-AI coordination event — the named foil of the architecture — while appearing to external inspection to be a governed FAI event. The combination is dangerous not merely because it accumulates two deficiencies but because it produces a false appearance of governance that the constituent anti-patterns alone might not sustain.

### Highly Dangerous: AP-8 + AP-19 — Exchange Bounding Violation and Time-Pressure Governance Bypass

AP-8 names the condition in which an exchange during a FAI event carries content that violates the instinct/reasoning separation — content that should not cross the inter-Self boundary has crossed it. Detecting and investigating an AP-8 violation is the governance response that limits its damage: the violation is identified, its scope is bounded, and the separation is restored before the violated content propagates into the home substrate's evolution machinery.

AP-19 names the condition in which time-pressure during an FAI event causes governance to bypass investigation requirements. When AP-19 is also present at the moment AP-8 occurs, the investigation that would detect, scope, and remediate the AP-8 violation is bypassed. The exchange bounding violation proceeds unexamined. The instinct/reasoning separation is compromised without resolution. Content that should not have crossed the inter-Self boundary may be ingested into the evolution feed without governance awareness that a violation occurred. AP-8 is damaging; AP-8 without investigation is substantially more damaging because the damage is invisible.

### Significant Risk: AP-18 + AP-17 — Forgotten Standing Configuration and N-Blind Configuration

AP-18 names the condition in which a standing configuration established for a prior FAI event relationship — typically an N=2 relationship between two specific Selves — remains in place without review when the relationship's composition changes. AP-17 names the condition in which a FAI event's configuration does not account for the N-ary cardinality of the current event's participant set.

When a standing configuration from an N=2 relationship (AP-18) is applied to an N=3 event without being updated for the third participant Self (AP-17), the result is a governance framework that is simultaneously stale with respect to prior evolution and incomplete with respect to current participants. The outdated configuration contains authority assumptions, conflict-handling logic, and evolution-feed parameters built for two Selves. The N-blind configuration fails to specify governance for the third Self's contributions. Together, the event operates under governance that is both behind its own history and ahead of its own specification — governing a relationship that no longer exists while failing to govern the relationship that does.

---

## 4. Detection Priority Order

For governance auditors conducting an efficiency-constrained audit — one in which not every anti-pattern can be checked in every event — the following detection priority order reflects both severity and causal structure.

1. **AP-6 (Implicit Configuration)** — first because it is the root cause of the implicit configuration cascade. Finding AP-6 immediately warrants checking AP-1, AP-22, and AP-23 as likely co-occurrences. Addressing AP-6 may resolve all four simultaneously.

2. **AP-8 (Exchange Bounding Violation)** — second because it is the severity trigger for the most damaging operational failure in a running FAI event. An AP-8 violation that proceeds uninvestigated (the AP-8 + AP-19 combination) produces lasting damage to the instinct/reasoning separation.

3. **AP-24 (Automated Governance)** — third because its presence transforms the severity of AP-6 from a governance gap into a governance void. If AP-6 is detected, AP-24 must be checked immediately to determine whether the dangerous combination is present.

4. **AP-3 (Silent Conflict Collapse)** — fourth because it is among the hardest anti-patterns to detect directly. AP-3 rarely announces itself as a discrete event; it manifests as the gradual absence of preserved conflicts in the shared substrate. Checking AP-12 first is the practical path to AP-3 detection.

5. **AP-1 and AP-2 (Lifecycle Governance)** — fifth, checked together, because together they establish whether the event is a lifecycle governance void. Their detection is foundational: an event that fails both establishes that every governance artifact produced during the event is unsupported at both ends.

---

## 5. Cross-Category Detection Efficiency

The co-occurrence patterns identified in §2 generate actionable detection efficiency rules. These rules convert the twenty-seven-anti-pattern taxonomy from a reference list into a triage protocol. The logic in each rule follows directly from the causal or structural relationship between the anti-patterns named.

**If AP-6 is detected:** Also check AP-1, AP-22, and AP-23 immediately. Co-occurrence likelihood is high because AP-6 is the root cause of the implicit configuration cascade; the three downstream anti-patterns are its probable consequences.

**If AP-3 is detected:** Also check AP-12. Silent conflict collapse is frequently the outcome of informal resolution rules operating without inspectable specification. Finding AP-3 without finding AP-12 requires an alternative causal explanation; AP-12 is the first candidate.

**If AP-5 is detected:** Also check AP-15 and AP-16. Attribution loss at ingestion cascades upward through the evolution chain. AP-15 and AP-16 are the downstream manifestations of AP-5's attribution loss; they may not be detectable at the ingestion layer but will be present at the propagation and proposing-substrate layers.

**If AP-8 is detected:** Also check AP-19. The dangerous combination requires that both be present; checking AP-19 immediately after finding AP-8 determines whether the violation is proceeding uninvestigated.

**If AP-1 is detected:** Also check AP-2. The lifecycle governance void requires both; finding one warrants checking the other immediately.

**If AP-18 is detected:** Also check AP-17. A forgotten standing configuration from a prior N-composition warrants checking whether the current event's configuration accounts for its actual participant set.

These rules do not require checking all twenty-seven anti-patterns on every event. They require checking the most likely co-occurring anti-patterns whenever a trigger anti-pattern is found. A governance auditor who follows this triage protocol will, in most cases, surface the entire co-occurrence cluster from a single initial detection — reducing audit cost while increasing detection coverage.

---

## 6. Position in the D3 Phase

D3.29 occupies the penultimate position in Phase D3. Notes D3.01 through D3.28 formalize each anti-pattern in isolation, establishing the vocabulary and structural specificity on which this cross-category analysis depends. D3.30, the final Phase D3 note, provides closure for the phase. The cross-category analysis in D3.29 is the analytical synthesis that the isolation posture of D3.01–D3.28 makes possible; it does not replace the individual notes but operates at the structural layer above them.

---

*Derivation note #604 in the CKS defensive publication series. License: CC BY 4.0. This note may be freely used, adapted, and redistributed with attribution.*
