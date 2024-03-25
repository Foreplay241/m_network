import socket
import threading


class MServer:
    def __init__(self, host='', port=840):
        self.connected_addresses_dict = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start_simple_server(host, port)
        self.client_socket = None
        self.client_address = None

        recv_thread = threading.Thread(target=self.receive_data, args=())
        send_thread = threading.Thread(target=self.send_data, args=())
        connection_thread = threading.Thread(target=self.receive_connection, args=(False, ))
        recv_thread.start()
        send_thread.start()
        connection_thread.start()
        recv_thread.join()
        send_thread.join()
        connection_thread.join()

    def start_simple_server(self, host='', port=840, max_clients=5):
        self.server_socket.bind((host, port))
        print(f"server_socket bound to {port}.")
        self.server_socket.listen(max_clients)
        print("server_socket is listening.")

    def receive_connection(self, single_connection=False):
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Got a connection from {self.client_address}.")
        self.connected_addresses_dict[self.client_socket] = self.client_address

    def send_data(self):
        while True:
            message = str(input("What you wanna say about that? _"))
            self.client_socket.sendall(message.encode())

    def receive_data(self):
        while True:
            data = self.server_socket.recv(1024)
            if not data:
                break
            print(f"{self.client_address}:" + data.decode())

