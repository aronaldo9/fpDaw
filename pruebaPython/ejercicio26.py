nota = input("Introduce tu nota del examen: ")

aprobado = int(nota) >= 5 
suspenso = not aprobado

print(f'¿Has aprobado? {aprobado}')
print(f'¿Has suspendido? {suspenso}')