---
section: methods
status: revised
hash: 7adf87606b59b435d616d9b23f28d3ead268ad7a962798b44a8a48fd06499932
updated: 2026-09-17T20:50:03.181Z
---



## 3.1 Problem identification and motivation

The study organizes artifact construction and evaluation as a design-science investigation [@al2004design]. Its six research activities follow the design science research methodology, which distinguishes demonstrating an artifact from evaluating observed behavior against the solution objectives [@al2007design]. The design problem is the translation of fallible acoustic observations into explicit, reversible intervention state in a tool-augmented agent. Perception accuracy and governance correctness are separate constructs: an accurately executed restriction can still be inappropriate for the task. Accordingly, the evaluation must measure legitimate task completion alongside constraint satisfaction and withheld permitted actions. Recent affective dialogue work motivates the perception-to-action connection, while permissive runtime shielding motivates examining retained capability rather than restriction alone [@mallolragolta2024coupling; @shi2026synthesizing].

## 3.2 Definition of the solution objectives

The artifact has four operational objectives: retain a stable reference during a sustained deviation; keep interventions explicit and removable; check tool authorization at invocation; and expose enough state to reconstruct effective policy transitions. The secondary utility objective is separate: determine whether this orchestration improves independently scored interaction outcomes over an agent receiving the same acoustic information through instructions. Additional contextual information must not be mistaken for an orchestration benefit [@workspace2026independent].

## 3.3 Design and development of the artifact

The design separates observation processing, rule evaluation, effective policy composition, and tool dispatch. The observation processor emits an abstained, nominal, pending, or triggered assessment. Rules map triggered assessments to contributions to the effective catalog and context. The dispatcher applies host permissions independently of these contributions. This separation permits inspection of an acoustic decision without treating that decision as authority to grant a capability [@workspace2026public].

The public-task baseline implementation is pinned to source revision 4a840ba4a581a2640a8c0d3738ac725ea0f6b796. The formal specification below describes that baseline revision and its configured execution path. Earlier results cannot be pooled with new results without checking changes to the mechanism, sample construction, and measurement protocol. Other engineering measurements retain their separately reported revisions. The interaction protocol remains a proposed evaluation until its metered runs are completed.

The design-to-evidence mapping makes the limits of each research activity explicit.

Table II maps the objectives to mechanisms and the evidence required to assess them.

**TABLE II. Design objectives, mechanisms, and evidence boundaries**

| Objective | Artifact mechanism | Required evidence | What that evidence cannot establish |
|---|---|---|---|
| Preserve intervention state under sustained accepted deviations | Frozen reference and same-direction persistence | Long traces including onset, sustained input, recovery, and gaps | Whether the deviation warrants intervention |
| Retire policy effects consistently | Per-axis composition, deduplicated directives, host expiry | Effective catalog/context transitions and corresponding audit records | Whether a particular directive helps a user |
| Enforce current authority at invocation | Host-permission intersection, schema checks, revision-bound approvals | Denial before callback effects, approval replay and transition checks | Safety of execution paths outside the runtime |
| Improve interaction utility | Configured temporal interventions in a shared agent | Independent task outcomes against equally informed alternatives | Human empathy or field effectiveness from simulation alone |

## 3.4 Demonstration as a research activity

The development demonstration connects the Rust runtime to public simulated telecom tasks. The user simulator produces text, which is synthesized into input speech and transcribed for the agent. The same speech supplies acoustic observations. Agent outputs remain textual. This is an input-voice experiment, not a full-duplex speech benchmark. Three fixed development tasks and four treatment arms provide twelve integration sessions. Runs using mocked external generation verify connectivity and accounting; they do not measure dialogue quality or treatment utility [@workspace2026public].

## 3.5 Evaluation

The proposed primary comparison is PGSO against an equally informed instruction-based agent. An uninformed reference agent and an instantaneous-threshold intervention provide secondary comparisons. Each arm receives matched task initialization and model configuration. PGSO and the informed reference receive the acoustic history and its configuration; their difference therefore concerns how the observations are represented and acted upon, rather than access to the observations alone. This comparison still bundles context representation with orchestration, requiring component ablations before attributing an effect to enforcement alone [@workspace2026independent; @workspace2026public].

