class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            self.itens.append((produto, quantidade))
            produto.atualizar_estoque(quantidade)
        else:
            print(f'Estoque insuficiente para {produto.nome}.')

    def calcular_total(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens)

    def listar_itens(self):
        for produto, quantidade in self.itens:
            print(f'{produto.nome} x{quantidade} - R${produto.preco * quantidade:.2f}')
