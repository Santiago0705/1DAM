import math

# Solicitar al usuario los valores de los catetos
a = float(input("Por favor, ingrese el valor del cateto a: "))
b = float(input("Por favor, ingrese el valor del cateto b: "))

# Calcular la hipotenusa del triángulo rectángulo
hipotenusa = math.sqrt(a**2 + b**2)

# Imprimir el resultado
print("La hipotenusa del triángulo rectángulo es: ", hipotenusa)