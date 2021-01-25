#Author: Irasema
#Clase padre
class Fichero:
    def __init__(self, directorio, nombre, extension):
        self.directorio = directorio
        self.nombre = nombre
        self.extension = extension
    
    def __str__(self):
        return self.directorio + self.nombre + "." + self.extension

#Clase Hijo 1
class Excel(Fichero):
    def __init__(self, Fichero):
        self.directorio = Fichero.directorio
        self.nombre = Fichero.nombre
        self.extension = "xls"

    def comprimir(self):
        zip = Zip(self)
        print("Se ha comprimido el fichero ==> ", zip)
        return zip
    
    def ejecutarMacro(self):
        print("Se ha ejecutado la macro!")

#Clase Hijo 2
class Zip(Fichero):
    def __init__(self, Fichero):
        self.directorio = Fichero.directorio
        self.nombre = Fichero.nombre
        self.extension = "zip"

    def descomprimir(self):
        excel = Excel(self)
        print("Se ha descomprimido el fichero ==> ", excel)
        return excel
    
    def enviarEmail(self):
        print("Se ha enviado por email!")

print("== Programa que simula la compresion y descompresión de un fichero dependiendo de su extensión (xls y zip) ==\n")
dir = input("Path absoluto donde se ubica el fichero: ").lower()
nom = input("Nombre del fichero: ").lower()
ext = input("Extension del fichero: ").lower()

fichero = Fichero(dir, nom, ext)
print("Datos ingresados ==> ", fichero)
op = 1

while (op < 3):
    if fichero.extension == "zip":
        print('''\nMENU
        1. Desomprimir
        2. Enviar email
        3. Salir''')
        op = int(input("Opcion: "))
        zip = Zip(fichero)
        if op == 1:
            fichero = zip.descomprimir()
        elif op == 2:
            zip.enviarEmail()
        else:
            break
    elif fichero.extension == "xls":
        print('''\nMENU
        1. Ejecutar macro
        2. Comprimir
        3. Salir''')
        op = int(input("Opcion: "))
        excel = Excel(Fichero)
        if op == 1:
            excel.ejecutarMacro()
        elif op == 2:
            fichero = excel.comprimir()
        else: 
            break
    else:
        op = 3
        print("\nERROR: Solo se admiten archivos .xls y .zip")
print("Fin")

