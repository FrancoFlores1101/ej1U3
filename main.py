from ManejadorFacultades import  manejafacultad
from menu import Menu

if __name__ == '__main__':
    unmanejador=manejafacultad()
    unmanejador.leercsv()
    unmenu=Menu()
    unmenu.ejecutarMenu(unmanejador)
