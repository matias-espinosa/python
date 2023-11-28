#############################################################
# "BASE DE DATOS"
#############################################################

db_users=["admin","admin"]

#############################################################
# VISTA
#############################################################

def login():
    user=input("Ingrese el user: ")
    password=input("Ingrese el password: ")

    while user!=db_users[0] or password!=db_users[1]:
        print("El user o la contraseña no son correctos, ingreselos nuevamente.")
        user=input("Ingrese el user: ")
        password=input("Ingrese el password: ")
    main()

def main():
    diccionario = {}
    key_inicial = 0
    opcion = 1

    while opcion != 0:
        print(" ")
        print("-= Que accion desea realizar? =-")
        print("1= Cargar tiempo y estilo en 50mts para un alumno.")
        print("2= Listar tiempos por alumno.")
        print("3= Editar tiempos de alumno.")
        print("4= Borrar tiempos del alumno.")
        print("5= Listar los mejores tiempos por estilo.")
        print("0= Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            nuevo_tiempo(diccionario, key_inicial)
            key_inicial += 1
        elif opcion == 2:
            tiempos_alumno(diccionario)
        elif opcion == 3:
            editar_tiempos(diccionario)
        elif opcion == 4:
            borrar_tiempos(diccionario)
        elif opcion == 5:
            mejores_tiempos(diccionario)

#############################################################
# MODELO
#############################################################

def nuevo_tiempo(diccionario, key_inicial):
    print("Alta nuevo tiempo")
def tiempos_alumno(diccionario):
    print("Tiempos del alumno")
def editar_tiempos(diccionario):
    print("Editar tiempo")
def borrar_tiempos(diccionario):
    print("Borrar tiempo")
def mejores_tiempos(diccionario):
    print("Mejores tiempos.")

#############################################################
# CONTROLADOR
#############################################################

login()
