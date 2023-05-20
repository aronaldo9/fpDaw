edad1 = input("Introduce la edad 1: ")
edad2 = input("Introduce la edad 2: ")

mayor_edad = int(edad1) >= 18 and int(edad2) >= 18
mayor = int(edad1) > int(edad2)

print(f'¿Son mayores de edad? {mayor_edad}')
print(f'¿La primera persona es mayor que la segunda? {mayor}')