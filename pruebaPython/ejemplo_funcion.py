def get_frase_larga(f1,f2):
	"""Vamos a hacer una función que recibe dos frases y devuelve la frase con mayor longitud"""
	resultado = ""
	if len(f1) > len(f2):
		resultado = f1
	else:
		resultado = f2
	return resultado


def get_frase_larga_v2(f1:str,f2:str) -> str:
	"""Vamos a hacer una función que recibe dos frases y devuelve la frase con mayor longitud"""
	return f1 if len(f1) > len(f2) else f2

print(get_frase_larga("hola","adios"))



