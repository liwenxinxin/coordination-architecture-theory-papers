# Aspect-Level Governance Inherits All Six Paper 1 Commitments

**Derivation Note C1.06 — CKS Cross-Derivation Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

---

## Abstract

Paper 2 of the Coordination Knowledge Substrate (CKS) series introduces the *aspect* as an intermediate structural level — a composition of cells serving a particular coordination purpose within a Self. Paper 2 Claim 6 (formalized in derivation notes B0.06 and B1.20) commits to recursive applicability: all Paper 1 architectural commitments apply at every structural level Paper 2 introduces. This note formalizes what that commitment means concretely at aspect scope. Each of Paper 1's six architectural commitments — hybrid architecture with governance boundary, conflict preservation as first-class state, human-governed authority (three rights), AI-as-substrate-mediator (five properties), tool-agnosticism (three minimal requirements), and path retraceability (six provenance fields) — holds at aspect scope with the same definitions, the same tests, and the same violation conditions that apply at cell scope. A governance failure at aspect scope is not a novel failure mode; it is a Paper 1 commitment violation instantiated at a higher structural level. This note states the inheritance edge, specifies what each commitment means at aspect scope, identifies what is genuinely new at aspect scope beyond Paper 1's coverage, states the prior-art significance of the inheritance, and provides an operational test for each commitment at aspect scope. Note C1.07 follows with the parallel treatment for Self scope.

---

## 1. The Inheritance Edge

Paper 1 established its six architectural commitments at cell and substrate scope. The commitments define governance requirements for any CKS deployment unit: a cell is a bounded unit with a persistent substrate carrying coordination knowledge under human authority, with an LLM operating as mediator over that substrate rather than as its owner. Paper 1 did not address whether these commitments apply at structural levels above the cell. The concept of an *aspect* — a governed coordination arrangement of multiple cells serving a shared purpose — does not appear in Paper 1.

Paper 2 introduces the aspect as an intermediate structural level between the cell and the Self. With this introduction comes an explicit architectural commitment: Paper 2 Claim 6, formalized in derivation notes B0.06 and B1.20, asserts recursive applicability — all six Paper 1 commitments hold at every structural level the Paper 2 architecture introduces. Paper 2 §5.6 states this directly: "Claim 2 inherits all six Paper 1 architectural commitments at every level of the three-level structure."

The inheritance edge this note formalizes is the subset of that commitment at aspect scope:

> **C1.06:** The set of governance commitments required at aspect scope is a strict extension (⊃) of Paper 1's six architectural commitments. Every Paper 1 commitment is satisfied at aspect scope with the same definitions, tests, and violation conditions. Paper 2 adds aspect-specific governance requirements on top; it does not replace or weaken the Paper 1 base.

The mechanism is recursive applicability (B0.06/B1.20), not a separate design decision for multi-cell coordination. The aspect does not get a bespoke governance regime; it inherits the regime Paper 1 established and adds what the aspect's coordination role requires.

---

## 2. Each Paper 1 Commitment at Aspect Scope

### 2.1 Hybrid Architecture with Governance Boundary

**At cell scope:** The cell combines a persistent human-governed substrate (reasoning layer) with an LLM (instinct layer). The governance boundary separates what humans own — substrate content, orchestration rules — from what the LLM does under those rules. The LLM does not own the substrate.

**At aspect scope:** The aspect has its own substrate carrying DNA-layer content (coordination rules, membership rules, purpose statement, content-domain policy) and Action-layer content (recorded aspect-level task instances). Any LLM operating at aspect scope — for example, performing aspect-level synthesis across member cells' outputs — operates over this substrate rather than replacing it. The governance boundary at aspect scope separates human-owned aspect substrate content from LLM-mediated operations over it. The aspect is not a middleware layer or a routing mechanism; it is a governed structural unit with its own substrate under the same hybrid architectural commitment.

**Violation at aspect scope:** An aspect implementation in which the synthesis or coordination logic is held entirely within an LLM's inference, with no persistent aspect-level substrate carrying human-accessible coordination rules, violates Paper 1's hybrid commitment at aspect scope.

