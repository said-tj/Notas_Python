# """
# Para desempaquetar cada elemento que este en una
# lista o en una tupla.
# """

# lista = [1, 2, 3, 4]

# # print(*lista)

# lista2 = [5, 6]

# combinada = [*lista, *lista2]

# combinada2 = ["Hola",*lista, "mundo", *lista2]

# print(combinada)
# print(combinada2)


"""
También este operador funciona con los
diccionarios, pero para este caso
se utilizan **
"""
punto1 = {"x": 10, "y": "hola"}
punto2 = {"y": 20}

# Los diccionario se leen de derecha a izquierda, por lo cual
# no se va a leer el "y": "hola"
nuevoPunto = {**punto1, "a": "hola", **punto2, "z": "mundo"}
print(nuevoPunto)