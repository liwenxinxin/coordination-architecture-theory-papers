# Expression Mechanism Bypass — The Anti-Pattern That Arises When the Governed Harness-Substrate Pathway per B1.07 Is Circumvented, Recognizable as Direct Cell DNA Modification Bypassing Expression Configuration, Expression-Configuration-Absent Design, and Carry-Strategy Omission Breaking Cross-Deployment Portability

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

The Coordination Knowledge Substrate (CKS) pattern, as extended in Paper 2, establishes the expression mechanism as the governed pathway by which Self-level and aspect-level DNA activation reaches individual cell behavior. The harness substrate per B2.30 is the expression governor; the carry-strategy per B2.32 specifies whether a cell carries the full Self DNA with selective expression or a partial slice. Together these constitute the architectural downward channel through which Self-level DNA changes propagate to cell behavior without requiring direct individual cell modification. Expression Mechanism Bypass is the anti-pattern that arises when this governed pathway is circumvented. It manifests in three recognizable forms: direct cell DNA modification that bypasses expression configuration, deployment of cells without harness substrate configuration so the expression channel does not exist, and carry-strategy omission that breaks cross-deployment portability. The consequences are architecturally compounding: downward vertical evolution per B2.81 cannot function through the governed channel, every Self-level architectural change requires cell-by-cell modification whose burden scales with cell count, cross-deployment composition per A2.47 is unpredictable, and A1.05 tool-agnosticism at cell scope is undermined. Detection proceeds through B2.30 harness substrate presence, B2.32 carry-strategy specification, B2.34 expression mechanism verification, and a vertical evolution propagation test. Remediation establishes expression configuration through directed selection per B1.14 and authors carry-strategy for each cell as part of its birth specification per B2.40.

---

## 1. The Commitment This Note Formalizes

B1.07 establishes the expression mechanism as the governed pathway for Self-level and aspect-level DNA activation to reach cell behavior. Expression is not an incidental implementation convenience; it is the architectural channel through which downward vertical influence — from Self DNA to cell DNA elements — operates under governance. B2.30 specifies the harness substrate as the expression governor: each cell carries a harness substrate, itself human-governed, fully inspectable, modifiable, and overridable, that selects which DNA sub-substrates are active for current cell activity. B2.31 specifies the DNA activation pattern — cells can carry full Self DNA with selective expression, or carry partial slices where storage and cognitive load matter more. B2.32 specifies the carry-strategy: for each cell, the carry-strategy names which DNA-layer content from the Self or aspect the cell holds and how that content activates under Self-level configuration. B2.34 provides the expression mechanism inheritance verification — a check that tests whether the governed pathway from Self DNA to cell behavior functions end to end.

The expression mechanism is what makes Self-level DNA changes propagate downward to cell behavior through a governed channel rather than requiring manual intervention at every cell. The architectural cost is paid once, at expression configuration time, and amortizes across every future Self-level evolution cycle that propagates through that channel. The carry-strategy is what makes cells portable across deployments: a cell whose DNA-dependency on Self-level activation is explicitly specified can be re-deployed in a new context and composed correctly under governed conditions; a cell without a specified carry-strategy cannot be governed in new contexts because its behavior under different Self configurations is unknown.

B3.08 formalizes Expression Mechanism Bypass as the anti-pattern that arises when this governed pathway is circumvented.

---

## 2. Pattern Name and Commitment Violated

**Pattern name:** Expression Mechanism Bypass

**Commitment violated:** B1.07 — the expression mechanism as the governed pathway for Self-level DNA activation to reach cell behavior, further specified by B2.30 (harness substrate as expression governor), B2.31 (DNA activation patterns), B2.32 (carry-strategy specification), and B2.34 (expression mechanism inheritance verification).

---

## 3. Recognizable Form

Expression Mechanism Bypass takes three distinct sub-forms. Each represents a different mode of circumventing or omitting the governed harness-substrate pathway.

### Form 1 — Direct Cell Modification Bypass

In this form, the expression mechanism exists in architectural intent but is bypassed in practice. When a Self-level DNA change should propagate to cell behavior through harness substrate expression configuration per B2.30, the change is instead applied by directly modifying individual cell DNA per B2.25. The governed downward channel is not absent; it is simply not used.

