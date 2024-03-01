from tkinter import Tk
import vista

def main ():
    root = Tk()
    aplicacion = vista.Ventana(root)
    botones = vista.Buttons(root, aplicacion.dni_value, aplicacion.nombre_value, aplicacion.tiempo_value, aplicacion.entry_dni, aplicacion.tree)
    root.mainloop()

if __name__ == "__main__":
    main()