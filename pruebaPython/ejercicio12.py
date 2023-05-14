precioNormal = float(input("Introduce un número con decimales: "))
porcentajeRebaja = float(input("Introduce otro número con decimales: "))
descuentoAplicado = precioNormal * porcentajeRebaja / 100
precioFinal = precioNormal - descuentoAplicado

print(f'Precio normal del artículo: {precioNormal} euros')
print(f'Porcentaje de rebaja aplicado: {porcentajeRebaja}%')
print(f'Descuento aplicado: {descuentoAplicado} euros')
print(f'Precio final del artículo: {precioFinal} euros')
