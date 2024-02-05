# Función para calcular el perímetro
def calcular_perimetro(base, altura):
    return 2 * (base + altura)

# Función para calcular el área
def calcular_area(base, altura):
    return base * altura

# Solicitar al usuario los valores de la base y la altura
base = float(input("Por favor, ingrese la base del rectángulo: "))
altura = float(input("Por favor, ingrese la altura del rectángulo: "))

# Calcular el perímetro y el área del rectángulo
perimetro = calcular_perimetro(base, altura)
area = calcular_area(base, altura)

# Imprimir los resultados
print("El perímetro del rectángulo es: ", perimetro)
print("El área del rectángulo es: ", area)