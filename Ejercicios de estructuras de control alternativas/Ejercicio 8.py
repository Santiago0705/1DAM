# Entrada de datos
nota = float(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (F/M): ").upper()

# Lógica del programa
if nota >= 5 and edad >= 18 and sexo == 'F':
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == 'M':
    print("POSIBLE")
else:
    print("NO ACEPTADA")