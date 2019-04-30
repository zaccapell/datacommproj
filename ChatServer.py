import socket
from threading import Thread
import sys

addresses = []

host = str(sys.argv[1])
port = int(sys.argv[2])
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(10)


def client_thread(conn, addr):
    conn.send("Welcome to the chat room".encode())
    while True:
        message = conn.recv(buffer)
        msg = message.decode()
        if msg != "!quit":
            msg = str(addr[0]) + ": " + msg
            print(msg)
            broadcast(msg, conn)
        else:
            remove(conn)


def broadcast(msg, conn):
    for sock in addresses:
        if sock != conn:
            sock.send(msg.encode())


def remove(conn):
    if conn in addresses:
        addresses.remove(conn)
        conn.close()


while True:
    print("Waiting for connection...")
    connection, address = server.accept()
    addresses.append(connection)
    broadcast(str(address[0]) + " has connected", connection)
    Thread(target=client_thread, args=(connection,address)).start()
