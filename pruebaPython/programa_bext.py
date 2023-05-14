# 1) Descarga usando pip install una librería que se llama bext
# 2) Busca en internet la web oficial de la librería bext
# 3) Haz un programa que haga esto: Escribe hola en el centro de la pantalla en color rojo

import bext

ancho, alto = bext.size()
bext.fg("red")
bext.bg("white")
bext.goto(int(ancho/2), int(alto/2))
print("Hola")

