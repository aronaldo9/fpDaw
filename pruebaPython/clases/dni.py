
class Dni:
    """Esta clase es un dni"""

    def __init__(self, n: int):
        """Este método es el constructor. Recibe:
        self --> es el objeto que queremos crear
        n --> es el número del dni que vamos a ponerle
        """
        # Esto añade la propiedad numero al objeto self
        self.numero = n

        # Añadimos al objeto self la propiedad letra
        # Observa que "self." es obligatorio en Python
        self.letra = self.calcular_letra(self.numero)

    def calcular_letra(self,num:int) -> str:
        """Este método calcula la letra correspondiente al número"""
        lista = ['T','R','W','A','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

        return lista[num % len(lista)]
    
    
    def get_ultimo_digito(self) -> str:
        """Devuelve el último dígito del dni"""
        return str(self.numero)[-1]
    

    def ultimo_digito_par(self) -> bool:
        """Devuelve true si el último dígito del dni es par"""
        return self.numero %2 == 0
        # return int(self.get_ultimo_digito()) %2 == 0
        # return self.get_ultimo_digito() in ("0", "2", "4", "6","8")


    def __bool__(self):
        """Este método convierte el objeto en un boolean
        Se supone que un dni se convierte en falso cuando su número es 0
        """
        return self.numero != 0
    
    def __int__(self):
        """Este método convierte el dni en un número entero.
        Se supone que un dni se convierte en entero mediante
        su propio número
        """
        return self.numero
    

    def __str__(self):
        """Este método convierte el dni en un string"""
        return f"{self.numero} - {self.letra}"
    


def crearDni(s:str) -> Dni:
    """Crea un dni a partir de un string"""
    return Dni(int(s))



class Nadador:
    """Esta clase va a simular la interfaz Nadador"""

    def nadar(self):
        """Este método hace que el nadador nade"""
        pass


class Persona(Nadador):
    """Es una clase persona"""
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def nadar(self):
        print("La persona está nadando")

    @staticmethod
    def comparar_personas(p1, p2):
        """Este método devuelve la persona con mayor edad"""
        return p1 if p1.edad>p2.edad else p2
    



class Caja:
    def __init__(self):
        self.__mensaje = None
        self.__abierto = False

    def abrir_caja(self):
        self.__abierto = True

    def get_mensaje(self) -> str:
        if self.__abierto:
            return self.__mensaje
        else:
            raise IOError("La caja está cerrada")
    
    def cambiar_mensaje(self,m:str):
        if self.__abierto:
            self.__mensaje = m
        else:
            raise IOError("La caja está cerrada")
        
    def __bool__(self):
        return self.__abierto
    