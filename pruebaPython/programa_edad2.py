""" Repetimos lo mismo con asgnación condicional"""
repetir = True
while repetir:
	texto_edad = input("Dime tu edad: ")
	if texto_edad in ("salir","SALIR"):
		repetir = False

	elif texto_edad.isdecimal():
		edad = int(texto_edad)

		# Asignación condicional
		resultado = "Eres mayor de edad" if edad>=18 else "Eres menor de edad"
		print(resultado)
