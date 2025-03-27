def palindromo(mensaje):
    mensaje_sin_espacio = mensaje.lower().replace(" ", "")
    texto_a = ""
    texto_b = ""
    for i in mensaje_sin_espacio:
        texto_a += i
    for h in range(len(mensaje_sin_espacio)-1, -1, -1):
        contador = mensaje_sin_espacio[h]
        texto_b += contador
    if texto_a == texto_b:
        print(f"El texto {mensaje} es un palindromo.")
    else:
        print(f"El texto {mensaje} no es un palindromo.")

palindromo(mensaje="Abba")