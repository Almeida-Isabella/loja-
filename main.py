import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from classes.produtos import Produto
from classes.carrinho import Carrinho
from classes.pagamento import Pagamento


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


class Pagamento:
    def __init__(self, total):
        self.total = total

    def simular_pagamento(self, metodo):
        if metodo == '1':
            desconto = self.total * 0.1
            valor_final = self.total - desconto
            print(f'Pagamento via PIX (10% desconto). Total: R${valor_final:.2f}')
        elif metodo == '2':
            juros = self.total * 0.05
            valor_final = self.total + juros
            print(f'Pagamento com cartão (5% acréscimo). Total: R${valor_final:.2f}')
        elif metodo == '3':
            print(f'Pagamento em dinheiro. Total: R${self.total:.2f}')
        else:
            print('Método de pagamento inválido.')


class Loja:
    def __init__(self):
        self.produtos = []
        self.carregar_produtos()

    def carregar_produtos(self):
        self.produtos.append(Produto(1, 'Sutiã Renda', 59.90, 10))
        self.produtos.append(Produto(2, 'Calcinha Algodão', 19.90, 20))
        self.produtos.append(Produto(3, 'Cueca Boxer', 29.90, 15))
        self.produtos.append(Produto(4, 'Conjunto Lingerie', 89.90, 8))
        self.produtos.append(Produto(5, 'Cueca Slip', 24.90, 12))

    def exibir_menu(self):
        while True:
            print('\n=== MENU LOJA ÍNTIMA ===')
            print('1. Listar Produtos')
            print('2. Realizar Compra')
            print('3. Verificar Estoque')
            print('4. Sair')
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                self.listar_produtos()
            elif opcao == '2':
                self.realizar_compra()
            elif opcao == '3':
                self.verificar_estoque()
            elif opcao == '4':
                print('Encerrando o sistema.')
                break
            else:
                print('Opção inválida.')

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def realizar_compra(self):
        carrinho = Carrinho()
        while True:
            self.listar_produtos()
            try:
                codigo = int(input('Digite o código do produto (0 para finalizar): '))
            except ValueError:
                print('Código inválido.')
                continue
            if codigo == 0:
                break
            produto = self.buscar_produto(codigo)
            if produto:
                try:
                    quantidade = int(input('Quantidade: '))
                    carrinho.adicionar_item(produto, quantidade)
                except ValueError:
                    print('Quantidade inválida.')
            else:
                print('Produto não encontrado.')

        total = carrinho.calcular_total()
        print('\nResumo da compra:')
        carrinho.listar_itens()
        print(f'Total sem descontos: R${total:.2f}')
        metodo = input('Escolha forma de pagamento:\n1. PIX (10% desconto)\n2. Cartão (5% acréscimo)\n3. Dinheiro\nOpção: ')
        pagamento = Pagamento(total)
        pagamento.simular_pagamento(metodo)

    def verificar_estoque(self):
        self.listar_produtos()

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None


loja = Loja()
loja.exibir_menu()
