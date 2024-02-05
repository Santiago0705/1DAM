# Santiago José Gutiérrez Guillén
# Ejercicio 6
# Enunciado: Realice un programa que reciba de nuevo el fichero calificacionfinal.csv para  generar dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la 
# asistencia tiene que ser mayor o igual que el 75% y la nota final mayor o igual que 5. Se deberá guardar las dos listas en dos ficheros distintos con los nombres aprobados.csv y suspensos.csv.

import csv

# Leer el archivo calificacionfinal.csv y crear listas de aprobados y suspensos
aprobados_gutierrez = []
suspendidos_gutierrez = []

with open('calificacionfinal.csv', newline='') as file_gutierrez:
    csv_reader_gutierrez = csv.reader(file_gutierrez)
    next(csv_reader_gutierrez)  # Saltar la primera fila que contiene los encabezados

    for row_gutierrez in csv_reader_gutierrez:
        # Obtener datos relevantes
        asistencia_gutierrez = float(row_gutierrez[-2])
        nota_final_gutierrez = float(row_gutierrez[-1])

        # Verificar condiciones para aprobación
        if asistencia_gutierrez >= 75 and nota_final_gutierrez >= 5:
            aprobados_gutierrez.append(row_gutierrez)
        else:
            suspendidos_gutierrez.append(row_gutierrez)

# Guardar lista de aprobados en aprobados.csv
with open('aprobados.csv', 'w', newline='') as file_aprobados_gutierrez:
    csv_writer_aprobados_gutierrez = csv.writer(file_aprobados_gutierrez)
    csv_writer_aprobados_gutierrez.writerows(aprobados_gutierrez)

# Guardar lista de suspendidos en suspendidos.csv
with open('suspendidos.csv', 'w', newline='') as file_suspendidos_gutierrez:
    csv_writer_suspendidos_gutierrez = csv.writer(file_suspendidos_gutierrez)
    csv_writer_suspendidos_gutierrez.writerows(suspendidos_gutierrez)
