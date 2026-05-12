# Deployment-Level-Only Governance: The Anti-Pattern That Arises When Paper 1 Governance Applies Only at Deployment Scope Without Recursive Application per B1.20

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Paper 2 of the CKS theory series commits, through B1.20, that the Paper 1 governance architecture applies recursively at cell, aspect, and Self scope — not only at the deployment or system scope at which architects commonly satisfy governance requirements. The Deployment-Level-Only Governance anti-pattern is the failure mode that results when this recursive commitment is absent: governance operates at the deployment container, the deployment appears governed, and individual entities — cells, aspects, Selves — are not independently governed. This note names the anti-pattern, identifies the B1.20 commitment it violates, describes three recognizable forms, traces three emergence conditions and four operational consequences, and specifies detection and remediation procedures. It also acknowledges its position as the twentieth and final primary anti-pattern in Phase B3, completing the one-to-one correspondence with B1.01–B1.20, and notes that B3.22–B3.30 will address cross-cutting anti-patterns.

## 1. Pattern name and commitment violated

**Pattern name:** Deployment-Level-Only Governance

**Commitment violated:** B1.20 — recursive Paper 1 commitments. Paper 2 establishes that the full Paper 1 governance architecture — including the human-governed commitment (A1.01), the labor allocation framework (A1.12), path retraceability (A1.07), the substrate as source of truth (A1.08), and the associated governance affordances (A2.01–A2.04) — applies at cell, aspect, and Self scope, not only at deployment scope. B2.98 formalizes the recursive commitment frame; B2.102–B2.108 specify what each Paper 1 commitment means at each of the three entity levels; B2.109 provides entity-level operational tests; B2.110 provides recursive commitments verification to confirm the architecture is complete.

The anti-pattern is not the absence of governance. A deployment exhibiting this anti-pattern may carry substantial governance investment: review processes, compliance demonstrations, audit records, and human authority exercised at the deployment level. What is absent is the recursive extension of that governance architecture to the entity levels Paper 2 specifies.

## 2. Recognizable forms

The anti-pattern presents in three recognizable forms, each representing a different degree or kind of governance scope failure.

### Form 1 — Top-Level-Only Governance

Governance operates at the deployment or Self level but individual cells and aspects are not independently governed. Paper 1 commitments are satisfied at deployment scope — the deployment can demonstrate that humans retain inspect, modify, and override rights over the system as a whole, that the substrate is the source of truth at deployment scope, and that path retraceability is implemented — but these commitments have not been extended to individual entities.

Recognition signals: governance reviews and compliance demonstrations reference the deployment as the unit of analysis; there are no independent governance records for individual cells per A2.40; B2.14 and B2.19 cell-level and aspect-level inheritance verification procedures have never been run; A2.01–A2.04 governance affordances are exercisable at deployment scope but not configured at cell or aspect scope; B2.110 recursive commitments verification, if run, finds entity-level verification absent.

This is the most common form because it maps directly onto familiar compliance practice. Architects who understand governance as a deployment-level property satisfy the requirements they recognize — system-level compliance, deployment-level audit — and do not encounter entity-level requirements in familiar frameworks.

### Form 2 — Level-Selective Governance

Some levels have governance applied but others do not. The recursive governance architecture is partial: Self level may be governed but aspect level is not; or cell level is governed but Self level is not; or governance covers cell and Self but skips aspects. The commitment B1.20 specifies is that the same governance architecture applies at all three levels — cell, aspect, and Self. A partial architecture that covers some levels is not the same as an absent architecture, but it fails the recursive commitment nonetheless.

Recognition signals: running B2.102–B2.108 per-commitment recursive applications reveals gaps at specific levels; B2.99 cell-level commitments check shows Paper 1 applied at cell scope while B2.100 aspect-level check fails; governance records, audit trails, and affordance configurations exist for some entity levels but are absent for others. The gaps may not be uniform — different Paper 1 commitments may be partially applied at different levels, producing a patchwork that is difficult to characterize as either governed or ungoverned.

Level-selective governance is architecturally more difficult to detect than top-level-only governance because some governance investment has been made. An architect who has extended governance to cells may believe the recursive commitment is satisfied without recognizing that aspect-level governance is absent or that only some Paper 1 commitments have been recursively applied.

### Form 3 — Entity-Inspection-Absent

Governance affordances per A2.01–A2.04 exist at deployment level but cannot be exercised at individual entity scope. The inspect right (A2.01), modify right (A2.02), override right (A2.03), and rule-authoring right (A2.04) are available to humans operating at the deployment level but are not configured or accessible at the entity level. A human exercising governance cannot inspect individual cell DNA directly through governance channels; cannot individually modify cell DNA or action layer content; cannot author orchestration rules at cell or aspect scope.

