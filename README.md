# Hybrid Cloud PoC

Repositório para execução remota experimental e projetos científico-computacionais.

## Projeto principal

**[Curtimento de couros: base de dados e conhecimento + observador físico-químico](projects/curtimento/README.md)**

- [Base de conhecimento offline](projects/curtimento/kb/README.md): registros versionados em JSON para consulta por IA, Python e pessoas.
- [Fontes científicas, normas e resultados](projects/curtimento/kb/data/sources.json).
- [Etapas, substâncias, fatos e fórmulas](projects/curtimento/kb/data/processes.json).
- [Instruções para agentes de IA](projects/curtimento/AGENTS.md).

A base é factual e rastreável; hipóteses e desenhos de sensores permanecem separados. O SQLite é opcional e gerado localmente.

## Infraestrutura existente (preservada)

- `.github/workflows/cloud-poc.yml`: cálculo sintético ao fazer push em `main` e sob demanda.
- `.github/workflows/benchmark.yml`: benchmark sintético sob demanda.

Esses workflows anteriores **não** calculam eficiência de curtimento. Um workflow adicional de validação da base roda somente quando arquivos do projeto mudam em PR ou sob demanda.
