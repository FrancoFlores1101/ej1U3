from ClaseCarrera import Carrera
from ManejadorCarreras import manejadorcarrera

class facultad:
    __codigo=None
    __nombre=None
    __direccion=None
    __localidad=None
    __telefono=None
    __carreras=None
    def __init__(self,cod,nom,direc,local,tel):
        self.__codigo=cod
        self.__nombre=nom
        self.__direccion=direc
        self.__localidad=local
        self.__telefono=tel
        self.__carreras=manejadorcarrera
    def agregarcarrera(self,a,b,c,e,d):
        instancia=Carrera(a,b,c,e,d)
        self.__carreras.agregarCarrera(instancia)
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def listar(self):
        for Carrera in self.__lista:
            print(carrera.getNombre(),carrera.getDuracion())
    def buscarCarrera(self,nombre):
        cadena=None
        indice=self.__carreras.buscarCarrera(nombre)
        if indice != -1
            cadena=self.__nombre
        return  cadena
