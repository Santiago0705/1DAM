# Santiago José Gutiérrez Guillén
# Ejercicio 15
# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
# de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

# Crear listas para los equipos y los resultados de la quiniela
equipos_gutierrez = [[] for _ in range(15)]  # Lista de listas para los equipos de cada partido
resultados_gutierrez = [[] for _ in range(15)]  # Lista de listas para los resultados de cada partido

num_jornadas_gutierrez = int(input("Ingrese el número de jornadas a gestionar: "))

# Capturar los nombres de los equipos y los resultados de cada jornada
for jornada_gutierrez in range(num_jornadas_gutierrez):
    print(f"Ingrese los equipos y resultados para la jornada {jornada_gutierrez + 1}:")
    for partido_gutierrez in range(15):
        equipo_local_gutierrez = input(f"Equipo local del partido {partido_gutierrez + 1}: ")
        equipo_visitante_gutierrez = input(f"Equipo visitante del partido {partido_gutierrez + 1}: ")
        resultado_local_gutierrez = int(input(f"Goles del equipo local en el partido {partido_gutierrez + 1}: "))
        resultado_visitante_gutierrez = int(input(f"Goles del equipo visitante en el partido {partido_gutierrez + 1}: "))

        equipos_gutierrez[partido_gutierrez].append((equipo_local_gutierrez, equipo_visitante_gutierrez))
        resultados_gutierrez[partido_gutierrez].append((resultado_local_gutierrez, resultado_visitante_gutierrez))

# Imprimir la quiniela de cada jornada
for jornada_gutierrez in range(num_jornadas_gutierrez):
    print(f"Quiniela de la jornada {jornada_gutierrez + 1}:")
    for partido_gutierrez in range(15):
        equipo_local_gutierrez, equipo_visitante_gutierrez = equipos_gutierrez[partido_gutierrez][jornada_gutierrez]
        goles_local_gutierrez, goles_visitante_gutierrez = resultados_gutierrez[partido_gutierrez][jornada_gutierrez]
        print(f"Partido {partido_gutierrez + 1}: {equipo_local_gutierrez} vs {equipo_visitante_gutierrez} - Resultado: {goles_local_gutierrez}-{goles_visitante_gutierrez}")
