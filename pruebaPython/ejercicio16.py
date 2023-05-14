padrino = 3.5
padrino2Dias = padrino*2
odisea = 2.95
odisea2Dias = odisea*2
alquilerTotal = padrino2Dias + odisea2Dias
billete = 5

print(f'Para alquilar "El Padrino" dos días se necesitan {padrino2Dias}€')
print(f'Para alquilar "Odisea 2001" dos días se necesitan {odisea2Dias}€')
print(f'Para alquilar las dos películas dos días se necesitan {alquilerTotal}€')

if billete>=alquilerTotal:
	print(f'Puedes alquilar las dos películas 2 días')
elif billete<alquilerTotal:
	print(f'No puedes alquilar las dos películas dos días porque sólo tienes {billete}€')
