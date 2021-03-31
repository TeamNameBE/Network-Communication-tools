import socket


class TCPWrapper:
    def __init__(self, hostname: str, port: int):
        self.hostname = hostname
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        self.sock.connect((self.hostname, self.port))

    def send(self, msg):
        self.sock.sendall(msg.encode('ascii'))

    def receive(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()
