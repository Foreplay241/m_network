import time
import socket
import subprocess
import threading


class MClient:
    def __init__(self, host='0.0.0.0', port=840):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(host, port)
        self.client_socket.connect((host, port))
        self.server_socket = None
        self.server_address = None

        recv_thread = threading.Thread(target=self.receive_data, args=())
        send_thread = threading.Thread(target=self.send_data, args=())
        recv_thread.start()
        send_thread.start()
        recv_thread.join()
        send_thread.join()

    def send_data(self):
        while True:
            message = str(input("What you gonna say about that? _"))
            self.client_socket.sendall(message.encode())

    def receive_data(self):
        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            print(data.decode())

    def send_ip_info(self):
        IP_STOFF = subprocess.run(["ipconfig"], encoding="UTF-8", capture_output=True)
        self.client_socket.sendall(IP_STOFF.stdout.encode())


if __name__ == '__main__':
    client = MClient(host=str(input("What host would you like? >")),
                     port=int(input("What port would you like? >")))
