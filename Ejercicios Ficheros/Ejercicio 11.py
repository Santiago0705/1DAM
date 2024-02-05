# Santiago José Gutiérrez Guillén
# Ejercicio 11
# Enunciado: Escribe un programa en python que lea el fichero gazpacho.json con datos su origen e ingredientes, a continuación deberá  crear otro fichero primerapellido_ingredientes.json con los todos los 
# datos de sus ingredientes.

import json

# Leer el archivo gazpacho.json y obtener datos de los ingredientes
with open('gazpacho.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

ingredientes_gutierrez = data_gutierrez['receta']['ingredientes']

# Crear un nuevo archivo primerapellido_ingredientes.json con los datos de los ingredientes
with open('primerapellido_ingredientes.json', 'w') as file_ingredientes_gutierrez:
    json.dump({"ingredientes": ingredientes_gutierrez}, file_ingredientes_gutierrez, indent=4)
