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

palindromo(mensaje="Reconocer")





# Solución 2.
# def no_space(texto):
#     nuevo_texto = ""
#     for char in texto:
#         if char != " ":
#             nuevo_texto += char
#     return nuevo_texto

# def reverse(texto):
#     texto_al_reves = ""
#     for char in texto:
#         texto_al_reves = char + texto_al_reves
#     return texto_al_reves

# def es_palindromo(texto):
#     texto = no_space(texto)
#     texto_al_reves = reverse(texto)
#     return texto.lower() == texto_al_reves.lower()

# print(es_palindromo("amo la paloma"))
# print(es_palindromo("Hola Mundo"))
# print(es_palindromo("Reconocer"))