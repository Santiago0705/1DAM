# Solicita el número del día de la semana al usuario
numero_dia = int(input("Introduzca un número del 1 al 7: "))

# Usa un diccionario para mapear los números a los días de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Verifica si el número está en el rango válido (1 al 7)
if numero_dia in dias_semana:
    # Obtiene el día correspondiente al número ingresado
    dia_correspondiente = dias_semana[numero_dia]

    # Muestra el resultado
    print(f"El día correspondiente al número {numero_dia} es {dia_correspondiente}.")
else:
    print("ERROR: Número fuera de rango. Debe ser un número del 1 al 7.")
