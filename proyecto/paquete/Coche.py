from .Vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindros):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindros = cilindros
    
    def __str__(self):
        return super().__str__() + ", {}, {}".format(self.velocidad, self.cilindros)
