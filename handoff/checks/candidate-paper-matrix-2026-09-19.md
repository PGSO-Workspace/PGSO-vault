# Matriz de papers candidatos — podada y clasificada por verificación

Las 44 referencias del borrador original `sources/PGSO_Paper.pdf`. El investigador indica que esa bibliografía se construyó con asistencia de IA y que no ha leído la mayor parte de las fuentes. Esta matriz se organiza, por tanto, por **estado de verificación** antes que por tema.

Una entrada generada por IA puede traer un DOI que no resuelve, autoría alterada o un trabajo inexistente. Ninguna de las filas «sin verificar» de abajo se ha comprobado contra una fuente real: no hay red en este entorno y no hay documento local para ellas.

- **Verificadas**: 6. Citadas hoy, con el documento en el vault y el título coincidiendo en su texto.
- **Registradas sin verificar contra documento**: 2.
- **Sin verificar**: 21. Existen solo como entrada bibliográfica del borrador original.
- **Excluidas**: 15, con motivo por fila.

## Verificadas — el núcleo defendible

| Ref | Clave | Título |
|---:|---|---|
| [5] | `zhang2024paralbench` | ParaLBench: A Large-Scale Benchmark for Computational Paralinguistics over Acoustic  |
| [14] | `leem2026describe` | Describe Where You Are: Improving Noise-Robustness for SER with Text Description of  |
| [27] | `mallolragolta2024coupling` | Coupling Sentiment and Arousal Analysis Towards an Affective Dialogue Manager, |
| [34] | `serapiogarcia2025psychometric` | A Psychometric Framework for Evaluating and Shaping Personality Traits in Large Lang |
| [40] | `jia2025coverageguaranteed` | Coverage-guaranteed speech emotion recognition via calibrated uncertainty-adaptive p |
| [42] | `shi2026synthesizing` | Synthesizing Efficient and Permissive Programmatic Runtime Shields for Neural Polici |

## Registradas en el vault, sin citar

Están en el registro, pero eso no significa que alguien las haya leído. Verificar antes de citar.

| Ref | Clave | Título |
|---:|---|---|
| [6] | `eyben2016geneva` | The Geneva Minimalistic Acoustic Parameter Set (GeMAPS), |
| [12] | `geifman2017selective` | Selective Classification for Deep Neural Networks, |

## Sin verificar — no citar hasta comprobar que existen

Primer paso para cada una: resolver el DOI contra Crossref y confirmar título, autores y año. Requiere abrir la red, y esa decisión es del investigador.

| Ref | Título | DOI declarado |
|---:|---|---|
| [1] | A Survey on Speech Large Language Models for Understanding, | `10.1109/jstsp.2025.3640535` |
| [2] | A Large-Scale Evaluation of Speech Foundation Models, | `10.1109/taslp.2024.3389631` |
| [3] | Speech Emotion Recognition in Conversations Using AI: A Systematic Review an | `10.1007/s10462-025-11197-8` |
| [4] | Dawn of the Transformer Era in Speech Emotion Recognition: Closing the Valen | `10.1109/TPAMI.2023.3263585` |
| [9] | Tool Learning with Large Language Models: A Survey, | `10.1007/s11704-024-40678-2` |
| [10] | LLM-Based Agents for Tool Learning: A Survey, | `10.1007/s41019-025-00296-9` |
| [11] | Larger and More Instructable Language Models Become Less Reliable, | `10.1038/s41586-024-07930-y` |
| [15] | Multi-Task Emotion Recognition Based on Dimensional Model and Category Label | `10.1109/access.2024.3404990` |
| [16] | Speech Emotion Recognition via Graph-Based Representations, | `10.1038/s41598-024-52989-2` |
| [17] | ELP-Adapters: Parameter-Efficient Adapter Tuning for Various Speech Processi | `10.1109/taslp.2024.3434445` |
| [18] | Personalized Adaptation with Pre-trained Speech Encoders for Continuous Emot | `10.21437/Interspeech.2023-2170` |
| [23] | Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Hum | `10.1177/1529100619832930` |
| [24] | Tracing Intricate Cues in Dialogue: Joint Graph Structure and Sentiment Dyna | `10.1109/tpami.2025.3581236` |
| [25] | Geng Tu, Feng Xiong, Bin Liang, Hui Wang, Xi Zeng, and Ruifeng Xu. 2024. Mul | `10.1145/3664647.3681515>` |
| [28] | Adapting Virtual Agent Interaction Style with Reinforcement Learning to Enha | `10.3389/fdgth.2025.1680605` |
| [29] | Between Reality and Delusion: Challenges of Applying LLMs to Companion Robot | `10.1007/s10514-02510190-y` |
| [33] | A Study on Classification-Based Concurrent API Calls and Optimal Model Combi | `10.1038/s41598-025-06469-w` |
| [38] | On the Foundations of Noise-free Selective Classification, | **sin DOI** |
| [39] | Reliable Uncertainty Estimation in Emotion Recognition in Conversation Using | `10.1017/nlp.2024.48` |
| [41] | Shield Synthesis: Runtime Enforcement for Reactive Systems, | `10.1007/978-3-662-46681-0_51` |
| [43] | Safety Guardrails for LLM-Enabled Robots, | `10.1109/lra.2026.3667488` |

