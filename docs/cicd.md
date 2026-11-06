# CI/CD sugerido

La automatización debe dar confianza sin convertir el curso en una clase de configuración de herramientas. El pipeline mínimo para cada repositorio de estudiante puede ser:

1. **Validate:** estructura esperada, Markdown, nombres y enlaces.
2. **Quality:** formato, lint y pruebas unitarias de transformaciones o consultas.
3. **Data checks:** esquema, nulos, rangos, duplicados, frescura y contratos.
4. **Build:** empaquetar documentación, dashboard exportable o artefactos del proyecto.
5. **Deploy:** publicar únicamente después de revisión; separar ambientes dev/staging/prod.
6. **Observe:** registrar métricas, fallas, costo y fecha de revisión.

## Opciones de implementación

- **GitHub Actions:** opción recomendada para el repositorio del curso; fácil de compartir y suficiente para validaciones, Python/SQL y documentación.
- **GitLab CI/CD:** buena alternativa si el curso requiere runners propios o una experiencia integrada de repositorio, registry y despliegue.
- **Azure DevOps Pipelines:** apropiado cuando el caso usa Azure, Power BI, Fabric o controles empresariales.
- **dbt Cloud + GitHub Actions:** útil para enseñar transformaciones, tests de datos, documentación y despliegues separados.
- **Snowflake Tasks/Streams + CI externo:** útil para discutir qué debe vivir en la plataforma y qué debe vivir en el repositorio.

## Reglas de seguridad y costo

Nunca guardar secretos, tokens, datos personales o credenciales en el repositorio. Usar datos sintéticos o anonimizados, permisos mínimos, entornos separados y límites de costo. Un pipeline que despliega automáticamente también necesita rollback, revisión y una forma de detenerlo.

El workflow inicial [`ci.yml`](../.github/workflows/ci.yml) valida que exista el esqueleto mínimo y sirve como punto de partida.
