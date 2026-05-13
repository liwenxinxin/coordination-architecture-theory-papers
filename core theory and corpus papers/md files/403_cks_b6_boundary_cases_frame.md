# Boundary Cases Integrating Frame: Formalizing What Boundary Cases Are in the CKS Architecture, How They Differ from Anti-Patterns as Valid Edge Configurations Rather Than Violations, and Why Naming the Architecture's Edges Is Itself Architecturally Significant Prior Art

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Phase B6 of the Series B derivation notes addresses boundary cases: deployment configurations of the CKS architecture in which one or more architectural commitments are correctly present and functional, but the deployment operates at or near the architectural limit of what those commitments specify. This note is the integrating frame for Phase B6. It formalizes what boundary cases are, distinguishes them precisely from anti-patterns (Phase B3), describes the six-component structure common to each Phase B6 note, provides a taxonomy of the fourteen boundary cases B6.02–B6.15 address, and explains why formalizing the architecture's edges constitutes architecturally significant prior art. The note establishes the frame within which all subsequent Phase B6 notes operate.

---

## 1. What Boundary Cases Are, and How They Differ from Anti-Patterns

The CKS architecture specifies a set of architectural commitments. Paper 1 contributes six: the substrate/LLM hybrid drawn at the governance boundary; conflict preservation as a first-class substrate operation; human-governed authority over substrate content and orchestration rules; AI-as-substrate-mediator with five governing properties; tool-agnosticism defined by three minimal requirements; and linear-cost composition. Paper 2 extends these commitments through the instinct/reasoning separation at Self scope, adding structural levels (cell, aspect, Self), the DNA/action layer distinction within every cell, expression as governed selection, lifecycle primitives (birth, mating, death), three evolution mechanisms (instinct evolution, DNA evolution, action-feedback evolution) in productive tension, multi-shaped human governance over each mechanism, and the enterprise brain Self as an architecturally coherent design pattern.

Each of these commitments can be violated. Phase B3 of the Series B derivation notes formalizes anti-patterns: the configurations in which a commitment is broken or absent. An anti-pattern is a violation. The architecture does not hold at an anti-pattern; the commitment is missing, circumvented, or structurally incompatible with the deployment. The governance response to an anti-pattern is remediation: identifying the violation and restoring the commitment.

Boundary cases are not violations. A boundary case is a deployment configuration in which all relevant architectural commitments are correctly present and functional, but the deployment approaches the limit of what those commitments specify. The commitments hold. The architecture is intact. The deployment is valid. What distinguishes a boundary case from a typical deployment is that it operates at or near the architectural edge — the point where the specification's coverage becomes thin, where governance implications become unfamiliar, or where stress on one commitment makes adjacent commitments more likely to weaken.

Two examples clarify the distinction:

**Minimum viable cell deployment.** The CKS architecture specifies the cell as its modular unit. Paper 1 does not set a floor on cell count for a valid deployment; a deployment with exactly one cell satisfies all architectural commitments. That deployment is therefore architecturally valid. It is also a boundary case: with a single cell, there are no inter-cell mating operations, no aspect-level coordination, and no cross-cell conflict resolution events. The governance implications of operating at this minimum — what governance mechanisms are structurally dormant, which commitments operate with no opportunity to exercise themselves, what planning is needed for scaling — are different from the implications of a multi-cell deployment. The single-cell deployment is not wrong. It is valid at the architecture's minimum edge.

**High-frequency instinct evolution.** The CKS architecture's instinct evolution mechanism covers LLM version changes as undirected mutation events requiring verification governance. Nothing in Paper 2 sets a frequency ceiling for valid instinct evolution; a deployment experiencing fifty LLM version changes per day satisfies the architectural commitments if it governs each change through verification substrates as specified. That deployment is therefore architecturally valid. It is also a boundary case: at this frequency, the governance load on verification substrates is qualitatively different from the governance load anticipated in a typical deployment, and the window between instinct mutations may be too short for action-feedback evidence to accumulate meaningfully. The high-frequency deployment is not wrong. It tests the architecture's temporal edge.

