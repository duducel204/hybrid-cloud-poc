# Observador físico-químico do curtimento de couros

**Estado:** fundação documental / exploração técnica; nenhum modelo preditivo ou hardware validado.

## Missão

Transformar conhecimento químico e físico disponível na literatura em **modelos calculáveis** de processamento de peles em fulões. Confrontar previsões com dados industriais, observar o comportamento mecânico do banho/couros e, quando houver evidência suficiente, explorar condições de processo mais eficientes.

O objetivo vai além do monitoramento: calcular eficiência de **água, tempo, produtos químicos, energia, transporte, penetração, fixação e qualidade**, considerando efeitos entre etapas.

## Decisões e limites atuais

1. **Primeira fase: receita nominal fixa.** Compreender a eficiência da execução antes de propor mudança de dosagem, tempo, RPM ou temperatura.
2. **Escopo inicial:** remolho → depilação/caleiro → descarne/divisão conforme a rota → desencalagem → purga → píquel → curtimento ao cromo → basificação → wet blue.
3. **Instrumentação candidata:** dois ladrões/fundos falsos anulares nas cabeceiras de um fulão de madeira; quatro módulos por cabeceira, intercalados em 45° como **rascunho**, além de medições externas e, se útil, uma esfera livre experimental.
4. **Não confundir:** pH do banho ≠ pH no interior da pele; cromo ausente do banho ≠ cromo fixado; potência do motor ≠ trabalho efetivamente transmitido ao couro; sensor molhado ≠ sensor submerso.
5. **Comunicação e energia:** fixação passante na madeira para conectar antena e eletrônica externa rotativa; geração pela rotação, alimentação indutiva e sistemas passivos seguem como alternativas, não decisões aprovadas.
6. **Nenhuma parada automática** será baseada em estimativas não validadas; funções críticas permanecem nos controles industriais próprios.

## Índice: ordem de leitura para pessoas e IAs

1. [Processo e química](docs/01-processo.md)
2. [Modelo matemático e estados](docs/02-modelo-fisico-quimico.md)
3. [Geometria e opções de sensores](docs/03-sensores-e-geometria.md)
4. [Evidências, hipóteses e erros a evitar](docs/04-evidencias-e-hipoteses.md)
5. [Protocolo Forward/Backward](docs/05-metodo-forward-backward.md)
6. [Plano de validação industrial](docs/06-plano-validacao.md)
7. [Catálogo de fontes](references/README.md)
8. [Contrato de medição JSON](schemas/observacao.schema.json)

## Pergunta nuclear

> Com os modelos publicados, parâmetros disponíveis e observações acessíveis, quais estados do couro conseguimos estimar com erro conhecido? Que medições adicionais são necessárias para distinguir explicações alternativas?

**Fluxo:** literatura → mecanismo → equações → parâmetros/unidades → observáveis → estimativa com incerteza → análise independente → comparação previsto × observado → revisão do modelo → somente então otimização.

Conservar uma trilha de proveniência: **[LITERATURA]**, **[OBSERVADO]**, **[HIPÓTESE]**, **[INFERIDO]** ou **[DECISÃO VALIDADA]**. Não converter uma classe em outra sem evidência explícita.

O projeto é experimental e não especifica ajustes operacionais seguros de químicos perigosos. Toda decisão industrial requer validação por profissionais responsáveis.
