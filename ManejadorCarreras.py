class manejadorcarrera:
    __carreras=[]
    __cantidad=0
    def __init__(self):
        self.__carreras=[]
        self.__cantidad=0
    def agregarCarrera(self,unaCarrera):
        self.__carreras.append(unaCarrera)
    def buscarCarrera(self,n):
        i=0
        while i < len(self.__carreras) and self.__carreras[i].getNombre() != n
            i+=1
        if i == len(self.__carreras):
            i=-1
        return i
