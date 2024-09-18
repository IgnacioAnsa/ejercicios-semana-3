# 2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
# de las mismas figuras que el punto 1.
# 3- generar paquete.
# 4- subir a github.

from.modulo_areas import *

def calcular_perimetro_circulo(radio)-> float:
    perimetro = 2 * 3.14 * radio
    print(perimetro)
    return perimetro

def calcular_perimetro_cuadrado(longitud_lado)-> float:
    perimetro = 4 * longitud_lado
    print(perimetro)
    return perimetro

def calcular_perimetro_triangulo(lado1: float, lado2: float, lado3: float)-> float:
    perimetro = lado1 + lado2 + lado3
    print (perimetro)
    return perimetro

