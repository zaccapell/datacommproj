import socket
import sys
from threading import Thread

host = str(sys.argv[1])
port = int(sys.argv[2])
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))


def receive():
    while True:
        msg = server.recv(1024)
        msg = msg.decode()
        print(msg)


while True:
    rcv = Thread(target=receive)
    rcv.start()
    message = input()
    if message == "!quit":
        server.send(message.encode())
        print("Leaving room")
        break
    server.send(message.encode())

exit()
