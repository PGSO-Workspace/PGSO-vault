# Figuras para presentar el OE2

Base: Project Charter, OE2 y sus indicadores I1–I4. Las vistas 4+1 ayudan a comprobar la cobertura; no requieren un diagrama adicional por cada escenario.

| Diagrama | Cobertura | Archivo / estado |
|---|---|---|
| C4 contexto | OE2-I1 | [SVG](pgso-c1-context.svg) · [PNG](pgso-c1-context.png) |
| C4 contenedores | OE2-I1 | [SVG](pgso-c2-containers.svg) · [PNG](pgso-c2-containers.png) |
| C4 componentes y contratos | OE2-I1 / lógica | [SVG](pgso-c3-components.svg) · [PNG](pgso-c3-components.png) |
| Máquina de estados | OE2-I2 / lógica | [Original existente](pgso-lifecycle-friendly-es.svg); pendiente de contrastar con el SDK actual |
| Modelo del registro de auditoría | OE2-I4 | Pendiente |
| Dependencias entre crates | Desarrollo | Pendiente de una versión compacta en el vault |
| Secuencia de autorización | Procesos y escenarios | [Protocolo existente](pgso-invocation-protocol.svg); pendiente de contrastar con el SDK actual |
| Despliegue de referencia | Física | Pendiente |

Completar con una tabla de contratos (tipos, entradas, salidas, errores) y otra de garantías con criterios de verificación (OE2-I3). Un diagrama de componentes no reemplaza esas especificaciones.

C1 identifica al agente de voz como consumidor de PGSO. C2 detalla el adaptador Python y el proceso Rust de la integración experimental `public_voice`; no representa la instalación de Sami ni un despliegue obligatorio. El SDK también admite integración como biblioteca.

C3 muestra las responsabilidades y contratos del SDK dentro del runtime. La biblioteca coordina `Signal::extract` desde el pipeline; el bridge experimental separa los comandos `extract` y `observe` e inyecta las lecturas. Las flechas de C3 representan dependencias e interfaces, no una secuencia temporal de comandos. La confianza acústica no es una probabilidad calibrada de emoción. Los crates `pgso-actuator-local` y `pgso-actuator-http` ofrecen alternativas de integración; esta vista desarrolla el runtime con `McpActuator`, no enumera todos los adaptadores.

Los tres C4 fueron regenerados mediante PhDude como FIG-a505e15474 y revisados visualmente. Los antiguos C4 del experimento se conservan en `experimental-harness-20260917/`. Los originales de estados y protocolo no fueron corregidos en esta entrega; no presentarlos como revisados.

Fuentes editables: `figures/src/c4/sdk.c4`. Salidas registradas: `figures/out/pgso-c*.svg` y `.png`; esta carpeta contiene copias de presentación. No se ha modificado el manuscript ni aprobado evidencia científica nueva.
