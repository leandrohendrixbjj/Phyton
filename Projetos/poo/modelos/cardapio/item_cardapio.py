from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    """
      O @abstractmethod é um decorador do módulo abc do Python que indica que um método deve ser implementado pelas classes concretas 
      que herdam de uma classe abstrata.

      Finalidade muito semelhante à de uma interface em linguagens como Java e PHP.
    """
    @abstractmethod
    def aplicar_desconto(self):
        pass    