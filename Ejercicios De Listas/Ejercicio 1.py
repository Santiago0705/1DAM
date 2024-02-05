# Santiago José Gutiérrez Guillén
# Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente 
# muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

# Inicializar la lista con 10 valores aleatorios (del 1 al 10)
lista_gutierrez = [random.randint(1, 10) for _ in range(10)]

# Mostrar en pantalla cada elemento de la lista junto con su cuadrado y su cubo
for i_gutierrez in lista_gutierrez:
    print(f"{i_gutierrez}² = {i_gutierrez**2}, {i_gutierrez}³ = {i_gutierrez**3}")