import socket

server = socket.socket()
server.bind(('127.0.0.1',9999))

server.listen()

s,raddr = server.accept()

while True:
    data = s.recv(1024)
    print(data)

    s.send('ack. {}'.format(data.decode()).encode())

s.close()

server.close()
