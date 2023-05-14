horas = int(input("Introduce un número entero: "))
minutos = int(input("Introduce otro número entero: "))
segundos = int(input("Introduce otro número entero: "))
totalSegundos = segundos + (minutos * 60) + (horas * 60 *60)

print(f'El número total de segundos es: {totalSegundos} segundos')
