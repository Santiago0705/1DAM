# Santiago José Gutiérrez Guillén
# Ejercicio 12
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
#  111111111111111
#  100000000000001
#  100000000000001
#  100000000000001
#  111111111111111
# Visualiza el contenido de la matriz en pantalla.

# Crear una matriz bidimensional de longitud 5x15 y nombre ‘marco’
marco_gutierrez = [[0]*15 for _ in range(5)]

# Cargar la matriz con dos únicos valores 0 y 1
for i_gutierrez in range(5):
    for j_gutierrez in range(15):
        if i_gutierrez == 0 or i_gutierrez == 4 or j_gutierrez == 0 or j_gutierrez == 14:
            marco_gutierrez[i_gutierrez][j_gutierrez] = 1
        else:
            marco_gutierrez[i_gutierrez][j_gutierrez] = 0

# Mostrar el contenido de la matriz en pantalla
for i_gutierrez in range(5):
    for j_gutierrez in range(15):
        print(marco_gutierrez[i_gutierrez][j_gutierrez], end=" ")
    print()