# Bounded Non-Determinism Within the Mediator Role: The Composition of AI-as-Substrate-Mediator and the Determinism Contract in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the emergent architectural property that arises when two of the source paper's foundational commitments — the **AI-as-substrate-mediator role** (§4.1, §4.2) and the **determinism contract** (§4.1, §6.2, §11.3) — compose, namely *bounded non-determinism within the mediator role*: the architectural pattern under which LLM consultation non-determinism is operationally bounded so that it does not propagate to substrate state, even in deployments where LLM consultations dominate cell processing.

## Abstract

The CKS pattern names AI-as-substrate-mediator and the determinism contract as two of its load-bearing architectural commitments. Each is formalized in a separate derivation note; each is independently testable. Neither commitment, on its own, says how the two properties coexist in deployments that consult LLMs at scale: the mediator role specifies where the LLM is allowed to operate but does not bound its inherent non-determinism; the contract specifies what the substrate must guarantee but does not specify how AI participates without breaking the guarantee. Their *composition* yields an architectural property neither parent yields independently — LLM consultation is non-deterministic, but the substrate-state changes that result from AI-mediated cell execution are deterministic, because the rule-mediated transformation that turns LLM output into a substrate write is itself deterministic. This note formalizes that property, *bounded non-determinism within the mediator role*, through four operational components, identifies the architectural decisions the composition forces, distinguishes it from four neighboring concepts, names the anti-patterns that violate it, and provides an operational test with three sharpening properties. The composition is the third member of the A1.04 composition triplet — alongside the mediator-with-retraceability and mediator-with-source-of-truth compositions — that together describes the architectural envelope for AI mediation in CKS.

## 1. Why the composition needs to be formalized as standalone

The mediator-role commitment specifies the role an LLM occupies in a CKS deployment: substrate reads as primary state, substrate writes only under human-authored orchestration rules, no substrate-relevant state outside the substrate, no authority over substrate content, and recorded attribution for any LLM-derived write. The determinism contract specifies what the substrate guarantees: read determinism, cell-behavior determinism modulo LLM output, write addressability, conflict preservation, and substrate-as-source-of-truth. Each commitment is independently derived and independently testable.

Each one, taken alone, leaves a question the other answers — and the question matters operationally. The mediator role does not, by itself, specify how the LLM's inherent non-determinism is bounded; a system can satisfy every property of the role and still permit LLM non-determinism to propagate to substrate writes through unbounded transformations between LLM output and substrate state. The contract names *allowed non-determinism* generically and lists LLM output text as one allowed category, but does not specify how AI participation is architected so that the LLM's non-determinism stays inside the allowed category and does not cross over into substrate state. Two systems can each satisfy the parents individually while differing on whether the composition holds: in one, an LLM's stochastic output flows directly to a substrate write; in the other, the same output is processed by a deterministic rule before any substrate write occurs. The composition is the architectural property that distinguishes the second from the first.

The composition is operationally critical for the deployment population the source paper's framing intends. LLMs are non-deterministic at the model layer — temperature, sampling, vendor model updates, and per-request stochasticity mean the same prompt can produce different outputs across runs. Any deployment that consults LLMs as part of cell processing inherits that non-determinism at the cell-internal layer. Without the composition, the contract's cell-behavior-determinism guarantee fails: substrate writes from AI-mediated cells will vary across runs. With the composition, AI-heavy deployments can be both LLM-mediated and contract-coherent — a posture the surrounding 2024–2026 discourse on "deterministic AI" and "auditable AI" wants without giving up the value LLMs deliver.

The composition also closes the triplet of A1.04 compositions. The mediator role composes with three commitments most directly relevant to its operation: with path retraceability (yielding AI-mediated retraceability), with substrate-as-source-of-truth (yielding AI-mediated authority preservation), and with the determinism contract (yielding bounded non-determinism within the mediator role). Together, the three compositions describe the architectural envelope for AI mediation in CKS — mediated participation is retraceable, authority-preserving, and determinism-preserving simultaneously. This note formalizes the third member.

## 2. The emergent property: four operational components

The composition produces *bounded non-determinism within the mediator role* as an emergent architectural property with four operational components.

**(a) LLM consultation non-determinism is bounded to LLM operations within cells.** When a cell consults an LLM during execution, the LLM's output may differ across invocations — for the same prompt under the same substrate state — because the model itself is non-deterministic. The composition admits this fact without contesting it; LLM output text is the canonical example of allowed non-determinism the contract names. What the composition adds is that this non-determinism is *bounded*: it lives within the LLM's invocation, not in the substrate-state change the cell ultimately produces.

**(b) Cell-behavior determinism holds despite LLM consultation.** The contract guarantees that two cells executing under the same orchestration rule over the same substrate state produce equivalent substrate writes — equivalence judged at the substrate-write layer, not at the LLM-output layer. The composition operationalizes this guarantee for the case where the cell's execution path includes one or more LLM consultations. Cell-behavior determinism is not weakened by LLM participation; it is preserved by routing LLM outputs through the deterministic rule logic that determines what the cell writes back.

