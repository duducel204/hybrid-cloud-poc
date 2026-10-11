# Base de conhecimento técnico-científico

**Fonte de verdade estruturada:** os arquivos `data/*.json`. Esta pasta não é uma coleção de prompts, nem uma transcrição da conversa.

## O que já está preenchido

- `sources.json`: catálogo de fontes **identificadas e verificadas** em páginas oficiais ou publicações científicas; acesso ao resumo não significa leitura integral de uma norma.
- `processes.json`: fases da ribeira ao wet blue e mecanismos/saídas por fase.
- `chemistry.json`: espécies e classes químicas, papel por etapa, condições e alertas.
- `knowledge.json`: afirmações técnicas atômicas, cada qual com fonte, contexto e limite.
- `evidence.json`: resultados empíricos quantitativos ou comparativos, sem extrapolação.
- `models.json`: equações físicas/algébricas conhecidas com unidades e hipóteses.
- `measurements.json`: grandezas e métodos de medição, inclusive o que **não** demonstram.
- `relations.json`: relações entre etapas e variáveis que seguem com o couro.
- `raw_material_routes.json`: diferenças de condição inicial entre pele salgada e pele verde do frigorífico.
- `process_matrix.json`: matriz etapa → mecanismo → variáveis → modelo → sensor → ensaio → eficiência, com páginas da fonte BASF.
- `mass_balance_cases.json`: quatro balanços históricos com correntes de entrada e saída, incluindo frações de Cr2O3 e massas seca/água.
- `reference_ranges.json`: faixas da CETESB/UNIDO, sempre com denominador e página.
- `reference_formulations.json`: formulações de referência do Anexo 1 UNIDO 2000, **documentais, nunca instruções para operar fulões**.

## Consultar sem infraestrutura

Execute a partir da raiz do repositório:

```bash
python projects/curtimento/kb/query.py validate
python projects/curtimento/kb/query.py stats
python projects/curtimento/kb/query.py balance MB003
python projects/curtimento/kb/query.py balance MB004
python projects/curtimento/kb/query.py search cromo
python projects/curtimento/kb/query.py search rotacao --collection models
python projects/curtimento/kb/query.py build-db --output /tmp/curtimento-kb.sqlite
```

O banco SQLite é **gerado a partir dos JSON versionados**, nunca a base única de verdade. O comando `search` não requer SQLite e funciona sem internet. Para atualizar, edite o JSON, valide e faça commit. Cada afirmação deve permanecer rastreável.

## Política de conhecimento

1. Separar `documentado`, `inferencia_fisica` e `hipotese`; a última vive preferencialmente no documento `docs/04-evidencias-e-hipoteses.md`.
2. Dados quantitativos observados ficam em `evidence.json` com desenho do estudo, condições e limite de interpretação. Nenhuma medição industrial está armazenada aqui.
3. Fontes com acesso limitado (normas ISO) têm apenas seu **escopo público resumido**, não o conteúdo integral reproduzido.
4. Os dados numéricos de UNIDO/CETESB são **cenários de referência**: a igualdade do balanço não é prova de comportamento real de qualquer fulão.
5. A UFRGS 2004 está catalogada por resumo e metadados; seu PDF integral não pôde ser aberto nesta atualização.
6. Equações universais (`models.json`) não são modelos calibrados de fulão. Parâmetros não publicados permanecem desconhecidos.
7. Não colocar receitas comerciais confidenciais, identificadores pessoais, fotos privadas, telemetria bruta ou credenciais no repositório público.
8. Ao encontrar fontes divergentes, criar novas afirmações ou marcar a divergência; não substituir silenciosamente a anterior.
9. Nenhum resultado do banco constitui autorização para comando industrial automático ou manipulação de reagentes perigosos.

## Backward e Forward

**Backward:** dado um resultado de qualidade desejado, consultar `processes.outcomes`, depois `measurements` e `models` para saber o que falta medir.

**Forward:** dado um sinal (pH, RPM, potência), recuperar `knowledge`, `models` e `evidence` para estabelecer precisamente o que ele permite e não permite inferir.

É intencional existir conhecimento descrito apenas qualitativamente: atribuir uma constante numérica sem fonte seria criar uma falsa precisão.
