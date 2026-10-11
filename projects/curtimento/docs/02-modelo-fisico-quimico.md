# Núcleo matemático: modelos existentes, hipóteses e limites

O objetivo é **compor modelos conhecidos**, extrair parâmetros e verificar seus domínios de validade. Não inventar constantes para fazer uma previsão parecer numérica.

## Entradas e estados

- `u(t)`: RPM/sentido/pausas, adições químicas e água, temperatura controlada, eventos de operação.
- `x(t)`: concentrações no banho, estados internos da pele, temperatura, massa/água, parâmetros de dinâmica e mistura.
- `y(t)`: sinais observados (pH, T, condutividade, pressão, vibração, potência, concentração laboratorial).
- `theta`: cinética e propriedades de produtos/lotes químicos, parâmetros da matéria-prima e do fulão.

Formalmente: `dx/dt = f(x,u,theta)`, `y = h(x,u,theta) + erro`. Estados não distinguíveis pelas observações **não** podem ser apresentados como recuperados.

## Mecânica rotativa

- `omega [rad/s] = 2*pi*RPM/60`.
- `Fr [-] = omega^2*R/g` (com raio `R [m]`, gravidade `g [m/s²]`).
- `E_eixo [J] = integral(torque_eixo [N.m] * omega [rad/s] dt)`.
- Energia elétrica, energia de eixo e energia útil transmitida às peles são diferentes; eficiência e perdas precisam ser estimadas. Froude auxilia comparação de regimes e não determina sozinho a dinâmica de peles flexíveis.

## Banho, transporte, reação

Em aproximação de banho perfeitamente misturado, a massa `V*C_b` de uma espécie pode obedecer:

`d(V*C_b)/dt = m_dosado_ponto - m_saida_ponto - A_ef*k_m*(C_b-C_s) - m_outras_perdas_ponto`

Unidades consistentes: `V [m³]`, `C [kg/m³]`, `A_ef [m²]`, `k_m [m/s]`, fluxos `[kg/s]`. Recirculação interna não é perda líquida do balanço global. A hipótese de mistura perfeita precisa ser avaliada.

A difusão no couro exige modelo espacial e condições de contorno adequadas; retirar cromo do banho **não equivale** a coordená-lo ao colágeno. Modelos de Arrhenius, `k(T)=A*exp(-Ea/(Rgas*T))`, só podem ser aplicados quando a cinética e seus parâmetros forem justificados. Usar `T` absoluta em kelvin.

## Pressão, rotação e volume

`p_local = p_referencia + rho*g*h_local + p_dinamico` é uma **decomposição idealizada**. Em sensor que gira com o fulão, acelerações, superfície livre deformada, película aderente e circulação no ladrão exigem correções. A matriz 4+4 não garante volume absoluto.

Sem peles e em equilíbrio quase-estático, um segmento circular fornece volume geométrico ideal de um cilindro parcialmente cheio. Com peles, deslocamento, absorção e retenção invalidam equivalência direta ao volume livre. Usar também vazões de entrada/saída e balanço hídrico.

## Indicadores diferentes

- **Esgotamento aparente:** diferença de inventário químico no banho após corrigir dosagens, drenagens, volume e perdas; não significa ligação.
- **Fixação:** requer evidência química no couro, além do banho.
- **Resultado útil:** exige propriedades-alvo e integridade do material (uniformidade, resistência, flor, temperatura de retração quando aplicável).

## Cadeia interetapas

`X_(etapa+1) = F_etapa(X_etapa, historia_controles, lote_quimico)`.

O problema matemático central é **identificabilidade**: variações de RPM, volume, carga, propriedades da pele e insumos podem gerar sinais semelhantes. Não atribuir causalidade a correlações isoladas.
