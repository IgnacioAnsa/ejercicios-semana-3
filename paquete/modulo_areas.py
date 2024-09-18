# Repaso funciones
# 1- Elabore un módulo que contenga 3 funciones:
# a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
# que en caso de no recibir un radio el valor del mismo será 3.
# b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
# parámetro, sin parámetros opcionales.
# c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro

def calcular_area_circulo(radio = 3)-> float:
    area = 3.14 * radio ** 2
    print(area)
    return area

def calcular_area_cuadrado(longitud_lado: float)-> float:
    area = longitud_lado ** 2
    print(area)
    return area

def calcular_area_triangulo(base: float, altura: float)-> float:
    area = (base * altura) / 2
    print (area)
    return area






