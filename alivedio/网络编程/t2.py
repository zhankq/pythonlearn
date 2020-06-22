import socket
import threading
import logging

class ChatServer:

    def a(self):
        print("aaaaa")
        

    def b(self):
        self.a()


s = ChatServer()

s.b()
