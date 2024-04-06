import json
import sqlite3


class Manager:
    def __init__(self):
        """Class for managing the miners database."""
        self.list_of_owners = ["DW11", "DK8", "BPK4", "CK7"]
        self.master_miner_dict = {
            "Master": {}
        }
        self.running = True
        self.commands_dict = {
            "add": [self.prompt_new_miner, "Add a new miner."],
            "remove": [self.prompt_remove_miner, "Remove a miner."],
            "show": [self.show_miner_dict, "Show all of the miners."],
            "exit": [self.end_command_prompt, "Exit the command prompt."],
            "help": [self.print_available_commands, "Show this help message."]
        }
        self.start_command_prompt()

    def add_new_miner_master_dict(self, miner_owner: str, miner_name: str, miner_model: str, miner_hashrate: int):
        """
        Adds a new miner to the master dictionary.
        :param miner_owner: Name of owner of the new miner.
        :param miner_name: Username of the new miner.
        :param miner_model: Model of the new miner.
        :param miner_hashrate: Hashrate of the new miner.
        :return:
        """
        if miner_owner not in self.master_miner_dict:
            self.master_miner_dict[miner_owner] = {"Miner Model": miner_model,
                                                   "Miner Hashrate": miner_hashrate,
                                                   "Status": "Up/Down",
                                                   "IP": "10.69.4.20"}
        elif miner_name != "Master":
            self.master_miner_dict[miner_owner][miner_name] = {"Miner Model": miner_model,
                                                               "Miner Hashrate": miner_hashrate,
                                                               "Status": "Up/Down",
                                                               "IP": "10.69.4.20"}
        self.master_miner_dict["Master"][miner_name] = {"Miner Model": miner_model,
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
        """
        Prompt the user to add a new miner.
        :return:
        """
        new_owner = str(input("Who will own this miner?  >"))
        new_name = str(input("What is the miners name?  >"))
        new_model = str(input("What model is this miner?  >"))
        new_hashrate = int(input("What hashrate does the miner have?  >"))
        self.add_new_miner_master_dict(new_owner, new_name, new_model, new_hashrate)

    # def show_master_dict(self, owner="Master"):
    #     """
    #     Show the master dictionary of all miners added.
    #     :return:
    #     """
    #     for entry in self.master_miner_dict[owner]:
    #         print(f'{entry}╟→ {self.master_miner_dict[owner][entry]}')

    def show_miner_dict(self):
        """
        Show the master dictionary of all miners added.
        :return:
        """
        owner = str(input("Which owner would you like to see?  >"))
        print(owner + "╖")
        for i, entry in enumerate(self.master_miner_dict[owner]):
            if i < len(self.master_miner_dict[owner])-1:
                print(f'{" "*len(owner)}╟→ {self.master_miner_dict[owner][entry]}')
            elif i == len(self.master_miner_dict[owner].keys())-1:
                print(f'{" "*len(owner)}╙→ {self.master_miner_dict[owner][entry]}')

    def show_owner_dict(self, owner: str):
        """
        Show a specified owners dictionary of miners.
        :param owner:
        :return:
        """
        pass

    def start_command_prompt(self):
        while self.running:
            command = str(input("Wutdo?  >"))
            if command in self.commands_dict:
                self.commands_dict[command][0]()
            else:
                print("The fuck did you just say?..")

    def prompt_remove_miner(self):
        pass

    def end_command_prompt(self):
        print("Goodbye!")
        self.running = False

    def print_available_commands(self):
        for cmnd in self.commands_dict:
            print(f'{cmnd}{" " * (12 - len(cmnd)) + "-"}{self.commands_dict[cmnd][1]}')
