# Pedir al usuario que ingrese los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias
x1, y1, x2, y2, r1, r2 = map(float, input("Ingrese los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias separados por espacios: ").split())

# Calcular las distancias entre los centros de las circunferencias
d = ((x2-x1)**2 + (y2-y1)**2)**0.5

# Clasificar las circunferencias según sus relaciones
if d >= r1 + r2:
    print("Los dos círculos son exteriores.")
elif d == r1 + r2:
    print("Los dos círculos son concéntricos.")
elif d < r1 and d < r2:
    print("Los dos círculos son interiores.")
elif d == r1 or d == r2:
    print("Los dos círculos son tangentes interiores o exteriores.")
else:
    print("Los dos círculos son secantes.")