# Protocolo Forward / Backward para qualquer IA ou colaborador

## Leitura obrigatória

Começar pelo `projects/curtimento/README.md` e seguir seu índice. Nenhum relatório anterior é fonte de verdade automática: cada afirmação requer classificação e referência. Preservar a receita nominal na fase atual.

## Backward: do resultado à informação necessária

1. Formular a grandeza-alvo: por exemplo, quantidade útil de Cr fixado por kg de couro, com definição analítica.
2. Identificar mecanismo, estados latentes, unidades e restrições.
3. Encontrar equações estabelecidas, parâmetros exigidos, condições de contorno e faixas de validade.
4. Separar quantidades já conhecidas das que exigem observação.
5. Definir que medição independente poderia confirmar a estimativa.

## Forward: do conhecimento e dos instrumentos ao que se pode estimar

1. Inventariar conhecimento publicado, medições disponíveis, incerteza e resolução temporal.
2. Derivar, com equações e unidades, o que é calculável sem estimativas novas.
3. Avaliar ambiguidade: estados distintos geram leituras indistinguíveis?
4. Identificar qual novo sensor/ensaio/modelo desfaz a ambiguidade com menor custo e risco.
5. Registrar alternativas não selecionadas e por quê.

## Encontro e progressão

`Backward(alvo) ∩ Forward(capacidades verificadas)` determina a região em que uma resposta pode ser defendida. Quando vazio: explicitar o dado, equação ou parâmetro ausente. **Não preencher lacunas por narrativa de IA.**

Iteração:
`formalizar → projetar → comparar → questionar melhor opção → aprofundar seletivamente → medir → previsto×observado → corrigir → reprojetar`.

## Contrato mínimo de qualquer contribuição

- Pergunta exata / estado desejado.
- Fonte(s) primária(s), ano, URL/DOI quando disponíveis, ou identificação de origem do dado.
- Equações, símbolos, unidades, hipóteses e faixa válida.
- Fatos confirmados × hipóteses × inferências × decisões.
- Dados faltantes e como obtê-los sem interferir desnecessariamente na produção.
- Alternativas e trade-offs de custo, manutenção, risco e valor informacional.
- Nenhum número de eficiência ou confiança sem cálculo verificável.

## Critério de progresso

Melhora real significa reduzir uma incerteza importante, provar/rejeitar uma relação ou ampliar o conjunto de resultados calculáveis, não acumular sensores, dashboards ou textos. Não automatizar decisões críticas antes da validação.
