import socketserver
import datetime

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        log_message = data.decode('utf-8')

        # Log the received message with a timestamp
        with open("server_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()}: {log_message}\n")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        print(f"Servidor corrriendo en {HOST}:{PORT}")
        server.serve_forever()