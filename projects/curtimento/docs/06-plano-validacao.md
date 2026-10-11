# Plano de investigação e validação

**Fase A — Fundamentação, sem alterar a receita**

- Mapear por etapa a química, os modelos cinéticos e de transporte já publicados; extrair parâmetros com domínio de validade.
- Documentar geometria real dos ladrões, massa e volume operacional, rota de adição/drenagem e pontos de amostragem.
- Definir resultados independentes: pH interno da pele, teor de Cr do banho e couro, distribuição, retração, qualidade conforme artigo.
- Relacionar lotes químicos e de peles às condições iniciais.

**Fase B — Observabilidade instrumental**

- Comparar sinais disponíveis sem instrumentação interna com medições independentes.
- Se houver lacuna, comparar malha fixa 4+4, esfera livre e alternativas por **informação adicional útil**, não pelo número de sensores.
- Distinguir molhamento persistente, contato hidráulico e leitura química representativa.
- Provar desempenho de energia e comunicação em rotações reais, inclusive inversões/pausas.

**Fase C — Modelo e validação**

- Trabalhar com histórico sincronizado e unidades consistentes. Preservar parâmetros e versão dos modelos.
- Calibrar parâmetros somente em lotes de treino; validar em lotes não vistos de matéria-prima e químicos.
- Comparar baseline operacional (receita existente) com o modelo, reportando erro, intervalo e qualidade da previsão.
- Se um efeito não for distinguível de carga/volume/RPM ou teor ativo do produto, declarar *não identificável*, não adivinhar.

**Fase D — Projeção de condições alternativas, posterior**

Só depois da validação estimar consequências de alterações de RPM, volumes, adição, tempo e temperatura; comparar qualidade e custos, respeitando limites de processo, segurança química e autoridade do operador.

## Entregáveis de próxima rodada

1. Tabela de parâmetros publicados e suas fontes, por etapa, com unidades e validade.
2. Inventário dos sinais realmente disponíveis em um fulão-alvo.
3. Matriz modelo × observável × teste laboratorial × incerteza.
4. Primeiro problema de cálculo que já seja resolvível sem calibrar parâmetros inexistentes.

**Não há ensaio executado, modelo calibrado ou sensor instalado registrado neste repositório nesta versão.**
