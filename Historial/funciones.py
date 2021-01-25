# print("Paso de parametros - por valor----------------------")

# # def doblar_valor(numero):
# #     numero *= 2

# def doblar_valor(numero):
#     return numero * 2

# n = 30
# print("antes: ", n)
# n = doblar_valor(n)
# print("despues: ", n)

# print("Paso de parametros - por referencia-----------------------")

# def doblar_numeros(numeros):
#     for i, n in enumerate(numeros):
#         numeros[i] *= 2

# ns = [10, 50, 100]
# print("antes: ", ns)
# doblar_numeros(ns)
# print("despues: ", ns)

# print("FUNCIONES ANONIMAS, LAMBDAS--------------------")

# mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos #funciones simples sin ciclos ni instrucciones complejas

#formato = lambda sentencia : '{}?'.format(sentencia)
# formato = lambda sentencia : sentencia + "?"
#no_valor = lambda : 10

# no_resultado = lambda : print("Debe ejecutar alguna accion---")

#resultado = mi_funcion(10,20)

#resultado =  formato("Puedes hacer esto una pregunta")

# resultado = no_resultado()
# print(resultado)

print ("FUNCIONES ANIDADAS-----")

def division(num_uno, num_dos):
    
    def validacion():
        return num_uno > 0 and num_dos > 0
    
    if validacion():
        return num_uno / num_dos
    else:
        return "No se puede dividir"

print(division(8,0))