### 2.2 Conflict Preservation as First-Class State

**At cell scope:** Contradictions arising within a cell's substrate are not silently collapsed, averaged, or resolved without record. They are preserved as first-class substrate objects — addressable, inspectable, and subject to human-governed resolution logic.

**At aspect scope:** Conflicts arising at aspect scope are similarly first-class substrate objects. Two categories of aspect-scope conflict are architecturally relevant: (a) conflicts between member cells' outputs when those outputs disagree on substance, and (b) conflicts within the aspect's own coordination rules when rules pull in incompatible directions. Both must be registered in the aspect substrate as addressable objects. An aspect-level conflict that is silently resolved — collapsed into a synthetic output without a conflict record — violates Paper 1 Claim 2 at aspect scope, not a novel aspect-specific rule.

**Violation at aspect scope:** An aspect implementation that merges conflicting cell outputs into a single synthesized result with no persistent conflict record violates conflict preservation at aspect scope.

### 2.3 Human-Governed Authority (Three Rights)

**At cell scope:** Humans hold three rights at all times: the right to inspect any substrate content and orchestration rule; the right to modify any substrate content and orchestration rule; the right to override any LLM-produced output that touches substrate content or orchestration rules. These rights apply to scope objects — substrate content and orchestration rules — as properties of the system's design, not as procedural promises.

**At aspect scope:** The three rights apply to the aspect's DNA-layer content and Action-layer content. Humans can inspect, modify, and override: aspect coordination rules (how member cells' outputs are combined and routed), aspect membership rules (which cells participate in the aspect under which roles), the aspect's purpose statement, and content-domain policy at aspect scope. Authority over this content does not devolve to the LLM or to automated aspect-management logic. The actor-neutrality from Paper 1 §3.3 holds at aspect scope: human-governed does not mean human-authored; what humans own at aspect scope is authority over the aspect's substrate content, not the labor of writing every coordination rule.

**Violation at aspect scope:** An aspect whose coordination rules or membership rules are not accessible or modifiable by the humans governing the system — because they are embedded in opaque middleware, held inside LLM inference, or locked behind vendor access controls — violates the three rights at aspect scope.

### 2.4 AI-as-Substrate-Mediator (Five Properties)

**At cell scope:** An LLM operating within a cell acts as substrate mediator: it reads from and writes to the cell's substrate under orchestration rules, does not own the substrate, does not hold authoritative state outside the substrate, does not modify orchestration rules, and its outputs are subject to human override.

**At aspect scope:** Any LLM operating at aspect scope — performing aspect-level synthesis, coordinating outputs across member cells, generating aspect-level Action-layer records — is subject to the same five mediator properties. It reads from and writes to the aspect substrate under aspect-level orchestration rules. It does not own the aspect substrate. It does not hold the aspect's coordination state in its own memory as authoritative shadow state. It does not autonomously rewrite aspect-level DNA content. Its outputs at aspect scope are subject to human override under the three rights in §2.3.

**Violation at aspect scope:** An aspect-level LLM that accumulates coordination history in its own context rather than recording it to the aspect substrate, or that modifies aspect coordination rules without human authorization, violates the mediator commitment at aspect scope.

### 2.5 Tool-Agnosticism (Three Minimal Requirements)

**At cell scope:** The cell's substrate host must satisfy three minimal requirements: it must support persistent structured state, it must support human read and write access to that state, and it must support LLM access to that state. Beyond these three requirements, the choice of host tool is a deployment decision.

**At aspect scope:** The aspect's substrate — the host carrying the aspect's DNA-layer and Action-layer content — must satisfy the same three requirements. The choice of host tool for aspect-level substrate is likewise a deployment decision. An architecture that requires a specific coordination platform, orchestration engine, or vendor-provided multi-agent framework to operate the aspect's substrate violates tool-agnosticism at aspect scope.

**Violation at aspect scope:** An aspect implementation that can only function when run inside a specific proprietary orchestration platform — with aspect coordination state held in that platform's internal storage rather than in a substrate satisfying the three minimal requirements — violates tool-agnosticism at aspect scope.

