"""
Classe: 
  - É a representação de um elemento do mundo real, descrevendo seus atributos (características) e métodos (comportamentos).
  - Classe é a planta de uma casa, objeto é a casa construída.

+-----------+-----------------------+----------------------------+-------------------------+
| Elemento  | Classe                | Atributos                  | Métodos                 |
+===========+=======================+============================+=========================+
| Pessoa    | Pessoa                | nome, idade, cpf           | falar(), andar()        |
+-----------+-----------------------+----------------------------+-------------------------+
| Carro     | Carro                 | marca, modelo, cor         | ligar(), acelerar()     |
+-----------+-----------------------+----------------------------+-------------------------+
| Livro     | Livro                 | titulo, autor, isbn        | abrir(), fechar()       |
+-----------+-----------------------+----------------------------+-------------------------+
  
"""

class Pessoa:
  def __init__(self, nome: str, idade: int):
    self.nome = nome
    self.idade = idade
  
pessoa = Pessoa("João", 30)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")  