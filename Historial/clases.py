print("Clases y atributos-----------------------")
# class Alumno:

#     def __init__(self, nombre): #constructor
#         self.nombre = nombre
#         #self.edad = 0 #se puede definir aunque no este en el constructor
    
#     def saludar(self, dia): #metodo
#         print("Hola, {}! Feliz {}".format(self.nombre, dia))

# alumno = Alumno("Tatiana")
# print(alumno.nombre)
# #print(alumno.edad)
# alumno.saludar("Lunes")

# class Rectangulo:
#     """
#     Define un rectangulo según su base y su altura
#     """

#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
    
#     def area(self):
#         return self.b * self.h
    
# rectangulo = Rectangulo(2,3)
# print("Area del rectangulo: ", rectangulo.area())

# print("Herencia ----------------------------------")

# class Poligono:
#     """
#     Define un poligono segun su base y su altura
#     """
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
    
#     def sumar(self):
#         return self.b + self.h

# class Figuras:
#     def __init__(self, color, tamaño, lados):
#         self.color = color
#         self.tamaño = tamaño
#         self.lados = lados
    
# class Rectangulo(Poligono):

#         def area(self):
#             return self.b * self.h
    
# class Triangulo(Poligono, Figuras):

#     def area(self):
#         return (self.b * self.h) / 2

# rectangulo = Rectangulo(20, 10)
# triangulo = Triangulo(20,12)

# print("Area del rectangulo: ", rectangulo.area())
# print("Area del triangulo: ", triangulo.area())
# print("Suma rectangulo: ", rectangulo.sumar())
# print("Suma triangulo: ", triangulo.sumar())

print("Metodos especiales --------------------------")

class Alumno:

    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    def saludar(self):
        print("Hola, {}!".format(self.nombre))
    
alumno = Alumno("Tatiana", "Ascoy", 30, "Italiana")
print(alumno)