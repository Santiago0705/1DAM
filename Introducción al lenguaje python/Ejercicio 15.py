def main():
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
    
    print("Antes del intercambio: A =", A, ", B =", B)
    
    # Intercambiar los valores de A y B
    A, B = B, A
    
    print("Después del intercambio: A =", A, ", B =", B)

main()