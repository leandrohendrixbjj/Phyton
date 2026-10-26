"""
  O que é Encapsulamento?

  Encapsulamento é um dos pilares da Programação Orientada a Objetos (POO). Ele permite proteger os dados de uma classe e controlar 
  como eles podem ser acessados ou modificados.

  Exemplo: em uma conta bancária, não queremos que qualquer pessoa altere o saldo diretamente. Em vez disso, disponibilizamos métodos
  como depositar(), sacar() e consultar_saldo(), que controlam as operações permitidas.
"""

class ContaBancaria:
  def __init__(self, titular: str, saldo: float):
    self.titular = titular
    self.__saldo = saldo

  def depositar(self, valor: float):
    if valor > 0:
     self.__saldo += valor
    else:
     print("Valor inválido.")

  def consultar_saldo(self):
    return self.__saldo


conta = ContaBancaria("Maria", 1000)
conta.depositar(200)
print(f"Saldo: R$ {conta.consultar_saldo():.2f}")

# Tentativa de acessar o atributo diretamente
try:
  print(conta.__saldo)  # Gera AttributeError
except AttributeError as e:
  print(f"Erro: {e}")