# Santiago José Gutiérrez Guillén
# Ejercicio 14
# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# Las cantidades totales de cada articulo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del articulo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.

# Inicializar listas para almacenar los datos
precios_gutierrez = []
cantidades_sucursales_gutierrez = [[], [], [], []]

# Leer precios de los 5 artículos
for i_gutierrez in range(5):
    precio_gutierrez = float(input(f"Ingrese el precio del artículo {i_gutierrez + 1}: "))
    precios_gutierrez.append(precio_gutierrez)

# Leer cantidades vendidas en cada sucursal para cada artículo
for sucursal_gutierrez in range(4):
    print(f"Ingrese las cantidades vendidas en la sucursal {sucursal_gutierrez + 1}:")
    for articulo_gutierrez in range(5):
        cantidad_gutierrez = int(input(f"Cantidad del artículo {articulo_gutierrez + 1}: "))
        cantidades_sucursales_gutierrez[sucursal_gutierrez].append(cantidad_gutierrez)

# Calcular las cantidades totales de cada artículo
cantidades_totales_gutierrez = [sum(cantidades_gutierrez) for cantidades_gutierrez in zip(*cantidades_sucursales_gutierrez)]

# Informar las cantidades totales de cada artículo
print("\nCantidades totales de cada artículo:")
for i_gutierrez, cantidad_gutierrez in enumerate(cantidades_totales_gutierrez):
    print(f"Artículo {i_gutierrez + 1}: {cantidad_gutierrez}")

# Informar la cantidad de artículos en la sucursal 2
cantidad_sucursal_2_gutierrez = sum(cantidades_sucursales_gutierrez[1])
print(f"Cantidad de artículos en la sucursal 2: {cantidad_sucursal_2_gutierrez}")

# Informar la cantidad del artículo 3 en la sucursal 1
cantidad_articulo_3_sucursal_1_gutierrez = cantidades_sucursales_gutierrez[0][2]
print(f"Cantidad del artículo 3 en la sucursal 1: {cantidad_articulo_3_sucursal_1_gutierrez}")

# Calcular y mostrar la recaudación total de cada sucursal
recaudacion_sucursales_gutierrez = [sum(cantidades_gutierrez) * precios_gutierrez[i_gutierrez] for i_gutierrez, cantidades_gutierrez in enumerate(cantidades_sucursales_gutierrez)]
print("Recaudación total de cada sucursal:")
for i_gutierrez, recaudacion_gutierrez in enumerate(recaudacion_sucursales_gutierrez):
    print(f"Sucursal {i_gutierrez + 1}: {recaudacion_gutierrez}")

# Calcular y mostrar la recaudación total de la empresa
recaudacion_total_empresa_gutierrez = sum(recaudacion_sucursales_gutierrez)
print(f"Recaudación total de la empresa: {recaudacion_total_empresa_gutierrez}")

# Encontrar la sucursal con mayor recaudación
sucursal_mayor_recaudacion_gutierrez = recaudacion_sucursales_gutierrez.index(max(recaudacion_sucursales_gutierrez)) + 1
print(f"Sucursal con mayor recaudación: {sucursal_mayor_recaudacion_gutierrez}")
