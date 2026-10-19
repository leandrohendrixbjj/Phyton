"""
Objeto:
  - É uma instância de uma classe.
  - É um espaço real, com endereço, características e usos próprios.
  - Pode ser utilizado e modificado de diversas formas.

Alegoria para entender:
  - Classe como a planta de um edifício: ela define todos os detalhes e possibilidades da construção.
  - Objeto como o prédio concreto erguido a partir dessa planta — um espaço real, com endereço, características e usos próprios.  
"""

class Predio:
    def __init__(self, nome: str, andares: int):
        self.nome = nome
        self.andares = andares

    def descricao(self):
        return f"Prédio {self.nome} com {self.andares} andares."

# Objetos são instâncias da classe Predio    
predio1 = Predio("Edifício Central", 10)
print(predio1.descricao())

predio3 = Predio("Torre Sul", 20)
print(predio3.descricao())