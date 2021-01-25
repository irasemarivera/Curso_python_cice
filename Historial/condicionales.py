"""
print("CONDICIONALES------------------------------")
num1 = 20
num2 = 80
num3 = 40
num4 = 5
print("num1: ", num1)
print("num2: ", num2)
print("num3: ", num3)
print("num4: ", num4)

#Igual
if (num1 == num2):
    print("num1 y num2 son iguales")
else:
    print("num1 y num2 no son iguales")

#diferente
if (num1 != num2):
    print("num1 y num2 son diferentes")
else:
    print("num1 y num2 no son diferentes")

#menor
if (num1 < num2):
    print("num1 es menor que num2")
else:
    print("num1 no es menor que num2")

#menor o igual
if (num1 <= num2):
    print("num1 es menor o igual que num2")
else:
    print("num1 no es menor o igual que num2")

#mayor
if (num1 > num2):
    print("num1 es mayor que num2")
else:
    print("num1 no es mayor que num2")

#mayor o igual
if (num1 >= num2):
    print("num1 es mayor o igual que num2")
else:
    print("num1 no es mayor o igual que num2")

fruta = input("Escribe una fruta: ")
if fruta.upper() == 'KIWI':
    print("Es un kiwi")
elif fruta.upper() == 'MANZANA':
    print("Es una manzana")
else:
    print("Es otra fruta: ", fruta)

valor = [4]
if valor: #Si la lista no tiene elementos por defecto es falso
    print("Es verdadero")
else:
    print("Es falso")

mensaje = "El valor es kiwi" if fruta.upper() == "KIWI" else "Es otra fruta!"
print(mensaje)
"""
print("BUCLES---------------------------")
"""
contador = 0
bandera = True
while bandera:
    print(contador)
    contador +=1
    if contador == 6:
        bandera = False #break

else:
    print("El bucle ha terminado")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for valor in lista:
    print("for: ", valor)

for valor in range(0,10,2):
    print("for rango: ", valor)
"""
for indice, valor in enumerate(range(0, 10, 2), 100):
    print(valor, "tiene indice", indice)

# print(list(range(10,20,2)))
# lista = range(10,20,2)
# print(lista)

# for valor in "Curso intensivo de Python":
#     print(valor)

# diccionario = {'a': 30, 'b': 20, 'c': 500}
# for llave, valor in diccionario.items():
#     print("la llave", llave, "tiene el valor", valor)
