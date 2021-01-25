#strings

"""
mi_nombre = "Hola Irasema"
print(mi_nombre)

mi_nombre = "Hola Irasema, 'buenos dìas'!"
print(mi_nombre)

mi_nombre = "Hola Irasema, \"buenos dìas\"!"
print(mi_nombre)

mi_nombre = 'Hola Irasema, "buenos dìas"!'
print(mi_nombre)

mi_nombre = '''linea uno
otra màs 
esta es la tercera linea!
ahora una cuarta
no hay quinto malo
'''
print(mi_nombre)

#numero1 = 20
#numero2 = 20
#if (numero1 < numero2):
#    print("numero1 es menor")
#else:
#    if numero1 > numero2:
#        print("numero2 es menor")
#    else:
#        print("son iguales")

nombre = "Irasema"
apellido = "Rivera"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
print(nombre, apellido)
print("nombre_completo[0]: ",nombre_completo[0])
print("nombre_completo[1]: ",nombre_completo[1])
print("nombre_completo[2]: ",nombre_completo[2])
print("nombre_completo[3]: ",nombre_completo[3])
print("\n")
print("nombre_completo[-3]: ",nombre_completo[-3])
print("nombre_completo[-2]: ",nombre_completo[-2])
print("nombre_completo[-1]: ",nombre_completo[-1])

print("Metodos String-----------------------------")")
course = "Curso"
my_string = "INTENSIVO de PyThOn"
result = 'Bienvenidos al {a} {b} del cice'.format(a=course, b=my_string)
print("original: "+ result)
result = result.lower()
# print("lower: "+ result)
# result = result.upper()
# print("upper: " + result)
# result = result.title()
# print("title: " + result)

print("Métodos de búsqueda-----------------------------")")
busqueda = result.find('curso')
print("find: ", busqueda)
count = result.count('c')
print("count: ", count)
replace = result.replace('c','w')
print("replace: ", replace)
split = result.split(" ")
print("split: ", split)
print(len(split))

print("LISTAS-----------------------------")")
mi_lista = ["palabra", 12, 12.9, True]
frutas = ["platano", "manzana", "kiwi", "uva", "piña"]
print(frutas)
# print(frutas[0])
# print(frutas[1])
# print(frutas[2])
# print(frutas[3])
frutas.append("arandano")
frutas.insert(1, "fresa")
print(frutas)
frutas.remove("fresa")
print(frutas)
frutas.pop()
print(frutas)

mi_lista1 = [51, 6.1, 72, 3, 11]
mi_lista2 = [100, 80, 40, 50]
mi_lista1.sort() #ordena ascendentemente
print("mi_lista1 sort", mi_lista1)
mi_lista1.sort(reverse=True)
print("mi_lista1 sort reverse", mi_lista1)
# frutas.sort()
# print(frutas)

mi_lista1.extend(mi_lista2)
print(mi_lista1)
mi_lista1.extend([1001,1002])
print(mi_lista1)
mi_lista1.append(mi_lista2)
print(mi_lista1)


print("TUPLAS-----------------------------")")
mi_tupla = (1, "palabra", True)
print(mi_tupla)
print(mi_tupla[0])
#mi_tupla[1] = 1 -- no es posible
mi_lista1.extend(mi_tupla)
print(mi_lista1)
mi_lista1.append(mi_tupla)
print(mi_lista1)



print("DICCIONARIO-----------------------------")
diccionario = {'a': 55,
                1: "esto es un string",
                "cice": ["AULA1", "AULA2", "AULA3", "AULA4", "AULA5"]}
print(diccionario)
diccionario['a'] = 60
diccionario['c'] = "Un nuevo string"
print(diccionario)
diccionario['a'] = False
print(diccionario)

print("diccionario.keys(): ", diccionario.keys())
print("diccionario.values()", diccionario.values())

lista1 = list(diccionario.keys())
print("lista1: ", lista1)
lista2 = tuple(diccionario.values())
print("lista2: ", lista2)

diccionario2 = {'a': 123,
                'y': 456,
                'z': 789}
diccionario.update(diccionario2)
print(diccionario)
"""

print("FUNCIONES ---------------------------")
def nombreFuncion():
    print("Dentro de nombreFuncion")
    pass

def suma(a, b):
    return a + b

#funcion con valores por defecto
def suma2(a = 1, b = 2):
    c = a + b
    return c

print(suma2(a=6))

a = int(input("valor de a: "))
b = int(input("valor de b: "))
print(suma2(a,b))
