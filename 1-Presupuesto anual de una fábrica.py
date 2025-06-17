def calcular_presupuestos(monto):
    recursos_humanos = monto * 0.50
    manufactura = monto * 0.25
    empaquetado = monto * 0.15
    publicidad = monto * 0.10
    
    print(f"Recursos Humanos: ${recursos_humanos:.2f}")
    print(f"Manufactura: ${manufactura:.2f}")
    print(f"Empaquetado: ${empaquetado:.2f}")
    print(f"Publicidad: ${publicidad:.2f}")

# Ejemplo de uso
presupuesto_anual = float(input("Ingrese el monto del presupuesto anual: "))
calcular_presupuestos(presupuesto_anual)