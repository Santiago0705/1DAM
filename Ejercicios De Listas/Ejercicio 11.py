# Santiago José Gutiérrez Guillén
# Ejercicio 11
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.

# Crear una matriz bidimensional de longitud 5x5 y nombre ‘diagonal’
diagonal_gutierrez = [[0]*5 for _ in range(5)]

# Cargar la matriz de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0
for i_gutierrez in range(5):
    diagonal_gutierrez[i_gutierrez][i_gutierrez] = 1

# Mostrar el contenido de la matriz en pantalla
for i_gutierrez in range(5):
    for j_gutierrez in range(5):
        print(diagonal_gutierrez[i_gutierrez][j_gutierrez], end=" ")
    print()