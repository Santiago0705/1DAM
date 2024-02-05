# Santiago José Gutiérrez Guillén
# Ejercicio 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un 
# año, si al final de cada mes deposita cantidades variables de dinero; 
# además, se quiere saber cuánto lleva ahorrado cada mes.

# Inicializar variables
ahorro_anual_gutierrez = 0

# Bucle para cada mes del año
for mes_gutierrez in range(1, 13):
    # Pedir el monto a ahorrar en el mes actual
    ahorro_mes_gutierrez = float(input(f"Introduce la cantidad a ahorrar en el mes {mes_gutierrez}: "))
    
    # Sumar al ahorro anual
    ahorro_anual_gutierrez += ahorro_mes_gutierrez
    
    # Mostrar el ahorro acumulado hasta el mes actual
    print(f"Ahorro acumulado hasta el mes {mes_gutierrez}: {ahorro_anual_gutierrez}")

# Mostrar el ahorro total al final del año
print(f"\nAhorro total al final del año: {ahorro_anual_gutierrez}")
