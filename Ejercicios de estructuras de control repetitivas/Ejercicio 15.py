# Santiago José Gutiérrez Guillén
# Ejercicio 15
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 
# 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
# para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

# Inicializar variables
pago_mensual_gutierrez = 10  # Pago inicial del primer mes
total_pagado_gutierrez = 0

# Bucle para los 20 meses
for mes_gutierrez in range(1, 21):
    total_pagado_gutierrez += pago_mensual_gutierrez
    print(f"Mes {mes_gutierrez}: Pago mensual = {pago_mensual_gutierrez} €, Total pagado = {total_pagado_gutierrez} €")
    
    # Duplicar el pago mensual para el próximo mes
    pago_mensual_gutierrez *= 2

# Mostrar el total pagado después de los 20 meses
print(f"\nTotal pagado después de 20 meses: {total_pagado_gutierrez} €")
