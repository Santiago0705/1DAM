# Solicita el número del dado al usuario
numero_dado = int(input("Introduzca número del dado: "))

# Verifica si el número está en el rango válido (1 a 6)
if 1 <= numero_dado <= 6:
    # Usa un diccionario para mapear los números a las cadenas
    mapping = {1: "seis", 2: "cinco", 3: "cuatro", 4: "tres", 5: "dos", 6: "uno"}

    # Obtiene la cadena correspondiente al número ingresado
    resultado = mapping[numero_dado]

    # Muestra el resultado
    print(f"En la cara opuesta está el \"{resultado}\".")
else:
    print("ERROR: número incorrecto.")
