# Santiago José Gutiérrez Guillén
# Ejercicio 8
# Enunciado: Escribe un programa en python que lea el fichero json colores.json con datos de colores, deberá mostrar en la terminal todos los nombres de colores, sus códigos rgba y hexadecimal respectivamente.

import json

# Leer el archivo colores.json
with open('colores.json') as file_gutierrez:
    datos_colores_gutierrez = json.load(file_gutierrez)

# Mostrar los nombres, códigos RGBA y códigos hexadecimales en la terminal
for color_gutierrez in datos_colores_gutierrez['colores']:
    nombre_gutierrez = color_gutierrez['nombre']
    rgba_gutierrez = color_gutierrez['rgba']
    hexadecimal_gutierrez = color_gutierrez['hexadecimal']
    print(f"Nombre: {nombre_gutierrez}, RGBA: {rgba_gutierrez}, Hexadecimal: {hexadecimal_gutierrez}")
