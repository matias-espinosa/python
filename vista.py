from tkinter import *
from tkinter import ttk
from modelo import cerrar_programa
from modelo import actualizar_treeview
from modelo import seleccion_en_tree
from modelo import scroll_vertical
from modelo import InteraccionBd


# ##############################################
# VISTA
# ##############################################

class Ventana:
    def __init__(self, window) -> None:
        self.root=window

        root.title("Swim Tracker")
        root.configure(bg="#c5e1ff")

        fuente_titulo = ("Arial", 16, "bold")
        fuente_campos = ("Calibri", 11)

        self.titulo = Label(self.root,padx=10, anchor="w", font=fuente_titulo, text="Swim Tracker", bg="#001c3b", fg="white", height=2, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)

        self.dni = Label(self.root, font=fuente_campos, bg="#c5e1ff",text="DNI (números, sin puntos)")
        self.dni.grid(row=2, column=0, padx=10, sticky=W)
        self.nombre_apellido=Label(self.root, font=fuente_campos, bg="#c5e1ff", text="Nombre y Apellido")
        self.nombre_apellido.grid(row=3, padx=10, column=0, sticky=W)
        self.tiempo_50=Label(self.root, font=fuente_campos,  bg="#c5e1ff", text="50 mts Crol (MM:SS)")
        self.tiempo_50.grid(row=4, padx=10, column=0, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.dni_value, self.nombre_value, self.tiempo_value = IntVar(), StringVar(), StringVar()

        w_ancho = 31

        self.entry_dni = Entry(root, textvariable = self.dni_value, width = w_ancho)
        self.entry_dni.grid(row = 2, padx=10, column = 2, sticky=E, columnspan=2)
        self.entry_nombre = Entry(root, textvariable = self.nombre_value, width = w_ancho)
        self.entry_nombre.grid(row = 3, padx=10, column = 2, sticky=E, columnspan=2)
        self.entry_tiempo = Entry(root, textvariable = self.tiempo_value, width = w_ancho)
        self.entry_tiempo.grid(row = 4, padx=10, column = 2, sticky=E, columnspan=2)

        self.tree = ttk.Treeview(root, selectmode="browse")
        self.root.geometry("420x530")

        self.tree["columns"]=("col1", "col2", "col3")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=105, minwidth=80)
        self.tree.column("col2", width=110, minwidth=80)
        self.tree.column("col3", width=105, minwidth=80)
        self.tree.heading("#0",text="ID")
        self.tree.heading("col1", text="DNI")
        self.tree.heading("col2", text="Nombre y Apellido")
        self.tree.heading("col3", text="50mts Crol")

        self.tree.grid(row=11, padx=10, column=0, columnspan=4,sticky=W)

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        root.rowconfigure(1, weight=1, minsize=1)
        root.rowconfigure(8, weight=1, minsize=10)
        root.rowconfigure(10, weight=1, minsize=1)
        root.rowconfigure(12, weight=1, minsize=1)
        root.rowconfigure(14, weight=1, minsize=10)

        self.tree.bind("<<TreeviewSelect>>", lambda event: seleccion_en_tree(event, self.tree, self.entry_dni, self.entry_nombre, self.entry_tiempo))

        scrollbar = ttk.Scrollbar(root, orient='vertical', command=self.tree.yview)
        scrollbar.grid(row=11, column=3, padx=10,sticky='ens')
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lambda *args: scroll_vertical(self.tree, *args))


        #----------  FUNCIONES AUXILIARES   -----------

class FuncionesAuxiliares:
    def __init__(self, dni_value, nombre_value, tiempo_value, entry_dni, tree) -> None:
        self.dni_value = dni_value
        self.nombre_value = nombre_value
        self.tiempo_value = tiempo_value
        self.entry_dni = entry_dni
        self.tree = tree
        self.objeto_interaccionBd = InteraccionBd()

    def limpiar(self):
        self.entry_dni.configure(state='normal')
        self.dni_value.set("")
        self.nombre_value.set("")
        self.tiempo_value.set("")

    def alta_vista(self):
        retorno = self.objeto_interaccionBd.alta(self.dni_value.get(), self.nombre_value.get(), self.tiempo_value.get(), self.tree)
        if retorno == "Alta":
            self.limpiar()

    def modificar_vista(self):
        retorno = self.objeto_interaccionBd.modificar(self.dni_value.get(), self.nombre_value.get(), self.tiempo_value.get(), self.tree)
        if retorno == "Modificado":
            self.limpiar()



        #----------  INICIO BOTONES   -----------
class Buttons:
    def __init__(self, root, dni_value, nombre_value, tiempo_value, entry_dni, tree) -> None:
        self.objeto_interaccionBd = InteraccionBd()
        self.root = root
        self.funciones_auxiliares = FuncionesAuxiliares(dni_value, nombre_value, tiempo_value, entry_dni, tree)

        button_width = 15
        button_frame_top = Frame(self.root, bg="#c5e1ff")
        button_frame_top.grid(row=9, column=0, columnspan=4)
        button_frame_bottom = Frame(self.root, bg="#c5e1ff")
        button_frame_bottom.grid(row=13, column=0, columnspan=4)

        self.boton_cerrar=Button(self.root, text="Cerrar Aplicación", width=button_width, command=lambda:cerrar_programa(root, tree))
        self.boton_cerrar.grid(row=0, column=3, sticky=E, padx=10)

        self.boton_alta=Button(text="Agregar tiempo", width=button_width, command=lambda:self.funciones_auxiliares.alta_vista())
        self.boton_alta.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        self.boton_limpiar=Button(text="Limpiar", width=6, command=lambda:self.funciones_auxiliares.limpiar())
        self.boton_limpiar.grid(row=6, column=2,sticky=E)

        self.boton_modificar=Button(button_frame_top, text="Modificar tiempo", width=button_width, command=lambda:self.funciones_auxiliares.modificar_vista())
        self.boton_modificar.grid(row=9, column=2, padx=12)

        self.boton_borrar=Button(button_frame_top, text="Borrar tiempo", width=button_width, command=lambda:self.objeto_interaccionBd.borrar(tree))
        self.boton_borrar.grid(row=9, column=1, padx=12)

        self.boton_mejor_tiempo=Button(button_frame_bottom, text="Mejor tiempo", width=button_width, command=lambda:self.objeto_interaccionBd.mejor_tiempo(tree))
        self.boton_mejor_tiempo.grid(row=13, column=2, padx=12)

        self.boton_consulta=Button(button_frame_bottom, text="Listar tiempos", width=button_width, command=lambda:actualizar_treeview(tree))
        self.boton_consulta.grid(row=13, column=1, padx=12)

        #----------   FIN BOTONES   -----------
if __name__ == "__main__":
    root = Tk()
    aplicacion = Ventana(root)
    botones = Buttons(root, aplicacion.dni_value, aplicacion.nombre_value, aplicacion.tiempo_value, aplicacion.entry_dni, aplicacion.tree)
    root.mainloop()
