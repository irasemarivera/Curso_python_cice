from poo1 import *

coche = Coche("azul", 4, 150, 1200)
camioneta = Camioneta("blanca", 4, 100, 6, 1000)
bicicleta = Bicicleta("gris", 2, "deportiva")
motocicleta = Motocicleta("roja", 2, "urbana", 180, 2)

print(coche)
print(camioneta)
print(bicicleta)
print(motocicleta.getPrivado())