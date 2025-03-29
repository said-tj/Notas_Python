# numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Para imprimir los elementos de la lista.
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero) 

# Como desempaquetar elementos de una lista, de manera elegante y corta.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primero, segundo, *otros, penultimo, ultimo = numeros
print(primero, segundo, penultimo, ultimo, otros)

