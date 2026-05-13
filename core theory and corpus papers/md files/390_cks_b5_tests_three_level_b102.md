# Operational Tests for Three-Level Structure (B1.02): Five Deployment-Facing Tests Including Level Instantiation, Level Distinguishability, Membership Substrate Residency, Level-Distinct Governance Scope, and Level-Boundary Integrity, Each With Question, Mechanism, Pass, Fail, and Remediation Signal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's second paper (Li, April 2026) introduces three architectural levels — cell, aspect, and Self — with relational role membership as the structural machinery that allows the same underlying CKS artifact to participate in different structural arrangements simultaneously (§5.2). B1.02 formalizes this three-level commitment as a foundational architectural claim. This note derives five deployment-facing operational tests for that commitment. The tests address whether all three levels are instantiated (Level-Instantiation Test), whether entities at each level can be distinguished through functional criteria (Level-Distinguishability Test), whether entity membership in aspects and Selves is substrate-resident (Membership Substrate Test), whether each level exercises governance scope distinct from the others (Level-Distinct Scope Test), and whether structural boundaries between levels are maintained without level collapse (Level-Boundary Integrity Test). Each test states a test question, test mechanism, pass condition, fail condition, and remediation signal. All five tests must pass for full B1.02 operational test passage. The primary anti-patterns detected by this test suite are B3.03 Flat Architecture, B3.29 Cross-Level Confusion, and B3.18 Intrinsic Type Assignment.

---

## 1. Why three-level structure requires operational testing

B1.02 commits to three architectural levels — cell, aspect, and Self — as the structural machinery through which Paper 2's instinct/reasoning separation operates at the Self scope (§5.2). Without this structure, the instinct/reasoning separation of B1.01 is a commitment that has nowhere to compose: the Self scope at which the separation operates cannot hold together as architectural composition under unified human governance if the levels through which it composes are absent or conflated.

Three-level structure is not self-verifying from implementation choices alone. An architecture that names three levels in documentation but instantiates entities only at one level is not three-level; it is a flat architecture with three labels. An architecture that instantiates entities at each level but allows a single entity to pass functional tests for multiple levels has failed to maintain level-distinguishability, producing Cross-Level Confusion where the commitment calls for distinct scope. An architecture that instantiates entities at each level and maintains level-distinguishability, but carries membership relationships in configuration files or documentation rather than in the substrate, has failed the substrate-residency commitment that makes membership human-governed and inspectable.

Operational tests are necessary because each of these failure modes looks correct from a surface description and becomes detectable only through systematic examination of functional behavior and substrate content. The five tests in this note examine B1.02's commitment from five independent angles: presence (are all levels there?), distinguishability (can each level be identified functionally?), residency (is membership substrate-resident?), scope distinction (does each level govern distinct content?), and boundary integrity (are level boundaries maintained architecturally?). Together they constitute the composite operational test for B1.02.

---

## 2. Test 1 — Level-Instantiation Test

**Source:** B2.10 level-instantiation patterns.

**TEST QUESTION:** Does the deployment instantiate all three structural levels — cell, aspect, and Self?

**TEST MECHANISM:** Enumerate all entities in the deployment. Categorize each entity as cell-level, aspect-level, or Self-level using B2.85 level-determination records as the authoritative classification source. Verify that at least one entity exists at each of the three levels: at least one cell (an atomic CKS artifact carrying substrates, orchestration rules, and DNA and action layers), at least one aspect (a coordination arrangement of cells serving a particular purpose with an authored purpose statement per B2.15), and at least one Self (an integrated whole holding multiple aspects under unified human governance with Self integration architecture per B2.21). Confirm that level-determination records per B2.85 are themselves substrate-resident and carry A2.40 provenance.

**PASS CONDITION:** At least one cell, at least one aspect, and at least one Self are present in the deployment. Each entity's level is recorded in governed B2.85 level-determination records with A2.40 provenance. No level is absent.

**FAIL CONDITION:** One or more levels are absent from the deployment. Two primary failure forms: (a) no aspects present — cells are coordinated without aspect mediation, producing a flat cell architecture in which coordination relationships exist but no level holds the aspect commitment (purpose-defined structural arrangement of cells with authored purpose statement); (b) no Self present — aspects or cells are coordinated without Self-level integration, producing a structure that may achieve coordination across cells without the unified human governance and integration architecture that the Self scope commits to.

**REMEDIATION SIGNAL:** Flat Architecture (B3.03). When aspects are absent, the deployment exhibits B3.03 Form 1 (missing coordination layer). When the Self is absent, the deployment exhibits B3.03 Form 3 (missing integration layer). The remediation path is to introduce the absent level through governed origination per B1.06, with the introduced level carrying appropriate DNA-layer content, authored purpose statement (for aspects) or integration architecture (for Selves), and governed level-determination records per B2.85.

