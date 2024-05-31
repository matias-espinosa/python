from tkinter import *
from tkinter import ttk
from modelo import cerrar_programa
from modelo import Treeview
from modelo import Nadador
from modelo import Servidor
import os

class Ventana:
    """**Clase principal que arma la ventana de la App**"""
    def __init__(self, window) -> None:
        self.root = window
        self.objeto_treeview = Treeview()
        self.objeto_nadador = Nadador()
        self.objeto_servidor = Servidor()

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_path = os.path.join(self.script_dir, 'img', 'swim-cap_5155580.png')
        self.img = PhotoImage(file=self.img_path)
        self.root.iconphoto(True, self.img)
        self.root.title("Swim Tracker")
        self.root.configure(bg="#c5e1ff")

        fuente_titulo = ("Arial", 16, "bold")
        fuente_footer = ("Arial", 9, "bold")
        self.titulo = Label(self.root, padx=10, anchor="w", font=fuente_titulo, text="Guarda tus tiempos!", bg="#001c3b", fg="white", height=2, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)

        self.footer = Label(self.root, padx=10, anchor="n", font=fuente_footer, text="S E R V E R     S E T T I N G S", bg="#c5e1ff", fg="#001c3b", height=1, width=60)
        self.footer.grid(row=14, column=0, columnspan=4, sticky=S)

        # LABELS
        fuente_campos = ("Calibri", 11)
        self.dni = Label(self.root, font=fuente_campos, bg="#c5e1ff",text="DNI")
        self.dni.grid(row=2, column=0, padx=1, sticky=E)
        self.nombre=Label(self.root, font=fuente_campos, bg="#c5e1ff", text="NOMBRE")
        self.nombre.grid(row=3, padx=1, column=0, sticky=E)
        self.apellido=Label(self.root, font=fuente_campos, bg="#c5e1ff", text="APELLIDO")
        self.apellido.grid(row=4, padx=1, column=0, sticky=E)
        self.tiempo_50=Label(self.root, font=fuente_campos,  bg="#c5e1ff", text="TIEMPO")
        self.tiempo_50.grid(row=5, padx=1, column=0, sticky=E)

        #EJEMPLO SEPARADOR
        #separator = ttk.Separator(self.root, orient='horizontal')
        #eparator.grid(row=8, column=0, columnspan=5, sticky="ew", pady=5)

        #spacer = Frame(self.root, height=20)
        #spacer.grid(row=8, column=0)

        # VARIABLES FOR ENTRY
        self.dni_value, self.nombre_value, self.apellido_value, self.tiempo_value = StringVar(),StringVar(),StringVar(), StringVar()

        # ENTRY & PLACEHOLDERS
        self.placeholders = {
            "dni": "Números, sin puntos.",
            "nombre": "Letras, sin espacios",
            "apellido": "Letras, sin espacios",
            "tiempo": "MM:SS"
        }
        self.placeholder_color = "grey"
        self.default_color = "black"

        w_ancho = 30
        self.entry_dni = Entry(self.root, textvariable=self.dni_value, width=w_ancho)
        self.entry_dni.grid(row=2, pady=3,padx=5, column=1, sticky=W, columnspan=2)
        self.add_placeholder(self.entry_dni, self.placeholders["dni"])

        self.entry_nombre = Entry(self.root, textvariable=self.nombre_value, width=w_ancho)
        self.entry_nombre.grid(row=3, pady=3,padx=5, column=1, sticky=W, columnspan=2)
        self.add_placeholder(self.entry_nombre, self.placeholders["nombre"])

        self.entry_apellido = Entry(self.root, textvariable=self.apellido_value, width=w_ancho)
        self.entry_apellido.grid(row=4, pady=3, padx=5, column=1, sticky=W, columnspan=2)
        self.add_placeholder(self.entry_apellido, self.placeholders["apellido"])

        self.entry_tiempo = Entry(self.root, textvariable=self.tiempo_value, width=7)
        self.entry_tiempo.grid(row=5, pady=3,padx=5, column=1, sticky=W, columnspan=2)
        self.add_placeholder(self.entry_tiempo, self.placeholders["tiempo"])

        #DROPDOWN
        self.options = ["Mariposa", "Espalda", "Pecho", "Crol"]
        self.default_message = "Estilo"

        self.combo = ttk.Combobox(self.root, values=self.options, width=10, state="readonly")
        self.combo.grid(row=5, column=2, padx=5,pady=3, sticky=E)

        self.combo.set(self.default_message)

        # FOCUS
        self.entry_dni.bind("<FocusIn>", lambda event: self.on_focus_in(event, self.placeholders["dni"]))
        self.entry_dni.bind("<FocusOut>", lambda event: self.on_focus_out(event, self.placeholders["dni"]))

        self.entry_nombre.bind("<FocusIn>", lambda event: self.on_focus_in(event, self.placeholders["nombre"]))
        self.entry_nombre.bind("<FocusOut>", lambda event: self.on_focus_out(event, self.placeholders["nombre"]))

        self.entry_apellido.bind("<FocusIn>", lambda event: self.on_focus_in(event, self.placeholders["apellido"]))
        self.entry_apellido.bind("<FocusOut>", lambda event: self.on_focus_out(event, self.placeholders["apellido"]))

        self.entry_tiempo.bind("<FocusIn>", lambda event: self.on_focus_in(event, self.placeholders["tiempo"]))
        self.entry_tiempo.bind("<FocusOut>", lambda event: self.on_focus_out(event, self.placeholders["tiempo"]))

        self.combo.bind("<FocusIn>", self.on_focus_in)
        self.combo.bind("<FocusOut>", self.on_focus_out)

        # TREEVIEW
        self.tree = ttk.Treeview(self.root, selectmode="browse")
        self.root.geometry("440x600")

        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=60, minwidth=60)
        self.tree.column("col2", width=73, minwidth=73)
        self.tree.column("col3", width=73, minwidth=73)
        self.tree.column("col4", width=73, minwidth=73)
        self.tree.column("col5", width=60, minwidth=60)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="DNI")
        self.tree.heading("col2", text="Nombre")
        self.tree.heading("col3", text="Apellido")
        self.tree.heading("col4", text="Estilo")
        self.tree.heading("col5", text="Tiempo")

        self.tree.grid(row=11, padx=10, column=0, columnspan=4, sticky=W)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.root.rowconfigure(1, weight=1, minsize=1)
        self.root.rowconfigure(8, weight=1, minsize=15)
        self.root.rowconfigure(10, weight=1, minsize=1)
        self.root.rowconfigure(12, weight=1, minsize=1)
        self.root.rowconfigure(15, weight=1, minsize=10)

        self.tree.bind("<<TreeviewSelect>>", lambda event: self.objeto_treeview.seleccion_en_tree(event, self.tree, self.entry_dni, self.entry_nombre, self.entry_apellido, self.entry_tiempo))

        # SCROLL BAR
        scrollbar = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        scrollbar.grid(row=11, column=3, padx=10, sticky='ens')
        self.tree.configure(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=lambda *args: self.objeto_treeview.scroll_vertical(self.tree, *args))

        # FUNCIONES AUXILIARES
        def limpiar(dni_value, nombre_value, tiempo_value, apellido_value, entry_dni, tree):
            entry_dni.configure(state='normal')
            dni_value.set("")
            self.add_placeholder(self.entry_dni, self.placeholders["dni"])
            nombre_value.set("")
            self.add_placeholder(self.entry_nombre, self.placeholders["nombre"])
            apellido_value.set("")
            self.add_placeholder(self.entry_apellido, self.placeholders["apellido"])
            tiempo_value.set("")
            self.add_placeholder(self.entry_tiempo, self.placeholders["tiempo"])

        def alta_vista():
            retorno = self.objeto_nadador.alta(
                self.dni_value.get(),
                self.nombre_value.get(),
                self.tiempo_value.get(),
                self.tree
            )
            if retorno == "Alta":
                limpiar(self.dni_value, self.nombre_value, self.apellido_value, self.tiempo_value, self.entry_dni, self.tree)

        def borar_vista():
            retorno = self.objeto_nadador.borrar(self.dni_value.get(), self.nombre_value.get(), self.tiempo_value.get(), self.tree)

        def modificar_vista():
            retorno = self.objeto_nadador.modificar(self.dni_value.get(), self.nombre_value.get(), self.tiempo_value.get(), self.tree)
            if retorno == "Modificado":
                limpiar(self.dni_value, self.nombre_value, self.tiempo_value, self.entry_dni, self.tree)

        # BOTONES: USAN LAS FUNCIONES AUXILIARES
        button_width = 15
        #button_frame_top = Frame(self.root, bg="#c5e1ff")
        #button_frame_top.grid(row=9, column=0, columnspan=4)
        button_frame_bottom = Frame(self.root, bg="#c5e1ff")
        button_frame_bottom.grid(row=13, column=0, columnspan=4)
        button_frame_footer = Frame(self.root, bg="#c5e1ff")
        button_frame_footer.grid(row=15, pady=6, sticky=N, column=0, columnspan=4)

        boton_cerrar = Button(self.root, text="Cerrar Aplicación", width=button_width, command=lambda: cerrar_programa(self.root, self.tree))
        boton_cerrar.grid(row=0, column=3, sticky=E, padx=10)

        boton_alta = Button(text="Registrar tiempo",  command=lambda: alta_vista())
        boton_alta.grid(row=6, padx=5, pady=9 , columnspan=2, column=1, sticky=W+E)

        boton_limpiar = Button(text="Borrar campos", width=button_width, command=lambda: limpiar(self.dni_value, self.nombre_value, self.apellido_value, self.tiempo_value, self.entry_dni, self.tree))
        boton_limpiar.grid(row=2, pady=3,padx=5, column=3, sticky=W)

        boton_modificar = Button( text="Modificar tiempo", width=button_width, command=lambda: modificar_vista())
        boton_modificar.grid(row=3, pady=3,padx=5, column=3, sticky=W)

        boton_borrar = Button( text="Borrar nadador", width=button_width, command=lambda: borar_vista())
        boton_borrar.grid(row=4, pady=3,padx=5, column=3, sticky=W)

        boton_mejor_tiempo = Button(button_frame_bottom, text="Mejor tiempo", width=button_width, command=lambda: self.objeto_nadador.mejor_tiempo(self.tree))
        boton_mejor_tiempo.grid(row=13, column=2, pady= (4,15), padx=12)

        boton_consulta = Button(button_frame_bottom, text="Listar tiempos", width=button_width, command=lambda: self.objeto_treeview.actualizar_treeview(self.tree))
        boton_consulta.grid(row=13, column=1, pady= (4,15), padx=12)

        boton_prender = Button(button_frame_footer, text="Prender Server", width=button_width, command=lambda: self.objeto_servidor.try_connection())
        boton_prender.grid(row=15, column=1 , padx=12)

        boton_apagar = Button(button_frame_footer, text="Apagar Server", width=button_width, command=lambda: self.objeto_servidor.stop_server())
        boton_apagar.grid(row=15, column=3 ,padx=12)

        boton_check = Button(button_frame_footer, text="Check Server Status", width=button_width, command=lambda: self.objeto_servidor.check_server_status())
        boton_check.grid(row=15, column=5 ,sticky=N,  padx=12)

    def add_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(fg=self.placeholder_color)

    def on_focus_in(self, event, placeholder=None):
        widget = event.widget
        if isinstance(widget, Entry):
            if widget.get() == placeholder:
                widget.delete(0, END)
                widget.config(fg=self.default_color)
        elif isinstance(widget, ttk.Combobox):
            if widget.get() == self.default_message:
                widget.set("")

    def on_focus_out(self, event, placeholder=None):
        widget = event.widget
        if isinstance(widget, Entry):
            if widget.get() == "":
                self.add_placeholder(widget, placeholder)
        elif isinstance(widget, ttk.Combobox):
            if widget.get() == "":
                widget.set(self.default_message)