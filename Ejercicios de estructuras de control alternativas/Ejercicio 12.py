year = int(input("Ingrese un año: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("El año es bisiesto.")
        else:
            print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")