### 2.6 Path Retraceability (Six Provenance Fields)

**At cell scope:** Governance events recorded in the substrate carry six provenance metadata fields: who acted, what action was taken, what substrate content was affected, when the action occurred, why (the rationale), and from what prior state the action departed. This makes cell-level governance history independently verifiable.

**At aspect scope:** Governance events at aspect scope — creation of the aspect, modification of coordination rules, membership changes, conflict registrations and resolutions, lifecycle transitions — carry the same six provenance fields. The aspect's lineage chain is accessible through its substrate. An observer can independently trace how the aspect's coordination rules reached their current form, which cells joined or left and when, and which conflicts were registered and resolved under whose authority. This traceability is not a reporting feature; it is an architectural property of the aspect substrate.

**Violation at aspect scope:** An aspect whose governance history is not recorded to its substrate — with coordination rule changes applied silently, membership changes not logged with rationale, or conflict resolutions not linked to prior conflict records — violates path retraceability at aspect scope.

---

## 3. What Is Genuinely New at Aspect Scope

The six commitments above are inherited without modification. Paper 2 adds governance requirements at aspect scope that Paper 1 did not establish, because Paper 1 had no aspect concept. Four categories of new content are architecturally specific to aspect scope:

**Aspect-specific governance objects.** The aspect's DNA layer carries objects Paper 1 does not define at any level: coordination rules specifying how member cells' outputs are combined and routed, membership rules governing which cells participate under which relational roles, a purpose statement identifying the coordination purpose the aspect serves, and content-domain policy applicable at aspect scope. These are new substrate objects, not extensions of cell-level orchestration rules.

**Aspect lifecycle as governed events.** Paper 2 Claim 3 establishes lifecycle primitives (birth, mating, death) at every structural level. At aspect scope, lifecycle events — an aspect coming into existence through cell composition, an aspect merging with another aspect, an aspect dissolving — are governed substrate events carrying the six provenance fields (§2.6). Paper 1 established no lifecycle primitives; the aspect lifecycle is a Paper 2 contribution that sits on top of the inherited Paper 1 commitment to path retraceability.

**Cross-cell conflict handling at aspect scope.** When member cells produce conflicting outputs, conflict preservation (§2.2) requires that the conflict be registered as a first-class substrate object at aspect scope. What happens next — how the conflict is presented to human governors, what resolution logic applies, whether it escalates — is governed by aspect-level orchestration rules. Paper 1's two-level conflict-handling structure (substrate-level preservation, cell-level resolution by orchestration rules) extends naturally to aspect scope, as Paper 2 §5.6 notes explicitly. The cross-cell conflict-handling machinery is a Paper 2 addition; the first-class-object requirement is Paper 1 inheritance.

**Expression mechanism at aspect scope.** Paper 2 introduces expression as the mechanism by which governance selects which DNA-layer substrates activate per cell goal within a coordination context. At aspect scope, expression governs which aspects of member cells' rule sets apply within the aspect's coordination frame. Expression is a Paper 2 concept with no Paper 1 antecedent; it operates over the substrate content Paper 1's commitments govern.

---

## 4. Prior-Art Significance

Formalizing the C1.06 inheritance edge forecloses three adversarial claims:

**Claim (a): Aspect-scope governance is architecturally novel relative to Paper 1.** This claim fails because the inheritance edge is explicit in Paper 2 Claim 6. Aspect-scope governance is a strict extension of Paper 1's commitments, not a departure from them. The six commitments hold at aspect scope with unchanged definitions; anyone implementing aspect-scope governance under those definitions is necessarily instantiating Paper 1's commitments.

**Claim (b): Paper 1's commitments do not extend to multi-cell coordination layers.** This claim fails because Paper 2 §5.6 states the extension explicitly: "Claim 2 inherits all six Paper 1 architectural commitments at every level of the three-level structure." The extension is not implicit or derived by inference; it is an explicit architectural commitment in Paper 2.

