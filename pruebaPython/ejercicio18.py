precio_hora = 7
horas_semana_alumno1 = 2
horas_semana_alumno2 = 3

ganancia_alumno1 = 4*(precio_hora*horas_semana_alumno1)
ganancia_alumno2 = 4*(precio_hora*horas_semana_alumno2)
ganancia_total = ganancia_alumno1+ganancia_alumno2
print( f'El estudiante ganará al mes {ganancia_total}€' )

horas = 900/precio_hora
print( f'Si quiere ganar 900€ tendrá que impartir {horas} horas de clase')