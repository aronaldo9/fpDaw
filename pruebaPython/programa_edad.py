"""Haz un programa que pregunte al usuario su edad y nos diga si es mayor de edad.
El programa se repite hasta que escribamos SALIR
"""

repetir = True
while repetir:
	texto_edad = input("Dime tu edad: ")
	# En Python el == hace lo mismo que el equals de Java
	# if texto_edad == "SALIR" or texto_edad == "salir":
	if texto_edad in ("salir","SALIR"):
		repetir = False
	else:
		# Detecto si texto_edad guarda un número
		if texto_edad.isdecimal():
			# paso a número el texto
			edad = int(texto_edad)
			# compruebo si es mayor de edad
			if edad >= 18:
				print("Eres mayor de edad")
			else:
				print("Eres menor de edad")
		else:
			print("No has introducido un número")

print("Programa finalizado")
