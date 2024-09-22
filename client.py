import socket
import threading
import sys

username = ""

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"\r{message}\n{username}: ", end='', flush=True)
        except:
            print("Disconnected from server.")
            break

def send_messages(sock):
    while True:
        message = input(f"{username}: ")
        full_message = f"{username}: {message}"
        sock.send(full_message.encode())

def main():
    global username
    server_address = ('88.178.231.193', 17172)
    
    username = input("Enter your username: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        print("Connected to the server.")

        threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
        send_messages(sock)

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
