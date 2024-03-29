import json
import sqlite3


class Manager:
    def __init__(self):
        """Class for managing the miners database."""
        self.list_of_owners = ["DW11", "DK8", "BPK4", "CK7"]
        self.master_miner_dict = {}
        self.commands_dict = {
            "add": self.prompt_new_miner,
            "remove": self.prompt_remove_miner,
            "show": self.show_master_dict
        }
        self.running = True
        self.start_command_prompt()

    def add_new_miner_master_dict(self, miner_owner: str, miner_name: str, miner_model: str, miner_hashrate: int):
        """
        Adds a new miner to the master dictionary.
        :param miner_owner:
        :param miner_name:
        :param miner_model:
        :param miner_hashrate:
        :return:
        """
        if miner_owner not in self.master_miner_dict:
            self.master_miner_dict[miner_owner] = {}
        else:
            self.master_miner_dict[miner_owner][miner_name] = {"Miner Model": miner_model,
                                                               "Miner Hashrate": miner_hashrate,
                                                               "Status": "Up/Down",
                                                               "IP": "10.69.4.20"}

    def delete_miner_master_dict(self):
        """
        Deletes a miner from the master dictionary.
        :return:
        """
        pass

    def prompt_new_miner(self):
        new_owner = str(input("Who will own this miner?  >"))
        new_name = str(input("What is the miners name?  >"))
        new_model = str(input("What model is this miner?  >"))
        new_hashrate = int(input("What hashrate does the miner have?  >"))
        self.add_new_miner_master_dict(new_owner, new_name, new_model, new_hashrate)

    def show_master_dict(self):
        for entry in self.master_miner_dict["Trevor"]:
            print(f'{entry}╟→ {self.master_miner_dict["Trevor"][entry]}')

    def start_command_prompt(self):
        while self.running:
            command = str(input("Wutdo?  >"))
            if command in self.commands_dict:
                self.commands_dict[command]()
            else:
                print("The fuck did you just say?..")

    def prompt_remove_miner(self):
        pass

