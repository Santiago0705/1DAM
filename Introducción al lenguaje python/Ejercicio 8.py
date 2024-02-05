# Función para calcular la comisión por venta
def calcular_comision(venta):
    return venta * 0.10

# Función para calcular el total a recibir por el vendedor en el mes
def calcular_total_a_recibir(sueldo_base, comisiones):
    return sueldo_base + comisiones

# Entrada de datos
sueldo_base = float(input("Por favor, ingrese el sueldo base del vendedor: "))
venta1 = float(input("Por favor, ingrese el monto de la primera venta: "))
venta2 = float(input("Por favor, ingrese el monto de la segunda venta: "))
venta3 = float(input("Por favor, ingrese el monto de la tercera venta: "))

# Cálculo de comisiones por venta
comision1 = calcular_comision(venta1)
comision2 = calcular_comision(venta2)
comision3 = calcular_comision(venta3)

# Cálculo del total a recibir por el vendedor en el mes
total_a_recibir = calcular_total_a_recibir(sueldo_base, comision1 + comision2 + comision3)

# Salida de resultados
print(f"El vendedor obtendrá {comision1 + comision2 + comision3} en concepto de comisiones por las tres ventas que realiza en el mes.")
print(f"El total que recibirá el vendedor en el mes tomando en cuenta su sueldo base y comisiones es de {total_a_recibir}.")