# Hybrid Cloud PoC

Repositório de experiências de execução remota e projetos técnico-científicos.

## Projetos

- **[Observador físico-químico do curtimento de couros](projects/curtimento/README.md)**: integrar química, mecânica, instrumentação e cálculo para compreender a eficiência real da ribeira ao wet blue.

## Infraestrutura existente (preservada)

- `.github/workflows/cloud-poc.yml`: cálculo sintético executado em push na `main` ou sob demanda.
- `.github/workflows/benchmark.yml`: benchmark sintético sob demanda.

Esses workflows **não** executam modelos de curtimento nem analisam dados industriais. Não há integração com fulões ou hardware neste momento.

O desenvolvimento de curtimento é documentado isoladamente em `projects/curtimento/`. Alterações devem preservar o isolamento entre evidência, hipótese, cálculo e decisão operacional.
