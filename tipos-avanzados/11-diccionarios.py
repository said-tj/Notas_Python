"""
Para este tipo de datos, como llave solo permite el tipo string
y el contenido pude ser cualquier cosa.
"""
punto = {"x": 25, "y": 50}
print(punto["x"])
print(punto["y"])

punto["z"] = 45
#print(punto)

if "lala" in punto:
    print("Encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]
del(punto["y"])

print(punto)

punto["x"] = 25

# Métodos para acceder a los diccionarios.
for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Francisco"},
    {"id": 2, "nombre": "Yahir"},
    {"id": 3, "nombre": "Armando"},
    {"id": 4, "nombre": "Carlos"}
]

"""
Si queremos solo ingresar a los nombres
de los usuarios, entonces
"""

for usuario in usuarios:
    print(usuario["nombre"])