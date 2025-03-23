# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

# comando = ""

# # Utiliza lower() para que independientemente de como lo escriba el usuario, lo transformemmos a minúsculas y funcione.
# while comando.lower() != "salir":   
#     comando = input("$ ")
#     print(comando)


# Este es un ciclo infinito, pero al agregar la instrucción de paro, lo limitamos.
while True:
    comando = input("$ ")
    print(comando)
    if comando == "salir":
        break