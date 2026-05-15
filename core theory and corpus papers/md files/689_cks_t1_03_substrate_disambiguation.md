# Disambiguating "Substrate" Across the Trilogy: Six Distinct Architectural Objects Each With Different Layer, Governance, and Scope Properties

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026), and "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026).

It does not introduce new axioms. Its sole contribution is to identify and precisely distinguish the six distinct architectural objects the trilogy names using the word "substrate," so that practitioners reading across all three papers can resolve references correctly and adversarial readings cannot exploit unqualified uses of the term.

---

## Abstract

The word "substrate" appears throughout the CKS trilogy but is not a single architectural object. Across the three papers, it refers to at least six distinct things: the governance substrate introduced in Paper 1 as the cell-scope coordination medium; the governance substrate at each of Paper 2's three tiers (cell, aspect, Self); the DNA layer and action layer as the two named substrate layers within every cell; the harness substrate as the instinct-layer specification that governs how the LLM connects to the governance substrate; the home substrate as each Self's full Paper 2 architecture; and the shared substrate as the temporary inter-Self coordination space introduced in Paper 3. These six objects occupy different architectural layers, stand in different governance relationships, and span different scopes. The most critical disambiguation separates the harness substrate (instinct layer, not governed through substrate content) from the governance substrate (reasoning layer, governed through substrate content); conflating them mischaracterizes the architecture's foundational instinct/reasoning separation. This note formalizes all six objects, presents a disambiguation table, and establishes prior-art coverage for each.

---

## 1. Why "substrate" requires explicit disambiguation

The CKS trilogy reuses a single word across three papers whose architectural scope expands from cell to Self to inter-Self. Each paper introduces new objects whose names inherit the word "substrate" because they share the same foundational commitment: a human-governed coordination medium whose content is authoritative and accessible outside the LLM. But sharing a word does not mean sharing architectural identity. Each of the six objects named below has a distinct layer assignment, a distinct governance relationship, and a distinct scope boundary.

The ambiguity is adversarially exploitable. A reader who treats every occurrence of "substrate" as referring to Paper 1's cell-scope governance substrate will misread Paper 2's harness substrate entirely — incorrectly placing an instinct-layer object in the reasoning layer and inverting the governance relationship. A reader who treats Paper 3's shared substrate as merely a scope-renamed version of Paper 1's substrate will miss that the shared substrate is temporary, jointly governed, and multi-Self — three properties Paper 1's substrate does not have. And any adversarial claim that the trilogy uses "substrate" inconsistently, or that a later paper's "substrate" is novel relative to an earlier paper's, must first specify which of the six objects is at issue before the claim has determinate meaning.

This note forecloses that exploitation by stating the six objects precisely and establishing that the taxonomy was in place across the trilogy from the time of publication.

---

## 2. Paper 1 usage: the governance substrate

Paper 1 introduces "substrate" in one architectural sense: the **governance substrate**, defined as the persistent, human-governed coordination medium outside the LLM where all authoritative coordination state lives. The LLM reads from and writes to the governance substrate under orchestration rules. Six commitments govern it: substrate-based hybrid composition with a governance boundary, conflict preservation as first-class state, human authority (inspect, modify, override rights) over content and rules, AI as substrate mediator, tool-agnosticism at the substrate layer, and linear-cost storage and composition.

The governance substrate at Paper 1 scope is cell-scoped: it is the authoritative coordination artifact for a single coordination cell. It is persistent (not temporary). It is home-governed: the humans in the cell's governance perimeter hold authority over it. It is in the reasoning layer: the structured, explicit, human-governable content that gives the architecture its coordination properties lives here, not inside the LLM's weights.

---

## 3. Paper 2 usages: governance substrate by tier, DNA layer, action layer, and harness substrate

Paper 2 extends the cell-scope architecture to a three-level structure (cell, aspect, Self) and introduces two new architectural objects that use the word "substrate." The result is four substrate-named objects in Paper 2, three of which are in the reasoning layer and one of which is in the instinct layer.