An optional implementation comparison adds NeMo Guardrails and Invariant at the same public-task boundary. Each integration maintains separate host-authored temporal state from the raw observations and uses its framework policy language to decide candidate calls. The common Rust bridge supplies schema checks, host permissions, and the actual sandbox callback without contributing a paralinguistic decision to these arms. This compares complete integrations under matched policies; it does not attribute the host temporal mechanism to either framework. Offline integration checks at revision 151b6b4 exercise these paths with external generation mocked. At that integration checkpoint, real-generation outcome comparisons remained pending; the later pilot is reported in the results [@workspace2026pgso-3].

The optional AgentSpec arm uses a pinned external checkout of its official parser and interpreter. Active exact-tool rules produce the upstream skip action; the host maintains temporal state and separately records allowance when no rule is active or applicable. This distinction prevents host behavior from being attributed to the upstream implementation. Offline checks exercise the real framework and sandbox with generation mocked, establishing integration behavior but no task-utility estimate [@workspace2026pgso-11].

Shared invocation checks are validity controls in this design. Because all arms use the same host-permission and sandbox boundary, conformance at that boundary cannot establish an incremental benefit of the acoustic controller. Executed domain-policy violations require a separate assessment of the applicable policy clause, dialogue, task state, and actual effect; tool availability alone does not determine domain-policy compliance [@workspace2026pgso-3].

The primary outcome is satisfaction of independent task predicates on the actual final environment. Attempted calls and executed effects are recorded separately. Replaying an attempted call to score the environment would be invalid when that call was denied during the interaction. Secondary outcomes distinguish executed policy violations, permitted actions withheld, unnecessary interventions, recovery delay, and execution overhead. Policy appropriateness must be defined independently of the PGSO output; agreement with PGSO under a perfect input is an autoconsistency measure, not an external correctness oracle.

A later optional evaluator composes supported task-specified reward components from observed state and dialogue. Database targets are constructed in a separate environment using only the task author's reference actions; attempted agent calls are never replayed to reconstruct observed effects. Communication checks reuse the benchmark's required-text matching and do not measure interaction quality. The current command-line pilot still selects the same environment-assertion tasks; broader-domain scoring and transfer have not been evaluated in real-generation sessions [@workspace2026pgso-6].

The proposed appropriateness assessment separates action permission from intervention value. A treatment-blind policy assessment classifies candidate tool effects as permitted, prohibited, or unresolved using the preceding dialogue and actual task state. A separate blinded checkpoint review considers the audio and task context and judges clarification or deferral as required, permissible but not required, or unwarranted. Both assessments must retain their supporting locators and disagreements. These judgments must be specified without access to PGSO decisions; an acoustic threshold cannot supply the reference label. Fixed-checkpoint agreement does not establish closed-loop task benefit. Without independent intervention judgments, the evaluation must report task retention and policy violations rather than intervention correctness. This assessment is proposed and has not been conducted.

Development tasks are excluded from confirmation. Before inspecting confirmatory outcomes, the study must freeze its task sample, intervention policy, practical effect thresholds, failure handling, and analysis. Repeated sessions within a task are dependent observations; window counts must not be presented as independent sample sizes. Task variants derived from the same underlying scenario must also remain together in the prespecified resampling scheme. Variation across model runs on a fixed benchmark and uncertainty about performance on new task populations are different targets; the report must identify which target an interval addresses. A benchmark average alone does not justify generalization to naturally occurring conversations. Temporal misalignment of acoustic observations provides a negative control for the proposed relevance of their timing. Noise and transfer conditions test the limits of any observed benefit. These are protocol requirements, not completed experiments [@workspace2026independent].

## 3.6 Communication

The research record distinguishes implementation checks, development outcomes, and confirmatory evidence. The release must identify source and dependency revisions, task fixtures, model settings, policy parameters, observations, attempted calls, actual effects, exclusions, and analysis commands. This paper uses public benchmark tasks; company recordings and YaVendio conversion outcomes belong to a separate applied study [@workspace2026public].