**The key distinction, stated precisely:**
- Anti-patterns (Phase B3): the commitment is broken or absent. Response: remediation.
- Boundary cases (Phase B6): the commitment holds, but at or near its architectural limit. Response: understanding and planning.

Some boundary cases are architecturally adjacent to anti-patterns. A deployment that operates at a boundary long enough, or without adequate planning, may develop into a violation. Boundary cases therefore also serve a diagnostic function: they identify where anti-patterns are most likely to develop if governance attention lapses. This does not make boundary cases violations in themselves; it makes them the configurations where governance discipline is most important.

---

## 2. The Six-Component Boundary Case Structure

Each Phase B6 note covers one boundary case in a common structure of six components. The structure ensures that boundary cases are formalized consistently and that each note provides actionable governance guidance for deployments legitimately operating at the relevant edge.

**Component 1: Configuration Description.** What is the boundary case deployment configuration? This component names the specific edge condition — the property of the deployment that places it at or near an architectural limit — and distinguishes it from both typical deployments (which share the same commitments but do not approach the limit) and anti-patterns (which lack the commitment).

**Component 2: Architectural Boundary Being Tested.** Which commitment or commitments are near their limits in this configuration? Not every architectural commitment is under stress in every boundary case. This component identifies the specific commitments whose coverage becomes thin at this edge, so that governance attention can be directed appropriately.

**Component 3: Governance Implications.** What governance considerations arise specifically at this boundary? Governance implications at boundary cases differ from governance implications in typical deployments not because the commitments change but because operating near a limit exposes aspects of a commitment that typical deployments do not exercise. This component articulates those implications.

**Component 4: Boundary Tests.** How can an operator verify that a deployment is correctly operating at this boundary rather than violating the relevant commitment? This component provides concrete tests that distinguish valid boundary-case operation from anti-pattern violation.

**Component 5: Stress Points.** Where might this boundary configuration develop into anti-patterns if governance discipline lapses? This component identifies the specific failure modes that are elevated at this edge — the adjacent violations that become more likely when a deployment operates near this limit.

**Component 6: Architectural Limits.** What does the architecture's specification say about this boundary? This component cites the relevant sections of Paper 1 and Paper 2 that address — or deliberately do not address — the edge condition, establishing what the architecture's coverage does and does not extend to at this boundary.

The six components together ensure that each Phase B6 note does three things: formalizes the boundary as a valid configuration, provides governance guidance for deployments legitimately at that edge, and establishes prior art for the architecture's coverage of that edge.

---

## 3. Taxonomy of Phase B6 Boundary Cases

The fourteen boundary cases addressed in B6.02–B6.15 fall into five categories.

**Minimum viable configuration cases (B6.02–B6.03).** These cases address deployments at minimum entity counts. B6.02 covers single-cell deployment — the minimum viable architecture in which exactly one cell is present and all multi-cell dynamics are structurally absent. B6.03 covers single-aspect deployment — the minimum viable structural configuration above the cell level, in which one aspect organizes one or more cells but no inter-aspect dynamics operate. Both cases test the architecture's lower bounds: the minimum entity counts at which each structural level's governance commitments remain meaningful and complete.

**Temporal boundary cases (B6.04).** B6.04 covers the high-frequency mutation environment, in which instinct evolution events arrive at a rate that places unusual demands on verification governance and compresses the period between mutations below the natural cadence of action-feedback evidence accumulation. This case tests the architecture's temporal governance commitments under conditions of accelerated change.

**Lifecycle boundary cases (B6.05–B6.07).** These cases address entities at the edges of their lifecycle. B6.05 covers the entity at level transition — a cell, aspect, or Self undergoing a structural change that repositions it within the three-level architecture, testing the architecture's coverage of transitional states. B6.06 covers mating with maximum DNA conflict — the case in which two cells or aspects contributing to a mating event carry maximally conflicting DNA-layer content, testing the conflict preservation and mating governance commitments at their outer limits. B6.07 covers archival reactivation — a cell or aspect retired to archival state that is subsequently reactivated into a new architectural context, testing whether the lifecycle governance commitments that governed retirement continue to apply under reactivation.

