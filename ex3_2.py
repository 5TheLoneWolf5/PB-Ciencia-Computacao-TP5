import socket
import ssl

def send_wrapper(self, data, *args, **kwargs):
    print("Dados enviados: ", data)
    return self.__original_send(data, *args, **kwargs)

def recv_wrapper(self, bufsize, *args, **kwargs):
    data = self.__original_recv(bufsize, *args, **kwargs)
    print("Dados recebidos: ", data)
    return data

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_client = context.wrap_socket(client_socket, server_hostname="127.0.0.1")

ssl_client.__original_send = ssl_client.send
ssl_client.__original_recv = ssl_client.recv

ssl_client.send = send_wrapper.__get__(ssl_client, type(ssl_client))
ssl_client.recv = recv_wrapper.__get__(ssl_client, type(ssl_client))

ssl_client.connect(("127.0.0.1", 60000))

ssl_client.send(b"Mensagem segura com logging de pacotes")

response = ssl_client.recv(1024)