---

## 3. Test 2 — Level-Distinguishability Test

**Source:** B2.09 level-distinguishability tests.

**TEST QUESTION:** Can entities at each level be distinguished from each other through functional criteria per B2.09?

**TEST MECHANISM:** Apply the three B2.09 level-distinguishability sub-tests to each entity in the deployment. The three sub-tests are:

- **CELL TEST:** Does this entity execute specific informational tasks without coordinating peer cells? A cell handles a task that is its own work; it does not orchestrate other cells as part of its function.
- **ASPECT TEST:** Does this entity coordinate multiple cells for a purpose, with an authored purpose statement per B2.15 in its substrate? An aspect's function is the arrangement of cells toward a defined purpose; its purpose statement is substrate content under human governance.
- **SELF TEST:** Does this entity integrate multiple aspects under unified human governance, with Self integration architecture per B2.21 carrying the composition relationships across levels in its substrate? A Self's function is the holding-together of multiple aspects as facets of one CKS-governed intelligence.

Each entity should pass exactly one of these three sub-tests. Compare the functional test result against the entity's B2.85 level-determination record.

**PASS CONDITION:** Each entity passes exactly one level-distinguishability sub-test. No entity passes multiple sub-tests simultaneously. No entity fails all three sub-tests. Each entity's functional test result matches its B2.85 level-determination record.

**FAIL CONDITION:** Two failure forms. First, an entity passes multiple level-distinguishability sub-tests simultaneously — for example, an entity that both executes specific informational tasks (cell behavior) and coordinates multiple cells for a purpose (aspect behavior) without a clear architectural boundary between the two functions. This is Cross-Level Confusion (B3.29). Second, an entity passes none of the three sub-tests, leaving it architecturally undefined — its function does not correspond to any of the three committed levels. A third failure form: level-determination records in B2.85 do not match the functional test results, indicating that the records were authored without reference to actual functional behavior, which is the Intrinsic Type Assignment anti-pattern (B3.18).

**REMEDIATION SIGNAL:** If an entity passes multiple tests: Cross-Level Confusion (B3.29). The remediation is to decompose the entity into distinct entities, one per level, with each carrying the appropriate function and substrate-resident level-determination record. If an entity's B2.85 record diverges from its functional test result: Intrinsic Type Assignment (B3.18). The remediation is to re-author level-determination records through governed selection per B1.14 that reflects functional behavior rather than nominal designation. Intrinsic Type Assignment is particularly consequential because it causes governance scope (§5, below) to be mis-applied — aspect governance affordances operating over what is functionally a cell, for example — producing silent mis-governance that persists until the functional test is performed.

---

## 4. Test 3 — Membership Substrate Test

**Source:** B2.08 aspect and Self membership substrate residency.

**TEST QUESTION:** Is entity membership in aspects and Selves substrate-resident per B2.08?

**TEST MECHANISM:** Inspect the substrate for membership records. For each aspect in the deployment: does the aspect carry substrate-resident cell membership records per B2.08, specifying which cells participate in this aspect's coordination arrangement? For each Self: does the Self carry substrate-resident aspect membership records per B2.08, specifying which aspects this Self integrates? Verify that all membership records reside in the DNA layer per B1.06 (the layer of stabilized orchestration substrates and behavior substrates that define how the entity functions). Verify that membership records carry A2.40 provenance. Check that membership records are accessible through the substrate's human read/write interface — not only machine-readable but human-inspectable and human-modifiable under the three governance rights (inspect, modify, override).

**PASS CONDITION:** All aspect-cell membership and all Self-aspect membership is substrate-resident per B2.08. All membership records reside in the DNA layer per B1.06. All records carry A2.40 provenance. Membership is inspectable, modifiable, and overridable by humans through the substrate interface.

**FAIL CONDITION:** Two failure forms. First, membership is implicit — understood from the deployment's implementation (e.g., from which code modules call which) rather than recorded as substrate content. Implicit membership is not human-governed because it is not inspectable, modifiable, or overridable through the substrate's governance interface without modifying the implementation itself. Second, membership records exist but reside in configuration files, documentation, or tool-specific metadata rather than in the governed substrate. Off-substrate membership records are not subject to the DNA layer's governance properties, cannot carry A2.40 provenance in the CKS sense, and do not support the relational role membership commitment that allows cells to participate in multiple aspects simultaneously under governed structural arrangements.

