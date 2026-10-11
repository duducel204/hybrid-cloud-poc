# Observador físico-químico do curtimento de couros

**Estado:** base de conhecimento estruturada preenchida + investigação de modelagem; **sem hardware instalado nem modelo preditivo calibrado.**

## Para ler do zero (pessoas, scripts e IAs)

1. **[Base de conhecimento pesquisável](kb/README.md)**: conteúdo factual estruturado em JSON; fontes, oito etapas, química, medições, modelos e evidências.
2. [Protocolo de atuação das IAs](AGENTS.md): como consultar e acrescentar conhecimento sem reinventar ou misturar hipóteses e fatos.
3. [Processo e química](docs/01-processo.md) e [modelos físicos](docs/02-modelo-fisico-quimico.md).
4. [Geometria e sensores candidatos](docs/03-sensores-e-geometria.md).
5. [Hipóteses e limites](docs/04-evidencias-e-hipoteses.md).
6. [Forward/Backward](docs/05-metodo-forward-backward.md) e [plano de validação](docs/06-plano-validacao.md).
7. [Referências comentadas](references/README.md) e [schema de observações futuras](schemas/observacao.schema.json).

**Primeiro comando útil:** `python projects/curtimento/kb/query.py search cromo`.
**Verificar integridade:** `python projects/curtimento/kb/query.py validate`.

## Missão

Reutilizar conhecimento já estabelecido na química do couro, física rotativa, transferência de massa e métodos analíticos para construir **modelos calculáveis** da ribeira ao wet blue. As medições reais alimentarão e verificarão os modelos. O valor final é poder calcular eficiência e, depois, projetar mudanças de RPM, volumes, químicos, temperatura e tempo com evidência.

**Primeira fase: receita nominal fixa.** Não otimizar ou alterar operações antes de entender o que ocorre realmente.

## Hipóteses de engenharia em aberto

- Fulão de madeira com dois ladrões/fundos falsos **anulares** nas cabeceiras.
- Malha candidata com quatro módulos por cabeceira, intercalados a 45° (rascunho, não desenho executivo).
- Módulos fixos protegidos, esferas livres como instrumento experimental opcional; sensores externos como referência.
- Fixação com passagem vedada pela madeira para eletrônica/antena rotativa externa.
- Energia por rotação, transferência indutiva, sensores passivos ou alimentação compartilhada, sem opção escolhida.

A base factual está em `kb/data/`; as hipóteses estão em `docs/04-evidencias-e-hipoteses.md`. **Nem o formato dos sensores nem o Wi-Fi substituem a definição matemática do que medir.**

## Relações que não podem ser confundidas

- pH do banho ≠ pH interno da pele.
- Ausência de cromo no banho ≠ cromo fixado.
- RPM ≠ movimento efetivo da carga.
- Potência elétrica ≠ trabalho útil sobre as peles.
- Superfície molhada ≠ imersão no banho renovado.
- Esgotamento ≠ qualidade final.

**Processo científico:** literatura → equações e parâmetros → observações requeridas → previsão com incerteza → verificação por resultados independentes → revisão → só então otimização.

Este repositório público não guarda dados industriais confidenciais nem substitui controle de segurança de um curtume.
