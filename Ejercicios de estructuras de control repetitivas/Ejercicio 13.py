# Santiago José Gutiérrez Guillén
# Ejercicio 13
# Una empresa tiene el registro de las horas que trabaja diariamente un 
# empleado durante la semana (seis días) y requiere determinar el total de
# éstas, así como el sueldo que recibirá por las horas trabajadas.

# Bucle para los seis días de la semana
for dia_gutierrez in range(1, 7):
# Pedir las horas trabajadas en el día actual
    horas_trabajadas_gutierrez = float(input(f"Introduce las horas trabajadas en el día {dia_gutierrez}: "))
    
# Calcular el total de horas trabajadas (sumando las horas introducidas)
    total_horas_trabajadas_gutierrez = (total_horas_trabajadas_gutierrez + horas_trabajadas_gutierrez) if 'total_horas_trabajadas' in locals() else horas_trabajadas_gutierrez

# Calcular el sueldo (considerando un valor fijo por hora, por ejemplo, $10)
sueldo_por_hora_gutierrez = 10
sueldo_total_gutierrez = total_horas_trabajadas_gutierrez * sueldo_por_hora_gutierrez

# Mostrar resultados
print(f"\nTotal de horas trabajadas durante la semana: {total_horas_trabajadas_gutierrez} horas")
print(f"Sueldo correspondiente: ${sueldo_total_gutierrez}")
