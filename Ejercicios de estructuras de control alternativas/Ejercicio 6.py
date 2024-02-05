# Entrada de datos
input_str = input("Ingrese una cadena: ")

# Lógica del programa
if len(input_str) == 1 and input_str.isupper():
    print("La cadena ingresada es una letra mayúscula.")
else:
    print("La cadena ingresada no es una letra mayúscula o tiene más de un carácter.")
