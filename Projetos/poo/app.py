from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante = Restaurante('praça', 'Gourmet')

prato = Prato('Pizza', 30.00, 'Pizza de calabresa')
bebida = Bebida('Coca-Cola', 5.00, 'Coca-Cola 350ml')

restaurante.adicionar_produto_ao_cardapio(prato)
restaurante.adicionar_produto_ao_cardapio(bebida)

def main():
    restaurante.get_cardapio()

if __name__ == '__main__':
    main()  