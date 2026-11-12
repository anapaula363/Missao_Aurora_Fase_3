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
  O saldo energético é calculado na função verificar_energia(), a partir dos valores informados na
interface. A expressão utilizada é: \n energia_final = energia_inicial − consumo + recarga
O cálculo representa a energia inicial disponível, descontada do consumo informado e acrescida da
recarga informada pelo usuário. O resultado é exibido como energia final. A previsão solar e a previsão
eólica são apresentadas separadamente e não são somadas automaticamente a esse saldo.
Essa distinção é importante: o valor de recarga digitado é o único acréscimo incorporado ao balanço.
As estimativas calculadas para as fontes renováveis são indicadores informativos independentes no
comportamento atual do programa.
</p>

<h2>Desenvolvedores</h2>

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
