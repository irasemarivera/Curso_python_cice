from .Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindros):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindros = cilindros  

    def __str__(self):
        return super().__str__() + ", {}, {}".format(self.velocidad, self.cilindros)  
