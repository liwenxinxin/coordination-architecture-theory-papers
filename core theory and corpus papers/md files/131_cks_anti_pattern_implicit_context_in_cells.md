# Anti-Pattern: Implicit Context in Cells — Standalone Formalization of the Failure Mode Where Cell Behavior Depends on Environmental, Runtime, or Configuration Context Not Captured in Substrate, Violating the Determinism Contract in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize, as a standalone derivation, the anti-pattern in which cell behavior depends on environmental, runtime, or configuration context held outside both the substrate and the cells themselves — violating the determinism contract directly through the cell-behavior-determinism guarantee, exceeding the bounded non-determinism categories the source paper permits, and breaking the determinism boundary at substrate operations.

## Abstract

The CKS determinism contract commits substrate operations to being deterministic from substrate state, with non-determinism bounded to specific allowed categories: LLM outputs within rule-governed cells, external-system responses through consultation patterns, and time-of-day expressed through substrate-recorded timestamps. This note formalizes the anti-pattern in which cells consume context outside the substrate-cell boundary — environment variables not promoted to substrate, runtime configuration that varies across deployments, system clock for non-timestamp logic, locale and timezone defaults, machine-specific paths and hostnames, deployment-environment differences without substrate-resident specification, and language-runtime defaults that vary across versions. Cells consuming such context behave non-deterministically from substrate state alone: identical substrate produces different cell outputs across environments, machines, runtimes, or configurations. The note states the four operational components of the anti-pattern, the CKS commitments violated, the failure mode, the architectural correction, four adjacent legitimate patterns it must be distinguished from, and an operational test with three sharpening properties. The anti-pattern is architecturally distinct from cell-internal-hidden-state (treated separately): hidden state lives inside cells; implicit context lives in the runtime environment outside both substrate and cells. The two compound when cells cache implicit context internally, but the failure loci differ.

## 1. Why a standalone formalization is needed

The determinism contract permits a narrow band of non-determinism: LLM outputs within rule-governed cells, external-system responses through consultation patterns, and time-of-day expressed through substrate-recorded timestamps. Anything outside these categories is not part of the contract's permitted variability.

The implicit-context-in-cells anti-pattern is the operational form in which this bound is exceeded by sources the surrounding engineering culture treats as routine. Modern application frameworks expose environment variables by convention; deployment platforms inject metadata cells access implicitly; language runtimes carry version-specific behavior; system libraries default to host locale and timezone; "convention over configuration" patterns encourage exactly the implicit consumption the contract rules out. A cell that reads the host timezone for date formatting, that consults `NODE_ENV` to switch behavior, that uses the system clock to decide whether a record is expired, that parses a date with the host locale's collation rules, or that branches on hostname to differentiate dev from staging — each is, under the contract, a determinism violation. None of these patterns is unusual. That is precisely why the anti-pattern needs to be named.

The contract has five guarantees; this anti-pattern most directly violates Guarantee B (cell-behavior determinism). Naming the unique violation lets the failure be addressed surgically rather than blurred into a generic "non-determinism" complaint, and places the configuration-as-determinism-violation territory into the public record for prior-art purposes.

## 2. The anti-pattern, defined precisely

A deployment exhibits the anti-pattern when cell behavior depends on context that is neither substrate-resident nor cell-execution-scoped — context held in the runtime, environment, or system layer external to both substrate and cells. The failure has four operational components.

**(a) Cell behavior depending on environment or runtime context not substrate-resident.** The cell reads environment variables, deployment metadata, runtime configuration, or process-launch parameters; cell behavior depends on what it reads. Common instantiations: feature-flag environment variables consulted at execution time, deployment-platform metadata read for behavior switching, configuration files loaded from filesystem paths the substrate does not record.

**(b) Cell behavior depending on system clock for non-timestamp logic.** The cell uses system time to make decisions, not merely to record when something happened. The decision logic — "is this expired now," "what is today's batch," "which time-of-day routing applies" — reads the host clock rather than substrate-recorded timestamps. Recording a timestamp during a substrate write is not the failure mode; using current host time to drive a logical branch is.

