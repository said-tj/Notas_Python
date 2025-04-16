mascotas = [
    "Wolfgram",
    "Pelusa",
    "Pulga",
    "Tobi",
    "Shagui"
]
mascotas.insert(1,"Palomo")
mascotas.append("Canelito")
mascotas.append("Torti")

mascotas.remove("Pelusa")
mascotas.pop()
mascotas.pop(0)
del mascotas[1]
mascotas.clear() # Para limpiar totalmente el arreglo.
print(mascotas)