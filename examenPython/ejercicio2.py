ingresos = [15000, 16000, 10000, 9000, 12000, 13000, 7000, 6000, 11000, 13000, 14000, 15000]
gastos = [8000, 9000, 10000, 9000, 12000, 10000, 9000, 8000, 9000, 9000, 12000, 14000]


for (i,j) in zip (ingresos,gastos):
    resta = i - j
    if resta > 0:
        print('El saldo del mes es positivo')
    elif resta == 0:
        print('El saldo del mes es 0')
    else:
        print('El saldo del mes es negativo')


# calculamos la media de ingresos
media_ingresos = sum(ingresos) / len(ingresos)
print(f'La media de ingresos anual es {media_ingresos}€')

# Calculamos la media de gastos
media_gastos = sum(gastos) / len(gastos)
print(f'La media de gastos anual es {media_gastos}€')

# Calculamos el balance final
balance_final = sum(ingresos) - sum(gastos)
if balance_final > 0:
    print("El balance ha sido positivo")
else:
    print("El balance final ha sido 0 o negativo")