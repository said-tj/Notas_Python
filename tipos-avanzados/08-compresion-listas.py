usuarios = [
    [4, "Palomo"],
    [1, "Shagui"],
    [8, "Canelo"]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)
"""
El siguiente código es una manera más elegante 
de hacer lo que se propone en el código anterior
"""

# Lista transformada. Que este estilo/método es llamada map.
# nombres = [usuario[1] for usuario in usuarios]

# Lista filtrar. Que este estilo/método es llamada filter.
# nombres = [usuario for usuario in usuarios if usuario[0] >  2]

# Lista filtrada y transformada.
# nombres = [usuario[1] for usuario in usuarios if usuario[0] >  2]


# nombres = list(map(lambda usuario: usuario[1], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[0]> 2, usuarios))
print(menosUsuarios)