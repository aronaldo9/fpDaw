aprobados = int(26 * 66 / 100)
suspensos = int(26 * 19.5 / 100)
no_presentados = int(26 - (aprobados + suspensos))

print(f'Han aprobado {aprobados} alumnos')
print(f'Han suspendido {suspensos} alumnos')
print(f'No se han presentado {no_presentados} alumnos')