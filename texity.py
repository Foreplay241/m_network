from tkinter import *


class TEXITY(Entry):
    """
    Text input for Texioty.
    """
    def __init__(self, master=None):
        self.full_kommand_list = []
        self.kom_index = 0
        self.kommand_string_var = StringVar()
        self.isTestingKeys = False

        super(TEXITY, self).__init__(master=master, background='light green', width=69,
                                     textvariable=self.kommand_string_var)

        self.bind('<Up>', lambda e: self.kommand_list_previous())
        self.bind('<Down>', lambda e: self.kommand_list_next())

    def parse_input_kommand(self) -> list:
        """
        Returns a list of kommand arguments.
        :return: list
        """
        text_input = self.kommand_string_var.get()
        return text_input.split()

    def kommand_list_previous(self):
        if self.kommand_string_var.get() == '':
            self.kom_index = 0
        if self.kom_index <= len(self.full_kommand_list) - 1:
            self.kom_index += 1
            final_kom = clamp(len(self.full_kommand_list) - self.kom_index, 0, len(self.full_kommand_list) - 1)
            self.kommand_string_var.set(self.full_kommand_list[final_kom])
        self.icursor(END)

    def kommand_list_next(self):
        """Changes the input box to the next kommand in the list."""
        if self.kom_index >= 1:
            self.kom_index -= 1
            final_kom = clamp(len(self.full_kommand_list) - self.kom_index, 0, len(self.full_kommand_list) - 1)
            self.kommand_string_var.set(self.full_kommand_list[final_kom])
        if self.kom_index == 0:
            self.kommand_string_var.set('')
        self.icursor(END)


def clamp(n, minn, maxn) -> int:
    return max(min(maxn, n), minn)