**(c) Substrate state changes from AI-mediated cells are deterministic.** A substrate write produced by a cell that consulted an LLM is, at the substrate layer, indistinguishable in its determinism properties from a write produced by a cell that did not. The substrate carries the write, the write is addressable to its writer and rule, and replay of the same substrate state under the same rule produces the same write — even though one of the inputs to the rule's computation, the LLM output, was itself non-deterministic.

**(d) The contract's "allowed non-determinism" is specifically operationalized for LLM consultation.** The contract names allowed non-determinism generically — LLM output text, timestamps, presentation order, cell execution paths — without specifying how each category is architecturally bounded. The composition specifies the binding for the LLM-output-text category: LLM output text is not merely *allowed*; it is structurally prevented from leaving the LLM's invocation envelope, by the requirement that any substrate write derived from LLM output passes through deterministic rule processing before reaching the substrate. The general allowance becomes a specific architectural pattern.

The four components are independent — a system can satisfy a subset and fail others — but composition coherence requires all four. A system that satisfies (a) and (d) but fails (b) is permitting LLM non-determinism inside cells while letting cell behavior diverge across runs, which the contract forbids. A system that satisfies (b) and (c) but fails (a) and (d) is asserting that LLMs are deterministic, which the source paper's mediator-role definition deliberately does not require.

## 3. What the composition forces beyond either commitment alone

The composition forces a small set of architectural decisions that neither commitment requires on its own.

**Rule-mediated transformation must be deterministic.** The orchestration rules under which LLMs write to substrate content must be deterministic transformations from their inputs — substrate state, prior cell context, any LLM output the rule consumes — to the substrate writes they produce. The rule is the structural element that bounds LLM non-determinism; if the rule's processing of LLM output is itself non-deterministic, the boundary disappears. Neither parent, on its own, requires that the rule be deterministic; the composition does.

**LLM outputs enter the rule as inputs, not as substrate writes.** The composition forbids the architectural shortcut in which an LLM's output is recorded directly as a substrate write, with attribution attached but no rule-mediated transformation between them. Attribution alone does not bound non-determinism — a non-deterministic value with attribution is still non-deterministic. The rule must process the LLM output before any substrate write occurs.

**LLM configuration affects LLM output, not substrate state.** Temperature, sampling parameters, model version, and other LLM-side configuration may legitimately vary across deployments and across invocations. The composition requires that variation in this configuration affects the LLM's output but not the substrate-state change that follows from a given substrate state and rule. Two deployments running the same rule over the same substrate state with different LLM temperatures must produce equivalent substrate writes, even though the intermediate LLM output text may differ.

**Cell behavior is a deterministic function of substrate state and rule, with LLM consultation as a bounded non-deterministic input.** The composition lets cells be modelled as deterministic functions whose closures include the substrate state and the rule. LLM consultation enters the closure as a bounded source of variation that the rule absorbs deterministically. This is the operational shape cell-behavior determinism takes when exercised in an AI-mediated deployment.

**LLM consultation non-determinism is documented as an allowed-non-determinism category.** When a cell consults an LLM in the course of executing a rule, the consultation's non-determinism is an instance of the contract's "LLM output text" allowed category. Implementations make this explicit — in the substrate's content, in the rule's specification, or in the deployment's contract documentation — so that downstream auditors do not interpret the non-deterministic intermediate output as a contract violation.

These five decisions follow from the composition; none follows from either parent alone.

## 4. What the composition is NOT

Four neighboring concepts are commonly conflated with bounded non-determinism within the mediator role.

**Not LLM-without-non-determinism.** The composition does not require the LLM to be deterministic. It does not require temperature zero, fixed sampling, or pinned model versions. The LLM remains non-deterministic by design; what the composition does is bound where that non-determinism lands.

**Not determinism-without-AI.** The composition does not require deployments to forgo LLM consultation in order to satisfy the contract. The architecture admits AI participation; the composition is what makes admission compatible with the contract.

**Not deterministic-LLM-output.** The composition does not require LLM outputs themselves to be reproducible across runs. It is unconcerned with whether the same prompt produces the same output text on two invocations; it requires only that the substrate writes the system records be equivalent at the substrate layer, regardless of whether intermediate LLM outputs were.

**Not LLM-output-direct-to-substrate-with-attribution.** Attribution is required by the mediator role for any LLM-derived substrate write, and is necessary for the composition. It is not sufficient. Attaching attribution to a non-deterministic value does not bound the non-determinism; only rule-mediated transformation does.

## 5. Anti-patterns specifically violating the composition

Six anti-patterns recur in systems that approximate the composition without satisfying it.

**LLM-as-terminal-producer.** The canonical composition violation. The LLM produces an output that becomes a substrate write directly, with no rule-mediated transformation between them. Substrate writes vary with whatever the LLM happened to produce on this invocation; components (b) and (c) fail; the mediator role's "writes under orchestration rules" property is satisfied in name only because the rule has degenerated into a pass-through.

