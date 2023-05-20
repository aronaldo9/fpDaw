# Del "paquete" itertools importamos la función "product"
#	(módulo)
from itertools import product

lista = ["Carlos", "Arturo", "Belén", 'Javier', 'Ambrosio']

# Muestra los nombres en pantalla

for nombre in lista:
    print(nombre)

# mostrar los nombres sin bucles
print(*lista,sep='\n')

# mostrar el nombre junto con la posición en la lista
for posicion,nombre in enumerate(lista):
    print(posicion,nombre)

# En Python los objetos que se pueden recorrer con un for mejorado se llaman ITERABLES
# las listas son iterables
# un string es un iterable con sus letras
frase = "Hoy es lunes y la semana que viene hay fiesta"
for letra in frase:
    print(letra)


# vamos a generar los números entre 10 y 500
for i in range(10,501):
    print(i)

# vamos a mostrar los números pares entre 10 y 50
for i in range(10,51,2):
    print(i)

# vamos a recorrer dos listas a la vez
lista1 = ["granada", "madrid", "jaen"]
lista2 = [958,91,953]
for ciudad,prefijo in zip(lista1,lista2):
    print (ciudad,prefijo)

# vamos a recorrer el producto cartesiano de las dos listas
for ciudad,prefijo in product(lista1,lista2):
    print(ciudad,prefijo)

# vamos a hacer un diccionario y vamos a recorrerlo
alumnos = {
	"antonio":9,
	"jaime":5,
	"maria":8,
	"luis":4
}

# vamos a mostrar por pantalla los nombres de los alumnos y si están aprobados o suspensos
for nombre in alumnos:
	nota = alumnos[nombre]
	if nota>=5:
		print(nombre,"aprobado")
	else:
		print(nombre,"suspenso")

# repetimos lo mismo pero recorriendo (nombre,nota) a la vez
for nombre,nota in alumnos.items():
    if nota>=5:
        print(f"El alumno {nombre} ha aprobado")
    else:
        print(f"El alumno {nombre} está suspenso")

try:
	#mostramos en pantalla las líneas de un archivo
	with(open("hola chavales.txt222222222","r")) as archivo:
		# el archivo es iterable con sus líneas de texto
		for linea in archivo:
			print(linea)
except IOError as e:
	print("Se ha producido un error: {e}")
