# BASF, Vade-mécum do Curtidor, 4ª edição (2004)

**Fonte:** [S012 no catálogo](../kb/data/sources.json) | [exemplar consultado no Scribd](https://pt.scribd.com/document/525888183/Vade-mecum-Do-Curtidor)

- Editora/autoria institucional: BASF Aktiengesellschaft; edição revisada e ampliada; abril 2004; 370 páginas.
- Tradução indicada no próprio volume: Dieter Lehmann e Felipe K. Schuck.
- A plataforma de terceiros apresenta o texto de boa parte do volume. Imagens, tabelas complexas e fórmulas desenhadas podem não ter transcrição fiel.
- A **5ª edição (2005)** mencionada no levantamento do projeto **não foi conferida neste ciclo**. Não misturar dados de edições.
- **Direitos:** livro protegido por direitos autorais. Não reproduzir PDF, tabelas extensas, capítulos ou texto integral no repositório público. Guardar referências e fatos/extratos científicos limitados.

## Índice temático útil (páginas impressas da edição 2004)

| Seção | Páginas | Uso na base |
|---|---:|---|
| Pele crua, estrutura, colágeno e proteínas | 13–23 | Matéria-prima e variáveis iniciais |
| Conservação, água e remolho | 44–55 | Diferenciar pele verde vs. salgada; hidratação, sal e água |
| Depilação e caleiro | 56–64 | Atividade redutora, alcalinidade, depilação, inchamento |
| Descalcinação | 65–68 | Cálcio residual, alcalinidade e poder de descalcinação |
| Purga/desengraxe | 69–72 | Enzimas, condições de atuação, remoção de graxa |
| Piquelagem | 73–75 | Ácidos, sais, preparação do curtimento |
| Curtimento, incl. cromo | 76–98 | Agentes, basicidade, mascaramento, distribuição |
| Métodos para testar couro | 205–243 | Ensaios e critérios |
| Indicadores, ambiente e unidades | 244–328 | Conversões, indicadores, balanços, geometria |
| Volume cilíndrico de fulão | 306 | Cálculo do volume geométrico interno |
| Rotação vs. carga e volume de banho | 307 | Limite mecânico de sobrecarga e revolvimento |

## Relação quantitativa conferida: basicidade do cromo (p. 92–93)

A 4ª edição apresenta a expressão teórica:

`m_basificante_g_L = (B_final_pct - B_inicial_pct) * Cr2O3_g_L * fator`

**A diferença B é medida em pontos percentuais Schorlemmer**, não em frações decimais. Cr₂O₃ em g/L, resultado em g/L do agente na apresentação indicada. Fatores históricos da própria edição foram cadastrados em [M008](../kb/data/models.json) com cinco reagentes/apresentações.

Não se trata de uma receita universal. A previsão da **quantidade estequiométrica teórica** não determina o pH de reação, o tempo da basificação, a distribuição ou a fixação real de Cr(III). Precisaria de composição/teor ativo reais e análise do sistema químico atual.

## Relação mecânica: carga vs. RPM (p. 307)

O manual distingue `VC` (volume da carga), `dC` (diâmetro do fardo), `nC` (revolvimento da massa de couros), `nF` (RPM do fulão). Sob sobrecarga, `nC` pode cair abaixo do regime necessário; maior `nF` não necessariamente restaura o movimento útil.

**Não foi copiada uma fórmula numérica de rotação:** a parte acessível em texto não preserva o gráfico/diagrama completo. A afirmação qualitativa está cadastrada em [K023](../kb/data/knowledge.json). Para reconstruir equação própria, é necessário conferir a figura da página impressa 307.

## Duas condições iniciais

O manual distingue a matéria-prima preservada por sal e as peles verdes comercializadas sob conservação curta pelo frio. A base registra essas rotas em [raw_material_routes.json](../kb/data/raw_material_routes.json).

**Não são duas receitas universais fechadas:** os passos podem ser semelhantes, mas o estado inicial do couro, massa de sal removível, hidratação e variabilidade da matéria-prima mudam as condições do modelo.

## Matriz operacional do conhecimento

[process_matrix.json](../kb/data/process_matrix.json): vincula cada etapa a mecanismos, dados, modelos, medições candidatas e análises independentes. O conteúdo da coluna `signals` é seleção de engenharia do projeto e **não necessariamente recomendação ou especificação de sensores da BASF**.