**REMEDIATION SIGNAL:** Flat Architecture (B3.03) sub-form — the structural commitment to three levels is in principle present but is not carried in the substrate, which means the levels are nominally asserted rather than architecturally instantiated. Remediation: author membership records as substrate content per B2.08, residing in the DNA layer per B1.06, through the governed origination process per B1.06. Membership records authored through governed origination carry A2.40 provenance and are subject to the governance rights from the moment of origination. Off-substrate membership records cannot be converted by annotation alone; the substrate-resident record must be created through the governed authoring path to carry the architectural properties the commitment requires.

---

## 5. Test 4 — Level-Distinct Scope Test

**Source:** B2.07 level-distinct governance scope verification.

**TEST QUESTION:** Does each level have governance scope distinct from the others per B2.07?

**TEST MECHANISM:** Verify the governance scope associated with each level in the deployment by examining the governance affordances per A2.01–A2.04 that operate at each level and confirming that they operate on distinct content. Three scope commitments to verify:

- **Cell governance scope:** Governance affordances at the cell level operate on cell operational behavior — the cell's own DNA-layer content, its orchestration rules, its action layer, and its lifecycle. Cell-scope modification per A2.02 modifies cell DNA; it does not modify the aspect coordination rules that govern how this cell participates in an aspect, nor the Self integration architecture that governs how the cell's aspects compose.
- **Aspect governance scope:** Governance affordances at the aspect level operate on coordination behavior — the aspect's purpose statement per B2.15, its cell membership per B2.08, and its coordination rules governing how member cells are orchestrated toward the aspect's purpose. Aspect-scope rule authoring per A2.04 authors aspect coordination rules, not cell operational rules and not Self integration rules.
- **Self governance scope:** Governance affordances at the Self level operate on integration behavior — the Self's aspect membership per B2.08, its Self integration architecture per B2.21, and its governance over cross-aspect coordination. Self-scope operations modify Self-level integration content, not aspect coordination content and not cell operational content.

Verify that these three scopes do not overlap. A governance operation that is described as "modifying the rules" without specifying which level's rules are being modified is not level-distinct.

**PASS CONDITION:** Cell, aspect, and Self governance scopes are distinct and non-overlapping. Governance operations at each level are unambiguously scoped to that level's content. The governance affordances per A2.01–A2.04 at each level can be confirmed to operate on content at exactly one level.

**FAIL CONDITION:** Governance scopes overlap or are undifferentiated. The primary failure form is the absence of level-scoped governance: a deployment in which "the rules" is a single body of content without level-differentiation, such that modifying rules can silently affect cell, aspect, and Self behavior simultaneously without architectural boundary. This failure produces silent authority escalation — an operation scoped to one level's governance inadvertently reaches content at another level — which is architecturally invisible until the resulting behavior divergence is traced.

**REMEDIATION SIGNAL:** Layer Conflation (B3.07) if the content layers are not distinguished, which is a prerequisite failure for level-distinct scope. Authority Ambiguity (B3.26) if governance authority does not follow level scope — for example, if a human with authority over cell-level governance can also modify aspect coordination rules without any additional governed step, because the two levels' content is not structurally differentiated. Remediation requires establishing the structural differentiation between levels' governance content in the substrate before level-distinct governance affordances can be correctly applied.

---

## 6. Test 5 — Level-Boundary Integrity Test

**Source:** B1.02 structural boundary commitment; B3.03 Flat Architecture; B2.96 cross-level access patterns.

**TEST QUESTION:** Are the structural boundaries between cell-aspect and aspect-Self relationships maintained without level collapse?

**TEST MECHANISM:** Verify the structural integrity of each level boundary in the deployment. Two boundaries to examine:

- **Cell-aspect boundary:** Cells operate within aspects — they are coordinated by aspects toward the aspect's purpose. Verify that cells are not integrated directly into Selves without aspect mediation: a cell whose work contributes to Self-level function should do so through its participation in at least one aspect, not through a direct cell-to-Self relationship that bypasses the aspect level. Where cross-level access per B1.19 occurs, verify that it follows governed access patterns per B2.96 rather than constituting an architectural collapse of the aspect level.
- **Aspect-Self boundary:** Aspects operate within Selves — they are held as facets of the Self's integration architecture. Verify that aspects are not floating without Self governance: an aspect whose cells are coordinated and whose purpose is defined should participate in at least one Self's integration architecture, not exist without Self-level governance holding it as a facet of a unified whole. Verify that no entity simultaneously occupies adjacent levels — the same entity cannot be both a cell and an aspect, or both an aspect and a Self, without the level-distinguishability failure already detected in Test 2.

**PASS CONDITION:** Cell-aspect boundaries and aspect-Self boundaries are architecturally maintained. Cells are coordinated by aspects; aspects are held by Selves. Cross-level access per B1.19 follows governed access patterns per B2.96. No entity simultaneously occupies adjacent levels.

