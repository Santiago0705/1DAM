import math

# Solicitamos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calculamos la raíz cuadrada del número
raiz_cuadrada = math.sqrt(numero)

# Calculamos la raíz cúbica del número utilizando la función cbrt de la biblioteca math
raiz_cubica = math.pow(numero, (1. / 3.))

# Mostramos la raíz cuadrada y la raíz cúbica en la pantalla
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("La raíz cúbica de", numero, "es:", raiz_cubica)