**Claim (c): Novel governance requirements are needed for multi-cell coordination layers beyond what Paper 1 established.** This claim misidentifies the relationship between inheritance and extension. The aspect-specific governance objects and lifecycle primitives (§3 above) are genuinely new at aspect scope — but they sit on top of Paper 1's inherited base, not in place of it. The correct characterization is: aspect scope adds new governance objects; it does not introduce replacement governance commitments for the six Paper 1 requirements.

Together, these three foreclosures mean that an implementer producing aspect-scope governance in a CKS-conforming system cannot claim that the governance requirements applicable at aspect scope were not publicly established before their implementation.

---

## 5. Operational Test: Each Commitment at Aspect Scope

An independent observer can verify whether each commitment holds at aspect scope using the following tests. Each test is distinct from the corresponding cell-scope test in that it targets the aspect's own substrate and governance objects rather than any member cell's.

| Commitment | Aspect-scope test |
|---|---|
| Hybrid architecture | Is there a persistent aspect-level substrate distinct from any member cell's substrate, carrying aspect DNA-layer and Action-layer content? Is the LLM operating at aspect scope reading from and writing to that substrate? |
| Conflict preservation | When two member cells' outputs conflict, is a conflict record present in the aspect substrate as an addressable object before any synthesis output is produced? |
| Human-governed (three rights) | Can a human with system access inspect the aspect's coordination rules and membership rules directly? Can they modify those rules without requiring LLM or middleware intermediation? Can they override any aspect-level LLM output before it becomes substrate-authoritative? |
| AI-as-mediator | Does the aspect-level LLM hold authoritative coordination state outside the aspect substrate? Can it modify aspect-level DNA content without human authorization? |
| Tool-agnosticism | Does the aspect substrate satisfy the three minimal requirements (persistent state, human R/W, LLM access) independent of any specific orchestration platform or vendor? |
| Path retraceability | Do aspect-level governance events — rule changes, membership changes, conflict registrations — carry six provenance fields in the aspect substrate? Can the aspect's governance history be reconstructed from its substrate without access to external logs? |

A system in which all six tests pass at aspect scope instantiates the C1.06 inheritance: aspect-level governance commitments include and extend Paper 1's commitments.

---

## 6. Relationship to C1.07

This note covers aspect scope — the intermediate structural level Paper 2 introduces between the cell and the Self. Note C1.07 covers Self scope — the enterprise-level structural unit Paper 2's Claim 6 also commits to under recursive applicability. Together, C1.06 and C1.07 close the recursive applicability inheritance for both new structural levels Paper 2 introduces. The argument structure in C1.07 is parallel to the one here: each of Paper 1's six commitments holds at Self scope with the same definitions and violation conditions, and Self scope adds its own governance objects on top of the inherited base.

---

## 7. Summary

Paper 2 Claim 6 (B0.06/B1.20) commits to recursive applicability of all Paper 1 architectural commitments at every structural level the Paper 2 architecture introduces. At aspect scope, this means:

1. Each of Paper 1's six commitments holds with unchanged definitions, tests, and violation conditions.
2. A governance failure at aspect scope — a conflict not preserved as first-class, a coordination rule outside human authority, an LLM holding authoritative aspect state in its own context — is a Paper 1 commitment violation, not a novel failure mode.
3. Aspect-specific governance objects (coordination rules, membership rules, purpose statement, content-domain policy), lifecycle primitives, cross-cell conflict handling, and the expression mechanism are genuine Paper 2 additions that sit on top of the inherited Paper 1 base.
4. Anyone implementing aspect-scope governance in a CKS-conforming system is necessarily instantiating Paper 1's six commitments at that scope; no claim of novelty relative to those commitments survives the C1.06 inheritance edge.

---

*Derivation note series: CKS Cross-Derivation Series (Series C). This note is #435 in the CKS derivation note series. Source papers: Paper 1 — Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems (Li, April 2026); Paper 2 — Coordination Knowledge Substrate: A Compositional Architecture for Human-Governed Multi-Level AI Systems (Li, April 2026). Prior cross-derivation notes: C1.01 (#430), C1.02 (#431), C1.03 (#432), C1.04 (#433), C1.05 (#434). Next: C1.07 (#436) — Self-level governance inherits all six Paper 1 commitments.*
