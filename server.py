import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def accept_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 17172))
server_socket.listen(5)
print("Server is listening for connections...")

accept_connections(server_socket)
