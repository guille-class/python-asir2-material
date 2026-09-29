# Funciones predeterminadas y personalizadas (Tema 3)

IVA = 0.21


# Función personalizada: la definimos nosotros
def precio_con_descuento(precio, descuento):
    return precio - precio * descuento / 100


# Función personalizada que usa una predeterminada (round)
def precio_final(precio, descuento):
    con_descuento = precio_con_descuento(precio, descuento)
    return round(con_descuento * (1 + IVA), 2)


# Invocaciones
print("80 € con un 25 % de descuento:", precio_con_descuento(80, 25))
print("Precio final con IVA:", precio_final(80, 25))