Recognition signals: attempting to exercise A2.01 inspect right at cell scope reveals that cell DNA cannot be individually inspected through governance channels; compliance audits can demonstrate deployment-level compliance but cannot produce entity-level compliance evidence; B2.109 recursive operational tests have never been run at entity scope; directed selection per B1.14 at entity scope is not operationally available because the governance infrastructure to exercise it does not extend to entity scope.

This form may occur even when governance architecture investment has been made at deployment level. The affordance gap is not a matter of insufficient will to govern but of governance infrastructure that was not extended to the granularity the recursive commitment requires.

## 3. Emergence conditions

Three conditions produce the Deployment-Level-Only Governance anti-pattern.

**Deployment-level compliance culture.** Regulatory, audit, and compliance frameworks familiar to architects and engineers operate at system or deployment level. The compliance vocabulary — system governance, deployment audit, platform certification — names the deployment as the governed unit. Architects who satisfy these familiar requirements have satisfied the governance commitments they recognize. The entity-level requirements Paper 2's B1.20 specifies do not appear in familiar compliance frameworks; they require a deliberate act of scope extension that familiar compliance practice does not prompt. The resulting deployment is compliant by the standards the architects know and ungoverned at the entity level by standards they have not encountered.

**Governance architecture underinvestment.** Entity-level governance requires more governance infrastructure than deployment-level governance. Extending A2.01–A2.04 affordances from deployment scope to cell, aspect, and Self scope requires additional configuration, tooling, and verification effort. Running B2.14, B2.19, and B2.24 level-specific inheritance verification for all entities requires operational procedures that do not exist by default. The additional investment is not made because its necessity is not recognized, because it is deprioritized against other costs, or because the architecture budget was set against deployment-level requirements alone.

**Paper 1 misread as deployment-scope-only.** Architects who read Paper 1 without Paper 2's recursive extension may understand the Paper 1 commitments as deployment-level commitments. The human-governed commitment (A1.01), path retraceability (A1.07), and substrate-as-source-of-truth (A1.08) can all be read as properties of a deployment without reading them as properties that must hold at every entity scope within that deployment. Paper 2's B1.20 commitment is the explicit statement that the recursive extension is required; without it, architects may implement a Paper 1-compatible deployment without implementing a Paper 2-compatible one.

## 4. Operational consequences

**Ungoverned entities within a governed deployment.** Individual cells may produce ungoverned behavior that the deployment-level governance cannot detect. A cell's DNA layer may carry content that has never been inspected at cell scope, modified at cell scope, or subjected to the override right at cell scope. Deployment-level governance provides a false sense of compliance: the system appears governed because the deployment container is governed, while individual entities operate without the governance constraints the recursive commitment requires. Failures that originate in ungoverned cell or aspect state are not detectable through deployment-level governance channels.

**Entity-level compliance impossible.** Regulated environments may require compliance demonstrations not only at system level but at the level of individual components — particularly as AI governance frameworks mature and begin specifying component-level accountability requirements. A deployment with Deployment-Level-Only Governance cannot produce entity-level compliance evidence because the governance infrastructure does not extend to entity scope. Compliance demonstrations can only operate at the level at which governance infrastructure exists. This consequence becomes operationally significant when external requirements specify entity-scope accountability, audit, or inspection.

**Governance affordance gaps.** Humans cannot exercise the A2.02 modify right or A2.04 rule-authoring right at cell or aspect scope if governance infrastructure does not extend there. This means that directed selection per B1.14 at entity scope is not operationally available: the human-governed mechanism by which entity-level DNA evolution is guided by deliberate human selection over candidate DNA variants requires that humans can exercise authority at entity scope. A deployment with Form 3 of this anti-pattern — entity-inspection-absent — may have the directed selection concept in its design vocabulary while lacking the infrastructure to execute it. The gap between the design intention and the operational capability is a governance affordance gap produced by the anti-pattern.

**Recursive governance architecture absent.** B2.102 recursive A1.01, B2.103 recursive A1.12, B2.104 recursive A1.08, and the other per-commitment recursive formalizations in B2.102–B2.108 specify the positive architecture that B1.20 requires. A deployment with Deployment-Level-Only Governance does not instantiate this architecture. The Paper 2 commitment of recursive governance is not fulfilled, and the substrate lacks the architectural properties that downstream work depending on recursive governance would require. Subsequent composition, extension, or compliance work that assumes recursive governance is in place will encounter failures that trace to this foundational absence.

## 5. Detection

**B2.110 recursive commitments verification.** The primary detection procedure asks directly: are Paper 1 commitments applied at entity level? Running B2.110 will surface whether each of the Paper 1 commitments named in B2.102–B2.108 has been operationalized at cell, aspect, and Self scope. A deployment with Deployment-Level-Only Governance will show either complete absence of entity-level application (Form 1), partial coverage across levels (Form 2), or affordance-configuration gaps (Form 3). B2.110 is the appropriate first detection step.

