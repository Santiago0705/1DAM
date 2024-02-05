# Santiago José Gutiérrez Guillén
# Ejercicio 9
# Enunciado: Escribe un programa en python que lea el fichero json pedidos.json con datos de órdenes, deberá mostrar en la terminal todos las órdenes de pedidos que no se hayan entregado.

import json

# Leer el archivo pedidos.json
with open('pedidos.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

# Mostrar las órdenes de pedidos que no se han entregado en la terminal
for orden_gutierrez in data_gutierrez['ordenes']:
    if not orden_gutierrez['entregado']:
        print(f"ID: {orden_gutierrez['id']}, Producto: {orden_gutierrez['producto']}, Entregado: {orden_gutierrez['entregado']}")
