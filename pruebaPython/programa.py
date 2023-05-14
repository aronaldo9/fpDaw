"""Vamos a hacer un programa que pregunta
 tu nombre y te saluda en un renglón diferente
"""
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

#print("Te llamas",nombre,"y tu edad es",edad)

#print("Te llamas {} y tu edad es {}".format(nombre,edad))

# cuidado: esto solo sirve si pegamos String
#print("Te llamas "+nombre+" y tu edad es "+edad)

print(f"Te llamas {nombre} y tu edad es {edad}")
