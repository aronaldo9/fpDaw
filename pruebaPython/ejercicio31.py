max_horas_marcas = 128 * 0.2
max_horas_redes = 192 * 0.2
max_horas_hardware = 96 * 0.2

print(f'En marcas se pueden faltar {max_horas_marcas} horas')
print(f'En redes se pueden faltar {max_horas_redes} horas')
print(f'En hardware se pueden faltar {max_horas_hardware} horas')

faltas = int (input("¿Cuántas faltas tienes en redes?: "))
if faltas > max_horas_redes:
    print("Has superado el límite de faltas en redes")
elif faltas <= max_horas_redes:
    print("No has superado el límite de faltas en redes")

