import socket

def send_log_message(message):
    HOST, PORT = "localhost", 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (HOST, PORT))

# Example usage in a CRUD application
def alta_server_log(dni, nombre, tiempo_50_mts):
    # Perform the creation of a new record in the database
    # ...

    # Send log message to the server
    log_message = f"Alta con Server prendido: DNI={dni}, Name={nombre}, Time={tiempo_50_mts}"
    send_log_message(log_message)

# Simulate creating a record

