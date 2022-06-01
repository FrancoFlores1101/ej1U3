import csv
from ClaseFacultad import facultad

class manejafacultad
    __listafacultades=[]
    def __init__(self):
        self.__listafacultades=[]
    def agregarfacultad(self,unaFacultad):
        self.__listafacultades.append(unaFacultad)

    def leercsv(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera =True
        filafac=next(reader)
        while bandera:
            unaFacultad=facultad(filafac[0],filafac[1],filafac[2],filafac[3],filafac[4])
            self.agregarfacultad(unaFacultad)
            try:
                filacarrera=next(reader)
            except StopIteration:
                bandera=False
            while bandera and filacarrera[0]==filafac[0]:
                unaFacultad.agregarcarrera(filacarrera[0],filacarrera[1],filacarrera[2],filacarrera[3],filacarrera[4],filacarrera[5])
                try:
                    filacarrera=next(reader)
                except StopIteration:
                    bandera=False
            filafac=filacarrera
        close(archivo)
    def buscarcod(self,codigo):
        i=0
        while i < len(self.__listafacultades) and self.__listafacultades[i].getCodigo() != codigo:
            i+=1
        if i == len(self.__listafacultades):
            i=-1
        return i
    def listarPorcodigo(self,codigo):
        indice=self.buscarcod(codigo)
        if indice != -1:
            self.__listafacultades[i].listarcarreras()
        else:
            print('no se encontró la carrera')
    def listarfacultades(self,nombre):
        for i in range(len(self.__listafacultades)):
            cadena += self.__listafacultades[i].buscarCarrera(nombre)
        if cadena == None:
            print('carrera no encontrada')
        else:
            print cadena