# 4. Solution

## 4.1 Application of the methodology in the design of the artifact

The resulting pipeline is observation → temporal assessment → rule contributions → effective catalog and removable context → invocation authorization → tool effect and receipt. A host-controlled expiry operation retires stale contributions. Host permissions remain an independent upper bound on available capabilities. This architecture makes the intervention lifecycle inspectable without assuming that acoustic confidence is a calibrated probability of distress or that the language model obeys the resulting directive [@workspace2026public].

## 4.2 Governance mechanism

For each observation axis, let the processor state be \(z_t=(b_t,n_t,k_t,s_t,\tau_t)\), where \(b_t\) is the baseline, \(n_t\) the accepted nominal count, \(k_t\) the current same-direction deviation run, \(s_t\) its direction, and \(\tau_t\) the last accepted timestamp. A reading comprises value \(v_t\), confidence \(q_t\), axis \(a_t\), and timestamp \(t_t\). The processor configuration comprises confidence threshold \(c\), deviation threshold \(\delta\), adaptation rate \(\alpha\), warm-up count \(W\), persistence count \(H\), and optional maximum accepted-reading gap \(G\).

A reading is accepted when the configuration is valid, its value is finite, its confidence lies in \([0,1]\) and is at least \(c\), and its timestamp does not precede the previous accepted timestamp. Rejected readings abstain and leave processor state unchanged. An accepted gap greater than \(G\), when configured, resets the deviation run. The deviation is evaluated against the pre-update baseline:

\[
d_t=\left|v_t-b_t\right|. \qquad (1)
\]