**LLM-as-autonomous-agent.** The LLM is delegated decisions whose results become substrate state, with the agent making non-deterministic choices among options without rule-mediated bounding. Substrate state depends on run-specific stochasticity. Components (b) and (c) fail; the mediator role's "no authority over substrate content" property fails alongside.

**LLM-as-source-of-truth.** The LLM is treated as the authoritative answer to *what is the case*, and that authority is exercised non-deterministically. Substrate state on any given run reflects whatever the LLM said this time. The contract's source-of-truth guarantee fails, and component (c) fails alongside.

**Implicit context in cells.** Cell behavior depends on context not represented in substrate state or in the orchestration rule — hidden prompts, ambient model state, prior-session memory the substrate does not carry. Two cells with the same substrate state and rule behave differently because the implicit context differs. Component (b) fails for non-LLM reasons that compound with composition failures whenever the implicit context affects how LLM outputs are interpreted.

**LLM-output-direct-to-substrate.** Even where the deployment is not formally an LLM-as-terminal-producer architecture, any path by which LLM output values reach the substrate without rule-mediated transformation propagates non-determinism. The path may be incidental — a debugging hook, a fallback that writes raw output when a rule fails — and the violation is the same. Components (a) and (c) fail along the path.

**LLM-temperature-affecting-substrate-state.** The deployment's LLM configuration (temperature, sampling, top-k, system prompt seed) affects substrate state, not merely intermediate LLM output. Two operators running the same substrate state and rule under different temperatures produce different substrate writes. Component (c) fails; cell-behavior determinism fails along with it.

In each of these the system may still produce useful results. What it loses is composition coherence; downstream consumers cannot rely on its substrate-state-determinism properties regardless of how often outputs happen to match across runs.

## 6. Why the composition is load-bearing — closing the A1.04 triplet

The composition is what allows AI-mediated deployments to satisfy the determinism contract at all. Without it, the contract's cell-behavior-determinism guarantee fails as soon as cells consult LLMs, which in practice is always. A determinism contract that excludes AI-mediated cells is not the contract the source paper defends; a mediator role that propagates LLM non-determinism is not the role the source paper defines. The composition is the architectural element that makes the two commitments mutually consistent in the deployment population the pattern intends.

The composition also supports reproducibility — the property that arises when the determinism contract composes with path retraceability. Reproducibility depends on substrate-state changes being deterministic functions of substrate state and rule; AI-mediated changes are reproducible only when their non-determinism is bounded so that replay of recorded provenance produces the same substrate write. The bounding is what this composition supplies; without it, AI-mediated retraceability decays from reproducibility into mere logging.

The composition closes the A1.04 triplet alongside the mediator-with-retraceability composition (which gives AI-mediated provenance) and the mediator-with-source-of-truth composition (which gives AI-mediated authority preservation). The three together describe what AI mediation in CKS is: retraceable to its writer and rule, authority-preserving in that the substrate remains the source of truth, and determinism-preserving in that LLM non-determinism stays inside the mediator role rather than crossing into substrate state. Each is independently formalized; the three together form the architectural envelope for the mediator role's interaction with the contract-bearing parts of the substrate.

## 7. Operational test

A system instantiates the composition of AI-as-substrate-mediator with the determinism contract if and only if all of the following are true at all times during the substrate's existence, for every cell in the system that consults an LLM as part of its execution:

1. **LLM-non-determinism-bounded.** LLM consultations within the cell may produce different output text across invocations under the same substrate state and rule (verifying that LLM non-determinism is admitted as an allowed category and not contested), and the variation is contained at the LLM-invocation layer.

2. **Substrate-state-determinism.** Two executions of the cell under the same orchestration rule over the same substrate state produce equivalent substrate writes, equivalence judged at the substrate-write layer, regardless of whether the intermediate LLM outputs were equivalent.

3. **Rule-mediated-transformation.** The orchestration rule under which the cell writes to substrate state processes LLM output deterministically: same substrate state, same rule, same LLM output value yields the same substrate write — and the path from LLM output to substrate write passes through rule logic rather than through direct recording.

A system that fails any of (1)–(3) may be a useful AI-mediated system, and may satisfy each of the parent commitments individually, but is not composition-coherent in the sense the source paper's two parents together require. **Stated as one sentence: the composition holds when LLMs are non-deterministic, the rule's processing of LLM output is deterministic, and substrate-state changes are determined by substrate state and rule rather than by LLM run-specific stochasticity.**

The three sharpening properties are independent — a system can satisfy any subset and fail others. Composition coherence requires all three together.

---

The composition formalized here is the third A1.04-anchored composition pair in this series. Subsequent Phase A4 notes will formalize the remaining pairs across the foundational commitments — including additional pairs anchored on the determinism contract, on the substrate-cell boundary, and on the linear-cost commitment — each one articulating an emergent architectural property that arises only at the seam between two parents. The strategic reading is that the architectural surface CKS defends is mostly composed of these seams: each commitment is independently derivable, but the deployment-relevant properties emerge where the commitments meet.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Bounded Non-Determinism Within the Mediator Role: The Composition of AI-as-Substrate-Mediator and the Determinism Contract in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
