def convertir_fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Solicitar al usuario que ingrese un valor en grados Fahrenheit
fahrenheit = float(input("Por favor, ingrese un valor en grados Fahrenheit: "))

# Convertir el valor en grados Fahrenheit a grados Celsius
celsius = convertir_fahrenheit_a_celsius(fahrenheit)

# Imprimir el resultado en pantalla
print(f"El valor en grados Celsius es: {celsius}")