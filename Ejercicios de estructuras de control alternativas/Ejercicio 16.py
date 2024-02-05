print("Bienvenido al cobrador de llamadas telefónicas.")
print("Por favor, ingrese los datos de la llamada:")

dia = int(input("Ingrese el día del mes (1-31): "))
mes = int(input("Ingrese el mes del año (1-12): "))
anio = int(input("Ingrese el año: "))

hora = int(input("Ingrese la hora de inicio de la llamada (0-23): "))
minuto = int(input("Ingrese los minutos de inicio de la llamada (0-59): "))

duracion = int(input("Ingrese la duración de la llamada en minutos: "))

# Obtener el día de la semana
dia_semana = (dia + (13 * (mes + 12) + 5) % 7) + 1

# Cálculo del cobro por el tiempo de la llamada
cobro_tiempo = 0

if duracion <= 5:
    cobro_tiempo = duracion * 1
elif duracion <= 8:
    cobro_tiempo = 5 * 1 + (duracion - 5) * 0.8
elif duracion <= 10:
    cobro_tiempo = 5 * 1 + 3 * 0.8 + (duracion - 8) * 0.7
elif duracion <= 20:
    cobro_tiempo = 5 * 1 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5
else:
    cobro_tiempo = 5 * 1 + 3 * 0.8 + 2 * 0.7 + 8 * 0.5 + (duracion - 20) * 0.5

# Cálculo del impuesto por el día de la semana
impuesto = 0

if dia_semana == 1: