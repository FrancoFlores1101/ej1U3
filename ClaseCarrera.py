

class Carrera:
    __codigo=None
    __nombre=None
    __fecha=None
    __duracion=None
    __titulo=None
    __nivel=None
    def __init__(self,cod,nom,fecha,duracion,titulo,nivel):
        self.__codigo=cod
        self.__nombre=nom
        self.__fecha=fecha
        self.__duracion=duracion
        self.__titulo=titulo
        self.__nivel=nivel
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
