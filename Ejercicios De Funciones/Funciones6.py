# Funciones Del Ejercicio 6: trata de calcular a través del radio de un circunsferencia su área y perímetro.

import math

def calcular_circunferencia(radio_gutierrez):
    diametro_gutierrez = radio_gutierrez * 2
    circunferencia_gutierrez = diametro_gutierrez * math.pi
    area_gutierrez = math.pi * (radio_gutierrez ** 2)

    return {
        'circunferencia': circunferencia_gutierrez,
        'area': area_gutierrez
    }