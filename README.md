# Coordination Architecture Theory

A design-pattern theory of how AI systems should be architected so that coordination knowledge, governance semantics, and conflict-handling logic live in a persistent, human-governed substrate **outside** the LLM — with the LLM handling high-dimensional reasoning, and humans holding authority over the substrate's content and rules.

The theory is developed across three papers (the **trilogy**) that progressively extend the same architectural pattern from cell scope, through AI Self scope, to inter-Self and population scope. The papers are self-published as research preprints on Zenodo under CC-BY 4.0.

---

## Where to Start

- **Shorter explanatory writing** — companion posts on individual concepts are published on the author's [Substack](https://liwenxin.substack.com/), which is the lower-friction entry point for readers approaching the trilogy.
- **The full papers** — the three core papers below, available on Zenodo with DOIs. Each paper is self-contained but designed to compose into the trilogy.
- **The corpus** — approximately 300 corpus papers used as research base for the trilogy's closest-neighbor analyses are in this repository under `core theory and corpus papers/`.

---

## The Three Core Papers

### Paper 1 — Cell scope

**Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems**
Wenxin Li · April 2026 · DOI: [10.5281/zenodo.19682983](https://doi.org/10.5281/zenodo.19682983)

Defines the **Coordination Knowledge Substrate (CKS)** as a design pattern and defends it through six architectural commitments: hybrid substrate-LLM division of labor at the governance boundary, conflict preservation as first-class substrate state, human-governed authority over content and rules, AI as substrate mediator, tool-agnosticism at the substrate layer, and linear-cost scaling inherited from database-backed external memory. The core theory is defended through five claims drawing on systematic review of 2024–2026 literature across governance-first AI architectures, epistemically-structured substrates, and execution-substrate research. A sixth claim extends the pattern to multi-role human-AI-human coordination. Both the core theory and the extension are demonstrated through one proof-of-concept in a regulated industry, instantiated in commodity spreadsheet infrastructure with a commercially available LLM integration.

### Paper 2 — AI Self scope

**The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance**
Wenxin Li · April 2026 · DOI: [10.5281/zenodo.19872145](https://doi.org/10.5281/zenodo.19872145)

Extends the CKS pattern from cell scope to **AI Self scope**, separating fast-pattern instinct (the LLM, functioning as a System-1 analogue) from deliberate reasoning (the CKS substrate, functioning as a System-2 analogue) into independently-evolving layers composed into one Self under unified human governance. Six architectural commitments at Self scope: the instinct/reasoning separation; structural modularity at every level (cells composing into aspects, aspects into Selves); lifecycle as governed primitives (birth, mating with three pattern variants, death with two distinct types); evolution as three mechanisms in productive tension (instinct evolution, DNA evolution, action-feedback evolution); human governance as multi-shaped; and the **enterprise brain Self** vision claim — a functioning unit composed of cells through aspects, supporting cross-aspect coordination as first-class architectural capability under unified human governance.

### Paper 3 — Inter-Self and population scope

**Substrate-Mediated Coordination Across the Inter-Self Perimeter: Extending the Coordination Knowledge Substrate Pattern to Cross-Organizational Coordination and Population Scope under Unified Human Governance**
Wenxin Li · May 2026 · DOI: [10.5281/zenodo.20017164](https://doi.org/10.5281/zenodo.20017164)

Extends the CKS pattern from intra-Self scope to **inter-Self and population scope**, defending substrate-mediated coordination across the inter-Self perimeter through six claims: shared-substrate construction at the perimeter under joint authority; aspect-bounded contribution with instinct-layer content held exchange-bounded; **Full Aspect Integration (FAI)** as canonical merge operation across the perimeter; **three-tier conflict handling** (preserve / resolve-via-orchestration / escalate-to-humans); **four-locus evolution-feed mechanism** returning learning across home-Self, shared-substrate, inter-Self, and population perimeters; and a sixth extension claim that population-scale collective evolution is what the preceding architectural commitments compose into under joint authority across population-level governance perimeters.

---

## The Substrate-Mediator Ladder

The trilogy's organizing structure. The same substrate-mediator architectural commitment progresses across six rungs at progressively larger scopes:

| Rung | Scope | Paper |
|------|-------|-------|
| 1 | Single human ↔ LLM within one cell | Paper 1 core theory |
| 2 | Multiple humans ↔ LLM within one cell | Paper 1 Claim 6 |
| 3 | Cell ↔ aspect ↔ Self within one Self | Paper 2 core theory |
| 4 | Self as enterprise-scope unified architecture | Paper 2 Claim 6 |
| 5 | Self ↔ Self mediated by shared substrate | Paper 3 core theory |
| 6 | Population-scale collective dynamics across many Selves | Paper 3 Claim 6 |

The six rungs are configurations of one architectural pattern at progressively larger scopes, not six separate patterns composed into a sequence. The hybrid-with-governance-boundary commitment is the load-bearing identity that holds identically across the rung-1-to-rung-6 contrast; the other five Paper 1 commitments carry through with within-scope rendering at each larger rung.

The ladder is observation rather than roadmap. Paper 1 did not promise Paper 3, and Paper 2 explicitly bracketed inter-Self dynamics as out of scope. The ladder becomes visible in retrospect because Paper 3 completes it.

---

## Repository Structure

- **`core theory and corpus papers/`** — the three trilogy papers (PDF and markdown source) plus approximately 300 corpus papers used as research base for the closest-neighbor analyses across the trilogy. The corpus is the methodological substrate underlying Paper 3's six-organizational-pattern and four-family closest-neighbor structures. The corpus continues to grow.

- **`featured papers/`** — closest-neighbor papers explicitly engaged in the trilogy, highlighted for direct access.

- **`docs/`** — supplementary documentation.

---

## Contribution Framing

The trilogy's contribution sits at the architectural-pattern register, not the empirical-evaluation register. CKS articulates a recurring structure of coordination problem and architectural response — named so that subsequent work can adopt it, vary it, compose it with adjacent patterns, or argue against it. The papers position CKS within an emerging research direction in CSCW-AI, governance-first AI architectures, epistemically-structured substrates, and inter-agent and multi-agent coordination.

Calibrated humility holds across the trilogy: architectural commitments are rendered confidently; empirical verification of Self-scope and population-scale deployment awaits real-world implementation.

---

## Author

**Wenxin Li** — Independent Researcher

- ORCID: [0009-0004-8065-3235](https://orcid.org/0009-0004-8065-3235)
- Substack (explanatory companion writing): [liwenxin.substack.com](https://liwenxin.substack.com/)
- Indexing landing page: [liwenxinxin.github.io/coordination-architecture-theory-papers](https://liwenxinxin.github.io/coordination-architecture-theory-papers/)

Current focus: substrate reasoning and the publication of an ambiguity-reduction corpus.

---

## How to Cite

```
Li, W. (2026). Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.
Zenodo. https://doi.org/10.5281/zenodo.19682983

Li, W. (2026). The Instinct/Reasoning Separation Outside the Model: Extending the Coordination
Knowledge Substrate Pattern to AI Selves under Human Governance.
Zenodo. https://doi.org/10.5281/zenodo.19872145

Li, W. (2026). Substrate-Mediated Coordination Across the Inter-Self Perimeter: Extending the
Coordination Knowledge Substrate Pattern to Cross-Organizational Coordination and Population
Scope under Unified Human Governance.
Zenodo. https://doi.org/10.5281/zenodo.20017164
```

---

## License

The papers are published on Zenodo under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/). This repository follows the same license for all author-original content.