**B2.109 recursive operational tests.** Running entity-level operational tests at cell, aspect, and Self scope produces direct evidence of governed or ungoverned state at each level. Entity-level test failures indicate absent entity-level governance regardless of how the deployment-level tests perform. These tests should be run independently for each entity-level scope, not only for the deployment as a whole.

**B2.14/B2.19/B2.24 level-specific inheritance verification.** These procedures verify whether the Paper 2 architectural commitments have been correctly inherited at cell level, aspect level, and Self level respectively. Whether they have ever been run, and whether they pass, is a direct indicator of whether the recursive governance architecture is in place. A deployment that has never run these procedures should be treated as unverified for B1.20 compliance until they are run and pass.

## 6. Remediation

Remediation of Deployment-Level-Only Governance consists of extending the governance architecture to entity scope per B2.102–B2.108, establishing entity-level governance reviews for cells, aspects, and Selves, and verifying the extension through the detection procedures named in §5.

**Step 1: Extend governance affordances to entity scope.** Configure A2.01–A2.04 governance affordances at cell, aspect, and Self scope. This means ensuring that the inspect right, modify right, override right, and rule-authoring right are exercisable at each entity scope — not only at deployment scope. The configuration requirements will vary by implementation, but the operational test is that a human with appropriate access can exercise each affordance at entity scope without deployment-level intermediation as a gate.

**Step 2: Establish entity-level governance reviews.** For each entity-level scope, establish governance review processes that operate at that scope. Directed selection per B1.14 at entity scope requires that governance can identify, inspect, and select among candidate entity states at entity scope; review processes that only operate at deployment scope do not satisfy this requirement.

**Step 3: Run B2.14/B2.19/B2.24 verification for all entities.** Execute the level-specific inheritance verification procedures for all cells, aspects, and Selves in the deployment. Record the results as entity-level governance records per A2.40. These records are what makes entity-level compliance demonstrations possible.

**Step 4: Run B2.110 recursive commitments verification.** Run the recursive commitments verification to confirm that all Paper 1 commitments have been correctly instantiated at all three entity levels. B2.110 is the confirmation step that the recursive governance architecture is complete, not partial.

This is a significant governance architecture investment. Deployments migrating from deployment-level-only to recursive governance should plan the migration as an architectural project, not as a procedural adjustment. The scope of work is proportional to the number of entities requiring entity-level governance extension and to how far from entity-level governance the deployment's current architecture is. For deployments in Form 3 (entity-inspection-absent), the primary work is affordance infrastructure; for deployments in Form 2 (level-selective), the work involves identifying and filling the specific level gaps B2.110 surfaces; for Form 1 (top-level-only), the full entity-level governance architecture must be built from the deployment container down.

## 7. Position in Phase B3 and the anti-pattern series

This note formalizes the twentieth and final primary anti-pattern of Phase B3, completing the one-to-one correspondence between B3.01–B3.21 and B1.01–B1.20. Each B3 primary anti-pattern names the failure mode that results when the corresponding B1 foundational commitment is absent or violated: the anti-pattern series is a complete negative specification of the B1 architecture, mapping every positive commitment to its characteristic failure mode. B1.20's recursive Paper 1 commitments produce, when absent, a deployment that appears governed at its container level while individual entities remain ungoverned — the Deployment-Level-Only Governance anti-pattern this note names.

B3.22–B3.30 will address cross-cutting anti-patterns: failure modes that involve interactions between multiple B1 commitments, failure modes that arise at composition boundaries between Paper 2 architectural elements, and failure modes at the boundary between Paper 2 and the Paper 1 foundation it extends. Those notes complete Phase B3.

## 8. Conclusion

Deployment-Level-Only Governance is the failure mode that results when architects satisfy governance requirements at the deployment container without extending the same governance architecture to the entity scopes Paper 2 specifies. It presents in three recognizable forms — top-level-only governance, level-selective governance, and entity-inspection-absent — each of which violates B1.20's recursive commitment while potentially leaving deployment-level governance intact. It arises from deployment-level compliance culture, governance architecture underinvestment, and a Paper 1 misread that does not recognize Paper 2's recursive extension. Its consequences include ungoverned entities within apparently governed deployments, entity-level compliance gaps, governance affordance failures, and an absent recursive governance architecture. Detection runs through B2.110 and B2.109; remediation requires extending governance infrastructure to entity scope and verifying the extension through B2.14/B2.19/B2.24 and B2.110. The investment is significant, and deployments undertaking it should plan accordingly.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Deployment-Level-Only Governance: The Anti-Pattern That Arises When Paper 1 Governance Applies Only at Deployment Scope Without Recursive Application per B1.20.* May 12, 2026. ORCID: 0009-0004-8065-3235.