Recognition signals are specific. Self DNA changes that should propagate to cells via expression configuration do not propagate through the harness substrate channel. Cell DNA is modified individually for each cell rather than through Self-level expression configuration. Engineers who want to update cell behavior across the Self perform per-cell edits rather than a single Self-level expression reconfiguration. Downward vertical evolution per B2.81 does not function through the governed channel even when that channel was intended to exist. B2.34 expression mechanism verification, if applied, finds that Self-level DNA changes do not reach cells through expression configuration.

The characteristic sign of Form 1 is an editorial reflex: when a change to cell behavior is needed, the architect opens the cell and edits its DNA directly, rather than asking whether a Self-level expression configuration change would propagate the intended behavior through the governed pathway. Over time this reflex accumulates. The expression mechanism falls into disuse, cell DNA diverges from anything the harness substrate would select, and the governed downward channel becomes vestigial without the decision ever having been made explicitly.

### Form 2 — Expression Configuration Absent

In this form, the governed pathway does not exist. Cells are deployed without harness substrate configuration per B2.30. No carry-strategy per B2.32 is specified. The expression mechanism channel from Self or aspect DNA to cell DNA elements was never established.

Recognition signals: the B2.30 harness substrate is absent from the cell DNA specification. B2.32 carry-strategy is not present in the birth specification per B2.40. B2.34 expression mechanism inheritance verification finds no harness configuration to verify. Cell DNA is fixed at deployment time and does not respond to Self-level DNA configuration changes, because no governed selection mechanism connects the two.

Form 2 is the design-time omission form. The architect never established the expression channel. Each cell carries its behavior as a closed specification: orchestration rules, schemas, conflict-handling logic are authored into the cell at birth as terminal configuration, not as expression-configurable content subject to Self-level activation. The cell executes tasks and produces outputs, but it cannot participate in governed downward evolution from the Self level. It is architecturally isolated from the Self's DNA activation structure.

### Form 3 — Carry-Strategy Omission

In this form, the harness substrate may be nominally present but the carry-strategy per B2.32 is implicit or absent. The cell was deployed without specifying whether it carries full Self DNA with selective expression — appropriate for lineage and reconstitution contexts such as regulated work — or a partial DNA slice appropriate for storage and cognitive-load-constrained deployments.

Recognition signals: B2.32 carry-strategy specification is absent from the cell's birth records per B2.40. Cells cannot be ported across deployments because their DNA dependency on Self-level activation is unspecified. Cross-deployment composition per A2.47 is governed procedurally — human authority is exercised over mating and birth operations — but the resulting cell behavior under a new Self's DNA configuration is unpredictable, because the carry-strategy was never specified and cannot be recovered from the cell's current content alone.

Form 3 is the portability form. It is recognizable in deployments where cells were built for one context and reuse in another is attempted. The cell arrives in the new deployment with an implicit carry relationship to its original Self. When the new Self's DNA activates, it activates against a cell whose DNA-carriage structure was never explicitly designed for portability. Whether the cell responds correctly, partially, or incorrectly depends on coincidences of structural alignment rather than on a governed specification.

---

## 4. Emergence Conditions

**Direct Control Preference.** The most common origin of Forms 1 and 2 is a preference for direct cell-level control over architectural pathway design. Establishing the expression mechanism per B2.30 requires upfront investment: the harness substrate must be configured, DNA activation patterns per B2.31 must be specified, and carry-strategy per B2.32 must be authored for each cell. This investment is architectural — it pays forward into every future Self-level evolution cycle that uses the governed channel — but it is invisible at the moment of first cell deployment. An architect focused on getting a cell working now, in this deployment, for this purpose, has every practical incentive to author the cell's DNA as a complete closed specification and move on. The governed downward pathway is a future-evolution investment; direct cell modification is a present-deployment convenience.

This preference is reinforced when the system is small. When a Self contains few cells, cell-by-cell modification is manageable, and the architect does not experience the governance burden that scales with cell count because the count is not yet large enough to make the burden felt. The bypass pattern is established before the cost becomes apparent; by the time it does, it has accumulated across many cell deployments and is difficult to remediate without architectural investment.

**Portability Neglect.** Form 3 emerges from treating the carry-strategy as an implementation detail rather than a governance requirement. Architects who build cells for a single deployment do not naturally plan for how the cell would behave under a different Self's DNA configuration. The carry-strategy feels like over-engineering for a cell that is not, at the time of birth, intended to travel anywhere. Cross-deployment composition per A2.47 is not a present concern.

