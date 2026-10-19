class Carro:
  def __init__(self, marca):
    self._marca = marca
    
  def get_marca(self):
    print(f"A marca do carro é {self._marca}")

carro = Carro("Ford")
carro.marca = "Chevrolet"
carro.get_marca()