## Excluidas, con motivo

| Ref | Título | Por qué sale |
|---:|---|---|
| [7] | AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applica | Survey. Cinco surveys en la bibliografía original; ninguno sostiene un argumento del manuscrito actual. |
| [8] | Evaluating LLM-based Agents for Multi-Turn Conversations | Survey. Mismo motivo. |
| [13] | Adversarial Domain Generalized Transformer for Cross-Cor | Redundante con ahn2025multitask, ya citada: misma revista, mismo tema, un año más reciente. |
| [19] | Speaker Normalization for Self-Supervised Speech Emotion | ICASSP 2022: conferencia y fuera de la ventana 2024-2026. No puede servir a la cuota Q1. |
| [20] | Lotfian, Reza & Busso, Carlos. (2017). Building Naturali | Paper del corpus MSP-Podcast. El HANDOFF del MVP registra que ese audio nunca se obtuvo, y el manuscrito actual no lo menciona. |
| [21] | Goncalves, Lucas & Salman, Ali & Naini, Abinay & Moro-Ve | Challenge sobre MSP-Podcast, corpus nunca obtenido ni usado por el manuscrito actual. |
| [22] | The Interspeech 2025 Challenge on Speech Emotion Recogni | Challenge sobre MSP-Podcast, corpus nunca obtenido ni usado por el manuscrito actual. |
| [26] | A Survey on Recent Advances in LLM-Based Multi-turn Dial | Survey. Mismo motivo. |
| [30] | Expressive Mode, | Documentación de producto, no un paper. Sin DOI ni revisión por pares. No cuenta para la cuota Q1 y el proyecto no tiene datos de ese proveedor. |
| [31] | From Language to Action: A Review of Large Language Mode | Review. Mismo motivo. |
| [32] | A Survey on the Optimization of Large Language Model-bas | Survey. Mismo motivo. |
| [35] | Evaluating the Ability of Large Language Models to Emula | Tercera fuente sobre personalidad inducida, en una subsección cuya conclusión es que no se adopta como resultado. |
| [36] | Stick to Your Role! Stability of Personal Values Express | Misma razón: personalidad inducida ya cubierta por serapiogarcia y benzion. |
| [37] | Helpful Assistant or Fruitful Facilitator? Investigating | Misma razón: personas y comportamiento, redundante para lo que el manuscrito afirma. |
| [44] | A multimodal corpus for emotion recognition in sarcasm | Paper del corpus MUStARD++. El original reportaba sobre él; el manuscrito actual mide sobre CREMA-D y no lo menciona. |

## El criterio

La prueba no es si un paper es bueno, sino si el argumento del manuscrito actual se apoya en él. Una referencia que solo engorda un conteo es peor que una bibliografía más corta: cada cita es una afirmación que hay que poder defender cuando pregunten por ella.

Esto choca con el comentario del asesor sobre las 80+ referencias, y el choque se resuelve del lado ya fijado en el handoff: no se puede afirmar haber revisado 80 papers Q1 porque no se hizo. El conteo no es el objetivo.

Nada se añadió ni se quitó del registro de citas al generar esta matriz.