# Taller 1
# Duracion: 20 min
# Nombre : Irasema


# 1
#  Dados dos números cualquiera y mostrar cuál de los dos es menor.
#  considerar el caso en que ambos números son iguales
# codigo aqui  - inicio
print("ejercicio 1---------------------------")
a = int(input("Escribe el Numero 1: "))
b = int(input("Escribe el Numero 2: "))

def numeroMenor(a, b):
    if a < b:
        print("Numero 1 (",a,") es el menor")
    else:
        print("Numero 2 (",b,") es el menor")
numeroMenor(a, b)
# codigo aqui  - fin



# 2
#   Dado un número entero, muestre su valor absoluto. Nota: para los números 
#   positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52),
#   mientras que, para los negativos, su valor absoluto es el número 
#   multiplicado por -1 (el valor absoluto de -52 es 52).
# codigo aqui  - inicio
print("Ejercicio 2---------------------------")
a = int(input("Escribe un numero entero: "))
if a < 0:
    abs = a * -1
else:
    abs = a
print ("El valor absoluto del número ",a," es:",abs)
# codigo aqui  - fin


# 3
#   Hacer un programa que permita saber si un año es bisiesto. Para que un año 
#   sea bisiesto debe ser divisible por 4 y no debe ser
#   divisible por 100, excepto que también sea divisible por 400.
# codigo aqui  - inicio
print("Ejercicio 3---------------------------")
a = int(input("Escribe un año: "))
if (a%20 == 0 and a%100 > 0) or a%400 == 0:
    print("El año", a, "SI es bisiesto")
else:
    print("El año", a, "NO es bisiesto")
# codigo aqui  - fin

    