**(c) Cell behavior depending on locale, timezone, or language-runtime defaults.** Parsing, formatting, comparison, or computation logic depends on host locale, host timezone, system collation, or version-specific runtime behavior. Date strings parse differently across locales; numeric formatting follows host conventions; string comparison follows host collation; runtime-version differences propagate into cell output.

**(d) Cell behavior varying across deployment environments without substrate-driven differentiation.** The cell behaves differently in dev, staging, and production based on implicit detection — `NODE_ENV`-style flags, hostname patterns, cloud-provider metadata, environment-specific config-file presence. The differentiation is not specified in substrate; it is read from the runtime context the cell happens to execute in.

A deployment exhibiting any one of (a)–(d) partially exhibits the anti-pattern; a deployment exhibiting all four exhibits it fully.

## 3. Which CKS commitments are violated

The anti-pattern violates a structured set of commitments, with one guarantee uniquely violated and others cascading.

**Determinism contract (parent commitment) — directly violated.** The contract commits substrate operations to being deterministic from substrate state. Implicit-context-in-cells introduces variability through context outside the determinism boundary.

**Cell-behavior determinism (Guarantee B) — uniquely and most directly violated.** The guarantee commits that cell behavior is deterministic from substrate input. Implicit context drives cell behavior from inputs that are not substrate; the guarantee fails surgically at this layer.

**Read determinism (Guarantee A) — extended-violated.** Substrate reads themselves may remain deterministic, but cell processing of those reads is non-deterministic because implicit context modulates what the cell does with what it reads.

**Change addressability (Guarantee C) — extended-implicated.** Changes produced by cells operating on implicit context may not be re-applicable when implicit context differs across environments, runtimes, or timezones.

**Conflict preservation (Guarantee D) — extended-implicated.** When implicit context affects conflict-handling logic (e.g., locale-dependent comparison of records), conflict states may be silently collapsed differently across environments.

**Substrate as source of truth (Guarantee E) — extended-implicated.** If implicit context determines authoritative behavior, "what is currently the case" requires consulting the runtime in addition to substrate.

**Allowed non-determinism categories — directly violated.** The bounded categories are exhaustive. Implicit context introduces non-determinism beyond them; the architectural commitment to bounded variability fails.

**Determinism boundary at substrate operations — directly violated.** When cell behavior depends on context outside the boundary, the closure is broken; the boundary no longer demarcates a determinism-preserving region.

**Path retraceability — extended-implicated.** Changes produced by cells operating on implicit context cannot be fully retraced; the trail has gaps where the rationale is "the environment was X" rather than substrate-resident.

**Human-governed — extended-implicated.** Implicit context is not substrate-resident and cannot be governed through inspect, modify, and override rights over substrate content and orchestration rules. Humans may govern the runtime through deployment processes, but those are procedural promises, not architectural rights.

**Tool-agnosticism — extended-implicated.** Implicit context creates dependency on specific runtime, environment, or deployment characteristics; coordination behavior is no longer portable across commodity tooling.

**AI-as-substrate-mediator — extended-implicated for LLM-based cells.** When LLMs operate within cells consuming implicit runtime context, the mediator role is compromised: the LLM's behavior over the substrate now depends on environment in addition to substrate, exceeding the mediator's substrate-relevant-state property.

## 4. The failure mode

Implicit context produces deployments where cell behavior is non-deterministic from substrate state alone. Two deployments holding bit-identical substrate may diverge because one runs in `America/New_York` and the other in `UTC`, or one on Node 20 and the other on Node 22. Re-applying a substrate change in a different environment may produce different results, breaking change addressability when implicit context was a hidden input. Cells behave differently across dev, staging, and production based on implicit detection that cannot be inspected, modified, or overridden from substrate. Diagnosing incorrect behavior requires reproducing the runtime — locale, environment variables, system clock, language-runtime version — degrading substrate-as-inspectable-artifact. Migrating between machines, cloud providers, language runtimes, or operating systems may produce behavior changes with no substrate explanation; tool-agnosticism fails operationally.

