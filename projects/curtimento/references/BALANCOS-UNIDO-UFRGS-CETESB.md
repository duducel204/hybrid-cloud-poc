# Balanços de massa documentados: UNIDO, UFRGS e CETESB

**Estado desta síntese:** UNIDO e CETESB examinados em PDF; UFRGS catalogada por resumo acadêmico, sem texto integral extraído.

## UNIDO 2000, S013

*Mass Balance in Leather Processing*, Buljan, Reich e Ludvik, documento de 30 páginas. [PDF na UNIDO](https://www.unido.org/publications/ot/9654228/pdf).

**Importante:** são cálculos para curtume **hipotético** com peles bovinas salgadas para cabedal, derivados de diferentes dados fabris, literatura e estimativas. As bases são declaradas: 1.000 kg de peles salgadas no início, 1.100 kg de pele caleirada no curtimento (p. 4, 24–25).

### Balanços numéricos informatizados

- `MB001` (p. 7): ribeira sem dividir no caleiro, 18.109 kg nas entradas e saídas.
- `MB002` (p. 7): ribeira com divisão no caleiro, 17.788 kg nas entradas e saídas.
- `MB003` (p. 10): distribuição de **22 kg como equivalente Cr₂O₃**: flor aproveitável 7,5 kg, raspa aproveitável 2,5 kg, sólidos 6,5 kg, efluente 5,5 kg.

A soma no couro aproveitável é 10 kg, ou 45,45% da oferta. **Os 75% mencionados no balanço de curtimento incluem também o cromo que depois acompanha resíduos sólidos**, e não significam 75% de retenção em produto vendável (p. 9–10).

A UNIDO também apresenta (p. 16–17) 149 kg do colágeno do cório em produto acabado sobre 280 kg de referência, ou aproximadamente 53%, e estima (p. 19) 72 kg de químicos em couro sobre 452 kg comprados (~15,9%, arredondado como ~15% pelo relatório). Essas grandezas **não são comparáveis entre si**: cada uma possui denominador e natureza própria.

### Formulação histórica, não receita industrial

`reference_formulations.json` guarda percentuais nominais de seis operações descritas no Anexo 1 (p. 24–25), com a **base de pesagem específica**. São insumos comerciais e banhos de um cálculo histórico. Não contêm controle de segurança, compatibilidade com matéria-prima atual, validação de atividade ou curvas operacionais. Não executar automaticamente.

## Aquim, UFRGS 2004, S014

Dissertação de mestrado de Patrice Monteiro de Aquim, orientada por Mariliz Gutterres, Universidade Federal do Rio Grande do Sul.

- [Registro acadêmico](https://lume.ufrgs.br/handle/10183/5049)
- [Link ao PDF institucional](https://lume.ufrgs.br/bitstream/10183/5049/1/000464394.pdf)

O **resumo acadêmico** confirma o tema: uso de balanços para quantificar perdas e aproveitamento em ribeira e curtimento, visando gestão técnica e redução dos impactos ambiental/econômico. Houve erro/timeout na abertura do PDF, por isso nenhum dado quantitativo foi atribuído à dissertação. **Pendência R001:** obter o PDF completo e extrair tabelas com páginas.

## CETESB 2015, S015

*Guia Técnico Ambiental de Curtumes*, 2ª edição. [PDF CETESB](https://repositorio.cetesb.sp.gov.br/bitstreams/efa182b5-ad26-4778-9a2f-f6028fc8ddfe/download).

- Tabela 7, **página impressa 37**: `MB004`, balanço global em massa bruta, massa seca e massa de água. Entradas e saídas fecham em 21.500 kg brutos, 1.100 kg secos e 20.400 kg de água. A categoria 'outros' reúne líquidos de efluente e outras perdas, não apenas descarte no fulão.
- Tabela 8, **página impressa 38**: ribeira 7–25, curtimento 1–3, pós-curtimento 4–8, acabamento 0–1, total 12–37, unidade **m³ por tonelada de pele salgada**, referenciada à IULTCS 2008a.
- O capítulo sobre tipo de matéria-prima, **página impressa 35**, destaca que pele salgada geralmente requer pré-remolho e lavagens adicionais; pele verde não é simplesmente o mesmo balanço com NaCl zerado.

CETESB apresenta médias e intervalos setoriais, **não dados operacionais deste projeto**.

## Interseção para cálculos

Os quatro casos em `mass_balance_cases.json` fornecem testes de conservação e composição; `reference_ranges.json` oferece contexto dos volumes. O próximo passo é ligar cada corrente a uma etapa do fulão e à definição analítica da espécie. Uma hipótese de economia deve ser testada contra **massa útil de couro e qualidade**, não apenas contra menor efluente.

**Leitura de IA:** para responder a um valor, identificar sempre: fonte, página, processo, matéria-prima, unidade, denominador, limite e se o número é medido, estimado ou modelado.

Exemplo reproduzível sem dependências externas:

```bash
python projects/curtimento/kb/query.py validate
python projects/curtimento/kb/query.py balance MB003
python projects/curtimento/kb/query.py balance MB004
python projects/curtimento/kb/query.py search "ribeira"
```
