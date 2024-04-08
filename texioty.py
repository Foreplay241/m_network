import json
import os
# from datetime import time, datetime
# from os.path import exists
from tkinter import *
# import requests

import texoty
import texity


class TEXIOTY(LabelFrame):
    def __init__(self, master=None):
        """
        Textual input from Texity.
        Textual output from Texoty.
        
        :param master:
        """
        super(TEXIOTY, self).__init__(master)
        self.configure(text=f'Texioty:')

        self.texo_w = 69
        self.texo_h = 26

        self.texoty = texoty.TEXOTY(self)
        self.texoty.grid(column=0, row=0, rowspan=1)
        self.texity = texity.TEXITY(self)
        self.texity.grid(column=0, row=1)

        self.texity.bind('<KP_Enter>', lambda e: self.process_kommand())
        self.texity.bind('<Return>', lambda e: self.process_kommand())

        self.isTestingKeys = False

        self.texity.focus_set()

        self.experimental_kommands_dict = {
            "echo": [self.perform_echo, "This will repeat whatever you typed."]
        }

        self.known_kommands_dict = {
            "tex8": [self.generate_texoty_masterpiece, "Generates a fun looking text image."]
        }

        self.gaym_kommands_dict = {
        }

    def perform_echo(self, eko_msg=""):
        self.texoty.priont_string(eko_msg)

    def generate_texoty_masterpiece(self, args):
        """
        Generate kre8dict entries for a texoty masterpiece.
        :param args:
        :return:
        """
        self.texoty.create_masterpiece(args)

    def clear_texoty(self):
        """Clear all the text from texoty."""
        self.texoty.delete("0.0", END)

    def process_kommand(self, event=None):
        """
        Process the kommand before executing it.
        :return:
        """
        # kommand_text = self.texity.kommand_string_var.get()
        parsed_kommand = self.texity.parse_input_kommand()
        print(parsed_kommand)
        kommand = parsed_kommand[0]
        arguments = parsed_kommand[1:]
        self.execute_kommand(kommand, arguments)
        self.texity.kommand_string_var.set("")

    def execute_kommand(self, kommand, arguments):
        """
        Execute the processed kommand.
        :param kommand: The command to be using.
        :param arguments: Arguments for the command to use.
        :return:
        """
        self.clear_texoty()
        if kommand in self.known_kommands_dict:
            self.known_kommands_dict[kommand][0](arguments)
        elif kommand in self.gaym_kommands_dict:
            self.gaym_kommands_dict[kommand][0](arguments)
        elif kommand in self.experimental_kommands_dict:
            self.texoty.priont_string("⦓⦙ I guess we can try this:")
            self.experimental_kommands_dict[kommand][0](*arguments)
        else:
            self.texoty.priont_string(f"⦓⦙ Uhh, I don't recognize '{kommand}'. Try one of these instead:")
        self.texity.full_kommand_list.append(self.texity.kommand_string_var.get())


def save_json(kre8dict: dict):
    """
    Saves the Meta dictionary as a JSON file in the folder of data_source.
    :return:
    """
    dumpDict = kre8dict
    with open(f'JSONs/{kre8dict["name"]}.json', 'w') as f:
        json.dump(dumpDict, f, indent=4)
