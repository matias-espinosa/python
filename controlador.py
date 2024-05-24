from tkinter import Tk
from vista import Ventana
from modelo import Treeview
from base_de_datos import Database
import observador

''''
def main ():
    """**Funcion principal que trata de crear la base de datos y lanza la ventana de Tkinter**"""
    root = Tk()
    aplicacion = Ventana(root)
    root.mainloop()
    db = Database()
    db.conexion()
    db.create_table()
    db.close()
    observadores.ConcreteObserverA(aplicacion.objeto_nadador)

if __name__ == "__main__":
    main()


def main ():
    """**Funcion principal que trata de crear la base de datos y lanza la ventana de Tkinter**"""
    root = Tk()
    aplicacion = Ventana(root)
    root.mainloop()
    db = Database()
    db.conexion()
    db.create_table()
    db.close()
    observadores.ConcreteObserverA(aplicacion.objeto_nadador)

if __name__ == "__main__":
    main()
'''
# from modelo import *

class Controller:
    """**Funcion principal que trata de crear la base de datos y lanzar la ventana de Tkinter**"""

    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = Ventana(self.root_controler)
        self.el_observador = observador.AltaRegistro(self.objeto_vista.objeto_nadador)
        self.el_observador = observador.ModificacionRegistro(self.objeto_vista.objeto_nadador)
        self.el_observador = observador.BajaRegistro(self.objeto_vista.objeto_nadador)
        db = Database()
        db.conexion()
        db.create_table()
        db.close()

if __name__ == "__main__":
    root = Tk()
    application = Controller(root)

    application.objeto_vista
    root.mainloop()
