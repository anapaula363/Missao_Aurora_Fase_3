# Missão Aurora - Sistema de Gerenciamento de energia
<h2>1. Sobre o projeto</h2>
<p>
  A Missão Aurora SIGER é uma aplicação desenvolvida em Python para representar, de forma didática, o acompanhamento de recursos energéticos de uma colônia instalada em Marte. O programa recebe informações sobre a energia disponível, o consumo, a recarga, a velocidade do vento e a irradiância solar. A partir desses dados, calcula um saldo energético, estima a geração solar e eólica e apresenta mensagens que auxiliam a interpretação da situação energética. A aplicação reúne estruturas de dados, funções de cálculo, regras condicionais e uma interface gráfica. Seu propósito é demonstrar como informações operacionais podem ser processadas e convertidas em resultados compreensíveis para o usuário. Trata-se de um modelo acadêmico simplificado, não de um sistema de controle físico ou de segurança para uma instalação real.
</p>

<h2>
  2. Estrutura de dados e informações da colônia 
</h2>
<p> 
  As informações de referência da colônia são organizadas no dicionário colonia. O grupo energia contém os valores de referência atribuídos às fontes solar (50) e eólica (30). O grupo sistemas registra três subsistemas e suas classificações: suporte_vida como essencial, laboratorio como secundário e comunicacao como importante. Essa estrutura hierárquica agrupa informações relacionadas em um único objeto e torna explícita a organização conceitual dos recursos e dos subsistemas. No código atual, entretanto, o dicionário funciona como cadastro de referência: seus valores não são consultados pelas funções de cálculo nem alteram automaticamente o consumo ou a prioridade dos sistemas. A previsão eólica utiliza duas listas paralelas: vento = [8, 10, 12] e energia_gerada = [20, 25, 30]. Cada posição representa um par de observações, relacionando uma velocidade do vento a uma quantidade de energia gerada. Esses valores constituem uma pequena base demonstrativa usada no ajuste do modelo.
</p>

<h2>
  3. Processamento do balanço energético
</h2>

<p>
  O saldo energético é calculado na função verificar_energia(), a partir dos valores informados na interface. A expressão utilizada é:
</p>
  <p align="center">
    energia_final = energia_inicial − consumo + recarga 
  </p>
<p>
  O cálculo representa a energia inicial disponível, descontada do consumo informado e acrescida da recarga informada pelo usuário. O resultado é exibido como energia final. A previsão solar e a previsão eólica são apresentadas separadamente e não são somadas automaticamente a esse saldo. Essa distinção é importante: o valor de recarga digitado é o único acréscimo incorporado ao balanço. As estimativas calculadas para as fontes renováveis são indicadores informativos independentes no comportamento atual do programa.
</p>

<h2>
  4. Regras de alerta e interpretação operacional
</h2>
<p>
  A função verificar_prioridade(energia) avalia o saldo recebido e aplica um limite de 50 unidades.
Quando o valor é inferior a 50, retorna uma mensagem de alerta que recomenda priorizar o suporte à
vida. Quando o valor é igual ou superior a 50, informa que há energia suficiente segundo essa
verificação.
</p>
<p>
  Além dessa regra, a interface utiliza uma segunda condição para definir a mensagem operacional.
Quando energia_final é maior que -1, o programa apresenta a mensagem de que a colônia está
funcionando, junto com o resultado da prioridade. Quando o saldo é igual ou inferior a -1, apresenta
uma mensagem indicando pouca energia e a necessidade de interromper ou rever a operação.
</p>
<p>
  Os dois limites têm funções diferentes: 50 unidades determinam o alerta de prioridade energética,
enquanto -1 é o limite usado para selecionar entre as duas mensagens principais da interface. Assim,
um saldo entre -1 e 50 pode resultar simultaneamente na indicação de que a colônia está funcionando
e em um alerta para priorizar o suporte à vida.
</p>
<p>
  O programa também compara energia inicial e consumo para gerar uma sugestão textual. Se a energia
inicial for maior que o consumo, recomenda armazenar energia excedente; se for menor, alerta que o
consumo supera a geração; se forem iguais, informa estabilidade. Essa comparação utiliza os valores
de energia inicial e consumo, não a geração estimada pelas funções solar e eólica. Por isso, a
mensagem deve ser entendida como uma regra simplificada de orientação, e não como um balanço
completo entre geração e consumo.
</p>

<h2>
  5. Estimativa de geração solar
</h2>

<p>
  A função prever_energia_solar(luminosidade) estima a contribuição solar a partir de um valor de
entrada. O código limita esse valor ao intervalo de 0 a 100 e aplica uma capacidade de referência igual
a 50. A estimativa é calculada pela relação:
</p>
<p align="center">
  energia_solar = 50 × (luminosidade / 100)
</p>
<p>
  Dessa forma, a estimativa varia de 0 a 50 unidades proporcionais à capacidade de referência. O
