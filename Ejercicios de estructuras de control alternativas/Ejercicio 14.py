while True:
    tipo = input("Ingrese el tipo de uva (A o B): ").upper()
    tamano = int(input("Ingrese el tamaño de la uva (1 o 2): "))
    peso = float(input("Ingrese el peso del embarque en kilogramos: "))

    precio_inicial = float(input("Ingrese el precio inicial al kilo de uva: "))

    if tipo == 'A':
        if tamano == 1:
            ganancia = peso * (precio_inicial + 0.20)
        elif tamano == 2:
            ganancia = peso * (precio_inicial + 0.30)
        else:
            print("Error: tamaño de uva inválido.")
            continue
    elif tipo == 'B':
        if tamano == 1:
            ganancia = peso * (precio_inicial - 0.30)
        elif tamano == 2:
            ganancia = peso * (precio_inicial - 0.50)
        else:
            print("Error: tamaño de uva inválido.")
            continue
    else:
        print("Error: tipo de uva inválido.")
        continue

    print(f"La ganancia obtenida por el productor es de {ganancia:.2f} euros.")

    play_again = input("¿Desea calcular otra ganancia? (S/N): ").lower()
    if play_again != 's':
        break