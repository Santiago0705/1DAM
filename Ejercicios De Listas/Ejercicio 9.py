# Santiago José Gutiérrez Guillén
# Ejercicio 9
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

temperaturas_gutierrez = []

for i_gutierrez in range(5):
    temperatura_min_gutierrez = float(input(f"Ingrese la temperatura mínima del día {i_gutierrez + 1}: "))
    temperatura_max_gutierrez = float(input(f"Ingrese la temperatura máxima del día {i_gutierrez + 1}: "))
    temperaturas_gutierrez.append((temperatura_min_gutierrez, temperatura_max_gutierrez))

# Calculando la temperatura media de cada día
print("Temperatura media de cada día:")
for i_gutierrez, (temp_min_gutierrez, temp_max_gutierrez) in enumerate(temperaturas_gutierrez, start=1):
    temp_media_gutierrez = (temp_min_gutierrez + temp_max_gutierrez) / 2
    print(f"Día {i_gutierrez}: {temp_media_gutierrez:.2f} grados")

# Encontrando los días con menos temperatura
minima_temperatura_gutierrez = min(temperaturas_gutierrez, key=lambda x: x[0])[0]
print(f"Días con menos temperatura ({minima_temperatura_gutierrez}°C):")
for i_gutierrez, (temp_min_gutierrez, temp_max_gutierrez) in enumerate(temperaturas_gutierrez, start=1):
    if temp_min_gutierrez == minima_temperatura_gutierrez:
        print(f"Día {i_gutierrez}")

# Búsqueda de días con una temperatura máxima específica
temp_buscada_gutierrez = float(input("Ingrese una temperatura máxima a buscar: "))
dias_con_temp_gutierrez = [i_gutierrez + 1 for i_gutierrez, (_, temp_max_gutierrez) in enumerate(temperaturas_gutierrez) if temp_max_gutierrez == temp_buscada_gutierrez]

if dias_con_temp_gutierrez:
    print(f"Días con temperatura máxima de {temp_buscada_gutierrez}°C: {', '.join(map(str, dias_con_temp_gutierrez))}")
else:
    print(f"No hay ningún día con una temperatura máxima de {temp_buscada_gutierrez}°C")
