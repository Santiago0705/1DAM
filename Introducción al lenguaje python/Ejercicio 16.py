def calcular_tiempo_reunio(d, v1, v2):
    if v1 < v2:
        v1, v2 = v2, v1
    tiempo = d / (v1 - v2)
    return tiempo * 60

# Solicitar al usuario que ingrese los datos
d = float(input("Ingrese la distancia entre los dos vehículos (km): "))
v1 = float(input("Ingrese la velocidad del primer vehículo (km/h): "))
v2 = float(input("Ingrese la velocidad del segundo vehículo (km/h): "))

# Calcular y mostrar el tiempo de reunión
tiempo_reunio = calcular_tiempo_reunio(d, v1, v2)
print("Los vehículos se reunirán en aproximadamente", tiempo_reunio, "minutos.")