Portability neglect is compounded by the absence of a visible failure at initial deployment. A cell without a specified carry-strategy functions correctly in the deployment it was built for. The failure only manifests when reuse in a different context is attempted — at which point the original birth specification may be incomplete, the original architect may not be available to reconstruct the carry-strategy, and the cell's DNA dependency on its original Self's configuration may be difficult to infer from current cell content alone.

---

## 5. Operational Consequences

**Vertical Evolution Blocked.** B1.14 establishes horizontal and vertical evolution as distinct mechanisms: horizontal evolution changes DNA content within existing structure; vertical evolution reorganizes structure across levels, with downward vertical evolution per B2.81 as the mechanism by which Self-level DNA changes propagate to cell behavior through the expression mechanism. When the expression mechanism is bypassed or absent, this propagation channel does not function. Self-level DNA changes do not reach cells through the governed channel. Vertical evolution — the architectural capability that allows a Self to evolve its behavior at Self level and have that evolution carry through simultaneously to constituent cells — is blocked.

This consequence is architecturally load-bearing, not merely inconvenient. Vertical evolution is what makes a CKS Self capable of coherent behavioral evolution across all its cells through a single Self-level governance action. Without the expression mechanism, every cell must be modified individually to receive any change the Self-level architecture intends to propagate. The governed downward channel becomes a dead letter.

**Cell-by-Cell Governance Burden.** Without the expression mechanism, every Self-level architectural change that should affect cell behavior requires individual cell DNA modification. The governance burden scales with cell count: a Self with ten cells requires ten modifications per Self-level change; a Self with a hundred requires a hundred. The architecture that should make Self-level evolution a single governed action becomes a per-cell administrative operation whose cost grows with the size of the deployment.

This is the anti-pattern's compounding failure. The direct-control preference that generates Forms 1 and 2 appears inexpensive at small scale because the cell count is small and cell-by-cell modification is manageable. As the Self grows, the omission becomes a structural liability. The architect who bypassed the expression mechanism to save configuration work at birth specification time pays that cost forward, repeatedly, at every future evolution cycle.

**Carry-Strategy Ambiguity.** Without a specified carry-strategy per B2.32, cells cannot be ported across deployments reliably. Cross-deployment composition per A2.47 is procedurally governed — human authority is exercised over mating and birth operations — but the cell's behavior in the new deployment depends on an unspecified DNA-dependency relationship with the new Self. Governance cannot guarantee behavioral correctness when the expression configuration is absent or unspecified. The cell may function as intended in the new context, or it may carry behavior appropriate to its original Self but misaligned with the new one, with no governed specification available to diagnose the discrepancy.

**Tool-Agnosticism Failure.** A1.05 establishes tool-agnosticism as requiring, at cell scope, that a cell remain portable across different LLM infrastructure — that it carry its DNA independently of any specific LLM configuration. When the expression mechanism is absent and no carry-strategy is specified, a cell cannot carry its DNA independently across LLM changes, because the relationship between the cell's DNA content and the Self's DNA activation structure is unspecified. A new LLM configuration at the Self level may activate DNA sub-substrates in a different pattern, and the cell — lacking a governed harness substrate and carry-strategy — has no specified behavior under that different activation pattern. The tool-agnosticism property at cell scope is undermined even when the substrate is technically host-agnostic in the sense A1.05 requires at substrate level.

---

## 6. Detection

Four checks identify Expression Mechanism Bypass in a CKS deployment.

**B2.30 Harness Substrate Check.** Is a harness substrate configuration present in the cell's DNA specification? The check is binary: the harness substrate either exists, is human-governed, and is inspectable in the cell's substrate content, or it does not. A cell deployed without harness substrate configuration per B2.30 exhibits Form 2 by definition. A cell whose harness substrate nominally exists but is not used by the Self-level expression activation process exhibits Form 1.

**B2.32 Carry-Strategy Specification.** Is a carry-strategy authored for the cell and present in the cell's birth specification per B2.40? The carry-strategy must name which DNA-layer content the cell holds from its originating Self or aspect, and under what activation conditions that content applies. A cell without a specified carry-strategy cannot be verified for portability, and the absence is detectable at birth record inspection. Systems in which carry-strategy specification is not a required element of the birth specification process are structurally prone to Form 3 at scale.

