# Santiago José Gutiérrez Guillén
# Ejercicio 4
# Enunciado: El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo al final del curso (convocatoria ordinaria). Realiza un programa que haga lo siguiente:
# Reciba el fichero de calificaciones.csv y devuelva una lista de listas, donde cada lista contiene la información de los exámenes y la asistencia de un alumno. Para ordenar la lista vamos a utilizar una función lambda:
#                    ordenados = sorted(csv_reader,key=lambda x:x[0])
# La función sorted recibe como parámetros la lista que deseas ordenar y el parámetro key es una función que le indica a sorted como debe ordenar, en este caso lambda x: x[0] le dice a sorted que como todos los elementos de la lista son listas escoja para comparar el primer valor de cada lista. Quizás es extraño ver lambda en el código pero es una abreviatura para funciones, si tienes dudas puede consultar documentaciones oficiales.
# Se deberá mostrar la lista ordenada en pantalla.

import csv

# Lee el archivo calificaciones.csv y crea una lista de listas con la información
with open('calificaciones.csv', newline='') as file_gutierrez:
    csv_reader = csv.reader(file_gutierrez)
    data_gutierrez = [row_gutierrez for row_gutierrez in csv_reader]

# Ordena la lista de datos por el primer elemento de cada sublista (nombre del alumno)
ordenados_gutierrez = sorted(data_gutierrez, key=lambda x: x[0])

# Muestra la lista ordenada en pantalla
for alumno_gutierrez in ordenados_gutierrez:
    print(alumno_gutierrez)

