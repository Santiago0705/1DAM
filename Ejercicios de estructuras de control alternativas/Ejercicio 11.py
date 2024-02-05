# Pedir al usuario que ingrese los puntos centrales
A, B, C = map(float, input("Ingrese las dimensiones de los lados del triángulo separados por espacios: ").split())

# Verificar que los datos ingresados correspondan a un triángulo
if A + B <= C or A + C <= B or B + C <= A:
    print("Los datos ingresados no corresponden a un triángulo.")
else:
    # Verificar el tipo de triángulo
    if A**2 + B**2 == C**2:
        print("El triángulo es rectángulo.")
    elif A == B or A == C or B == C:
        print("El triángulo es isósceles.")
    elif A != B and A != C and B != C:
        print("El triángulo es escaleno.")
    else:
        print("El triángulo es equilátero.")