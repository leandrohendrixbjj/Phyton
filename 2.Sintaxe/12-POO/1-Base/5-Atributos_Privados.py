"""
  Atributos Privados:

  são atributos que começam com um underscore (_) e não devem ser acessados de fora do objeto. 
  É uma forma de encapsulamento, um princípio da orientação a objetos.

  Servem para proteger dados internos, evitando que sejam modificados ou acessados de forma indevida.
"""

class Person:
  def __init__(self, name):
    self._name = name    

  def sleep(self):
    print(f"{self._name} está dormindo 8 horas")  

person = Person('Leandro')
person.name = 'Hendrix'
person.sleep()

