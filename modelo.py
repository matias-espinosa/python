import sqlite3
import re
from tkinter import messagebox

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

def alta(dni, nombre, tiempo_50_mts, entrada1, tree):
    dni_str = str(dni)
    regex_tiempo="([0-9]{2}):([0-5][0-9])$"
    regex_dni = r'^\d{7,8}$'
    if(re.match(regex_dni, dni_str)):
        if(re.match(regex_tiempo, tiempo_50_mts)):
            sql = "SELECT dni FROM alumnos WHERE dni=?"
            nuevo_dni = (dni,)
            con = conexion()
            cursor = con.cursor()
            datos = cursor.execute(sql, nuevo_dni)
            resultado = datos.fetchall()
            if  resultado == []:
                data=(dni, nombre, tiempo_50_mts)
                sql="INSERT INTO alumnos(dni, nombre, tiempo_50_mts) VALUES(?, ?, ?)"
                cursor.execute(sql, data)
                con.commit()
                actualizar_treeview(tree)
                messagebox.showinfo("Alta exitosa!", f'El tiempo de {nombre} fue dado de alta!')
                limpiar(dni, nombre, tiempo_50_mts, entrada1 ,tree)
                con.close
            else:
                messagebox.showinfo("DNI duplicado", f'El DNI: {dni} ya se encuentra en la base de datos.\n\nModifique el tiempo o nombre del alumno existente.')
        else:
            messagebox.showerror("Error en '50 metros crol'", f'El tiempo no esta expresado correctamente.\nUse el formato MM:SS')
    else:
        messagebox.showerror("Error DNI", "Ingrese un DNI valido.\nEjemplo: 30123456).")


def limpiar(dni, nombre, tiempo_50_mts, entrada1, tree):
    entrada1.configure(state='normal')
    dni.set("")
    nombre.set("")
    tiempo_50_mts.set("")


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
        con.close()


def modificar(dni, nombre, tiempo_50_mts, tree):
    regex_tiempo="([0-9]{2}):([0-5][0-9])$"
    if(re.match(regex_tiempo, tiempo_50_mts)):
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item['text']
        data_alumno = item['values']
        alumno = data_alumno[1]
        data = (dni, nombre, tiempo_50_mts,mi_id)
        respuesta = messagebox.askokcancel("Modificar", f"Esta seguro que desea modificar al alumno: {alumno}")
        if respuesta == True:
            con=conexion()
            cursor=con.cursor()
            sql="UPDATE alumnos SET dni=?, nombre=?, tiempo_50_mts=? WHERE id=?;"
            cursor.execute(sql, data)
            con.commit()
            con.close()
            actualizar_treeview(tree)
            limpiar(tree)
    else:
        messagebox.showerror("Error en '50 metros crol'", f'El tiempo no esta expresado correctamente.\nUse el formato MM:SS')


def mejor_tiempo(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql="""SELECT *
            FROM alumnos
            WHERE tiempo_50_mts = (SELECT MIN(tiempo_50_mts) FROM alumnos)"""
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    con.close()
    for fila in resultado:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
        limpiar(tree)


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM alumnos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    con.close()
    for fila in resultado:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


def seleccion_en_tree(event):
    fila_seleccionada = tree.focus()  # Obtener el item de Tkinter 'fila'
    valores = tree.item(fila_seleccionada, 'values')  # Obtener los valores de la fila seleccionada
    # Llenar los widgets vacios con la fila seleccionada
    entrada1.configure(state='normal')
    entrada2.configure(state='normal')
    entrada3.configure(state='normal')
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    if valores:
        entrada1.insert(0, valores[0])
        entrada2.insert(0, valores[1])
        entrada3.insert(0, valores[2])
        entrada1.configure(state='disabled')


def scroll_veritcal(*args):
    tree.yview(*args)


def cerrar_programa(tree):
    result = messagebox.askokcancel("OK o Cancelar", "Esta seguro que desea cerrar el programa?")
    if result == True:
        root.quit()
