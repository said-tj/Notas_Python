"""
Una tupla no la podemos modificar en absoluto,
a diferencia de una lista/array. Es decir
no se puede agregar elementos, no se pude quitar elementos
no se pueden modificar. Pero podemos crear nuevas tuplas 
con las existentes, es decir podemos crear nuevas tuplas pero 
no modificar las existentes.
"""

numeros = (1, 3, 5) + (1, 1, 1)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)


"""
En caso de querer modificar la tupla, lo único que podemos
hacer es convertirla a una lista/array y ahora si ya podemos
modificarla y demás.
"""
listaNumeros = list(numeros)
listaNumeros[0] = "S"

print(listaNumeros)