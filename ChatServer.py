import socket
import threading
import sys

addresses = {}

host = str(sys.argv[1])
port = int(sys.argv[2])
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))


def incoming():
    while True:
        client, addr = server.accept()
        print(str(addr) + " has connected")
        client.send(bytes("Welcome to the room!", "utf8"))
        addresses[client] = addr
        threading.Thread(target=handle(client)).start()


def handle(client):
    broadcast(str(addresses[client]) + " has joined the chat", client)
    while True:
        msg = client.recv(buffer)
        if msg != bytes("(quit)", "utf8"):
            broadcast(str(addresses[client]) + ": " + str(msg), client)
        else:
            client.send(bytes("(quit)", "utf8"))
            client.close()
            broadcast(str(addresses[client]) + "has left the room", client)
            del addresses[client]
            break


def broadcast(msg, client):
    for sock in addresses:
        sock.send(msg.encode())


if __name__ == "__main__":
    server.listen(5)
    print("Waiting for connection...")
    accept = threading.Thread(target=incoming())
    accept.start()
    accept.join()
    server.close()
