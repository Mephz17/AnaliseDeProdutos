# Análise de Produtos

## Descrição do Projeto

O projeto tem como objetivo analisar a relação entre preço, qualidade e vendas de produtos utilizando Python. Ele inclui uma classe para realizar cálculos estatísticos sobre os dados de produtos e gera gráficos que ajudam a visualizar essas relações.

## Funcionalidades

1. **Cálculo de Correlação**:
   - Correlação entre preço e quantidade de vendas.
   - Correlação entre qualidade e quantidade de vendas.

2. **Análise de Faturamento**:
   - Faturamento individual de cada produto.
   - Faturamento total de todos os produtos.

3. **Visualização de Dados**:
   - Gráfico de dispersão mostrando a relação entre preço e vendas.
   - Gráfico de dispersão mostrando a relação entre qualidade e vendas.

## Estrutura do Projeto

- **`AnaliseProdutos`**: Classe principal que realiza as análises e cálculos sobre os dados.
- **Script de Execução**: Lê os dados do arquivo CSV, inicializa a classe e gera os gráficos para visualização.

## Como Usar

1. **Preparar os Dados**:
   - Crie um arquivo chamado `produtos.csv` contendo as colunas: Nome, Preço, Qualidade, e Quantidade de Vendas.
   - Exemplo de formato:

     ```csv
     Nome,Preço,Qualidade,Quantidade de Vendas
     ProdutoA,10.0,8.0,100
     ProdutoB,15.0,6.5,150
     ProdutoC,8.0,9.0,90
     ```

2. **Executar o Projeto**:
   - Execute o script principal, que lê os dados do CSV, realiza as análises e exibe os gráficos gerados.

3. **Interpretar os Resultados**:
   - Verifique as correlações para entender como o preço e a qualidade influenciam as vendas.
   - Analise os gráficos para identificar padrões visuais nos dados.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas:
  - `numpy`
  - `matplotlib`

## Como Funciona

### Cálculo de Correlação

A correlação entre duas variáveis é calculada com base na fórmula:

![image](https://github.com/user-attachments/assets/6842ae32-047f-4120-af13-d62bd867e20d)


- Onde:
  - xi e yi são os valores individuais das variáveis.
  - x e y são as médias das variáveis x e y.

### Faturamento

- Faturamento é obtido multiplicando o preço pela quantidade vendida de cada produto.

### Visualização

- Gráficos de dispersão mostram como as variáveis (preço/qualidade) se relacionam com as vendas.

## Resultados Esperados

- Identificar produtos mais rentáveis e características que influenciam vendas.
- Observar como variações em preço e qualidade afetam as vendas de produtos.

## Contribuições

Sinta-se à vontade para contribuir com melhorias neste projeto por meio de pull requests ou abrindo issues para sugestões e problemas encontrados.

---

Espero que você aproveite este projeto para compreender melhor a relação entre variáveis nos negócios!

