#5. Programa que contenga una función la cual retorne el factorial de un número capturado por teclado.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = int(input("Ingrese un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")