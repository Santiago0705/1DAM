# Santiago José Gutiérrez Guillén
# Ejercicio 12
# Enunciado: Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.

from Funciones11 import Calcular_Dia_Juliano, DiasDelMes
from Funciones12 import EsFechaValida
from Funciones12 import LeerFecha

# Resto del código (DiasDelMes, EsBisiesto, Calcular_Dia_Juliano, y programa principal) permanece igual

# Programa principal
fecha_gutierrez = LeerFecha()
dia_juliano_gutierrez = Calcular_Dia_Juliano(*fecha_gutierrez)
print(f"El día juliano correspondiente a la fecha {fecha_gutierrez[0]}/{fecha_gutierrez[1]}/{fecha_gutierrez[2]} es: {dia_juliano_gutierrez}")
