from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio)  :
    def __init__(self, nome, preco, volume):
        super().__init__(nome, preco)
        self._volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume

    