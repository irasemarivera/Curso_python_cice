class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        self.__privado = 1234
    
    def __str__(self):
        return "{}, {}".format(self.color, self.ruedas)
    
    def getPrivado(self):
        return self.__privado

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindros):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindros = cilindros
    
    def __str__(self):
        return super().__str__() + ", {}, {}".format(self.velocidad, self.cilindros)

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindros):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindros = cilindros  

    def __str__(self):
        return super().__str__() + ", {}, {}".format(self.velocidad, self.cilindros)  

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindros, carga):
        super().__init__(color, ruedas, velocidad, cilindros)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", {}".format(self.carga) 

# coche = Coche("azul", 4, 150, 1200)
# camioneta = Camioneta("blanca", 4, 100, 6, 1000)
# bicicleta = Bicicleta("gris", 2, "deportiva")
# motocicleta = Motocicleta("roja", 2, "urbana", 180, 2)

# print(coche)
# print(camioneta)
# print(bicicleta)
# print(motocicleta.getPrivado())