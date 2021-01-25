print("FICHEROS LECTURA ---------------------------------")

dirFichero = "fichero.txt"
with open(dirFichero, 'r') as reader:
    for line in reader:
        print(line)

# print("FICHEROS ESCRITURA --------------------------------")
# lineas = ["uno", "dos", "tres"]
# cadena = "hola esto es una prueba!"
# lineas = cadena.split(" ")
# dirFichero = "fichero.txt"
# fichero = open(dirFichero, 'w+')
# for l in lineas:
#     fichero.write(l + "\n")
# fichero.close()
