import socket
import threading
import tkinter as tk

import texioty


class MServer(tk.Frame):
    def __init__(self, texioty_frame: texioty.TEXIOTY, master=None, host='', port=840):
        """
        Testing server possibilities and capabilities for connecting hundreds of clients together.
        Thorin has 4 quadrants of 70 clients.
        I am imagining to use 4 "chat room" style servers to connect to one main server.
        :param texioty_frame:
        :param master:
        :param host:
        :param port:
        """
        super().__init__(master=master)
        self.texioty = texioty_frame
        self.to = self.texioty.texoty
        self.ti = self.texioty.texity
        self.main_app = master

        self.connected_addresses_dict = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None
        self.to.priont_string(f"{host} is host and {port} is port.")
        self.running = False

    def start_simple_server(self, host='', port=840, max_clients=5):
        self.running = True
        self.server_socket.bind((host, port))
        self.server_socket.listen(max_clients)
        self.to.priont_string(f"{host} bound to {port} and listening.")

        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while self.running:
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"Got a connection from {self.client_address}.")
            self.connected_addresses_dict[self.client_socket] = self.client_address
            self.client_socket.sendall(f"Welcome, {self.client_address[0]} to homebase.".encode())
            self.main_app.connected_listbox.insert(tk.END, self.client_address)
            threading.Thread(target=self.receive_data, args=(self.client_socket,), daemon=True).start()
            threading.Thread(target=self.send_data, args=(self.client_socket,), daemon=True).start()

    def update_connection_dict(self):
        for device in self.connected_label_list:
            device.grid(column=3, row=len(self.connected_addresses_dict)-1)

    def send_data(self, client_socket):
        while self.running and self.client_socket:
            message = str(input("What you wanna say about that? _"))
            self.client_socket.sendall(message.encode())

    def receive_data(self, empty_arg):
        while self.running and self.client_socket:
            data = self.server_socket.recv(1024)
            if not data:
                break
            self.to.priont_string(f"{self.client_address}:" + data.decode())

    def stop_simple_server(self):
        self.running = False
        self.to.priont_string("No longer running.")