**B2.34 Expression Mechanism Verification.** The expression mechanism inheritance verification tests whether the governed pathway from Self DNA to cell behavior functions as specified. Verification applies the full pathway: a Self-level DNA configuration is modified; the expected propagation through harness substrate activation is named; the cell's resulting behavior is checked for conformance. A system in which B2.34 verification is never applied has not confirmed whether the expression mechanism is functioning — making Form 1 invisible until the cell count grows large enough to force the issue through governance burden.

**Vertical Evolution Test.** A targeted operational test: make a Self-level DNA change that should propagate to cell behavior through expression configuration. Does the change reach the cell through the governed harness substrate pathway, or does it require separate cell-by-cell modification to take effect? If the latter, the expression mechanism is bypassed in practice regardless of its nominal architectural presence. The test is the direct operational evidence of Form 1; it can be applied at any point in a deployment's lifecycle without requiring architectural reconstruction.

---

## 7. Remediation

**Establish harness substrate configuration per B2.30 through directed selection per B1.14.** For cells exhibiting Form 2, remediation is architectural: introduce the harness substrate as governed expression governor. This is a DNA evolution operation — a directed selection per B1.14 — that refactors the cell's DNA specification to include the harness substrate and its activation configuration. The refactoring should be governed under the authority architecture appropriate to DNA evolution, with the change authored at Self or aspect level and the resulting harness substrate configuration included in the cell's updated DNA specification.

**Specify carry-strategy per B2.32 for each cell.** For cells exhibiting Form 3, remediation is specification: author the carry-strategy as part of the cell's governance record. For existing cells whose carry-strategy was never specified, the carry-strategy should be reconstructed from the cell's current DNA content in consultation with the original deployment context, and authored as a retrospective birth specification amendment per B2.40. Cells for which the carry-strategy cannot be reconstructed reliably should be treated as unportable pending re-specification, with cross-deployment composition per A2.47 for those cells deferred until specification is complete.

**Run B2.34 expression mechanism verification.** After introducing or restoring the harness substrate configuration, run B2.34 verification to confirm the governed pathway functions end to end. Verification should be incorporated into the birth specification acceptance process going forward so that expression configuration absence does not reach deployment undetected.

**Migrate existing cell-by-cell modifications to Self-level expression configuration where appropriate.** For cells exhibiting Form 1, remediation is migration: identify cell DNA modifications applied directly rather than through expression configuration, assess whether they represent Self-level architectural intent that should propagate through the governed pathway, and refactor them into Self-level expression configuration where that intent holds. Modifications that represent genuinely cell-specific customization — not Self-level intent — may remain at cell scope. The migration forces the distinction to be made explicitly and recorded as governed specification, rather than left as implicit per-cell editing history.

**Author carry-strategy for each cell as part of governance of its birth specification per B2.40.** Going forward, carry-strategy specification should be a required element of every cell birth specification. The birth specification per B2.40 is the governed origination record; carry-strategy belongs in that record alongside the cell's DNA content, orchestration rules, and provenance metadata. Making carry-strategy a required field prevents Form 3 from accumulating silently as new cells are deployed, regardless of whether cross-deployment reuse is anticipated at the time of birth.

---

## 8. Conclusion

Expression Mechanism Bypass is recognizable because it appears inexpensive at small scale and at the moment of first deployment. The direct-control preference is natural; the carry-strategy omission is invisible when the cell is not being ported; the absence of harness substrate configuration does not prevent the cell from functioning in its initial deployment. The anti-pattern's cost is paid later — when the Self grows to a scale where cell-by-cell modification becomes burdensome, when a cell is ported to a new deployment and its behavior becomes unpredictable, or when a Self-level DNA evolution cycle fails to propagate through cells that were never given the governed downward channel.

B1.07's architectural contribution is precisely to prevent this future cost by requiring the governed pathway to be established at birth. The expression mechanism is not a feature to be added when the Self becomes large enough to justify it; it is the architectural channel through which a CKS Self's downward vertical influence operates, and through which the Self's evolutionary coherence at the level of individual cells is maintained. Bypassing it — in any of its three forms — is not a shortcut that can be corrected later without architectural refactoring. It is a design omission whose consequences compound with the Self's growth and with the reuse demands that cross-deployment composition eventually imposes.

---

*This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).*
