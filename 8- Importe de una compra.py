def calcular_pago_final(importe):
    if importe > 1000:
        return importe * 0.88  # 12% de descuento
    elif importe > 500:
        return importe * 0.90  # 10% de descuento
    elif importe > 300:
        return importe * 0.95  # 5% de descuento
    else:
        return importe

# Ejemplo de uso
compra = float(input("Ingrese el importe de la compra: "))
total_pagar = calcular_pago_final(compra)
print(f"Importe a pagar: ${total_pagar:.2f}")