# Santiago José Gutiérrez Guillén
# Ejercicio 11
# Enunciado: El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa 
# principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
# LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
# DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
# EsBisiesto: Recibe un año y nos dice si es bisiesto.
# Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

from Funciones11 import LeerFecha
from Funciones11 import DiasDelMes
from Funciones11 import EsBisiesto
from Funciones11 import Calcular_Dia_Juliano

dia_gutierrez, mes_gutierrez, anio_gutierrez = LeerFecha()
dia_juliano_gutierrez = Calcular_Dia_Juliano(dia_gutierrez, mes_gutierrez, anio_gutierrez)
print(f"El día juliano correspondiente a la fecha {dia_gutierrez}/{mes_gutierrez}/{anio_gutierrez} es: {dia_juliano_gutierrez}")