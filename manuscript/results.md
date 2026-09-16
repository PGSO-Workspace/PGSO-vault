---
section: results
status: revised
hash: 1c99dc1481c2326a49673b296944df517043b5835a293335e2f6d49083d32c69
updated: 2026-09-16T05:43:26.282Z
---


## 5.1 Configuration

The available measurements comprise three separately versioned activities: an acted-speech extractor diagnostic, an operational comparison of policy implementations, and a public-task integration check. Their experimental units differ. A speaker represented by a complete intensity triplet is the unit of the acoustic diagnostic; a fresh worker-process block is the unit of the operational comparison; and a simulated task session is the intended unit of the interaction experiment. Counts from these activities are not pooled into one sample or presented as interchangeable evidence of utility. Three of the subsections that follow report no measured outcome: 5.4, 5.5 and 5.7 state what the present evidence does not determine, and are retained to mark those gaps rather than to present findings.

The acoustic diagnostic uses extractor revision 60113da and the operational comparison uses revision 7805fb9. The public-task bridge is pinned to 4a840ba. These identifiers describe the measured implementations rather than a claim that every result was produced by the newest release. The public-task integration has been exercised with mocked external generation; metered task outcomes were unavailable at that initial integration checkpoint [@workspace2026pgso-4; @workspace2026public].

## 5.2 Verification of the design guarantees

The archived engineering run records two separate synthetic checks over different denominators, not one sample with a labeled subset. A contract suite reports no mismatch against the declared PGSO temporal contract across 184 labeled steps <!-- result: RESULT-795ec13397 -->, and a fixture-specific check reports no exposure or directive violation across 454 steps <!-- result: RESULT-d86c084124 -->. The run also covers 13 direct-execution scenarios and 14 HTTP cases. The direct-call cases each produced one receipt with the predeclared outcome and reason label. Two fresh processes produced equal normalized governance and execution outputs after excluding the measured duration field [@workspace2026pgso-4].

This evidence supports conformance on the exercised paths. The labels originate in the authored validation executable, so agreement is not an independent estimate of real-world intervention correctness. Likewise, equality across two local processes does not establish bitwise determinism across processor architectures or compiler targets. The receipts distinguish callback outcomes, but several confirmation histories share the same missing-confirmation reason. Reconstructing those histories requires the associated host records rather than the receipt alone [@workspace2026pgso-4].

## 5.3 Characterization of the paralinguistic signal

The recorded CREMA-D diagnostic contains 273 fixed-sentence anger recordings from 91 speakers, with instructed low, medium, and high intensity. Two low-intensity clips abstained, leaving 89 complete non-abstaining speaker triplets. In 87 of those triplets, the heuristic output for the high-intensity recording exceeded that for the low-intensity recording; two differences were negative. Across complete triplets, the median paired high-minus-low output was 0.4388, with a speaker-bootstrap 95% interval of 0.3701–0.4682. Sixty-eight complete triplets were monotonic across all three instructed levels. <!-- result: RESULT-51c41ddbc2 -->

This is evidence of sensitivity to an instructed acoustic contrast in the selected recordings. The labels describe acted anger intensity for one sentence, not continuous arousal, perceived distress, consent, or the need to restrict a tool. The extractor is the SDK's eGeMAPS-style heuristic, not the full openSMILE eGeMAPS feature set or a learned emotion model. Its confidence is a voicing-quality proxy. The comparison therefore cannot establish superior emotion recognition or natural conversational usefulness.

![Paired heuristic outputs for instructed low and high anger intensity in CREMA-D. Each point represents a speaker with a complete non-abstaining triplet; the two incomplete speakers are excluded from this conditional plot.](figures/out/cremad-intensity-v1.svg){width=6.8in}

The interval is conditional on complete triplets. Missing observations remain visible in the run record; a post-hoc bounded sensitivity analysis was recorded separately rather than treating abstentions as observed values. Both the restricted speech setting and this conditioning limit generalization.

## 5.4 Governance correctness vs signal quality

An independent estimate of appropriate governance under imperfect observations is not yet available. Mechanism agreement under an idealized input can check implementation consistency, but it cannot determine whether an observation should have caused an intervention. In the planned task experiment, task predicates and domain permissions provide outcome and authorization checks; they do not label high acoustic activation as a reason for restriction. The technical results do not supply an intervention-appropriateness curve; that construct remains outside the reported conformance assessment [@workspace2026independent].

## 5.5 Ablation of the components of the mechanism

The public-task harness includes an instantaneous-threshold condition and a PGSO condition, and the subsequent real-generation pilot produced no successful task outcomes in either condition. No task-level ablation effect is reported. The planned contrasts must distinguish temporal persistence from contextual information, directive effects, and invocation enforcement; otherwise a bundled treatment difference cannot identify which mechanism contributed [@workspace2026public; @workspace2026independent].

## 5.6 Comparison with prompt based governance

The equally informed prompting condition is implemented in the integration harness. It receives the retained observation history and configuration, while PGSO supplies current removable directives and enforces its configured tool policy. The mocked integration run verifies that both conditions complete the required execution path, not that either produces better conversations. The subsequent real-model pilot measures task success and callback effects, but does not establish independent intervention appropriateness or all permitted actions withheld [@workspace2026public].

The real-generation development pilot compared the same task harness under an ordinary agent, equally informed contextual prompting, an instantaneous threshold, PGSO, and adapters for NeMo, Invariant and AgentSpec. Each condition completed three scored sessions. All sessions reached the configured step limit and no condition satisfied the original final-state task predicates. <!-- result: RESULT-b2e138dc20 -->

