adulto = input("¿Eres adulto? true/false: ")
acompanhado = input("¿Eres menor y vas acompañado? true/false: ")

puedes_salir = bool(adulto) or bool(acompanhado)
print(f'¿Puedes salir? {puedes_salir}')