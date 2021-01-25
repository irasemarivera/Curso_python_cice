# Taller 2
# Duracion: 20 min
# Nombre : Irasema


# 1
# Crea una función que dados dos números mostrará todos los números que hay entre ellos.

# ejemplo

# numerosEntre(7,10)
# 8
# 9

print("Ejercicio 1")
a = int(input("Dame el numero de inicio: "))
b = int(input("Dame el numero de fin: "))
lista = list(range(a,b,1))
for valor in lista:
    print("Numero: ", valor)

# codigo aqui  - fin



# 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
# lo guarde en un diccionario. Despúes debe mostrar por pantalla la informacion agregada

# ejemplo

# ¿Cómo te llamas? Ben     
# ¿Cuántos años tienes? 20
# ¿Cuál es tu dirección? Salsipuedes 4
# ¿Cuál es tu número de teléfono? 555 021 234
# Ben tiene 20 años, vive en Salsipuedes 4 y su número de teléfono es 555 021 234

print("\nEjercicio 2")
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

diccionario = {'nombre': nombre,
                'edad': edad,
                'direccion': direccion,
                'telefono': telefono,
                }

print(diccionario['nombre'], "tiene", diccionario['edad'], "años, vive en", diccionario['direccion'], "y su numero de telefono es", diccionario['telefono'])

# codigo aqui  - fin


# 3
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
# con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
# pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# ejemplo

# ¿Cómo te llamas?  Alex
# ¿Cuál es tu sexo (M o H)?  H
# Tu grupo es B
# codigo aqui  - inicio
print("\nEjercicio 3")
nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")

primera_letra = nombre[0]
if (nombre[0].upper() < "M" and sexo[0].upper() == "M") or (nombre[0].upper() > "N" and sexo[0].upper() == "H"):
    print("Tu grupo es A")
else:
    print("Tu grupo es B")
    
# codigo aqui  - fin

    