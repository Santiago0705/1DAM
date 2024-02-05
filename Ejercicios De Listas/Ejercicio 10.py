# Santiago José Gutiérrez Guillén
# Ejercicio 10
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

# Crear la tabla (lista de listas) de 5x5 e inicializarla con valores numéricos enteros
tabla_gutierrez = []
for i_gutierrez in range(5):
    fila_gutierrez = []
    for j_gutierrez in range(5):
        valor_gutierrez = int(input(f"Ingrese el valor para la posición [{i_gutierrez+1},{j_gutierrez+1}]: "))
        fila_gutierrez.append(valor_gutierrez)
    tabla_gutierrez.append(fila_gutierrez)

# Mostrar la tabla ingresada
print("Tabla ingresada:")
for fila_gutierrez in tabla_gutierrez:
    print(fila_gutierrez)

# Sumar los elementos de cada fila y mostrar los resultados
print("Suma de elementos por fila:")
for i_gutierrez, fila_gutierrez in enumerate(tabla_gutierrez, start=1):
    suma_fila_gutierrez = sum(fila_gutierrez)
    print(f"Suma de la fila {i_gutierrez}: {suma_fila_gutierrez}")

# Sumar los elementos de cada columna y mostrar los resultados
print("\nSuma de elementos por columna:")
for j_gutierrez in range(len(tabla_gutierrez[0])):
    suma_columna_gutierrez = sum(tabla_gutierrez[i_gutierrez][j_gutierrez] for i in range(len(tabla_gutierrez)))
    print(f"Suma de la columna {j_gutierrez+1}: {suma_columna_gutierrez}")
