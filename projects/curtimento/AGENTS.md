# Instruções para IAs neste subprojeto

**Aplicação:** qualquer trabalho abaixo de `projects/curtimento/`.

## Inicialização obrigatória

1. Ler `README.md` deste diretório.
2. Ler `kb/README.md`, `kb/data/sources.json`, a coleção matemática `kb/data/models.json` e as coleções pertinentes em `kb/data/`. Consultar `kb/data/mass_balance_cases.json` para valores numéricos documentados.
3. Consultar `docs/04-evidencias-e-hipoteses.md` para não promover hipóteses a fatos.
4. Para projetar novas medições, seguir `docs/05-metodo-forward-backward.md`.

## Regras de execução

- Usar conhecimento já documentado antes de buscar/inventar modelos próprios.
- Fonte e unidade explícitas para afirmações quantitativas. Sem fonte ou calibração, reportar lacuna.
- Não atribuir ganhos de fixação a simples queda de concentração do banho.
- Não inferir estado interno do couro apenas de pH externo.
- Nunca alterar receita, operar máquina ou transmitir comandos de parada com base nesta base.
- Não reescrever arquivo existente para ocultar uma divergência; manter registro verificável.
- Receitas, lotes, telemetria e valores comerciais particulares não entram neste repositório público.
- Ao adicionar conhecimento, atualizar JSON e executar `python kb/query.py validate` a partir deste diretório.
- Para ciência experimental, distinguir resumo confirmado do acesso ao texto integral.

## Quando uma pergunta não tiver resposta

Entregar a relação Forward/Backward: variável-alvo → modelo/fonte → parâmetros → dado ausente → medição candidata e respectivo custo/risco. Não preencher o dado ausente com narrativa.
