from test_server import MServer
from test_client import MClient
from minerMan import Manager
import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import threading
import texioty
import subprocess


def start_simple_client():
    client_script_path = "./test_client.py"
    threading.Thread(target=subprocess.run, args=(["python3", client_script_path], )).start()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.texioty_frame = texioty.TEXIOTY()
        self.texioty_frame.grid(column=0, row=0, columnspan=3)
        self.the_server = MServer(master=self, texioty_frame=self.texioty_frame)
        self.the_server.grid(column=0, row=0)
        self.start_server_btn = tk.Button(text="Start Server", command=self.the_server.start_simple_server)
        self.stop_server_btn = tk.Button(text="Stop Server", command=self.the_server.stop_simple_server)
        self.start_client_btn = tk.Button(text="Start Client", command=start_simple_client)
        self.start_server_btn.grid(column=0, row=1)
        self.stop_server_btn.grid(column=1, row=1)
        self.start_client_btn.grid(column=2, row=1)

        self.connected_listbox = tk.Listbox(selectmode=tk.MULTIPLE)
        self.connected_listbox.grid(column=5, row=0)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Please be working.....')
    root.geometry('840x500')
    root.configure(background='#0f6faa')
    app = Application(root)
    app.mainloop()
