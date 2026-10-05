from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')

prato = Prato('Pizza', 30.00, 'Pizza de calabresa')
bebida = Bebida('Coca-Cola', 5.00, 'Coca-Cola 350ml')


def main():
    print(prato)
    print(bebida)

if __name__ == '__main__':
    main()  