When \(d_t<\delta\), the assessment is nominal, the run resets, and \(n'=n_t+1\). Only this branch updates the baseline:

\[
b_{t+1}=\begin{cases}
\frac{n'-1}{n'}b_t+\frac{1}{n'}v_t,&n'\le W,\\
(1-\alpha)b_t+\alpha v_t,&n'>W.
\end{cases} \qquad (2)
\]

When \(d_t\ge\delta\), the baseline and nominal count are frozen. Define the side indicator \(r_t=\mathbf{1}[v_t>b_t]\). A change of side resets an existing run before incrementing it. The assessment is pending while the resulting run is less than \(H\), and triggered otherwise. Thus a sustained accepted deviation produces a level-triggered assessment on every subsequent qualifying reading. In this implementation, both \(H=0\) and \(H=1\) trigger on the first qualifying reading.

A rule has its own axis, confidence threshold, deviation threshold, direction, and ordered actions. These rule thresholds are additional gates, distinct from the processor thresholds. Rising rules require \(v_t>b_t\); falling rules require \(v_t<b_t\); either-direction rules impose neither directional condition. A matching prune action targeting a rule-engine-protected tool is rewritten to a step-up requirement.

Let \(A_t\) map axes to active rule contributions. An abstained or pending assessment preserves the previous contribution. A nominal assessment removes that axis's contribution. A triggered assessment replaces it with the current matching decisions, removing it if none match. The effective state is recomputed from the nominal catalog and all active contributions: pruning removes unprotected tools, step-up marks tools as requiring approval, and directive text is deduplicated. Recomposition restores effects whose contributions have retired. Effective-state changes are audited; an unchanged repeated observation is not itself a new policy transition.

Silence does not autonomously retire a contribution. The trusted host must invoke expiry with a cutoff timestamp. A contribution survives when at least one of its decisions is at or after the cutoff. This explicit lifecycle avoids attributing wall-clock behavior to a processor that is invoked only when the host supplies an event.

## 4.3 Architecture of the system and deterministic guarantees

The pipeline figure separates observation-driven policy composition from host-controlled invocation and independent outcome scoring. The scorer reads actual environment state; its success criteria are not inputs to the agent or to the acoustic policy.

![Implemented public-task integration. Acoustic observations shape temporal policy, while the invocation boundary combines the current catalog with host permissions before executing a sandbox callback. Original task predicates inspect actual final state; the architecture alone does not establish task benefit.](figures/out/pgso-pipeline-v1.svg){width=6.8in}

Let \(C_t\) be the current governed catalog and \(L_t\) the host-permitted tool set. The served tool set is their intersection. For a request naming tool \(u\), arguments \(x\), session \(s\), and optional approval \(p\), execution requires all applicable conditions:

\[
\begin{gathered}
u\in C_t\cap L_t,\\
s=s_{\mathrm{runtime}},\\
\operatorname{Bound}(u),\\
\operatorname{SchemaValid}(u,x),\\
\operatorname{ApprovalValid}_t(u,x,p).
\end{gathered} \qquad (3)
\]

The binding condition requires that \(u\) is registered with the runtime as a tool binding, so that a handler and an argument schema exist for it; an identifier that is not registered is denied as an unknown tool. The conditions form a conjunction, but the reason the runtime records is the first one that fails, in the order it evaluates them: the trusted clock, the session, the host permission ceiling, the governed catalog, the binding, and then the argument schema. The approval condition is required only for tools currently marked for step-up. An approval binds the tool, exact arguments, and current policy revision; it must be unexpired at the trusted host time. It is single-use. Effective policy changes, permission changes, and detected host-clock rollback invalidate outstanding approvals. Observation-driven policy updates cannot enlarge \(L_t\). The callback executes inside the runtime authorization operation, under the shared runtime lock in the HTTP deployment, so a separately checked permit is not handed to the caller for later execution.

These statements are conditional guarantees of the inspected dispatch path. They require the host to retain control of permissions and approval issuance and to route relevant tool effects through that path. A hostile host, another execution endpoint, or a tool's effects beyond its registered contract are outside this argument. Catalog preservation for a protected tool is also distinct from permission to execute it. The rule engine and actuator expose separate protected sets; consistent configuration is a precondition for claiming their combined step-up behavior.

For a fixed nominal catalog \(C_0\) and a consistently configured protected set \(P\subseteq C_0\), the catalog invariant \(P\subseteq C_t\) follows by induction over policy recompositions. It holds initially. In the inductive step, pruning removes only identifiers outside \(P\); step-up and directive operations do not remove catalog entries. Retirement recomposes from \(C_0\) with the same protected-set exclusion, so it also preserves the invariant. This argument concerns the catalog under the stated transition rules, not arbitrary host reconfiguration or the intersection with host permissions. It does not grant a protected tool unconditional execution authority [@workspace2026pgso-4].

The development pilot uses arousal only, \(b_0=0.5\), \(c=0.5\), \(\delta=0.2\), \(H=2\), \(W=0\), \(\alpha=0\), rising-direction rules, and a 1200 ms maximum accepted-reading gap. Its host invokes expiry using a 1200 ms cutoff before observation and invocation. Consequently, its baseline remains fixed; the pilot does not test adaptation. It uses 800 ms acoustic windows with a 400 ms hop, and logical acoustic timestamps rather than complete interaction wall time. These choices define the development treatment and must not be generalized to all SDK configurations [@workspace2026public].

The reported real-generation development run used the seven configured conditions on the same three public telecom tasks. Model generation, user speech synthesis, transcription and sandbox callbacks were executed; all sessions and stopping outcomes were retained. The sample is a development feasibility check rather than a powered confirmatory utility study. Technical conformance and operational costs are evaluated separately from original task success. Natural-user experience and YaVendio conversion are reserved for a later applied study [@pgso2026da06f686a0].

The initial seven-condition pilot used gpt-4o-mini for the agent and simulated user, with a limit of 30 orchestrator transitions per session. The two subsequent baseline-only development checks used gpt-4.1-2025-04-14 for the agent and a limit of 100 transitions; the user model remained gpt-4o-mini. All used gpt-4o-mini-tts with the alloy voice, gpt-4o-mini-transcribe, temperature zero for agent and user generation, and seed 20260915. A transition is an orchestrator dispatch rather than a complete conversational turn. The identity-resolution iteration additionally appended one general instruction to resolve a resource against the user-supplied identifier before mutation, without supplying task-specific identifiers or expected actions. These changes preclude pooling the iterations into a single treatment comparison [@pgso2026da06f686a0; @pgso2026b0development].
