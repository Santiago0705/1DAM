# Santiago José Gutiérrez Guillén
# Ejercicio 12
# Enunciado: Escribe un programa en python que lea el fichero *movies.json con datos de películas. A continuación deberá crear un fichero primerapellido_pelicula1994.json con los títulos de las películas  
# que se hayan estrenado en 1994.
# *hay algunos títulos de películas que vienen con una mala codificación, no afectará a la resolución del ejercicio.

import json

# Leer el archivo movies.json y obtener los títulos de las películas estrenadas en 1994
with open('movies.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

peliculas_1994_gutierrez = [pelicula_gutierrez['titulo'] for pelicula_gutierrez in data_gutierrez['peliculas'] if pelicula_gutierrez['anio'] == 1994]

# Crear un nuevo archivo primerapellido_pelicula1994.json con los títulos de las películas estrenadas en 1994
with open('gutierrez_pelicula1994.json', 'w') as file_1994_gutierrez:
    json.dump({"peliculas_1994": peliculas_1994_gutierrez}, file_1994_gutierrez, indent=4)
