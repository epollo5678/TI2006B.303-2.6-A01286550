# Documentación del curso

## Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- traducir una necesidad de negocio en requisitos analíticos y arquitectónicos;
- comparar soluciones BI, data platform y ML con criterios explícitos;
- identificar costos, riesgos, deuda técnica, dependencia de proveedor y límites operativos;
- construir evidencia reproducible y comunicar incertidumbre;
- documentar decisiones mediante ADRs y validar sus consecuencias en operación.

## Modelo de decisión

Usaremos el ciclo **Pregunta → Evidencia → Alternativas → Trade-offs → Decisión → Operación → Revisión**. Una buena respuesta no es necesariamente la arquitectura más sofisticada: es la que satisface el contexto con riesgos y costos aceptables.

## Mapa de módulos

| Módulo | Enfoque | Evidencia sugerida |
| --- | --- | --- |
| 1. Decisiones y arquitectura | contexto, stakeholders, ADRs | mapa de contexto y ADR-001 |
| 2. Datos confiables | calidad, gobierno, privacidad, contratos | perfil de datos y data contract |
| 3. BI | dimensionalidad, semantic layer, KPIs | modelo y dashboard narrativo |
| 4. Sistemas distribuidos | batch, streaming, consistencia, resiliencia | diagrama y prueba de trade-off |
| 5. Plataformas | Snowflake y alternativas, costo y lock-in | matriz comparativa |
| 6. Visualización | Power BI, Tableau y diseño de decisiones | prototipo con audiencia definida |
| 7. ML aplicado | evaluación, sesgo, explicabilidad, MLOps | model card y evaluación |
| 8. Operación | CI/CD, observabilidad, seguridad, gobernanza | pipeline y runbook |

## Criterios transversales

Todas las actividades deben preguntar por: valor de negocio, calidad de datos, desempeño, disponibilidad, escalabilidad, seguridad, privacidad, mantenibilidad, costo total, experiencia de usuario, sostenibilidad y reversibilidad de la decisión.

