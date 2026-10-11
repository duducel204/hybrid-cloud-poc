# Fontes e proveniência

## Catálogo canônico

**[kb/data/sources.json](../kb/data/sources.json)** contém fontes com ID estável (S001 etc.), URLs, escopo e grau de acesso. **[kb/data/knowledge.json](../kb/data/knowledge.json)** liga afirmações às fontes, **[kb/data/evidence.json](../kb/data/evidence.json)** registra resultados experimentais.

Fontes prioritárias já identificadas:
- BREF europeu para curtumes (JRC, 2013): [entrada S001](../kb/data/sources.json).
- *Fabricação Moderna de Couro Vacum* (Leather Naturally/Buckman): S002.
- Lin, Jiang, Wang, Zeng, Xie, Shi (JALCA, 2023): S003. DOI `10.34314/jalca.v118i11.8242`; resultado de 41% refere-se ao **tempo em movimento rolling**, não à absorção.
- ISO 4045:2018 (pH do extrato aquoso do couro), ISO 5398-1:2018 (cromo total no couro) e ISO 3380:2015 (retração até 100°C): S008–S010; resumos oficiais, **não** reprodução de normas.
- ISO 4684:2005 (matéria volátil, não teor exato de água): S011.

## Estudos de balanço de massa incorporados

- **S013, UNIDO 2000:** cenário de balanços da ribeira ao acabamento. Dados de massa por corrente, repartição de Cr₂O₃ (p. 10) e formulação por base de pesagem (Anexo 1, p. 24–25). Texto integral consultado.
- **S014, Aquim/UFRGS 2004:** dissertação sobre balanço de massa da ribeira e curtimento. Resumo e metadados consultados; não foram extraídos resultados quantitativos não verificados.
- **S015, CETESB 2015:** Guia Técnico Ambiental de Curtumes, 2ª edição. Tabela 7 (p. 37) com balanço global, Tabela 8 (p. 38) com intervalos de água e texto sobre pele verde/salgada.
- [Comparação e limitações de leitura](BALANCOS-UNIDO-UFRGS-CETESB.md)
- [Balanços de referência em JSON](../kb/data/mass_balance_cases.json)

## Materiais exploratórios compartilhados

- *IoT no Curtimento de Couros: Automação e Benchmarking*, 17 páginas (2026-10-11).
- *Pesquisa aprofundada: o fulão como sistema físico-químico inteligente*, Relatório 1 (2026-10-11).
- Conversas, esquemas e definições do usuário: geometria do ladrão anular, distribuição candidata 4+4, energia por rotação, Forward/Backward, receita nominal fixa.

Os materiais compartilhados ajudam a localizar hipóteses e fontes. **Não foram copiados integralmente** ao repositório público. Informações de fonte primária passaram por checagem antes de integrar o catálogo factual.

## Próxima extração bibliográfica

Cada novo artigo deve ter: fonte, DOI/URL, condição experimental, equipamento, pele, método, grandeza, unidade, intervalo, incerteza, resultado observado e limite de extrapolação. Sem esses dados, não usar valores como calibração industrial.
