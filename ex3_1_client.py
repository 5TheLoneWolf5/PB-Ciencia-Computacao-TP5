import socket
import ssl
from time import sleep

HOST = "127.0.0.1"
PORT = 60000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client = context.wrap_socket(client, server_hostname=HOST)

if __name__ == "__main__":
    client.connect((HOST, PORT))
    print("Cliente: conexão estabelecida")

    while True:
        client.send("Olá, servidor TLS!".encode("utf-8"))
        print("Cliente: " + client.recv(1024).decode('utf-8'))
        sleep(1)