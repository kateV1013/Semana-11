#4. Un programa para capturar por teclado el número de horas trabajadas y el valor a pagar
def calcular_pago(horas):
    if horas <= 160:
        return horas * 6.5
    else:
        return (160 * 6.5) + ((horas - 160) * 7.5)

# Ejemplo de uso
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
pago = calcular_pago(horas_trabajadas)
print(f"El pago correspondiente es: ${pago:.2f}")