import socket
import select
import sys

host = str(sys.argv[1])
port = int(sys.argv[2])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

while True:
    socketList = [sys.stdin, server]
    readSocket, writeSocket, errorSocket = select.select(socketList)
    for sock in readSocket:
        if sock == server:
            msg = sock.recv(2048).decode("utf8")
            print(msg)
        else:
            msg = sys.stdin.readline()
            server.send(bytes(str(msg), "utf8"))
            sys.stdout.write("You: " + msg)
            sys.stdout.flush()

server.close()
