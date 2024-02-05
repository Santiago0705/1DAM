# Importamos la función sqrt de la biblioteca math
from math import sqrt

# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calculamos la distancia entre los dos puntos
distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostramos la distancia en la pantalla
print("La distancia entre los dos puntos es:", distancia)