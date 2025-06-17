def menor_de_tres(a, b, c):
    return min(a, b, c)

# Ejemplo de uso
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = menor_de_tres(num1, num2, num3)
print(f"El menor de los tres números es: {resultado}")