from .Coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindros, carga):
        super().__init__(color, ruedas, velocidad, cilindros)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", {}".format(self.carga) 
