# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# Crear e inicializar una lista con 5 notas leídas por teclado
notas_gutierrez = [float(input("Ingrese una nota: ")) for _ in range(5)]

# Calcular la nota media
nota_media_gutierrez = sum(notas_gutierrez) / len(notas_gutierrez)

# Encontrar la nota más alta y la más baja
nota_mas_alta_gutierrez = max(notas_gutierrez)
nota_mas_baja_gutierrez = min(notas_gutierrez)

# Mostrar los resultados por la pantalla
print("Notas: ", notas_gutierrez)
print("Nota media: ", nota_media_gutierrez)
print("Nota más alta: ", nota_mas_alta_gutierrez)
print("Nota más baja: ", nota_mas_baja_gutierrez)