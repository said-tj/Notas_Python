numeros = [5, 7, 2, 11, 3, 13]

# numeros.sort(reverse = True) # Ordenar de manera descendente.
numeros_2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros_2)

usuarios = [
    [4, "Palomo"],
    [1, "Shagui"],
    [8, "Canelo"]
]

# Para ordenar el listado, pero buscando el index 1, que es donde esta el 
# elemento ordenable.
# def ordena(elemento):
#     return elemento[1]

# Se implemento una función lambda, por eso se comento la función anterior.
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)