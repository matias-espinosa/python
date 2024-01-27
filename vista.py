from tkinter import *
from tkinter import ttk
from modelo import cerrar_programa
from modelo import alta
from modelo import borrar
from modelo import modificar
from modelo import limpiar
from modelo import mejor_tiempo
from modelo import actualizar_treeview
from modelo import seleccion_en_tree
from modelo import scroll_veritcal

# ##############################################
# VISTA INTEGRADA CON EL CONTROLADOR
# ##############################################

root = Tk()

root.title("Swim Tracker")
root.configure(bg="#c5e1ff")

fuente_titulo = ("Arial", 16, "bold")
fuente_campos = ("Calibri", 11)

titulo = Label(root,padx=10, anchor="w", font=fuente_titulo, text="Swim Tracker", bg="#001c3b", fg="white", height=2, width=60)
titulo.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)

dni = Label(root, font=fuente_campos, bg="#c5e1ff",text="DNI (números, sin puntos)")
dni.grid(row=2, column=0, padx=10, sticky=W)
nombre_apellido=Label(root, font=fuente_campos, bg="#c5e1ff", text="Nombre y Apellido")
nombre_apellido.grid(row=3, padx=10, column=0, sticky=W)
tiempo_50=Label(root, font=fuente_campos,  bg="#c5e1ff", text="50 mts Crol (MM:SS)")
tiempo_50.grid(row=4, padx=10, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = IntVar(), StringVar(), StringVar()

w_ancho = 31

entrada1 = Entry(root, textvariable = a_val, width = w_ancho)
entrada1.grid(row = 2, padx=10, column = 2, sticky=E, columnspan=2)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho)
entrada2.grid(row = 3, padx=10, column = 2, sticky=E, columnspan=2)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho)
entrada3.grid(row = 4, padx=10, column = 2, sticky=E, columnspan=2)


# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------


tree = ttk.Treeview(root, selectmode="browse")
root.geometry("420x530")

tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=105, minwidth=80)
tree.column("col2", width=110, minwidth=80)
tree.column("col3", width=105, minwidth=80)
tree.heading("#0",text="ID")
tree.heading("col1", text="DNI")
tree.heading("col2", text="Nombre y Apellido")
tree.heading("col3", text="50mts Crol")

tree.grid(row=11, padx=10, column=0, columnspan=4,sticky=W)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.rowconfigure(1, weight=1, minsize=1)
root.rowconfigure(8, weight=1, minsize=10)
root.rowconfigure(10, weight=1, minsize=1)
root.rowconfigure(12, weight=1, minsize=1)
root.rowconfigure(14, weight=1, minsize=10)

tree.bind("<<TreeviewSelect>>", seleccion_en_tree)

scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.grid(row=11, column=3, padx=10,sticky='ens')
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=scroll_veritcal)

#----------  INICIO BOTONES   -----------

button_width = 15
button_frame_top = Frame(root, bg="#c5e1ff")
button_frame_top.grid(row=9, column=0, columnspan=4)
button_frame_bottom = Frame(root, bg="#c5e1ff")
button_frame_bottom.grid(row=13, column=0, columnspan=4)

boton_cerrar=Button(root, text="Cerrar Aplicación", width=button_width, command=lambda:cerrar_programa(tree))
boton_cerrar.grid(row=0, column=3, sticky=E, padx=10)

boton_alta=Button(text="Agregar tiempo", width=button_width, command=lambda:alta(a_val.get(), b_val.get(), c_val.get(),entrada1, tree))
boton_alta.grid(row=6, column=3, padx=10, pady=5, sticky=E)

boton_limpiar=Button(text="Limpiar", width=6, command=lambda:limpiar(a_val.get(), b_val.get(), c_val.get(), entrada1, tree))
boton_limpiar.grid(row=6, column=2,sticky=E)

boton_modificar=Button(button_frame_top, text="Modificar tiempo", width=button_width, command=lambda:modificar(a_val.get(), b_val.get(), c_val.get(), tree))
boton_modificar.grid(row=9, column=2, padx=12)

boton_borrar=Button(button_frame_top, text="Borrar tiempo", width=button_width, command=lambda:borrar(tree))
boton_borrar.grid(row=9, column=1, padx=12)

boton_mejor_tiempo=Button(button_frame_bottom, text="Mejor tiempo", width=button_width, command=lambda:mejor_tiempo(tree))
boton_mejor_tiempo.grid(row=13, column=2, padx=12)

boton_consulta=Button(button_frame_bottom, text="Listar tiempos", width=button_width, command=lambda:actualizar_treeview(tree)) #Consulta se usaba aca
boton_consulta.grid(row=13, column=1, padx=12)

#----------   FIN BOTONES   -----------

root.mainloop()