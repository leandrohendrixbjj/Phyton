from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._desconto = 0.10
        self.init_functions()

    def init_functions(self):
        self.aplicar_desconto()

    def __str__(self):
        return f"Prato: {self._nome} - R$ {self._preco} - Descrição: {self._descricao}"

    def aplicar_desconto(self):
        self._preco = self._preco * (1 - self._desconto)