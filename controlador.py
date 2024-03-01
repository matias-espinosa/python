from tkinter import Tk
from vista import Ventana
from base_de_datos import Database

def main ():
    root = Tk()
    aplicacion = Ventana(root)
    root.mainloop()
    db = Database()
    db.conexion()
    db.create_table()
    db.close()

if __name__ == "__main__":
    main()