# Santiago José Gutiérrez Guillén
# Ejercicio 2
# Enunciado: Codifica un programa en python que nos permita guardar la temperatura mínima y máxima de los últimos 7 días la semana. Dicha información deberá ser guardada en un diccionario.
# El programa pedirá al usuario las temperaturas de todos los días . Al final el programa nos mostrará:
# -La lista de todos los días de la semana con su temperatura mínima y máxima con el siguiente formato:
# El día_de_la-semana ha tenido las siguientes temperaturas mínimas y máximas: ('mímima', 'máxima') 
# -Deberá mostrar también la temperatura media mínima y la temperatura media máxima de los últimos 7 días redondeada a dos cifras decimales.

# Crear un diccionario para almacenar las temperaturas
temperaturas_semana_santiago = {}

# Pedir al usuario las temperaturas de cada día de la semana
dias_semana_santiago = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

for dia_santiago in dias_semana_santiago:
    temp_min_santiago = float(input(f"Ingrese la temperatura mínima para el {dia_santiago}: "))
    temp_max_santiago = float(input(f"Ingrese la temperatura máxima para el {dia_santiago}: "))
    temperaturas_semana_santiago[dia_santiago] = (temp_min_santiago, temp_max_santiago)

# Mostrar las temperaturas mínimas y máximas de cada día
for dia_santiago, temperaturas_santiago in temperaturas_semana_santiago.items():
    print(f"El {dia_santiago} ha tenido las siguientes temperaturas mínimas y máximas: {temperaturas_santiago}")

# Calcular temperatura media mínima y máxima
temp_minima_media_santiago = sum(temp_santiago[0] for temp_santiago in temperaturas_semana_santiago.values()) / len(temperaturas_semana_santiago)
temp_maxima_media_santiago = sum(temp_santiago[1] for temp_santiago in temperaturas_semana_santiago.values()) / len(temperaturas_semana_santiago)

# Mostrar la temperatura media mínima y máxima
print(f"La temperatura media mínima de la semana es: {temp_minima_media_santiago:.2f}")
print(f"La temperatura media máxima de la semana es: {temp_maxima_media_santiago:.2f}")
