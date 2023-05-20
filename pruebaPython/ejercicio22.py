pregs_bien = 22
pregs_mal = 6

pregunta_bien = 10 * 1 /30
# si tiene 6 preguntas mal y cada 3 preguntas mal, se resta una pregunta bien...
pregs_bien_totales = 22 - 2
nota = pregs_bien_totales * pregunta_bien
print(f'El alumno ha sacado un {nota}')