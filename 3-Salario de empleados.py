#3. Un programa que permita ingresar los salarios de una cantidad indicada de empleados
def calcular_descuento(salario):
    return salario * 0.10

# Ejemplo de uso
n_empleados = int(input("Ingrese el número de empleados: "))
total_pagos = 0
total_descuentos = 0

for i in range(n_empleados):
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
    descuento = calcular_descuento(salario)
    total_empleado = salario - descuento
    
    print(f"Empleado {i+1}:")
    print(f"Salario bruto: ${salario:.2f}")
    print(f"Descuento (10%): ${descuento:.2f}")
    print(f"Total a pagar: ${total_empleado:.2f}")
    print()
    
    total_pagos += total_empleado
    total_descuentos += descuento

print(f"Total pagado a todos los empleados: ${total_pagos:.2f}")
print(f"Total de descuentos aplicados: ${total_descuentos:.2f}")