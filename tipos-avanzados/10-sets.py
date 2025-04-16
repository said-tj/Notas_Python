# set siginifica grupo o conjunto.
"""
Es una colección de datos que no se puede repetir y
que tampoco este ordenada. Con este tipo de datos (sets)
no podemos acceder a ellos (elementos) como si fuera una
lisata/array.
"""

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)
segundo = [3, 4, 5]

# La función set(), recibe como argumento un iterable y
# saebemos que las listas son iterables.
segundo = set(segundo)

# La operación unión de sets.
# print(primer | segundo)

# La operación intersección de sets.
# print(primer & segundo)

# La operación diferencia de sets.
# print(primer - segundo)

# La operación diferencia simetrica de sets.
# print(primer ^ segundo)

# No podemos acceder a ellos, pero podemos 
# preguntar si esta un x elementos dentro del set.
if 5 in segundo:
    print("Si existe")