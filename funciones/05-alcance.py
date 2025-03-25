saludo = 25

def saludar():
    global saludo   # Esto es una pésima práctica/no hacerlo.
    saludo = "Hola!"
    print(saludo)

def saluda():
    saludo = "Hola Crazy!"


resultado1 = saludo + 10
print(resultado1)
saludar()
resultado2 = saludo + 20    # Existe en esta línea un error pues tratamos de concatenar un string con un entero.
print(resultado2)
