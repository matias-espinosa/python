import socket

def enviar_mensaje_log(message):
    HOST, PORT = "localhost", 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (HOST, PORT))

def alta_server_log(dni, nombre, tiempo_50_mts):
    loguear_mensaje = f"Alta con Server prendido: DNI={dni}, Name={nombre}, Time={tiempo_50_mts}"
    enviar_mensaje_log(loguear_mensaje)

def modificar_server_log(dni, nombre, tiempo_50_mts):
    loguear_mensaje = f"Modificar con Server prendido: DNI={dni}, Name={nombre}, New Time={tiempo_50_mts}"
    enviar_mensaje_log(loguear_mensaje)

def borrar_server_log(dni, nombre):
    loguear_mensaje = f"Borrar con Server prendido: DNI={dni}, Name={nombre}"
    enviar_mensaje_log(loguear_mensaje)

