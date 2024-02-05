def invertir_numero(numero):
    # Convertir el número a string
    numero_str = str(numero)
    
    # Invertir el string
    numero_invertido_str = numero_str[::-1]
    
    # Convertir el string invertido a número
    numero_invertido = int(numero_invertido_str)
    
    return numero_invertido

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número de dos cifras: "))

# Verificar que el número tenga dos cifras
if numero < 10 or numero > 99:
    print("Por favor, ingrese un número de dos cifras.")
else:
    # Calcular e imprimir el número invertido
    numero_invertido = invertir_numero(numero)
    print("El número invertido es:", numero_invertido)