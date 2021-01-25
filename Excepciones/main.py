print("Manejo de errores y excepciones ---------------------")
# def suma1(a, b):
#     print(a + b)

# def suma2(a, b):
#     try:
#         return a + b
#     except Exception as e:
#         return 'Error capturado: ' + str(e)

#suma1(' ', 10)
# print(suma2(' ', 10))
# print(suma2(10,34))

#multiples excepciones
# try:
#     with open('fname') as f:
#         content = f.readlines()
# except (IOError, NameError) as e:
#     print(str(e))

#Definir una excepcion propia
# class NuevaExcepcion(Exception):
#     pass

#lanzar una excepcion
def sumar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a y b tienen que ser números enteros")
    return a + b

print(sumar(1, ' '))

