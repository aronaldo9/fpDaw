from datetime import date

dia = input("Introduce el día de la semana: ")
mes = input("Introduce el mes: ")
año = input("Introduce el año: ")

class date:
    def __init__(self,dia:int,mes:str,año:int):
        self.dia = dia
        self.mes = mes
        self.año = año