resultado é apresentado na interface como previsão de geração solar. Embora o campo seja
identificado como “Irradiância solar (W/m²)”, a função trata a entrada como um índice percentual
limitado a 0–100; portanto, a fórmula atual não converte irradiância física em potência ou energia real.
A unidade exibida junto ao resultado também deve ser interpretada com cautela, pois o cálculo não
realiza essa conversão.
</p>

<h2>
  6. Estimativa de geração eólica
</h2>
<p>
  A função prever_energia(velocidade_vento) utiliza regressão linear simples para estimar a energia
associada à velocidade do vento informada. O modelo ajusta uma reta aos três pares de observações
armazenados nas listas vento e energia_gerada. Sua forma matemática é:
</p>
<p align="center">
  ŷ = a · x + b
</p>
<p>
  O coeficiente angular é calculado pela razão entre a soma dos produtos dos desvios de cada variável e
a soma dos quadrados dos desvios da velocidade do vento. O intercepto é obtido a partir das médias
das observações. Para os dados registrados no programa, os coeficientes são a = 2,5 e b = 0,
resultando em:
</p>
<p align="center">
  ŷ = 2,5 · velocidade_vento
</p>
<p>
  Como exemplo, para uma velocidade de 11 m/s, a estimativa é de 27,5 unidades de energia. A
interface apresenta esse valor com duas casas decimais. O modelo é demonstrativo e utiliza apenas
três observações; não representa uma simulação aerodinâmica de turbinas nem considera fatores
como características do equipamento, densidade do ar, eficiência ou limites operacionais. Previsões
fora do intervalo observado devem ser interpretadas com cautela.
</p>

<h2>
  Interface gráfica e interação
</h2>
<p>
  A interface foi construída com a biblioteca CustomTkinter. A janela principal utiliza o tema escuro,
possui dimensões definidas de 800 por 600 pixels e apresenta o título “Missão Aurora - fase 3”. Os
elementos visuais são organizados verticalmente.
</p>
<p>
  A tela disponibiliza cinco campos de entrada:<br>
  • Energia inicial: quantidade de energia disponível no início da análise.<br>
  • Consumo: quantidade de energia descontada no cálculo do saldo.<br>
  • Recarga: quantidade adicionada ao saldo energético.<br>
  • Velocidade do vento (m/s): valor utilizado na estimativa eólica.<br>
  • Irradiância solar (W/m²): entrada utilizada pela função de estimativa solar, com a ressalva de modelagem descrita na seção 5.
</p>
<p>
  O botão “Verificar energia” executa a função verificar_energia(). Após a leitura dos campos, os valores
são convertidos para números de ponto flutuante. O programa realiza os cálculos, aplica as condições
e atualiza um rótulo da própria janela com o saldo, os alertas, as previsões e a sugestão
correspondente.
</p>
<p>
  Caso algum campo não possa ser convertido para número, a exceção ValueError é capturada e a
interface apresenta a mensagem “Erro: digite apenas numeros”. O tratamento atual cobre entradas não
numéricas; não há validação específica para campos vazios, faixas plausíveis ou valores negativos.
</p>
<h2>
  8. Fluxo de execução
</h2>
<p>
  O funcionamento da aplicação começa com a abertura da janela gráfica e a apresentação dos campos
de entrada. Quando o usuário aciona o botão de verificação, o programa lê os cinco valores, converteos para números, calcula a estimativa eólica, determina o saldo energético, calcula a estimativa solar e
avalia as condições de alerta e de sugestão. Por fim, apresenta as informações no rótulo de resultado.
Se ocorrer erro de conversão numérica, a mensagem de validação é exibida no mesmo espaço.
</p>

<h2>
  9. Limitações técnicas
</h2>
<p>
  • A base histórica da previsão eólica contém apenas três observações demonstrativas.<br>
  • A estimativa solar utiliza uma entrada limitada a 0–100 e uma capacidade fixa de 50, sem
conversão física de irradiância.<br>
  • As previsões solar e eólica são exibidas separadamente e não integram o cálculo do saldo
energético.<br>
  • O dicionário colonia registra fontes e categorias de subsistemas, mas não participa diretamente das
decisões executadas.<br>
  • As classificações de essencial, secundário e importante não provocam desligamento, redução ou
priorização automática de cargas.<br>
  • A sugestão de armazenamento compara energia inicial e consumo, sem incorporar diretamente as
previsões de geração.<br>
  • O tratamento de erro contempla falhas de conversão numérica, mas não valida limites operacionais
ou consistência física dos dados.
</p>
<p>
  Em razão dessas limitações, o SIGER deve ser compreendido como um protótipo educacional de
análise energética. Suas mensagens não devem ser utilizadas para comandar sistemas reais de
suporte à vida ou infraestrutura crítica.
</p>
<h2>
  10. Desenvolvedores
</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/anapaula363">
        <img src="https://avatars.githubusercontent.com/u/265589133?v=4" width="115"><br>
        <sub>Ana Silva</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/denis-bezerrax">
        <img src="https://avatars.githubusercontent.com/u/314802520?s=400&u=6073ed5be1b524436244bea5f53a388d07afee94&v=4" width="115"><br>
        <sub>Denis Bezerra</sub>
      </a>
    </td>
  </tr>
</table>
