import socket
import ssl

HOST = "127.0.0.1"
PORT = 60000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(keyfile='key.pem', certfile='cert.pem')

server = context.wrap_socket(
    server,
    server_side=True,
)

if __name__ == "__main__":
    server.bind((HOST, PORT))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        print(f"Conexão estabelecioda com ({client_address}, {PORT})")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Recebeu: {data.decode('utf-8')}")
            connection.sendall(data)
        connection.close()