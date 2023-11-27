#############################################################
# "BASE DE DATOS"
#############################################################

db_users=[
   ["entrenador","entrenador","entrenador"],
   ["admin","admin","admin"]
]

#############################################################
# VISTA
#############################################################

def menu_entrenador():
    print("    (a) Crear Alumno.")
    print("    (b) Cargar tiempo para Alumno.")
    print("    (c) Listar tiempos por Alumno.")
    print("    (d) Modificar Alumno.")
    print("    (e) Deshabilitar Alumno.")
    print("    (f) Eliminar Alumno.")
    print("    ó cualquier otra tecla para volver al menu anterior")
    eleccion = input("\n Que desea hacer: ")
    if eleccion=="a":
            print("Funcion para Crear alumno")
    elif eleccion=="b":
            print("Funcion para Cargar tiempo para Alumno.")
    elif eleccion=="d":
            print("Funcion para Listar tiempos por Alumno.")
    elif eleccion=="d":
            print("Funcion para Modificar Alumno.")
    elif eleccion=="e":
        print("Funcion para Deshabilitar Alumno.")
    elif eleccion=="f":
        print("Funcion para Eliminar Alumno.")
    else:
       print("Usted a sido deslogueado")
       login()

def menu_admin():
    print("    (a) Crear Usuario.")
    print("    (b) Resetear Password de Usuario.")
    print("    (c) Listar Usuarios.")
    print("    (d) Deshabilitar Usuario.")
    print("    ó cualquier otra tecla para salir")
    eleccion = input("\n Que desea hacer: ")
    if eleccion=="a":
            print("Funcion para Crear usuario")
    elif eleccion=="b":
            print("Funcion para Resetear Password de Usuario.")
    elif eleccion=="d":
            print("Funcion para Listar Usuarios.")
    elif eleccion=="d":
            print("Funcion para Deshabilitar Usuario.")
    else:
        print("Usted a sido deslogueado")
        login()

#############################################################
# MODELO
#############################################################

def login():
    rol=None
    user=input("Ingrese el user: ")
    password=input("Ingrese el password: ")

    for i in db_users:
        if i[0]==user and i[1]==password:
            rol=i[2]

    while rol!="entrenador" or rol!="admin":
        if rol=="entrenador":
            menu_entrenador()
        elif rol=="admin":
            menu_admin()
        else:
            print("El user o la contraseña no son correctos, ingreselos nuevamente.")
            user=input("Ingrese el user: ")
            password=input("Ingrese el password: ")
            for i in db_users:
                if i[0]==user and i[1]==password:
                    rol=i[2]

#############################################################
# CONTROLADOR
#############################################################

login()