**Governance substrate by tier.** Paper 2's governance substrate at each tier is the same architectural object as Paper 1's governance substrate, extended in scope. At cell tier it is exactly Paper 1's governance substrate. At aspect tier and Self tier, the same commitments hold — authoritative coordination content, human governance, LLM as substrate mediator — applied to the larger scope. Paper 1's six commitments hold at every tier.

**DNA layer.** Within every cell, the governance substrate divides into two named layers. The DNA layer carries stabilized orchestration and behavior content: orchestration rules, conflict-handling specifications, lifecycle policies, behavioral templates. The DNA layer is in the reasoning layer and is governed through substrate content. It is the governance substrate's behavior-carrying half.

**Action layer.** The action layer carries recorded task instances and operational outputs: the history of what the cell has done, under which rules, with what results. The action layer is also in the reasoning layer and is governed through substrate content. It is the governance substrate's operational-history-carrying half. The DNA/action distinction within every cell is Paper 2's internal articulation of Paper 1's governance substrate.

**Harness substrate.** The harness substrate is a fundamentally different object. It is an instinct-layer specification that configures how the LLM connects to the governance substrate — governing the LLM's fast-pattern behavior, specifying which instinct responses are triggered, and defining the interface between the LLM and the reasoning layer's explicit content. The harness substrate is **not** in the reasoning layer. It is **not** governed through substrate content in the same sense as the governance substrate. It is **not** the source of truth for coordination state. It governs the LLM's connection to the governance substrate from outside the reasoning layer, not the governed content of the reasoning layer itself.

This distinction is the most load-bearing disambiguation in the trilogy. Confusing the harness substrate with the governance substrate inverts the architecture: it would place an instinct-layer configuration object inside the reasoning layer, obscuring the principled separation between fast-pattern LLM behavior and explicit human-governed coordination. Paper 2's foundational architectural commitment — separating instinct from reasoning into independently-evolving layers under unified human governance — depends on keeping these two objects distinct.

---

## 4. Paper 3 usages: home substrate, shared substrate, harness substrate (exchange-bounded)

Paper 3 introduces the inter-Self coordination scope and with it two new substrate-named objects. The harness substrate carries through from Paper 2 with an additional constraint.

**Home substrate.** Each Self's own governance substrate — the full Paper 2 architecture of cell-tier governance substrates, DNA layers, action layers, and their aspect and Self extensions — is called the home substrate at Paper 3 scope. The home substrate is in the reasoning layer, governed by each Self's home governance, and spans each Self's full three-level Paper 2 architecture. The term "home" is introduced to distinguish a Self's own substrate from the shared substrate constructed for inter-Self coordination.

**Shared substrate.** The shared substrate is the new architectural object Paper 3 introduces for inter-Self coordination. It is a CKS substrate constructed temporarily for a Full Aspect Integration (FAI) event, spanning more than one Self's home governance perimeter, and governed jointly by the participating Selves' humans. All six Paper 1 commitments hold within it: the shared substrate carries coordination content, conflict-preservation applies, human authority (inspect, modify, override) applies under joint authority, the LLM operates as substrate mediator within it, tool-agnosticism holds, and composition is linear-cost. What exchanges through the shared substrate is DNA-layer and action-layer content from contributing aspects; LLM weights and instinct-layer content do not exchange.

