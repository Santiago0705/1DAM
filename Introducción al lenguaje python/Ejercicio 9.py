# Solicitar al usuario que ingrese el monto total de la compra
total_compra = float(input("Por favor, ingrese el monto total de la compra: "))

# Calcular el descuento del 15% sobre el total de la compra
descuento = total_compra * 0.15

# Calcular el monto final a pagar por el cliente
monto_final = total_compra - descuento

# Mostrar el monto final a pagar por el cliente
print(f"El cliente deberá pagar finalmente por su compra un monto de: {monto_final}")