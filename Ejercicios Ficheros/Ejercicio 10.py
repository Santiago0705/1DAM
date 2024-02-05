# Santiago José Gutiérrez Guillén
# Ejercicio 10
# Enunciado: Escribe un programa en python que lea el fichero json pedidos.json con datos de ordenes, a continuación deberá  crear otro fichero primerapellido_clientes.json con los todos los datos de los clientes.

import json

# Leer el archivo pedidos.json y obtener datos de clientes
with open('pedidos.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

clientes_gutierrez = []
for orden_gutierrez in data_gutierrez['ordenes']:
    cliente_gutierrez = orden_gutierrez['cliente']
    clientes_gutierrez.append(cliente_gutierrez)

# Crear un nuevo archivo primerapellido_clientes.json con los datos de los clientes
with open('primerapellido_clientes.json', 'w') as file_clientes_gutierrez:
    json.dump({"clientes": clientes_gutierrez}, file_clientes_gutierrez, indent=4)
