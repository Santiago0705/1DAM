# Santiago José Gutiérrez Guillén
# Ejercicio 6
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene 
# (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

# Crear una lista con los días de cada mes
dias_por_mes_gutierrez = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Crear una lista con los nombres de los meses
nombres_meses_gutierrez = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Pedir al usuario un número de mes
mes_gutierrez = int(input("Ingrese un número de mes (por ejemplo, 4): "))

# Calcular el índice del mes en la lista (recordando que las listas en Python comienzan en 0)
indice_mes_gutierrez = mes_gutierrez - 1

# Mostrar cuántos días tiene el mes y el nombre del mes
print("Ese mes tiene ", dias_por_mes_gutierrez[indice_mes_gutierrez], " días.")
print("El nombre del mes es ", nombres_meses_gutierrez[indice_mes_gutierrez], ".")