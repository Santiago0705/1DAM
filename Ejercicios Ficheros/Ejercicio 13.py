# Santiago José Gutiérrez Guillén
# Ejercicio 13
# Enunciado: Escribe un programa en python que lea el fichero *movies.json con datos de películas. A continuación deberá crear un fichero primerapellido_peliculasaventuras.json con los títulos de las películas cuyo género incluya aventura.
# *hay algunos títulos de películas que vienen con una mala codificación, no afectará a la resolución del ejercicio.

import json

# Leer el archivo movies.json y obtener los títulos de las películas de aventura
with open('movies.json') as file_gutierrez:
    data_gutierrez = json.load(file_gutierrez)

peliculas_aventura_gutierrez = [pelicula_gutierrez['titulo'] for pelicula_gutierrez in data_gutierrez['peliculas'] if 'Aventura' in pelicula_gutierrez['genero']]

# Crear un nuevo archivo primerapellido_peliculasaventuras.json con los títulos de las películas de aventura
with open('gutierrez_peliculasaventuras.json', 'w') as file_aventuras_gutierrez:
    json.dump({"peliculas_aventura": peliculas_aventura_gutierrez}, file_aventuras_gutierrez, indent=4)
