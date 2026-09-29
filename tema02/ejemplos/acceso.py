# Control de acceso (Tema 2, caso práctico 2)

# Constantes
EDAD_MINIMA = 18

# Datos de ejemplo
edad_usuario = 20
tiene_carne_universitario = True

# Verificación de acceso
puede_entrar = (edad_usuario >= EDAD_MINIMA) and tiene_carne_universitario

# Mostrar resultado
print("¿Acceso permitido?", puede_entrar)
