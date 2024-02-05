# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Enunciado: Realice un programa que reciba de nuevo el fichero calificaciones.csv para añadir a cada lista de cada alumno un nuevo elemento, será la Nota Final del curso. El peso de cada parcial de teoría en 
# la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%. Si el alumno ha realizado alguna recuperación ordinaria, para el cálculo de la nota final se tomará esta como última nota 
# del alumno. Se deberá mostrar finalmente en la terminal la lista ordenada y será guardada en un fichero que se llamará calificacionfinal.csv

import csv

# Leer el archivo calificaciones.csv
with open('calificaciones.csv', newline='') as file_gutierrez:
    csv_reader = csv.reader(file_gutierrez)
    data_gutierrez = [row_gutierrez for row_gutierrez in csv_reader]

# Calcular la nota final para cada alumno y agregarla a la lista de calificaciones
for row_gutierrez in data_gutierrez:
    parcial_1_gutierrez = float(row_gutierrez[1])
    parcial_2_gutierrez = float(row_gutierrez[2])
    practicas_gutierrez = float(row_gutierrez[3])

    # Verificar si el alumno ha realizado recuperación ordinaria
    if len(row_gutierrez) > 4:
        ultima_nota_gutierrez = float(row_gutierrez[-1])
        nota_final_gutierrez = ultima_nota_gutierrez
    else:
        # Calcular la nota final según el peso de cada parcial y práctica
        nota_final_gutierrez = (parcial_1_gutierrez * 0.3) + (parcial_2_gutierrez * 0.3) + (practicas_gutierrez * 0.4)

    # Agregar la nota final al final de la lista del alumno
    row_gutierrez.append(round(nota_final_gutierrez, 2))

# Ordenar la lista de calificaciones por el primer elemento de cada lista (el nombre del alumno)
data_sorted_gutierrez = sorted(data_gutierrez, key=lambda x: x[0])

# Mostrar la lista ordenada en la terminal
for row_gutierrez in data_sorted_gutierrez:
    print(row_gutierrez)

# Guardar la lista ordenada en un archivo calificacionfinal.csv
with open('calificacionfinal.csv', 'w', newline='') as file_gutierrez:
    csv_writer = csv.writer(file_gutierrez)
    csv_writer.writerows(data_sorted_gutierrez)


