monedas  = {("dolar",1.42),("libra",0.87),("yen",113.86),("peseta",166.386) } 

def pedir_cantidad() :
    repetir = False
    while repetir :        
        euros = input("¿Cuántos euros quieres convertir a esa moneda?")
        if int(euros) >= 0  and euros.isdecimal() :
           repetir = True

    return euros
    
def convertir(euros:int,nombre_moneda:str) :
    for moneda_cambiada in monedas:
        resultado = euros *(moneda_cambiada[nombre_moneda])
        if nombre_moneda not in(monedas):
           ValueError (f"La moneda {nombre_moneda} no está admitida") 
