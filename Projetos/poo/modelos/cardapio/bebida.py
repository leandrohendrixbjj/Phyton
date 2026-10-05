from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio)  :
    def __init__(self, nome, preco, volume):
        super().__init__(nome, preco)
        self._volume = volume

    def __str__(self):
        return f"Bebida: {self._nome} - R$ {self._preco} - Volume: {self._volume}ml"
    