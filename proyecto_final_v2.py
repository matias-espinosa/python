from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import re

# ##############################################
# MODELO
# ##############################################

def conexion():
    con = sqlite3.connect("alumnos_natacion.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE alumnos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             dni INTEGER NOT NULL,
             nombre TEXT NOT NULL,
             tiempo_50_mts TEXT)
    """
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")

def alta(dni, nombre, tiempo_50_mts, tree):
    dni_str = str(dni)
    regex_dni="^\d{1,2}\.?\d{3}\.?\d{3}$"  #regex para el campo cadena
    if(re.match(regex_dni, dni_str)):
        print(dni, nombre, tiempo_50_mts)
        con=conexion()
        cursor=con.cursor()
        data=(dni, nombre, tiempo_50_mts)
        sql="INSERT INTO alumnos(dni, nombre, tiempo_50_mts) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
        a_val.set("")
        b_val.set("")
        c_val.set("")
    else:
        messagebox.showerror("Error", "Ingrese un DNI valido.")


def consultar(tree):
    actualizar_treeview(tree)
    sql = "SELECT * FROM alumnos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    print(resultado)
    for fila in resultado:
        print(fila)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM alumnos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)


def actualizar_treeview(mitreview):

    records = mitreview.get_children()
    print(records)
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM alumnos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
        a_val.set("")
        b_val.set("")
        c_val.set("")


def modificar(dni, nombre, tiempo_50_mts, tree):
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    mi_id = item['text']
    print(mi_id)

    con=conexion()
    cursor=con.cursor()
    data=(dni, nombre, tiempo_50_mts,mi_id)
    sql="UPDATE alumnos SET dni=?, nombre=?, tiempo_50_mts=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()
    print("Registro Actualizado")
    actualizar_treeview(tree)
    a_val.set("")
    b_val.set("")
    c_val.set("")

def on_vertical_scroll(*args):
    tree.yview(*args)

# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("Swim Tracker")

titulo = Label(root, anchor="w",pady=10, padx=10, text="Swim Tracker", bg="black", fg="white", height=3, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

separador = Label(root, bg="black", fg="white", height=1, width=60)
separador.grid(row=7, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

dni = Label(root, text="DNI")
dni.grid(row=2, column=0, sticky=W)
nombre_apellido=Label(root, text="Nombre y Apellido")
nombre_apellido.grid(row=3, column=0, sticky=W)
tiempo_50=Label(root, text="Tiempo en 50 metros crol")
tiempo_50.grid(row=4, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = IntVar(), StringVar(), DoubleVar()
w_ancho = 30

entrada1 = Entry(root, textvariable = a_val, width = w_ancho)
entrada1.grid(row = 2, column = 1)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho)
entrada2.grid(row = 3, column = 1)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho)
entrada3.grid(row = 4, column = 1)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------


tree = ttk.Treeview(root)
root.geometry("460x500")

tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=40, minwidth=50, anchor=W)
tree.column("col1", width=125, minwidth=80)
tree.column("col2", width=125, minwidth=80)
tree.column("col3", width=125, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="DNI")
tree.heading("col2", text="Nombre y Apellido")
tree.heading("col3", text="Tiempo 50 metros")

scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.grid(row=10, column=3, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=on_vertical_scroll)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tree.grid(row=10, column=0, columnspan=4)

button_width = 15
button_frame = Frame(root)
button_frame.grid(row=0, column=0)

boton_alta=Button(root, text="Alta", width=button_width, command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
boton_alta.grid(row=6, column=1)

boton_consulta=Button(root, text="Consultar", width=button_width, command=lambda:consultar(tree))
boton_consulta.grid(row=8, column=0)

boton_borrar=Button(root, text="Borrar", width=button_width, command=lambda:borrar(tree))
boton_borrar.grid(row=8, column=1)

boton_modificar=Button(root, text="Modificar", width=button_width, command=lambda:modificar(a_val.get(), b_val.get(), c_val.get(), tree))
boton_modificar.grid(row=8, column=2)

boton_cerrar=Button(root, text="Cerrar Aplicacion", width=button_width, command=root.quit)
boton_cerrar.grid(row=0, column=2)

root.rowconfigure(1, weight=3, minsize=10)
root.rowconfigure(5, weight=3, minsize=10)
root.rowconfigure(7, weight=3, minsize=50)
root.rowconfigure(9, weight=3, minsize=15)
root.rowconfigure(11, weight=3, minsize=15)



# root.rowconfigure(5, weight=3, minsize=10)
# root.rowconfigure(7, weight=3, minsize=10)
# root.rowconfigure(9, weight=3, minsize=10)
# root.rowconfigure(11, weight=3, minsize=10)
# root.rowconfigure(13, weight=3, minsize=10)
# root.rowconfigure(15, weight=3, minsize=30)

root.mainloop()