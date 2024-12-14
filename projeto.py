import numpy as np
import matplotlib.pyplot as plt
import analiseProdutos as ap
dados = np.genfromtxt("produtos.csv", delimiter=",", dtype=None)
colunaPreco = [float(dados[i][1]) for i in range(1, len(dados))]
colunaQualidade = [float(dados[i][2]) for i in range(1, len(dados))]
colunaVendas = [float(dados[i][3]) for i in range(1, len(dados))]
colunaProdutos = [dados[i][0] for i in range(1, len(dados))]

print(colunaQualidade, colunaVendas, colunaPreco)

inicializando = ap.AnaliseProdutos(colunaProdutos, colunaPreco, colunaQualidade, colunaVendas)
co_preco_venda = inicializando.co_pre_vendas()
co_qualidade_venda = inicializando.co_qual_vendas()

print(co_preco_venda * 100)
print(co_qualidade_venda * 100)


# Criando grafico de relacao entre preco-venda
plt.figure("Figura1")
plt.scatter(colunaPreco, colunaVendas)
plt.grid()
plt.xlabel("Preco")
plt.ylabel("Quantidade de vendas")
plt.show()

plt.figure("Figura2")
plt.scatter(colunaQualidade, colunaVendas)
plt.grid()
plt.xlabel("Qualidade")
plt.ylabel("Vendas")
plt.show()