**FAIL CONDITION:** Two primary failure forms. First, cells integrated directly into the Self without aspect mediation — the aspect level has been bypassed, and the Self is composed directly of cells. This is B3.03 Form 1 from the integration direction: the Self scope is present, the cell scope is present, but the aspect level has collapsed. Second, aspects that exist without Self-level governance — coordination arrangements of cells whose purpose is defined but which are not held within a Self's integration architecture. This is B3.03 Form 3 from the coordination direction: coordination is happening but without the integration architecture that holds the coordination perspectives as facets of a unified whole.

**REMEDIATION SIGNAL:** Flat Architecture (B3.03) Form 1 (missing aspects) if cells are directly integrated into Selves. Flat Architecture (B3.03) Form 3 (missing Self integration) if aspects are not held within a Self. In either case, the remediation path is to introduce the missing structural relationship through governed origination per B1.06 — creating the aspect-level entity that mediates between cells and Self, or extending the Self's integration architecture to hold the floating aspects. The cross-level access patterns per B2.96 that allow the Self to access cells directly when purpose requires (§5.2 of the source paper) are governed access exceptions, not architectural absence of the aspect level; distinguishing governed access exceptions from level collapse requires verifying that the aspect-level substrate content and membership records are present even where direct access occurs.

---

## 7. Composite result and connected anti-patterns

All five tests must pass for full B1.02 operational test passage. The tests are not independent in the sense that one failure often predicts others: a deployment that fails Test 1 (absent level) will predictably fail Test 5 (level-boundary integrity) for the same reason; a deployment that fails Test 2 (level-distinguishability) will predictably fail Test 4 (level-distinct scope) because undifferentiated entities cannot carry differentiated governance scope. The test suite is designed to be administered in the order presented — Tests 1 and 2 are presence and identity tests that establish whether the structural commitments exist at all, Tests 3 and 4 are substrate and governance tests that establish whether the structural commitments are implemented correctly, and Test 5 is the boundary test that establishes whether the implementation is architecturally integrated without level collapse.

Three anti-patterns are the primary diagnostic outputs of this test suite:

**B3.03 Flat Architecture** is detected by Tests 1, 3, and 5. It describes deployments that nominally assert three-level structure but instantiate only one or two levels in practice — most commonly either a flat cell architecture without aspects, or a cell-and-aspect architecture without Self integration. Flat Architecture is the most consequential failure because it voids the Self-level commitment on which Paper 2's instinct/reasoning separation depends.

**B3.29 Cross-Level Confusion** is detected by Test 2. It describes deployments in which individual entities span multiple levels simultaneously — an entity that both executes specific informational tasks and coordinates cells, or an entity that both coordinates cells for a purpose and integrates aspects. Cross-Level Confusion is architecturally silent until functional testing is performed; it is not visible from level-determination records alone, which is why the functional sub-tests in Test 2 are applied regardless of record content.

**B3.18 Intrinsic Type Assignment** is detected by Test 2's comparison between functional test results and B2.85 level-determination records. It describes deployments in which level-determination records are authored from nominal designation — this entity is a cell because it is called a cell — rather than from functional behavior. Intrinsic Type Assignment is a failure of the authoring process rather than a failure of instantiation: the entities may be correctly implemented, but the records that govern them are mis-authored, causing governance scope to mis-apply silently.

A deployment that passes all five tests has demonstrated that its three-level structure is instantiated, functionally distinguishable, substrate-resident, governance-scoped, and boundary-maintained — the five operational properties that B1.02's architectural commitment requires.

---

## Source citations

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance." April 2026. §5.2 (three architectural levels and relational role membership), §5.3 (DNA and action layers), §6.2 (governed origination).

Li, Wenxin. "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems." April 2026. §2.3 (human-governed as authority-not-labor), §3.3 (governance is an authority architecture), §4.1 (substrate/LLM division at governance boundary), §7.4 (non-specialist governance).

## Self-citation

This note is part of the CKS Derivation Notes series. Related notes in the B5 operational-test phase include B5.01 (operational test conventions for Series B), B5.02 (operational tests for B1.01 instinct/reasoning separation), and B5.04 (operational tests for B1.09/B1.10/B1.11 lifecycle primitives). The B2.07–B2.10 operational-variant notes (planned) provide the detailed decompositions from which this note's test mechanisms are drawn. B3.03 (Flat Architecture), B3.18 (Intrinsic Type Assignment), and B3.29 (Cross-Level Confusion) are the anti-pattern formalizations whose detection criteria this test suite operationalizes.
