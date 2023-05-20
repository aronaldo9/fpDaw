notas = [6.5, 4.2, 5.75, 3.5, 8]
faltas = 10

media = sum(notas) / len(notas)

if faltas > 20:
    print("El alumno está suspenso")
elif faltas >= 10 and media > 5:
    print("El alumno ha aprobado")
elif 15 <= faltas <= 20 and media > 7:
    print("El alumno está aprobado")
else:
    print("El alumno está suspenso")
print (media)
