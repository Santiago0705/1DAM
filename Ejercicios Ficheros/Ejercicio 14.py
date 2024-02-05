# Santiago José Gutiérrez Guillén
# Ejercicio 14
# Enunciado: Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería y muestre en la terminal cuántos libros hay en la librería.

import json

# Leer el archivo libreria.json y contar los libros
with open('libreria.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

cantidad_libros_gutierrez = len(data_gutierrez['libros'])

print(f"La librería tiene {cantidad_libros_gutierrez} libros.")
