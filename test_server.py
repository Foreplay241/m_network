import socket
import threading
import tkinter as tk


class MServer(tk.Frame):
    def __init__(self, master=None, host='', port=840):
        super().__init__(master=master)
        self.server_status_str_var = tk.StringVar(value='okaynow')
        self.server_status_label = tk.Label(self, textvariable=self.server_status_str_var)
        self.server_status_label.grid(column=0, row=0)
        self.start_server_btn = tk.Button(text="Start Server", command=self.start_simple_server)
        self.start_server_btn.grid(column=1, row=1)

        self.connected_addresses_dict = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None
        self.server_status_str_var.set(f"{host} is host and {port} is port.")

    def start_simple_server(self, host='', port=840, max_clients=5):
        self.server_socket.bind((host, port))
        self.server_socket.listen(max_clients)
        self.server_status_str_var.set(f"{host} bound to {port} and listening.")
        print(f"{host} bound to {port} and listening.")

        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while True:
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"Got a connection from {self.client_address}.")
            self.connected_addresses_dict[self.client_socket] = self.client_address
            self.client_socket.sendall(f"Welcome, {self.client_address[0]} to homebase.".encode())
            connection_label = tk.Label(text=f"{self.client_address} is connected.")
            connection_label.grid(column=1, row=len(self.connected_addresses_dict))

            threading.Thread(target=self.receive_data, args=(self.client_socket,), daemon=True).start()
            threading.Thread(target=self.send_data, args=(self.client_socket,), daemon=True).start()

    def send_data(self, empty_arg):
        while True and self.client_socket:
            message = str(input("What you wanna say about that? _"))
            self.client_socket.sendall(message.encode())

    def receive_data(self, empty_arg):
        while True and self.client_socket:
            data = self.server_socket.recv(1024)
            if not data:
                break
            print(f"{self.client_address}:" + data.decode())

