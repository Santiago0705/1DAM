# Solicita al usuario un número entero entre 1 y 12
numero_mes = int(input("Introduzca un número entero entre 1 y 12: "))

# Usa un diccionario para mapear los números de mes a la cantidad de días
dias_por_mes = {
    1: 31,  # Enero
    2: 28,  # Febrero (sin considerar años bisiestos)
    3: 31,  # Marzo
    4: 30,  # Abril
    5: 31,  # Mayo
    6: 30,  # Junio
    7: 31,  # Julio
    8: 31,  # Agosto
    9: 30,  # Septiembre
    10: 31,  # Octubre
    11: 30,  # Noviembre
    12: 31   # Diciembre
}

# Verifica si el número está en el rango válido (1 a 12)
if numero_mes in dias_por_mes:
    # Obtiene la cantidad de días del mes correspondiente al número ingresado
    cantidad_dias = dias_por_mes[numero_mes]

    # Muestra el resultado
    print(f"El mes {numero_mes} tiene {cantidad_dias} días.")
else:
    print("ERROR: Número fuera de rango. Debe ser un número entre 1 y 12.")
