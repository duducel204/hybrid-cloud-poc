# Regras de ingestão e expansão da base

## Registro mínimo de uma afirmação
```json
{
  "id": "K019",
  "stage": "piquel",
  "claim": "Afirmação objetiva e verificável, sem prescrever dosagem.",
  "source_ids": ["S001"],
  "limits": "Condições de validade explícitas.",
  "status": "documentado"
}
```

Adicionar uma referência em `sources.json` antes de citá-la. Referências precisam de título, órgão/autoria, URL e escopo. Artigos e normas não devem ser copiados integralmente, apenas fatos, resultados próprios resumidos, metadados e links.

## Tipos de fatos

- `documentado`: afirmação amparada por fonte identificável.
- `inferencia_fisica`: conclusão lógica que requer hipótese específica; registrar a limitação.
- `lei_fisica_ideal` e `numero_adimensional`: modelo geral; não equivale a desempenho de fulão.
- `resultado_no_resumo_publicado`: resultado foi extraído do resumo científico acessível, não de dados completos.
- `hipotese`: conhecimento ainda não consolidado; manter fora do catálogo de fatos.
 
## Atualização e versionamento

IDs nunca devem ser reaproveitados para outro fato. Prefira registrar nova versão/contradição, em vez de apagar o histórico sem explicação. O padrão permite novos campos desde que o validador confirme vínculos e estrutura. Não introduzir faixas de pH/temperatura, coeficientes cinéticos ou indicadores de eficiência universais sem fonte e contexto definidos.
