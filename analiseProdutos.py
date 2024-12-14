class AnaliseProdutos:
    def __init__(self, produtos, preco, qualidade, qtd_vendas):
        self.produtos = produtos  # Lista com os nomes dos produtos
        self.preco = preco  # Lista com os preços dos produtos
        self.qualidade = qualidade  # Lista com as qualidades (pode ser uma métrica qualquer)
        self.qtd_vendas = qtd_vendas  # Lista com as quantidades vendidas
        self.media_vendas = sum(qtd_vendas) / len(qtd_vendas)
    def co_pre_vendas(self):
        media_preco = sum(self.preco) / len(self.preco)
        numerador = sum((p - media_preco) * (q - self.media_vendas) for p, q in zip(self.preco, self.qtd_vendas))
        denominador = ((sum((p - media_preco) ** 2 for p in self.preco) *
                        sum((q - self.media_vendas) ** 2 for q in self.qtd_vendas)) ** 0.5)
        return numerador / denominador
    def co_qual_vendas(self):
        media_qualidade = sum(self.qualidade) / len(self.qualidade)
        numerador = sum((q - media_qualidade) * (v - self.media_vendas) for q, v in zip(self.qualidade, self.qtd_vendas))
        denominador = ((sum((q - media_qualidade) ** 2 for q in self.qualidade) *
                        sum((v - self.media_vendas) ** 2 for v in self.qtd_vendas)) ** 0.5)
        return numerador / denominador
    def faturamento(self, nome_produto):
        if nome_produto in self.produtos:
            indice = self.produtos.index(nome_produto)
            return self.preco[indice] * self.qtd_vendas[indice]
        else:
            return f"Produto '{nome_produto}' não encontrado."
    def faturamento_produtos(self):
        return {produto: preco * qtd for produto, preco, qtd in zip(self.produtos, self.preco, self.qtd_vendas)}

