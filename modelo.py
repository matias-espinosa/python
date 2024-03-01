import sqlite3
import re
from tkinter import messagebox
from tkinter import END
from regex_validations import ValidationUtils

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

class Nadador():

    def __init__(self) -> None:
        pass
    def alta(self, dni, nombre, tiempo_50_mts, tree):
        self.objeto_treeview = Treeview
        dni_str = str(dni)
        if ValidationUtils.validate_dni(dni_str):
            if ValidationUtils.validate_tiempo(tiempo_50_mts):
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
                    self.objeto_treeview.actualizar_treeview(tree)
                    messagebox.showinfo("Alta exitosa!", f'El tiempo de {nombre} fue dado de alta!')
                    #limpiar(dni, nombre, tiempo_50_mts, entry_dni ,tree)
                    con.close
                    return "Alta"
                else:
                    messagebox.showinfo("DNI duplicado", f'El DNI: {dni} ya se encuentra en la base de datos.\n\nModifique el tiempo o nombre del alumno existente.')
                    return 1
            else:
                messagebox.showerror("Error en '50 metros crol'", f'El tiempo no esta expresado correctamente.\nUse el formato MM:SS')
                return 1
        else:
            messagebox.showerror("Error DNI", "Ingrese un DNI valido.\nEjemplo: 30123456).")
            return 1

    def borrar(self, tree):
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


    def modificar(self,dni, nombre, tiempo_50_mts, tree):
        self.objeto_treeview = Treeview
        if ValidationUtils.validate_tiempo(tiempo_50_mts):
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
                self.objeto_treeview.actualizar_treeview(tree)
                return "Modificado"
        else:
            messagebox.showerror("Error en '50 metros crol'", f'El tiempo no esta expresado correctamente.\nUse el formato MM:SS')
            return 1

    def mejor_tiempo(self, mitreview):
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

class Treeview:
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


    def seleccion_en_tree(event, tree, entry_dni, entry_nombre, entry_tiempo):
        fila_seleccionada = tree.focus()  # Obtener el item de Tkinter 'fila'
        valores = tree.item(fila_seleccionada, 'values')  # Obtener los valores de la fila seleccionada
        # Llenar los widgets vacios con la fila seleccionada
        entry_dni.configure(state='normal')
        entry_nombre.configure(state='normal')
        entry_tiempo.configure(state='normal')
        entry_dni.delete(0, END)
        entry_nombre.delete(0, END)
        entry_tiempo.delete(0, END)
        if valores:
            entry_dni.insert(0, valores[0])
            entry_nombre.insert(0, valores[1])
            entry_tiempo.insert(0, valores[2])
            entry_dni.configure(state='disabled')


    def scroll_vertical(tree,*args):
        tree.yview(*args)

def cerrar_programa(root, tree):
    result = messagebox.askokcancel("OK o Cancelar", "Esta seguro que desea cerrar el programa?")
    if result == True:
        root.quit()
