import socket
import sys

host = str(sys.argv[1])
port = int(sys.argv[2])
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

while True:
    message = server.recv(buffer)
    message = message.decode()
    print(message)
    message = input(str("Me > "))
    if message == "(quit)":
        message = "Leaving the Chat room"
        server.send(message.encode())
        print("\n")
        break
    server.send(message.encode())
