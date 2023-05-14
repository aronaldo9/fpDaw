"""Este archivo es una librería donde vamos a añadir funciones 
para usarlas en otros programas"""

from random import randint
from typing import List



"""Haz una función que reciba un número y devuelva true si es par y false si es impar"""

def es_Par(n:int) -> bool:
	resultado = False
	if n%2 == 0 :
		resultado = True
	return resultado


def es_Par_v2(n:int) -> bool:
	resultado = False
	if not n%2:     # el n%2 se convierte en False si n es par
		resultado = True
	return resultado


def es_Par_v3(n:int) -> bool:
	return True if n%2 == 0 else False


def es_Par_v4(n:int) -> bool:
	return False if n%2 else True


def es_Par_v5(n:int) -> bool:
	return not n%2





"""Haz una función que reciba un texto y nos diga si es un día de la semana"""
def es_Dia_Semana(texto:str) -> bool:
	dias = {"lunes","martes","miercoles","jueves","viernes","sabado","domingo"}
	return texto in dias

def es_Dia_Semana_v2(texto:str) -> bool:
	return texto in {"lunes","martes","miercoles","jueves","viernes","sabado","domingo"}





"""Haz una función que reciba un número y nos devuelva una lista rellenada con tantos números aleatorios entre 0 y 10
como indica el número que hemos recibido"""
def get_lista_aleatorios(cantidad:int) -> List[int]:
	lista = []
	for i in range(0,cantidad):
		aleatorio = randint(0,11)
		lista.append(aleatorio)		#lista += aleatorio
	return lista


def get_lista_aleatorios_v2(cantidad:int) -> List[int]:
	return [ randint(0,11) for i in range(0,cantidad) ]	#lista por comprensión




"""Haz una función que pida un número entre 0 y 10 al usuario por teclado. Si el número es incorrecto
lo vuelve a preguntar. La función termina devolviendo el número introducido por el usuario"""
def pedir_numero() -> int:
	resultado = 0
	repetir = True
	while repetir:		
		texto = input("Escribe un número entre 0 y 10: ")
		if texto.isdecimal():
			numero = int(texto)
			if 0 <= numero <= 10:
				resultado = numero
				repetir = False
	return resultado

"""n = pedir_numero()
print(n)"""



""" Realiza una función que reciba un diccionario y muestre por pantallas las claves que hay en ese diccionario"""
def mostrar_claves(diccionario):
	for clave in diccionario:
		println(clave) 





