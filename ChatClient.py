import socket
import sys
# from threading import Thread

host = str(sys.argv[1])
port = int(sys.argv[2])
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))
# receive_thread = Thread(target=receive)
# receive_thread.start()


while True:
    msg = server.recv(buffer).decode("utf8")
    print(msg)
    send = sys.stdin.readline()
    server.send(bytes(send, "utf8"))
    if send == "(quit)":
        server.close()
        exit()
    else:
        sys.stdout.write("You: ")
        sys.stdout.write(send)
        sys.stdout.flush()
