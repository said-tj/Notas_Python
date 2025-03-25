def get_product(**datos):
    print(datos["id"], datos["name"])   # Para acceder a un(os) parámetro especificos.

get_product(id="25",
            name="IPhone",
            desc="Esto es un Iphone")