LLM-based cells consuming implicit runtime context introduce variability beyond their own output non-determinism; the compound effect exceeds what the bounded categories permit. Cells reading the system clock for logic decisions produce different behavior at different real-world times against identical substrate — "is this record expired" returns different answers without any substrate change. String comparison, date parsing, and numeric formatting produce inconsistent results across locales without substrate-side explanation. When the runtime context has changed, reproducing a failing state may be impossible; substrate-as-source-of-truth is undermined.

The anti-pattern compounds with cell-internal hidden state. When cells cache implicit context internally — reading an environment variable once at startup and storing it in a cell-resident variable — the deployment exhibits both implicit-context dependency (this anti-pattern) and hidden-cell-state dependency (a separate anti-pattern at a different locus). The compound failure is severe because the implicit context becomes both invisible to substrate and persistent across executions.

## 5. The architectural correction

The correction operates through three foundational commitments together: cell-behavior determinism per the determinism contract, bounded non-determinism per the allowed categories, and substrate-resident context as the architectural source of any context affecting coordination.

**Cell-behavior determinism.** Cells read substrate at invocation; the substrate read provides all context the cell needs; cell behavior produces consistent outputs from consistent substrate inputs. Cells must operate identically across environments, machines, and runtimes given identical substrate state.

**Bounded non-determinism.** Non-determinism is restricted to the allowed categories: LLM outputs within rule-governed cells, external-system responses through consultation patterns, and time-of-day through substrate-recorded timestamps. Implicit context is not in these categories.

**Substrate-resident context for coordination behavior.** All context affecting coordination must live in substrate. Environment variables, runtime configuration, locale, timezone, and similar context are promoted to substrate when they affect coordination behavior.

A correctly architected deployment additionally promotes environment-affecting context to substrate (cells read substrate configuration; orchestration rules specify how the configuration affects behavior); uses substrate-recorded timestamps for time-based logic (where a cell needs current-time semantics, current time is provided as a substrate-recorded input by the orchestration rule that invoked the cell); abstracts language-runtime and machine-specific dependencies behind substrate-defined contracts (where the runtime version itself affects coordination, the version is substrate-recorded); specifies multi-environment behavior through substrate-resident environment specification rather than implicit hostname or env-var detection; substrate-binds locale and timezone where cells need them; and maintains a cell-portability audit verifying that cells produce identical behavior across environments given identical substrate.

## 6. What the anti-pattern is NOT

Four adjacent legitimate patterns are commonly conflated with implicit-context-in-cells.

**Not substrate-resident configuration that cells read at invocation.** Configuration that lives in substrate and that cells read at invocation is legitimate architecturally and is in fact part of the correction. The anti-pattern arises specifically when configuration is held in implicit runtime/environment context rather than substrate.

**Not cell-execution-scoped variables that do not affect coordination outcome.** Cells using runtime variables for internal computation — scratch values, intermediate parsing results, ephemeral counters — that are scoped to a single execution and do not affect coordination outcome are legitimate. The anti-pattern is about coordination-affecting context.

**Not allowed non-determinism within bounds.** The allowed non-determinism categories are legitimate by construction. The anti-pattern is non-determinism *beyond* these categories. A cell that produces variable LLM output within a rule-governed envelope is not exhibiting implicit-context-in-cells; a cell that branches on host timezone is.

**Not cell consultation of substrate-resident environment context.** A cell reading "this deployment's timezone is recorded in substrate as `America/New_York`" and using that to drive formatting is legitimate. Reading the host's `TZ` environment variable for the same purpose is the anti-pattern. The distinction is whether the context lives in substrate or in the runtime environment.

## 7. Why the anti-pattern is load-bearing

The violation is surgical: cell-behavior determinism is the specific guarantee uniquely compromised, and the bounded non-determinism categories are specifically exceeded — the contract's commitment to bounded variability fails surgically, not generically. The failure surface is operationally common because modern application frameworks, deployment platforms, runtime systems, and the "convention over configuration" pattern produce implicit-context dependencies by default. The failure compounds with adjacent anti-patterns: with cell-internal hidden state when cells cache implicit context; with cell-as-substrate when implicit context becomes cell-resident state used for coordination; with LLM-as-source-of-truth when LLM cells use implicit runtime context to generate authoritative-looking outputs. The anti-pattern uniquely affects deployment portability — tool-agnosticism fails for a specific architectural reason rather than an incidental engineering one. The four operational components are inspectable through architectural review, and the architectural correction is specific.

