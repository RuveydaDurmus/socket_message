import socket
import threading


class Connection(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def send(self, message):
        self.conn.sendall(message)

    def read(self):
        return self.conn.recv(1024)

    def run(self):
        while True:
            data = self.read()
            for _conn in connections:
                if self == _conn:
                    continue
                _conn.send(data)


s = socket.socket()

print("Socket Created")

port = 12345
s.bind(("127.0.0.1", port))
s.listen(10)
print("Socket is listening")

connections = []

while True:
    conn, addr = s.accept()
    conn = Connection(conn)
    conn.start()

    connections.append(conn)
