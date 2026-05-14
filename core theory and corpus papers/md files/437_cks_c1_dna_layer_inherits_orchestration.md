# DNA Layer Inherits Paper 1's Orchestration Rules and Behavior Substrates

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Subset (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, in precise operational form, that Paper 2's DNA layer is a strict extension (⊃) of Paper 1's orchestration rules and behavior substrates — carrying every governance commitment those objects carry under Paper 1, while adding naming, versioning, directed selection as the governed improvement mechanism, and two new named object types.

## Abstract

Paper 1 of the Coordination Knowledge Substrate (CKS) series establishes orchestration rules and behavior substrates as the primary objects through which human governance specifies LLM behavior. Both are substrate content: human-governed, stored in the substrate, accessible to the LLM under the mediator role, subject to conflict preservation, and modifiable at any time through the three rights. Paper 2 names the cell's governance layer explicitly as the **DNA layer** — a unified, bounded layer within the cell containing all specifications that govern the cell's behavior. This note formalizes the inheritance relationship: the DNA layer strictly contains (⊃) Paper 1's orchestration rules and behavior substrates. Every governance commitment Paper 1 makes for those objects travels unchanged into the DNA layer. What Paper 2 adds is not a new governance framework but four structural additions: explicit layer naming and bounding, a versioning commitment through the lineage chain, directed selection as the named governed mechanism for DNA improvement, and two new named object types (harness substrates, verification substrates) within the broader category of behavior substrates. These additions explain why the relationship is ⊃ rather than ≡. The note states the preserved commitments, characterizes the additions, explains the ⊃ / ≡ distinction, identifies three prior-art claims the inheritance edge forecloses, and provides an operational test.

## 1. Why the inheritance edge needs to be stated

The CKS theory series is constructed on a principle of cumulative inheritance: later papers extend earlier commitments without redefending them. Paper 2 explicitly states that all Paper 1 architectural commitments hold at every level of its three-level structure (cell, aspect, Self), but it does not separately analyze which Paper 2 architectural objects map to which Paper 1 architectural objects. That mapping is implicit in the papers' design but is not formalized as a named inheritance edge.

Formalizing the edge matters for two reasons. The first is prior-art clarity. An adversarial reader of Paper 2 who encounters the DNA layer described as a unified governed layer with versioning, directed selection, and multiple named object types might characterize it as a novel governance structure unrelated to Paper 1's orchestration rules — a new architectural commitment requiring fresh defense. This characterization is incorrect, and this note establishes publicly that it is incorrect: the DNA layer is the orchestration rules and behavior substrates from Paper 1, named, bounded, and extended. The second reason is downstream work. Papers 3 and beyond treat DNA-layer content as a standard object in inter-Self exchange. Every property of that content's governance follows from Paper 1, not from fresh commitments in Papers 2 or 3. Stating the inheritance edge makes the derivation path for downstream governance properties explicit.

## 2. Paper 1's commitments for orchestration rules and behavior substrates

Paper 1 establishes orchestration rules as the human-authored specifications that determine cell-level behavior: what the LLM is authorized to do on the substrate's behalf, how conflicts are handled, what output counts as valid, what conditions trigger which response. Paper 1 also commits to behavior substrates — the broader category of substrate objects that specify how the cell should operate in different contexts. Both are governed under the same framework:

**Substrate content.** Orchestration rules and behavior substrates are substrate content: structured representations carried in the persistent substrate, not in the LLM's weights or in runtime middleware. The substrate is the primary architectural artifact, and these specifications are inside it.

**Human-governed (three rights).** The three rights — to inspect, to modify, to override — apply fully to orchestration rules and behavior substrates. A human with appropriate access can read any orchestration rule in inspectable form at the time of their choosing, modify any such rule with the change taking effect as substrate state, and override any LLM operation touching these objects without justification to the system. These rights are architectural properties, not procedural promises.

**AI-as-mediator.** The LLM reads from orchestration rules and behavior substrates as its behavioral specification. It does not write to them outside human authority. It does not maintain parallel behavioral specifications of its own. The substrate's content is what the LLM operates under; there are no shadow behavioral specifications.

**Source of truth.** The substrate's orchestration rules and behavior substrates are the authoritative record of how the cell is specified to behave. There is no other authoritative location for this specification.

**Conflict preservation.** Where orchestration rules or behavior substrates contain contradictions — between rules, between a rule and substrate content, between two behavior substrates — the architecture commits to preserving those contradictions as first-class addressable objects rather than silently resolving them. Contradictions in the governance layer are auditable, addressable, and retraceable.

**Path retraceability.** Changes to orchestration rules and behavior substrates carry provenance metadata — writer attribution, antecedent references, rule-identity references — sufficient for an observer to reconstruct the causal path of any modification.

These six commitments constitute the governance framework Paper 1 applies to its orchestration rules and behavior substrates. No Paper 2 architectural commitment reduces, replaces, or supersedes any of them.

## 3. The inheritance: what is preserved

The DNA layer is the named, bounded, and versioned consolidation of Paper 1's orchestration rules and behavior substrates within Paper 2's two-layer cell architecture. Every piece of content in the DNA layer is, from a governance standpoint, subject to exactly the six commitments enumerated in §2:

**Substrate content identity is preserved.** DNA-layer content is substrate content. It resides in the persistent substrate, not in the instinct layer or in any component outside the substrate. The cell's DNA layer is not a separate datastore with its own access model; it is a named portion of the substrate the cell owns, carrying the same substrate-content properties it has always carried under Paper 1.

**Three rights are fully preserved.** Any DNA-layer content — orchestration rules, harness substrates, verification substrates, coordination rules, purpose statements, content-domain specifications, level determination records — falls within the three rights. Humans holding appropriate access can inspect, modify, or override any DNA-layer content at any time. LLM drafting of DNA-layer content is permissible under human authority; LLM-committed DNA content outside human authority is not admissible, by direct inheritance from Paper 1 §3.3's authority-vs-labor distinction.

**AI-as-mediator role is preserved.** The LLM in a cell reads from DNA-layer content as its behavioral specification under the same mediator role Paper 1 establishes. It does not hold behavioral specifications outside the DNA layer. No shadow orchestration rules exist outside DNA-layer substrate content. If any behavioral specification exists for the cell, it is in the DNA layer.

**Source-of-truth property is preserved.** The DNA layer is the authoritative record of the cell's behavioral specification. Downstream operations — expression, action-layer processing, directed selection, mating — all operate with reference to DNA-layer content as authoritative. There is no other location where the cell's behavioral specification is canonical.

**Conflict preservation is preserved.** Contradictions within DNA-layer content, or between DNA-layer content and action-layer content, are handled by the conflict-preservation commitment Paper 1 establishes. They become persistent first-class substrate objects with provenance, not silently resolved or deferred to runtime handling outside the substrate.

**Path retraceability is preserved.** Every modification to DNA-layer content carries provenance metadata sufficient for an observer to retrace the causal path of the change. This applies both to routine modifications through the three rights and to governed changes through the directed selection mechanism §4 introduces.

## 4. What Paper 2 adds

The DNA layer is a strict extension, not merely a renaming. Four structural additions distinguish the DNA layer from Paper 1's unstructured set of orchestration rules and behavior substrates:

**4.1 Explicit naming and layer bounding.** Paper 1 establishes orchestration rules and behavior substrates as substrate content but does not name them collectively as a layer or distinguish them structurally from operational records in the substrate. Paper 2 introduces the explicit architecture of two layers within every cell — DNA and Action — and names the DNA layer as the bounded container of all behavioral-specification content. This naming makes the governance layer of a cell a first-class architectural object: observable, separable from the action layer, and addressable as a whole for mating, versioning, and directed selection. The addition is structural and naming; the governance content of what the layer holds travels from Paper 1 unchanged.

**4.2 DNA versioning via the lineage chain.** Paper 1 commits to the modify right — humans may change orchestration rules at any time — but does not commit to a versioning structure that records each governed change as a version event in an explicit lineage chain. Paper 2 adds this commitment: the DNA layer carries an explicit version history, with each directed selection event recorded in the lineage chain. The version history is substrate content and therefore itself human-governed. An observer of a Paper 2 deployment can trace the DNA layer's governance history from the current state back through every governed change, not merely inspect the current state. This is the single most consequential structural addition, because it gives the governance layer a temporal dimension that Paper 1's modification commitment does not provide.

**4.3 Directed selection as the named governed improvement mechanism.** Paper 1 allows modification of orchestration rules and behavior substrates through the modify right but does not name a specific mechanism for governed improvement — how humans deliberately refine the cell's behavioral specification toward governance-defined goals. Paper 2 commits to directed selection as that mechanism: a deliberate, goal-oriented process that selects DNA-layer content by intent and outcome together, producing a predictable governance trajectory. Directed selection is governed through the standard Paper 1 authority architecture (the three rights apply to the selection criteria themselves, which are substrate content), but the mechanism — purposeful directed improvement of a versioned behavioral-specification layer — is new. It is what distinguishes DNA evolution from instinct evolution (which is undirected mutation) and from action-feedback evolution (which closes the action-to-DNA loop through operational experience).

**4.4 Harness substrates and verification substrates as named object types.** Paper 1 introduces behavior substrates as the broad category of substrate objects specifying how the cell operates in different contexts. Paper 2 names two specific object types within this category:

- *Harness substrates* are behavior substrates that specify which sub-substrates are active for current cell activity. A harness substrate is itself human-governed, fully inspectable, modifiable, and overridable; it is substrate content under Paper 1's framework. The addition is the naming and specificity: harness substrates carry the semantics of governed per-deployment activation — selecting which DNA-layer content is expressed for a given goal — which Paper 1's behavior-substrate category does not separately address.

- *Verification substrates* are behavior substrates that specify parallel-run behavior: running instinct-layer and reasoning-layer operations simultaneously to detect divergence and govern integration. Verification substrates are substrate content under Paper 1's framework, human-governed and accessible through the three rights. The addition is again naming and specificity: a verification substrate specifies a particular kind of governed test that Paper 1's general behavior-substrate category does not separately name.

Both additions are object-type additions within the DNA layer, not new governance principles. The governance of harness and verification substrates is inherited directly from Paper 1's behavior-substrate governance. An implementer who knows Paper 1's behavior-substrate governance commitments, and who encounters a harness substrate or a verification substrate in a Paper 2 deployment, applies exactly the same governance framework: inspect, modify, override as needed, with no additional requirements from the fact that the object is specifically a harness or verification substrate rather than an unnamed behavior substrate.

## 5. Why ⊃ rather than ≡

A strict extension (⊃) differs from an identity (≡) in that the extending object satisfies everything the extended object commits to and adds further commitments. The DNA layer satisfies every governance commitment Paper 1 makes for orchestration rules and behavior substrates — this is established in §3 above — and adds the four structural elements described in §4. Because of those additions, the relationship is strict extension rather than identity.

The contrast with C1.05 (the cell ≡ relation) is instructive. Paper 2's cell is identical to Paper 1's cell in architectural definition: the cell is the atomic unit, all Paper 1 commitments apply at the cell level, and Paper 2 adds no new structural elements to the cell itself. The DNA layer is not an identical preservation; it is a named, versioned, directed-selection-governed, two-new-object-type extension of what Paper 1 called orchestration rules and behavior substrates. Hence ⊃.

The ⊃ direction is also important for what it forecloses. If the DNA layer were ≡ to Paper 1's orchestration rules, a reader might argue that the additions (versioning, directed selection, harness substrates, verification substrates) are independent inventions not derived from Paper 1. The ⊃ relation says exactly the opposite: those additions are built on top of the Paper 1 governance framework, not alongside it. The additions are only coherent within that framework. Directed selection modifies DNA-layer content, which is substrate content under the three rights; without Paper 1's governance framework, directed selection is undefined as a governed mechanism. Harness and verification substrates are governed as behavior substrates under Paper 1's commitments; without Paper 1's behavior-substrate governance, they have no governance commitments to inherit.

## 6. Prior-art significance

Three adversarial claims are foreclosed by this inheritance edge:

**Claim (a): Paper 2's DNA layer introduces novel governance objects unrelated to Paper 1's orchestration rules.** Foreclosed. The DNA layer is the named, bounded consolidation of Paper 1's orchestration rules and behavior substrates. Its governance objects — the harness substrates, verification substrates, coordination rules, purpose statements, and all other DNA-layer content types — are behavior substrates and orchestration rules under Paper 1's framework. No DNA-layer governance object is independent of Paper 1's orchestration-rule and behavior-substrate category.

**Claim (b): DNA versioning is novel relative to Paper 1's modifiable substrate content.** Foreclosed in the form "Paper 2 introduces versioning into a previously unversioned governance context." Paper 1 commits to the modify right for orchestration rules and behavior substrates, establishing that such content is mutable substrate content subject to human authority. Paper 2's explicit lineage chain and version-history commitment for DNA-layer modifications is an extension of the modify right's implicit record-keeping, structured as an explicit architectural property. The versioning adds structure and explicit commitment; it does not introduce mutability into a previously immutable governance layer.

**Claim (c): Harness substrates and verification substrates are novel inventions unrelated to Paper 1's behavior substrates.** Foreclosed. Both are named species of behavior substrate under Paper 1's framework. The governance commitments that apply to them — substrate content, three rights, mediator role, source-of-truth, conflict preservation, path retraceability — are Paper 1's behavior-substrate governance commitments applied to these two specific object types. The novelty in Paper 2 is the naming and specification of what each object type carries, not the introduction of governance commitments for them.

## 7. Relationship to C1.09

This note covers the DNA layer as the inheritance of Paper 1's orchestration rules and behavior substrates. C1.09 will cover the corresponding inheritance edge for the action layer: the Paper 2 action layer (recorded task instances and their outputs) as the inheritance of Paper 1's substrate content for operational records. The DNA/action distinction is Paper 2's within-cell structural addition; together C1.08 and C1.09 establish that both layers of every Paper 2 cell are extensions of Paper 1 substrate content, each inheriting appropriate Paper 1 governance commitments.

## 8. Operational test

An observer examining a Paper 2 deployment can apply the following test to verify that Paper 1's orchestration-rule governance commitments hold for DNA-layer content, independently of the DNA versioning structure:

1. Take any DNA-layer content in the deployment — a coordination rule, a purpose statement, a harness substrate, a verification substrate, any element within the DNA layer.
2. Verify that a human with appropriate access can read that content directly, in inspectable form, without scheduling, approval, or LLM intermediation as a precondition. If this fails, the inspect right is not preserved for DNA-layer content, and Paper 1's governance commitment is not satisfied by this deployment regardless of what the versioning records show.
3. Verify that a human with appropriate access can modify that content with the change taking effect as substrate state. If this fails, the modify right is not preserved for DNA-layer content.
4. Verify that no LLM operation, vendor policy, or runtime middleware layer can in principle prevent (2) or (3). If this fails, the architectural character of the three rights is not preserved.
5. Verify that any DNA-layer content authored by an LLM was subject to human authority before it took effect — that LLM-drafted content was placed in the DNA layer under governance authorization, not committed autonomously. If this fails, Paper 1 §3.3's authority-vs-labor distinction is not preserved.
6. Verify that contradictions within DNA-layer content are preserved as first-class addressable substrate objects with provenance, not silently resolved. If this fails, conflict preservation is not preserved for DNA-layer content.

A deployment that passes all six checks satisfies Paper 1's governance commitments for the DNA layer independently of its versioning structure. The versioning structure (the lineage chain recording directed selection events) is then verified separately as a Paper 2 addition on top of the passing Paper 1 baseline. A deployment that fails any of (2)–(6) does not implement the DNA layer as the inheritance of Paper 1's orchestration rules and behavior substrates; it implements something structurally resembling the DNA layer but without the governance commitments the inheritance edge requires.

## 9. Conclusion

Paper 2's DNA layer strictly extends (⊃) Paper 1's orchestration rules and behavior substrates. Every governance commitment Paper 1 establishes for those objects — substrate content identity, three rights, AI-as-mediator, source-of-truth, conflict preservation, path retraceability — travels unchanged into the DNA layer. What Paper 2 adds is four structural elements: explicit layer naming and bounding that makes the governance layer of a cell a first-class architectural object; an explicit version history through the lineage chain that records each directed selection event; directed selection as the named, goal-oriented governed mechanism for DNA improvement; and two new named object types (harness substrates, verification substrates) within the broader category of behavior substrates. These additions are built on Paper 1's governance framework, not alongside it: they are only coherent as additions because the DNA layer is already governed under Paper 1's commitments. The inheritance relationship ⊃ rather than ≡ follows from the additions; the governance continuity follows from the preserved commitments.

Downstream work that operates on DNA-layer content — whether computing mating operations, tracing lineage chains, executing directed selection, or exchanging DNA-layer content across the inter-Self perimeter in Paper 3 — inherits Paper 1's governance commitments for that content without fresh defense. The governance properties of DNA-layer content in any CKS-governed deployment are Paper 1's properties.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *DNA Layer Inherits Paper 1's Orchestration Rules and Behavior Substrates.* May 14, 2026. ORCID: 0009-0004-8065-3235. Derivation note #437, Series C, CKS theory series. CC BY 4.0.
