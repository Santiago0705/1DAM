# Entrada de datos
base = float(input("Ingrese la base: "))
exponente = float(input("Ingrese el exponente: "))

# Lógica del programa
if exponente == 0:
    print("La potencia es 1.")
elif exponente > 0:
    potencia = 1
    for i in range(int(exponente)):
        potencia *= base
    print("La potencia es ", potencia)
else:
    potencia = 1
    for i in range(int(-exponente)):
        potencia *= base
    print("La potencia es 1/", potencia)