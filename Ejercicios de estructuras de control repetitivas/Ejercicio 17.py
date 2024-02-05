# Santiago José Gutierrez Guillén
# Ejercicio 17
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Para esto, se registran los días que trabajó y las horas de cada día. Realice un 
# algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto 
# pagó la empresa por los N empleados.

# Pedir al usuario el número de trabajadores
num_trabajadores_gutierrez = int(input("Ingrese el número de trabajadores: "))

# Inicializar la variable para el total pagado por la empresa
total_pagado_gutierrez = 0

# Iniciar el bucle para cada trabajador
for i_gutierrez in range(1, num_trabajadores_gutierrez + 1):
    # Pedir al usuario los días trabajados por el trabajador i
    dias_trabajados_gutierrez = int(input(f"Ingrese el número de días trabajados por el trabajador {i_gutierrez}: "))

    # Inicializar la variable para el sueldo semanal del trabajador i
    sueldo_semanal_gutierrez = 0

    # Bucle para cada día trabajado
    for dia_gutierrez in range(1, dias_trabajados_gutierrez + 1):
        # Pedir al usuario las horas trabajadas por día
        horas_dia_gutierrez = float(input(f"Ingrese las horas trabajadas por el trabajador {i_gutierrez} en el día {dia_gutierrez}: "))

        # Pedir al usuario la tarifa por hora del trabajador i
        tarifa_por_hora_gutierrez = float(input(f"Ingrese la tarifa por hora del trabajador {i_gutierrez}: "))

        # Calcular el sueldo para el día actual y sumarlo al sueldo semanal
        sueldo_dia_gutierrez = horas_dia_gutierrez * tarifa_por_hora_gutierrez
        sueldo_semanal_gutierrez += sueldo_dia_gutierrez

    # Imprimir el sueldo semanal del trabajador i
    print(f"El sueldo semanal del trabajador {i_gutierrez} es: ${sueldo_semanal_gutierrez}")

    # Sumar el sueldo al total pagado por la empresa
    total_pagado_gutierrez += sueldo_semanal_gutierrez

# Imprimir el total pagado por la empresa
print(f"\nLa empresa pagó un total de: ${total_pagado_gutierrez}")
