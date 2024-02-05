# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y 
# la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras 
# cada consulta el programa nos preguntará si queremos hacer otra consulta.

# Declarar el diccionario de precios de frutas
precios_frutas_gutierrez = {
    'manzana': 2.5,
    'banana': 1.8,
    'naranja': 3.0,
    'pera': 2.0,
    'kiwi': 2.7
}

while True:
    # Pedir el nombre de la fruta y la cantidad vendida
    fruta_gutierrez = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ").lower()
    
    # Salir del programa si se ingresa 'salir'
    if fruta_gutierrez == 'salir':
        print("¡Hasta luego!")
        break
    
    cantidad_gutierrez = int(input("Ingrese la cantidad vendida: "))
    
    # Verificar si la fruta está en el diccionario de precios
    if fruta_gutierrez in precios_frutas_gutierrez:
        precio_total_gutierrez = precios_frutas_gutierrez[fruta_gutierrez] * cantidad_gutierrez
        print(f"El precio total de {cantidad_gutierrez} {fruta_gutierrez}(s) es: ${precio_total_gutierrez}")
    else:
        print("Lo siento, la fruta ingresada no esta en el inventario.")
    
    continuar_gutierrez = input("¿Desea hacer otra consulta? (si/no): ")
    if continuar_gutierrez.lower() != 'si':
        print("¡Hasta luego!")
        break
