import socket
s = socket.socket()
host = socket.gethostname()
port = 1237
s.bind((host,port))

s.listen(5)
while True:
	c,addr = s.accept()
	print("Got connection from",addr)
	c.send("Thank you for connectiong".encode(encoding="utf-8", errors='strict'))
#	s.send(meg.encode(encoding='utf_8', errors='strict'))

	c.close()
