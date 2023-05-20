from dni import Dni
from dni import Persona

# Creo un objeto d ela clase Dni
# no hace falta poner new
d = Dni(11111111)

print(d.numero)
print(d.letra)
print(d.get_ultimo_digito())
print(d.ultimo_digito_par())

if d:
    print("El número de dni no es 0")
else:
    print("El número de dni es 0")

cuenta = 5 + int(d)
print(cuenta)

print(d)

a = Persona("Antonio",15)
b = Persona("Luis",20)

print(Persona.comparar_personas(a,b))