**Scale boundary cases (B6.08–B6.10).** These cases address deployments at unusual scale in one or more dimensions. B6.08 covers cross-partner composition — a deployment that composes cells or aspects originating from distinct organizational partners, testing the architecture's composition commitments when the participating units do not share a common orchestration lineage. B6.09 covers minimal governance capacity — a deployment in which the human governance function operates at or near the minimum required for the architecture's commitments to hold, testing the governance commitment under capacity constraints. B6.10 covers large-scale cell populations — a deployment with an unusually large number of cells, testing the linear-cost composition commitment and the substrate-as-source-of-truth commitment at scale.

**Evidence, evolution, and domain boundary cases (B6.11–B6.14).** These cases address deployments at the edges of the architecture's evidence-handling and evolutionary dynamics. B6.11 covers action-feedback at evidence scale — a deployment in which the volume of action-layer feedback exceeds what was anticipated in the governance design, testing the action-feedback evolution mechanism's governance commitments under high evidence load. B6.12 covers simultaneous lifecycle events — a deployment in which multiple birth, mating, and death events occur concurrently across levels, testing the architecture's governance commitments when lifecycle events are not sequentially isolated. B6.13 covers content-domain near-exhaustion — a deployment in which the DNA layer of one or more cells approaches the natural coverage limits of its content domain, testing what directed selection can accomplish when the available design space is nearly saturated. B6.14 covers deployment at an evolution inflection point — the configuration in which a deployment transitions from one evolutionary regime to another (for example, from primarily instinct-evolution-driven change to primarily DNA-evolution-driven change), testing the architecture's commitments during regime transitions.

**Phase synthesis (B6.15).** B6.15 is the Phase B6 synthesis and Series B closure note. It draws together the governance themes across all fourteen boundary cases, articulates what the full taxonomy of boundary cases reveals about the architecture's coverage, and closes Series B.

---

## 4. Why Boundary Cases Are Prior Art

Formalizing boundary cases is architecturally significant prior art for two distinct reasons.

**First, naming the architecture's edges establishes that the architecture's coverage extends to those edges.** An architecture without formally named boundaries is an architecture whose boundaries are unknown. When the boundaries are unknown, any party who subsequently describes governance implications at those edges can claim to have discovered novel territory — territory the architecture did not previously cover. Formalizing the boundary cases in Phase B6 establishes, as dated prior art, that the CKS architecture's governance commitments extend to each named edge. A minimum viable single-cell deployment is within the architecture's scope, not outside it. A high-frequency mutation environment is a configuration the architecture addresses, not a gap the architecture leaves open. Cross-partner composition is a boundary the architecture covers, not a novel architectural problem the architecture failed to anticipate. Phase B6 draws these boundaries explicitly, under the author's name, with dates, so that subsequent work cannot claim them as independent discoveries.

**Second, formalizing boundary cases provides governance guidance for deployments that legitimately operate at these edges.** Not every deployment is a typical mid-range configuration. Real deployments include startups operating with a single cell, infrastructure environments with high LLM version-change rates, and enterprises composing cells from multiple organizational lineages. These deployments are not architectural violations; they are valid deployments operating at architectural edges. Without formalized boundary case documentation, operators of such deployments have no architectural guidance specific to their edge condition. Phase B6 fills that gap: each note provides, for a specific edge configuration, the governance implications, boundary tests, and stress points that allow operators to run valid boundary-case deployments with appropriate governance discipline.

The combination of these two functions — prior art establishment and governance guidance — is what makes boundary case formalization architecturally necessary rather than merely exhaustive. It is not sufficient to say that an architecture extends to its edge cases; the edges must be named and their governance implications stated before anyone else names them.

**The prior art mechanism operates through specificity.** A general claim that the CKS architecture "applies in all deployment configurations" is prior art of weak form. A note that names exactly what single-cell deployment means, which commitments are near their limits in that configuration, what boundary tests distinguish valid single-cell operation from anti-pattern violation, and where single-cell deployments are most likely to develop violations — that is prior art of strong form. Phase B6 produces strong-form prior art for each named boundary case.

---

## 5. Phase B6 Sequence: B6.02–B6.15

