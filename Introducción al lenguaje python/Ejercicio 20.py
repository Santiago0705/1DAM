def calcular_dinero(cantidad_monedas_2_euros, cantidad_monedas_1_euro, cantidad_monedas_50_centimos, cantidad_monedas_20_centimos, cantidad_monedas_10_centimos):
    dinero_en_euros = (cantidad_monedas_2_euros * 2) + (cantidad_monedas_1_euro * 1)
    dinero_en_centimos = (cantidad_monedas_50_centimos * 50) + (cantidad_monedas_20_centimos * 20) + (cantidad_monedas_10_centimos * 10)

    # Sumamos el dinero en euros y en centimos para obtener el total
    dinero_total = dinero_en_euros + (dinero_en_centimos / 100)

    return dinero_total

# Solicitar al usuario que ingrese la cantidad de monedas de cada tipo
cantidad_monedas_2_euros = int(input("Ingrese la cantidad de monedas de 2€: "))
cantidad_monedas_1_euro = int(input("Ingrese la cantidad de monedas de 1€: "))
cantidad_monedas_50_centimos = int(input("Ingrese la cantidad de monedas de 50 céntimos: "))
cantidad_monedas_20_centimos = int(input("Ingrese la cantidad de monedas de 20 céntimos: "))
cantidad_monedas_10_centimos = int(input("Ingrese la cantidad de monedas de 10 céntimos: "))

# Calcular e imprimir el dinero total después de contar las monedas
dinero_total = calcular_dinero(cantidad_monedas_2_euros, cantidad_monedas_1