## 8. Operational test

A deployment exhibits implicit-context-in-cells if any of the following are true at any time during the deployment's existence.

1. Cell behavior depends on environment variables, runtime configuration, or deployment metadata that is not substrate-resident.
2. Cell behavior depends on system clock reads for non-timestamp decision logic — expiration checks, time-of-day routing, "today" determinations — using host time rather than substrate-recorded timestamps.
3. Cell behavior depends on locale, timezone defaults, language-runtime defaults, or system collation that varies across environments.
4. Cell behavior varies across deployment environments based on implicit environment detection (hostname, env-var flags, cloud-provider metadata) rather than substrate-resident environment specification.

Three sharpening properties make the test operationally usable.

**(a) Cell-behavior-environment-portability test.** Verify that cells produce identical behavior across environments given identical substrate state. Run the same cell over the same substrate in two environments differing only in runtime context (timezone, locale, environment variables, runtime version); behavior differences indicate the anti-pattern.

**(b) Implicit-context-substrate-promotion test.** Examine cell dependencies. For every input the cell consumes, the input must be either substrate-resident or cell-execution-scoped-and-coordination-irrelevant. Reads from environment variables, deployment metadata, system properties, host configuration, or process-launch parameters indicate implicit context that must be substrate-promoted or eliminated.

**(c) System-clock-vs-substrate-timestamp test.** Examine time-related cell logic. For every time-related branch, the cell must read substrate-recorded timestamps rather than the host clock. System clock reads driving logic decisions — as opposed to recording timestamps on writes — indicate the anti-pattern.

A deployment that fails any of (1)–(4) and any of (a)–(c) exhibits the anti-pattern.

## 9. The one-sentence test

If a deployment's cells depend on context external to both substrate and cells — environment variables not promoted to substrate, runtime configuration that varies across deployments, system clock for non-timestamp logic, locale or timezone defaults, machine-specific paths or hostnames, deployment-environment differences, or language-runtime defaults — and cell behavior varies based on that context such that identical substrate produces different cell outputs across environments, machines, runtimes, or configurations, the deployment exhibits implicit-context-in-cells; the determinism contract is directly violated, with cell-behavior determinism uniquely compromised, the bounded non-determinism categories exceeded, the determinism boundary at substrate operations broken, and human-governance over the variable inputs operationally foreclosed because the inputs are not substrate-resident and cannot be governed through the architectural rule-mediation mechanism.

## 10. Why naming the anti-pattern as standalone matters

Implementations under pressure to deliver AI products with environment-aware capabilities consistently default to implicit-context-in-cells because the surrounding engineering culture treats environment-variable consumption, system-clock reads, and host-locale dependence as standard practice. The drift is steady because audiences understand "we read environment variables" or "we use the system timezone" as ordinary engineering, without recognizing the architectural consequence: the determinism contract fails specifically through cell-behavior determinism, with cascading implications across the contract's other guarantees and across path retraceability, tool-agnosticism, and human-governed authority.

Naming the failure mode as a standalone anti-pattern gives downstream readers a precise specification of the failure and its correction. Implementations may be audited against the specification, corrected against it, or argued with on its terms. This note covers the anti-pattern at the determinism-contract position; subsequent notes in the same Phase A3 sequence formalize anti-patterns at other foundational commitments — composition-layer failures and tool-agnosticism failures — that compound earlier failure modes. Each anti-pattern formalized as standalone narrows the territory in which environment-aware AI coordination, deployment-adaptive AI architectures, or runtime-context-sensitive AI agents can be claimed as novel without bumping into the prior-art chain.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Anti-Pattern: Implicit Context in Cells — Standalone Formalization of the Failure Mode Where Cell Behavior Depends on Environmental, Runtime, or Configuration Context Not Captured in Substrate, Violating the Determinism Contract in CKS.* May 6, 2026. ORCID: 0009-0004-8065-3235.
