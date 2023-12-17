import socket
import threading


class Connection(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def send(self, message):
        self.conn.send(message)

    def read(self):
        return self.conn.recv(1024)

    def run(self):
        while True:
            print(self.read())


port = 12345

s = socket.socket()
s.connect(("127.0.0.1", port))

conn = Connection(s)
conn.start()

while True:
    user_input = (input(""))
    conn.send(user_input.encode('utf-8'))


