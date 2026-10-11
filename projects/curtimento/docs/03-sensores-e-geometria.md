# Geometria do fulão e instrumentação candidata

## Interpretação da geometria trazida pelo usuário

Fulão de madeira cilíndrico horizontal. Junto às **duas cabeceiras circulares** existem fundos falsos/ladrões **anulares**, separados da câmara principal das peles por ripas de madeira com passagens de banho. O vão atrás das ripas recebe/circula o banho e se comunica com drenagem. Toda a montagem rotaciona com o tambor.

Esta é a **geometria de trabalho baseada nos rascunhos e explicações do usuário**, não um desenho fabricável ou vistoria dimensional. Verificar ripa, frestas, vão, anel, fixações e renovação hidráulica em equipamento real.

## Malha exploratória 4 + 4

- **Cabeceira A:** quatro pontos aproximadamente espaçados por 90°.
- **Cabeceira B:** quatro pontos intercalados 45° em relação à A.
- Forma possível: **meia esfera/peça rasa fixa** na face protegida do ladrão.
- Os sensores seguem o tambor: suas alturas relativas à gravidade variam a cada volta.
- A superfície do sensor pode permanecer úmida mesmo fora da região de banho acumulado.
- Não há garantia de leitura analítica válida, nem de volume real calculado apenas por molhamento.
- Ambos os ladrões precisam ter representatividade e continuidade hidráulica verificadas; cobertura angular combinada não garante leitura de ambos os lados.

## Variantes a manter vivas

| Modalidade | Dado direto | Hipótese de uso | Principal risco |
|---|---|---|---|
| pH/temperatura no ladrão | Estado local do banho | Evolução ácido-base/térmica por etapa | Filme velho, incrustação, gradiente interno |
| Condutividade/ORP | Propriedade iônica/redox local | Complementar processo químico | Não identifica espécies isoladas |
| Membrana deslocável (contato/pressão) | Limiar de força ou pressão | Dinâmica hidráulica, mudança do contato | Inércia da peça, pressão de impacto e película |
| Transdutor contínuo de pressão | Pressão local | Resposta hidrodinâmica do ladrão | Referência e aceleração rotativa |
| IMU/encoder/potência/vibração | Movimento do equipamento e carga elétrica | Classificar regimes mecânicos | Não mede diretamente deformação da pele |
| Esfera livre opcional | Movimento local da esfera | Investigar correlação com movimento da massa | Trajetória diferente da pele, impacto, recuperação |
| Análise química e física externa | Concentrações/propriedades reais em amostra | Validar estados inferidos | Amostragem descontínua |

## Energia, fixação e comunicação

Hipótese do usuário: aproveitar fixação que atravessa a madeira, possivelmente com **parafuso passante oco e feedthrough vedado**, para levar sinal/antena à parte externa rotativa. O corpo metálico do parafuso não é automaticamente antena.

Alternativas de alimentação em estudo: captação da rotação lenta, energia indutiva entre parte fixa e rotativa, sensores passivos ou fornecimento compartilhado por cabeceira. Não assumir produção de potência a baixa RPM sem balanço energético. Supercapacitor armazena energia finita e não mantém medições durante parada indefinida.

Transmissão sem fio do **lado externo do tambor** evita atravessar o banho com RF, mas a antena ainda gira. Wi-Fi e Sub-GHz precisam de avaliação de rádio, geometria, metal, interferência e perda de pacotes.

**Escolha de hardware está em aberto.** Primeiro mapear observáveis necessários aos modelos; depois escolher elementos, frequência de amostragem, montagem e energia, incluindo custo total e manutenção.
