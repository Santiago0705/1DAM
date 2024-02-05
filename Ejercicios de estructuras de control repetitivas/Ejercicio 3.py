# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

# Inicializar variables
suma_gutierrez = 0
contador_gutierrez = 0

# Bucle para pedir números hasta que se introduzca un cero
while True:
    # Pedir un número al usuario
    num_gutierrez = float(input("Introduce un número (introduce 0 para salir): "))

    # Salir del bucle si se introduce un cero
    if num_gutierrez == 0:
        break

    # Actualizar la suma y el contador
    suma_gutierrez += num_gutierrez
    contador_gutierrez += 1

# Calcular la media (evitar división por cero)
if contador_gutierrez > 0:
    media_gutierrez = suma_gutierrez / contador_gutierrez
    print("La suma de los números es: ", suma_gutierrez)
    print("La media de los números es: ", media_gutierrez)
else:
    print("No se introdujo ningún número.")
