def minutos_a_horas(minutos):
    horas = minutos // 60
    minutos %= 60
    return horas, minutos

# Pedir al usuario que ingrese una cantidad de minutos
minutos = int(input("Por favor, ingrese una cantidad de minutos: "))

# Calcular a cuantas horas y minutos corresponde
horas, minutos_restantes = minutos_a_horas(minutos)

# Imprimir el resultado en pantalla
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")