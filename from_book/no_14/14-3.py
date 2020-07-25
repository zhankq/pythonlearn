from socketserver import TCPServer ,StreamRequestHandler

class Handler(StreamRequestHandler):
	def handle(self):
		addr=self.request.getpeername()
		print("Got connection from",addr)
		self.wfile.write("Thank you for connection")

server = TCPServer(("",1237),Handler)
server.serve_forever()