The Phase B6 notes proceed in the order of the taxonomy established in §3. Each note is self-contained: it addresses one boundary case fully, using the six-component structure described in §2. Notes are numbered in order of their category, from minimum viable configurations through synthesis.

**B6.02** — Single-cell deployment: the minimum viable architecture. Addresses what single-cell operation means for each of Paper 2's structural commitments, and what governance disciplines are most important when inter-cell dynamics are structurally absent.

**B6.03** — Single-aspect deployment: minimum viable structural configuration above the cell level. Addresses what single-aspect operation means for aspect-level governance commitments, and what planning is required for aspect-level scaling.

**B6.04** — High-frequency mutation environment: instinct evolution at rates that compress the typical governance cadence. Addresses verification substrate design under high mutation frequency and the relationship between mutation rate and action-feedback evidence accumulation.

**B6.05** — Entity at level transition: a cell, aspect, or Self repositioning within the three-level structure. Addresses governance continuity during structural transitions and how commitment applicability is maintained across level changes.

**B6.06** — Mating with maximum DNA conflict: the outer limit of conflict preservation under mating. Addresses what the conflict preservation commitment specifies at maximum conflict density, and how mating governance operates when parent DNA layers are maximally divergent.

**B6.07** — Archival reactivation: retired entities reactivated into new architectural contexts. Addresses how lifecycle governance commitments that governed retirement continue to apply under reactivation, and what new governance obligations arise when context has changed.

**B6.08** — Cross-partner composition: cells or aspects originating from distinct organizational lineages. Addresses what composition commitments require when participating units do not share a common orchestration history, and how conflict preservation operates across lineage boundaries.

**B6.09** — Minimal governance capacity: human governance operating near its minimum viable level. Addresses what the human-governed commitment requires under governance capacity constraints, and which governance functions are load-bearing when capacity is limited.

**B6.10** — Large-scale cell populations: deployments at the upper range of cell count. Addresses how the linear-cost composition commitment and the substrate-as-source-of-truth commitment perform at scale, and what governance design is required to maintain commitment integrity at large cell populations.

**B6.11** — Action-feedback at evidence scale: high-volume feedback loops. Addresses how the action-feedback evolution mechanism's governance commitments operate when evidence volume exceeds the anticipated governance design, and what substrate architecture supports high-evidence-load deployments.

**B6.12** — Simultaneous lifecycle events: concurrent birth, mating, and death across levels. Addresses how lifecycle governance commitments handle concurrency, and what coordination mechanisms are required when lifecycle events cannot be sequentially isolated.

**B6.13** — Content-domain near-exhaustion: DNA layers approaching natural coverage limits. Addresses what directed selection can accomplish as the available design space saturates, and what governance signals indicate approaching domain exhaustion.

**B6.14** — Deployment at evolution inflection point: regime transitions in evolutionary dynamics. Addresses what governance continuity requires during transitions between evolutionary regimes, and how the architecture's multi-mechanism design supports inflection-point navigation.

**B6.15** — Phase B6 synthesis and Series B closure. Draws the Phase B6 taxonomy together, articulates what the boundary case formalization reveals about the architecture's coverage, and closes Series B.

---

## 6. Conclusion

Boundary cases occupy a specific and important position in the architecture's prior art landscape. They are not violations — they are the valid configurations that test the architecture's edges. Formalizing them establishes that the architecture's governance commitments extend to those edges, preventing any subsequent party from claiming to discover governance implications the architecture left unnamed. It also provides governance guidance for real deployments that legitimately operate at these edges, which would otherwise have no architecture-specific guidance for their configurations.

Phase B6 addresses the boundary cases of Paper 2's architecture. The fourteen cases in B6.02–B6.15, organized by the six-component structure described here, together map the outer limits of the CKS architecture as Paper 2 specifies it. The frame established in this note governs all fourteen.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Boundary Cases Integrating Frame: Formalizing What Boundary Cases Are in the CKS Architecture, How They Differ from Anti-Patterns as Valid Edge Configurations Rather Than Violations, and Why Naming the Architecture's Edges Is Itself Architecturally Significant Prior Art.* May 13, 2026. ORCID: 0009-0004-8065-3235.
