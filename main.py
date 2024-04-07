from test_server import MServer
from test_client import MClient
from minerMan import Manager
import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import threading


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.the_server = None
        self.start_server_btn = tk.Button(text="New Server", command=self.new_server)
        self.start_server_btn.grid(column=0, row=1)

    def new_server(self):
        the_server = MServer(self)
        self.the_server = the_server
        self.the_server.grid(column=0, row=0)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Please be working.....')
    root.geometry('840x420')
    root.configure(background='#0f6faa')
    app = Application(root)
    app.mainloop()
