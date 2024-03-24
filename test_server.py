import socket
import sys


class MServer:
    def __init__(self, host='', port=840):
        self.connected_addresses_dict = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start_simple_server(host, port)
        self.client_socket = None
        self.client_address = None
        running = True
        while running:
            self.receive_connection()
            print(self.receive_data())

    def start_simple_server(self, host='', port=840, max_clients=5):
        self.server_socket.bind((host, port))
        print(f"server_socket bound to {port}.")
        self.server_socket.listen(max_clients)
        print("server_socket is listening.")

    def receive_connection(self, single_connection=False):
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Got a connection from {self.client_address}.")
        self.connected_addresses_dict[self.client_socket] = self.client_address
        self.send_greeting()

    def send_greeting(self):
        self.send_data("Welcome! Welcome, to the server of Foreplay!")

    def send_data(self, data):
        self.client_socket.sendall(data.encode())

    def receive_data(self):
        return self.client_socket.recv(1024).decode()
