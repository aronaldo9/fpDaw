nota1 = input ("Pon la nota de tu primer examen: ")
nota2 = input ("Nota de tu segundo examen: ")
nota3 = input ("Nota de tu tercer examen: ")

nota_media = (int(nota1) + int(nota2) + int(nota3)) / 3
# if nota_media >= 5:
#     print (f'Has aprobado con un {nota_media} de nota media')
# else:
#     print (f'Has suspendido con un {nota_media} de nota media')
aprobado = nota_media >= 5
print (f'{aprobado}')