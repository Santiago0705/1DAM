dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

# Validación de los días del mes
if mes == 2:
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        if dia > 29:
            print("La fecha ingresada es incorrecta")
            exit()
    elif dia > 28:
        print("La fecha ingresada es incorrecta")
        exit()

elif mes in [4, 6, 9, 11] and dia > 30:
    print("La fecha ingresada es incorrecta")
    exit()

# Validación de los meses
if mes < 1 or mes > 12:
    print("La fecha ingresada es incorrecta")
    exit()

# Validación del año
if anio < 1:
    print("La fecha ingresada es incorrecta")
    exit()

print("La fecha ingresada es correcta")