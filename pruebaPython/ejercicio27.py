edad = input("Introduce tu edad: ")

tiene_descuento = int(edad) > 60 or int(edad) < 18
print(f'¿La persona tiene descuento? {tiene_descuento}')