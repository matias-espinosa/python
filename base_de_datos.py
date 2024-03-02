"""Modulo que controla la conxexion a la base de datos"""
import sqlite3

class Database:
    def __init__(self, db_name="alumnos_natacion.db"):
        self.db_name = db_name
        self.con = None

    def conexion(self):
        try:
            self.con = sqlite3.connect(self.db_name)
            print("Base de Datos conectada.")
        except sqlite3.Error as e:
            print("Error al conectarse a la Base de Datos: ", e)

    def create_table(self):
        if self.con is None:
            print("La Conexion a la base de datos no fue establecida")
            return

        try:
            cursor = self.con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS alumnos
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              dni INTEGER NOT NULL,
                              nombre TEXT NOT NULL,
                              tiempo_50_mts TEXT NOT NULL)""")
            print("Tabla 'alumnos' creada.")
        except sqlite3.Error as e:
            print("Error creando tabla:", e)

    def close(self):
        if self.con:
            self.con.close()
            print("Conexion a Base de Datos cerrada.")

