def calcular_hora_llegada(H, M, S, T):
    # Calcular la hora total de viaje
    hora_total = H + (M + (S + T) // 60) // 60
    
    # Calcular los minutos y segundos restantes
    minuto_restante = (M + (S + T) // 60) % 60
    segundo_restante = (S + T) % 60
    
    # Devolver la hora, minutos y segundos de llegada
    return hora_total, minuto_restante, segundo_restante

# Solicitar al usuario que ingrese los datos
H = int(input("Ingrese la hora de partida (0-23): "))
M = int(input("Ingrese los minutos de partida (0-59): "))
S = int(input("Ingrese los segundos de partida (0-59): "))
T = int(input("Ingrese el tiempo de viaje en segundos: "))

# Calcular y mostrar la hora de llegada
hora_llegada, minuto_llegada, segundo_llegada = calcular_hora_llegada(H, M, S, T)
print("El ciclista llegará a la ciudad B a las", hora_llegada, "horas,", minuto_llegada, "minutos y", segundo_llegada, "segundos.")