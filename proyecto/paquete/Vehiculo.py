class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        self.__privado = 1234
    
    def __str__(self):
        return "{}, {}".format(self.color, self.ruedas)
    
    def getPrivado(self):
        """Adquiere el valor privado de la clase"""
        return self.__privado