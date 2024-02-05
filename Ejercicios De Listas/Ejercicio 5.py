# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

# Importar el módulo random
import random

# Generar una lista de 10 números aleatorios
lista_gutierrez = [random.randint(1, 100) for _ in range(10)]

# Mostrar los resultados por la pantalla
print("Vector antes de ordenar: ", lista_gutierrez)

# Ordenar la lista de números
lista_ordenada_gutierrez = sorted(lista_gutierrez)

# Mostrar los resultados por la pantalla
print("Vector después de ordenar: ", lista_ordenada_gutierrez)