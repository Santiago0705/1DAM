# Santiago José Gutiérrez Guillén
# Ejercicio 7
# Enunciado: El fichero cotizaciones.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
# Construir un programa que reciba el fichero de cotizaciones , devuelva un diccionario y lo imprima en la terminal con el mismo formato que el fichero. 
# A continuación se deberá crear una lista de diccionarios con el nombre de las columnas medibles, su máximo, su mínimo y su media aritmética. Esta lista se deberá guardar en un fichero llamado ejercicio7_primerapellido en formato csv.

import csv

# Leer el archivo cotizaciones.csv y crear un diccionario
cotizaciones_gutierrez = []

with open('cotizaciones.csv', newline='') as file_gutierrez:
    csv_reader = csv.DictReader(file_gutierrez)
    for row_gutierrez in csv_reader:
        cotizaciones_gutierrez.append(row_gutierrez)
        print(row_gutierrez)

# Crear una lista de diccionarios con el nombre de las columnas medibles,
# su máximo, su mínimo y su media aritmética
medidas_gutierrez = []

columnas_medibles_gutierrez = ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']

for columna_gutierrez in columnas_medibles_gutierrez:
    valores_columna_gutierrez = [float(dato_gutierrez[columna_gutierrez].replace(',', '.')) for dato_gutierrez in cotizaciones_gutierrez]
    maximo_gutierrez = max(valores_columna_gutierrez)
    minimo_gutierrez = min(valores_columna_gutierrez)
    media_gutierrez = sum(valores_columna_gutierrez) / len(valores_columna_gutierrez)
    medidas_gutierrez.append({'Columna': columna_gutierrez, 'Máximo': maximo_gutierrez, 'Mínimo': minimo_gutierrez, 'Media': media_gutierrez})

# Guardar la lista de diccionarios en un archivo llamado ejercicio7_primerapellido.csv
nombre_archivo_gutierrez = 'ejercicio7_gutierrez.csv'

with open(nombre_archivo_gutierrez, 'w', newline='') as file_gutierrez:
    fieldnames_gutierrez = ['Columna', 'Máximo', 'Mínimo', 'Media']
    writer_gutierrez = csv.DictWriter(file_gutierrez, fieldnames=fieldnames_gutierrez)
    
    writer_gutierrez.writeheader()
    writer_gutierrez.writerows(medidas_gutierrez)