Table III reports all configurations in the initial development pilot.

**TABLE III. Initial public-voice development outcomes** <!-- result: RESULT-b2e138dc20 -->

| Condition | Successful tasks / scored sessions | Assistant attempts reaching callbacks |
|---|---:|---:|
| Ordinary agent | 0/3 | 41 |
| Equally informed prompting | 0/3 | 36 |
| Instantaneous threshold | 0/3 | 37 |
| PGSO | 0/3 | 39 |
| NeMo adapter | 0/3 | 34 |
| Invariant adapter | 0/3 | 30 |
| AgentSpec adapter | 0/3 | 34 |

All 251 assistant attempts reached a sandbox callback, with no callback failures or recorded acoustic-policy denials. These counts do not imply that every action was permitted or that hidden tools never suppressed an attempted action. The shared failure floor prevents a task-superiority or equivalence conclusion; the independent experimental unit remains the task, not each model call. <!-- result: RESULT-b2e138dc20 --> <!-- claim: CLAIM-b29a7c7083 -->

A subsequent development check changed the common agent model and step budget; a separate iteration additionally supplied a generic identity-resolution instruction. The former produced one success and one task failure among two scored sessions, with a separate unscored API rate-limit failure. The latter produced two successes and one task failure among three scored sessions. Both retained a wrong-resource mutation and failed the frozen zero-wrong-mutation feasibility criterion. In the latter failed session, the supplied identifier survived transcription, but the agent mutated a resource whose retrieved identifier did not match. These development iterations are reported separately from the seven-arm pilot and provide no treatment-effect estimate [@pgso2026b0development]. <!-- result: RESULT-67f69e86a3 --> <!-- claim: CLAIM-2de8fa81bb -->

## 5.7 Complementary exploration: lexical prosodic divergence

No new independently validated lexical–prosodic divergence outcome is reported in the current evaluation. Earlier exploratory associations cannot establish when a tool intervention is warranted. The present controller does not use lexical–prosodic divergence as its intervention criterion. The acoustic sensitivity results therefore do not establish a discrepancy between literal intent and vocal delivery, and no such discrepancy is treated as permission to restrict an action.

## 5.8 End to end demonstration

The public-task integration check passed seven Python checks, including twelve complete orchestrator sessions across three development tasks and four arms. Those sessions used actual Rust dispatch and sandbox telecom tools with mocked external generation. The integration records attempted calls separately from callback effects and evaluates original predicates on the live final environment. This avoids executing a denied attempted call during a replay-based scoring pass [@workspace2026public].

These checks establish integration behavior on the tested cases. They are not twelve metered pilot observations and do not establish speech-agent utility. The implementation currently uses synthesized input speech and textual agent output, so the demonstration is not a full-duplex voice-agent evaluation.

A subsequent offline diagnostic illustrates a limitation of the configured treatment. Its test source is revision ff8f5ff, while the exercised bridge binary was built from the public-task baseline revision 4a840ba [@workspace2026roaming]. In the selected roaming-repair fixture, sustained injected observations caused the runtime to withhold `enable_roaming`; the attempted call produced no callback effect and the original task predicates remained unsatisfied. After a nominal observation retired the restriction, the same repair executed and the predicates were satisfied. This case suggests that correctly enforced acoustic governance can obstruct a legitimate task. It motivates independent intervention-appropriateness assessment and a recovery policy that does not equate continued acoustic activation with absent user clarification. The diagnostic uses scripted actions and injected observations, so it estimates neither conversational failure frequency nor a treatment effect [@workspace2026roaming].

## 5.9 Latency of the decision core

The newer operational experiment measures a broader integration path than the isolated decision core: parsing, session construction, temporal processing, callback dispatch, serialization, and local pipe transport. It excludes acoustic extraction, language-model inference, and network services. Four implementations each completed twelve process blocks with one hundred measured batches per process. Each batch repeated the same 23 authored scenarios and 96 candidate calls; all implementations executed 68 calls and blocked 28 under the matched contract. Repeated batches are not independent conversational tasks [@workspace2026pgso-4].

Table IV reports the operational measurements under the matched workload.

**TABLE IV. Operational latency and resident memory under matched policy workloads**

| Configured implementation | Batch latency, ms, median of block medians (95% interval) | Warm resident memory, MiB |
|---|---:|---:|
| Minimal Python reference | 0.604799 (0.603863–0.607871) | 12.311 |
| Invariant LocalPolicy | 23.086647 (23.023295–23.171516) | 62.777 |
| NeMo Colang input rail | 425.849599 (425.373111–427.079734) | 68.346 |
| PGSO runtime | 0.515425 (0.512073–0.518055) | 13.127 |

The intervals resample process blocks on the measured Linux virtual host. PGSO had lower batch latency for these configured paths, while the minimal Python reference used less warm resident memory. Differences include programming language and framework facilities; they do not establish an intrinsically faster governance algorithm or the performance of complete commercial products. The measured host, source and dependency revisions, affinity, warm-up, raw timings, and operational protocol are retained with the archived results [@workspace2026pgso-4].

No practical voice-conversation latency improvement follows from this table alone. The subsection's historical heading is retained, but the measurement boundary is explicitly broader than the core and narrower than a complete voice interaction. Independent task outcomes remain necessary to assess whether the intervention layer is useful.
