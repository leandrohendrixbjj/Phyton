"""
  O que é Abstração?

  Abstração é um dos pilares da Programação Orientada a Objetos (POO). Ela consiste em esconder os detalhes internos de implementação 
  e expor apenas as operações necessárias para utilizar um objeto.

  Exemplo: ao sacar dinheiro em um caixa eletrônico, você informa o valor e solicita o saque. Não precisa conhecer todos os processos
  internos para realizar a operação.

"""

class CaixaEletronico:
  def __init__(self, saldo: float):
    self.__saldo = saldo
    
  def sacar(self, valor: float):

    if valor <= 0:
      print("Valor inválido.")
    elif valor > self.__saldo:
      print("Saldo insuficiente.")
    else:
      self.__saldo -= valor
      print("Saque realizado com sucesso.")

caixa = CaixaEletronico(1000)

caixa.sacar(200)
caixa.consultar_saldo()
