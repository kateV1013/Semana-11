#6.Escribir el programa que tenga una función, esta devuelva el área de un círculo cuyo radio se le suministra como argumento.
import math

def area_circulo(radio):
    return math.pi * radio ** 2

# Ejemplo de uso
radio = float(input("Ingrese el radio del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")
