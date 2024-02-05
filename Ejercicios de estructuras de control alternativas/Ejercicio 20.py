ubicacion = input("Ingrese la ubicación del paquete (América del Norte, América Central, América del Sur, Europa, Asia): ")
peso = float(input("Ingrese el peso del paquete en kg: "))

# Zonas de envío
zonas = {
    "América del Norte": 1,
    "América Central": 2,
    "América del Sur": 3,
    "Europa": 4,
    "Asia": 5
}

# Costo por el servicio de transporte
costos_kg = {
    1: 24.00,
    2: 20.00,
    3: 21.00,
    4: 10.00,
    5: 18.00
}

# Revisar si la ubicación es válida
if ubicacion in zonas:
    zona = zonas[ubicacion]
    costo_kg = costos_kg[zona]
    
    # Revisar si el peso del paquete es válido
    if peso > 5:
        print("El paquete no puede ser transportado, su peso supera el límite permitido de 5 kg.")
    else:
        # Calcular el cobro por la entrega
        cobro = peso * costo_kg
        print(f"El cobro por la entrega del paquete es de {cobro} euros.")
else:
    print("La ubicación ingresada no es válida. Intente de nuevo.")