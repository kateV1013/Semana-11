#2. Calcular cuanto dinero tendra cada vendedor, por comision por las tres ventas realizadas, y tomando en cuenta su sueldo base y sus comisiones.
def calcular_comisiones(ventas):
    return ventas * 0.10

# Ejemplo de uso
n_vendedores = int(input("Ingrese el número de vendedores: "))
sueldo_base = float(input("Ingrese el sueldo base: "))

for i in range(n_vendedores):
    ventas = float(input(f"Ingrese el monto total de las 3 ventas del vendedor {i+1}: "))
    comision = calcular_comisiones(ventas)
    total = sueldo_base + comision
    
    print(f"Vendedor {i+1}:")
    print(f"Comisiones: ${comision:.2f}")
    print(f"Total a pagar: ${total:.2f}")
print()