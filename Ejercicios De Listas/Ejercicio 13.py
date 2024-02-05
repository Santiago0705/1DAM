# Santiago José Gutiérrez Guillén
# Ejercicio 13
# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

# Lista de conductores
conductores_gutierrez = ['Santi', 'María', 'Pepe']

# Matriz para guardar los kilómetros conducidos por cada conductor cada día de la semana
kms_gutierrez = [[100, 200, 300, 400, 500, 600, 700],
       [200, 300, 400, 500, 600, 700, 800],
       [300, 400, 500, 600, 700, 800, 900]]

# Generar la lista de total_kms con los kilómetros totales que realiza cada conductor
total_kms_gutierrez = [sum(fila_gutierrez) for fila_gutierrez in kms_gutierrez]

# Mostrar la lista con los nombres de conductores y los kilómetros que ha realizado
for i_gutierrez in range(len(conductores_gutierrez)):
    print(f"{conductores_gutierrez[i_gutierrez]}: {total_kms_gutierrez[i_gutierrez]} kms")