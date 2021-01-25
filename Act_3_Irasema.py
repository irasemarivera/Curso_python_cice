# Taller 3
# Nombre : 

# 1 Dadas las siguientes clases desarrolle los metodos de agregar, borrar y mostrar

from io import open
import pickle

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(
            self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:

    personajes = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, personaje):

        for p in self.personajes:
            if p.nombre == personaje.nombre:
                print("Personaje", personaje.nombre, "ya existe")
                return

        print("Se agrega nuevo personaje", personaje.nombre)
        self.personajes.append(personaje)
        self.guardar()

    def borrar(self, nombre):
        for p in self.personajes:
            if p.nombre == nombre:
                #print(self.personajes)
                self.personajes.remove(p)
                print(nombre, "borrado")

    def mostrar(self):
        print("Hay", len(self.personajes), "personajes")
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            # print("El fichero está vacío")
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes desde fichero".format( 
                len(self.personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()


# Realizamos las pruebas
G = Gestor()
G.agregar( Personaje("Caballero",4,2,4,2) )
G.agregar( Personaje("Guerrero",2,4,2,4) )
G.agregar( Personaje("Arquero",2,4,1,8) )
G.agregar( Personaje("Paladin",4,4,6,2) )
G.agregar( Personaje("Tanke",10,2,8,4) )
G.agregar( Personaje("Sacerdote",2,1,1,20) )
G.mostrar()
G.borrar("Arquero")
G.guardar()
G.mostrar()