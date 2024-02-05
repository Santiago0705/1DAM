# Santiago José Gutierrez Guillén
# Ejercicio 18
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

# Pedir al usuario la duración del cronómetro en segundos
duracion_gutierrez = int(input("Ingrese la duración del cronómetro en segundos: "))

# Iniciar el cronómetro
for segundos_restantes_gutierrez in range(duracion_gutierrez, 0, -1):
    # Calcular horas, minutos y segundos
    horas_gutierrez = segundos_restantes_gutierrez // 3600
    minutos_gutierrez = (segundos_restantes_gutierrez % 3600) // 60
    segundos_gutierrez = segundos_restantes_gutierrez % 60

    # Imprimir el tiempo restante en el formato HH:MM:SS
    print(f"{horas_gutierrez:02d}:{minutos_gutierrez:02d}:{segundos_gutierrez:02d}", end='\r')

    # Esperar un segundo
    time.sleep(1)

# Imprimir mensaje al finalizar el cronómetro
print("¡Cronómetro finalizado!")
