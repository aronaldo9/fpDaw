ingresos = [15000, 16000, 10000, 9000, 12000, 13000, 7000, 6000, 11000, 13000, 14000, 15000]
gastos = [8000, 9000, 11000, 10000, 12000, 10000, 9000, 8000, 9000, 9000, 12000, 14000]

for (i,j) in zip (ingresos,gastos):
    resta = i - j
    if resta > 0 : 
        print(f'El saldo del mes es positivo')
    elif resta == 0:
        print(f'El saldo del mes es 0')
    else:
        print(f'El saldo del mes es negativo')