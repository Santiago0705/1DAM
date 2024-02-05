# Funciones Del Ejercicio 11: trata de calcular cual es el dia jualiano de una fecha concreta introducida por teclado.

def LeerFecha():
    fecha_gutierrez = input("Ingrese la fecha (día, mes, año) separada por espacios: ").split()
    return int(fecha_gutierrez[0]), int(fecha_gutierrez[1]), int(fecha_gutierrez[2])

def DiasDelMes(mes_gutierrez, anio_gutierrez):
    dias_gutierrez = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if EsBisiesto(anio_gutierrez) and mes_gutierrez == 2:
        return 29
    else:
        return dias_gutierrez[mes_gutierrez-1]

def EsBisiesto(anio_gutierrez):
    if anio_gutierrez % 400 == 0:
        return True
    elif anio_gutierrez % 100 == 0:
        return False
    elif anio_gutierrez % 4 == 0:
        return True
    else:
        return False

def Calcular_Dia_Juliano(dia_gutierrez, mes_gutierrez, anio_gutierrez):
    if mes_gutierrez < 3:
        mes_gutierrez += 9
        anio_gutierrez -= 1
    A = anio_gutierrez // 100
    B = 2 - A + (A // 4)
    C = ((153 * (mes_gutierrez + 1)) // 5) + 80 * anio_gutierrez + dia_gutierrez + B - 1
    return C
