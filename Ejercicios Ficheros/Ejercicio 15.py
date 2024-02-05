# Santiago José Gutiérrez Guillén
# Ejercicio 15
# Enunciado: Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería, recibe por teclado un límite inferior y superior para el precio y muestre en la terminal 
# todos los libros cuyo precio esta en ese intervalo.

import json

# Leer el archivo libreria.json
with open('libreria.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

# Solicitar límite inferior y superior al usuario para el precio
limite_inferior_gutierrez = float(input("Introduce el límite inferior para el precio: "))
limite_superior_gutierrez = float(input("Introduce el límite superior para el precio: "))

# Mostrar los libros cuyos precios están en el intervalo dado
print(f"Libros cuyo precio está entre {limite_inferior_gutierrez} y {limite_superior_gutierrez}:")
for libro_gutierrez in data_gutierrez['libros']:
    if limite_inferior_gutierrez <= libro_gutierrez['precio'] <= limite_superior_gutierrez:
        print(f"Titulo: {libro_gutierrez['titulo']}, Precio: {libro_gutierrez['precio']}")