The shared substrate is **not** Paper 1's governance substrate at a larger scope in the sense of being the same object. It is a distinct architectural object with three properties Paper 1's governance substrate does not have: it is temporary by default (Paper 1's substrate is persistent), jointly governed across multiple Selves' perimeters (Paper 1's substrate is home-governed by one Self), and multi-Self in scope (Paper 1's substrate serves one Self). The shared substrate inherits Paper 1's six commitments, but it is a new object in Paper 3's architecture, not a renaming.

**Harness substrate at inter-Self scope.** The harness substrate from Paper 2 carries through to Paper 3 with an explicit additional constraint: instinct-layer content, including harness substrate specifications, does not cross the inter-Self perimeter. The exchange bounding commitment in Paper 3 states this explicitly. What exchanges in FAI is reasoning-layer content (DNA-layer and action-layer content); what does not exchange is instinct-layer content. This constraint makes Paper 2's instinct/reasoning separation operational at inter-Self scope.

---

## 5. Disambiguation table

| Substrate type | Layer | Governed by | Scope | Persistent? |
|---|---|---|---|---|
| Governance substrate (Paper 1) | Reasoning | Home governance (cell) | Single cell | Yes |
| Governance substrate by tier (Paper 2) | Reasoning | Home governance (per tier) | Cell / aspect / Self | Yes |
| DNA layer (Paper 2) | Reasoning | Home governance | Behavior content within each cell | Yes |
| Action layer (Paper 2) | Reasoning | Home governance | Operational records within each cell | Yes |
| Harness substrate (Paper 2/3) | Instinct | Not governed through substrate content | Home only; cannot cross inter-Self perimeter | Yes (within home) |
| Home substrate (Paper 3) | Reasoning | Home governance | Each Self's full Paper 2 architecture | Yes |
| Shared substrate (Paper 3) | Reasoning | Joint governance (multi-Self) | Temporary inter-Self scope; Paper 1 commitments hold within | Temporary by default; persistence governance-configured |

---

## 6. The most critical disambiguation: harness substrate vs. governance substrate

Of all the substrate-type pairs that could be confused, the harness substrate / governance substrate pair is the most consequential to get right, because the confusion maps directly to the trilogy's most fundamental architectural commitment.

The instinct/reasoning separation — Paper 2's first and foundational claim — holds that the LLM (instinct layer) and the CKS substrate (reasoning layer) are two independently-evolving layers under unified human governance. The governance substrate is the reasoning layer's coordination artifact: explicit, human-governed, authoritative, inspectable. The harness substrate is the instinct layer's configuration: it governs how the LLM connects to the reasoning layer, operating in the fast-pattern domain where the LLM's System-1 behavior is specified.

Confusing these two objects produces four specific architectural errors. First, it places an instinct-layer object inside the reasoning layer, collapsing the layer separation. Second, it suggests the harness substrate is directly governed through substrate content in the same sense as the governance substrate — which it is not; governance of the harness substrate operates through verification substrates and instinct-evolution mechanisms, not through the same direct inspect-modify-override rights that govern reasoning-layer content. Third, it suggests that instinct-layer specifications can cross the inter-Self perimeter in Paper 3, which they cannot (the exchange-bounding commitment holds). Fourth, it creates a false picture of how instinct evolution works: instinct evolves through undirected mutation on the LLM and infrastructure side, while DNA evolves through directed selection on the substrate side — two distinct mechanisms that governance shapes differently.

The test for distinguishing them is structural: ask which layer the object serves and how it is governed. If the object carries coordination state that humans govern through inspect-modify-override rights over substrate content, it is a governance substrate. If the object configures how the LLM's fast-pattern behavior connects to the governance substrate, it is a harness substrate. These are different questions with different answers.

---

## 7. Unifying claim and prior-art closure

The unifying claim across all six substrate types is that each is an instance of the same foundational commitment: a human-governed coordination medium outside the LLM whose content is authoritative for the questions within its scope. The scope expands from single cell to Self tier to inter-Self and population scope; the governance authority structure adapts from single-home to joint-multi-Self; the persistence policy shifts from default-persistent to default-temporary. But the architectural pattern — explicit, human-governed, accessible content as the coordination medium outside the LLM — is the same object operating at each scope.

Prior-art closure follows from the taxonomy. Any implementation of a shared substrate for inter-Self coordination is implementing a Paper 1 governance substrate at inter-Self scope with the temporary-construction, joint-authority, and multi-Self properties Paper 3 adds. Any claim that a "harness substrate" and a "governance substrate" are the same architectural object must first address the layer difference: the harness substrate is an instinct-layer object; the governance substrate is a reasoning-layer object; they are not the same thing at different sizes. Any claim that the DNA layer and action layer are novel objects unrelated to Paper 1's substrate must address the fact that they are the internal articulation of Paper 1's substrate at Paper 2's cell scope. The six-type taxonomy established here closes the space in which unqualified "substrate" references could be used to argue about novelty without specifying which object is at issue.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Disambiguating "Substrate" Across the Trilogy: Six Distinct Architectural Objects Each With Different Layer, Governance, and Scope Properties.* May 15, 2026. ORCID: 0009-0004-8065-3235.
