from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import re


# ##############################################
# MODELO
# ##############################################


#----------    INICIO BASE DE DATOS   -----------

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
             tiempo_50_mts TEXT NOT NULL)
    """
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("Excepcion: Error al tratar de crear la Base de Datos y/o Tabla cuando ya existen.")

#----------    FIN BASE DE DATOS   -----------

def alta(dni, nombre, tiempo_50_mts, tree):
    dni_str = str(dni)
    tiempo_str = tiempo_50_mts
    regex_tiempo="([0-9]{2}):([0-5][0-9])$"
    regex_dni="^\d{1,2}\.?\d{3}\.?\d{3}$"
    if(re.match(regex_dni, dni_str)):
        if(re.match(regex_tiempo, tiempo_str)):
            print(dni, nombre, tiempo_50_mts)
            con=conexion()
            cursor=con.cursor()
            data=(dni, nombre, tiempo_50_mts)
            sql="INSERT INTO alumnos(dni, nombre, tiempo_50_mts) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            actualizar_treeview(tree)
            messagebox.showinfo("Alta exitosa!", f'El tiempo de {nombre} fue dado de alta!')
            a_val.set("")
            b_val.set("")
            c_val.set("")
        else:
            messagebox.showinfo("Error en '50 metros crol'", f'El tiempo no esta expresado correctamente.\nUse el formato MM:SS')
    else:
        messagebox.showerror("Error DNI", "Ingrese un DNI valido.")


def borrar(tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item['text']
    data_alumno = item['values']
    alumno=data_alumno[1]
    respuesta = messagebox.askokcancel("Borrar", f"Esta seguro que desea borrar al alumno: {alumno}")
    if respuesta == True:
        con=conexion()
        cursor=con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM alumnos WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)


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


def modificar(dni, nombre, tiempo_50_mts, tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item['text']
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


def mejor_tiempo(tree):
    con=conexion()
    cursor=con.cursor()
    sql="SELECT nombre, MIN(tiempo_50_mts) FROM alumnos"
    mejor_tiempo = cursor.execute(sql)
    resultado = mejor_tiempo.fetchall()
    print (resultado)
    tupla = resultado[0]
    alumno = tupla[0]
    tiempo = tupla[1]
    print(f'{alumno} tiene el mejor tiempo: {tiempo}')
    con.commit()
    messagebox.showinfo("Mejor tiempo", f'{alumno} tiene el mejor tiempo: {tiempo}')


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    print(records)
    #print(type(records[0]))
    #print(records[1])
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM alumnos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        #print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
        a_val.set("")
        b_val.set("")
        c_val.set("")

def scroll_veritcal(*args):
    tree.yview(*args)

def cerrar_programa(tree):
    result = messagebox.askokcancel("OK o Cancelar", "Esta seguro que desea cerrar el programa?")
    if result == True:
        root.quit()

# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("Swim Tracker")
root.configure(bg="#B3B7BF")
fuente_titulo = ("Arial", 16, "bold")
fuente_campos = ("Arial", 10)

titulo = Label(root, anchor="w",pady=10, padx=10, font=fuente_titulo, text="Swim Tracker", bg="black", fg="white", height=3, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

dni = Label(root, font=fuente_campos, bg="#B3B7BF",text="DNI")
dni.grid(row=2, column=0, padx=25, sticky=W)
nombre_apellido=Label(root, font=fuente_campos, bg="#B3B7BF", text="Nombre y Apellido")
nombre_apellido.grid(row=3, padx=25, column=0, sticky=W)
tiempo_50=Label(root, font=fuente_campos,  bg="#B3B7BF", text="50 mts Crol (MM:SS)")
tiempo_50.grid(row=4, padx=25, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = IntVar(), StringVar(), StringVar()
w_ancho = 29

entrada1 = Entry(root, textvariable = a_val, width = w_ancho)
entrada1.grid(row = 2, padx=26, column = 2, columnspan=2)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho)
entrada2.grid(row = 3, padx=26, column = 2, columnspan=2)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho)
entrada3.grid(row = 4, padx=26, column = 2, columnspan=2)


# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------


tree = ttk.Treeview(root)
root.geometry("420x500")

tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=105, minwidth=80)
tree.column("col2", width=110, minwidth=80)
tree.column("col3", width=105, minwidth=80)
tree.heading("#0",text="ID")
tree.heading("col1", text="DNI")
tree.heading("col2", text="Nombre y Apellido")
tree.heading("col3", text="50mts Crol")

tree.grid(row=8, padx=10, column=0, columnspan=4,sticky=W)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.rowconfigure(1, weight=1, minsize=10)
root.rowconfigure(5, weight=1, minsize=20)
root.rowconfigure(7, weight=1, minsize=20)
root.rowconfigure(9, weight=1, minsize=15)
root.rowconfigure(11, weight=1, minsize=15)


scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.grid(row=8, column=3, padx=10,sticky='ens')
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=scroll_veritcal)

button_width = 15
button_frame_top = Frame(root, bg="#B3B7BF")
button_frame_top.grid(row=6, column=0, columnspan=4)
button_frame_bottom = Frame(root, bg="#B3B7BF")
button_frame_bottom.grid(row=10, column=0, columnspan=4)

boton_alta=Button(button_frame_top, text="Agregar tiempo", width=button_width, command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
boton_alta.grid(row=6, column=0, padx=5, pady=5)

boton_mejor_tiempo=Button(button_frame_top,  text="Mejor tiempo", width=button_width, command=lambda:mejor_tiempo(tree))
boton_mejor_tiempo.grid(row=6, column=2, padx=5, pady=5)

boton_consulta=Button(button_frame_bottom, text="Listar tiempos", width=button_width, command=lambda:consultar(tree))
boton_consulta.grid(row=10, column=0, padx=5, pady=5)

boton_borrar=Button(button_frame_bottom, text="Borrar tiempo", width=button_width, command=lambda:borrar(tree))
boton_borrar.grid(row=10, column=1, padx=5, pady=5)

boton_modificar=Button(button_frame_bottom, text="Modificar tiempo", width=button_width, command=lambda:modificar(a_val.get(), b_val.get(), c_val.get(), tree))
boton_modificar.grid(row=10, column=2, padx=5, pady=5)

boton_cerrar=Button(root, text="Cerrar Aplicacion", width=button_width, command=lambda:cerrar_programa(tree))
boton_cerrar.grid(row=0, column=3, sticky=E, padx=10)

root.mainloop()