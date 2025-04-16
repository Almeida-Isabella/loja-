class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * percentual / 100

    def atualizar_estoque(self, quantidade_vendida):
        self.quantidade -= quantidade_vendida

    def __str__(self):
        return f'{self.codigo} - {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.quantidade}'
