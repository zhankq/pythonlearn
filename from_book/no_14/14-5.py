from socketserver import TCPServer,ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn,TCPServer):pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("Got connection from",addr)
        self.wfile.write("Thank you from connecting")

server = Server(("",1234),Handler)
server.serve_forever()
