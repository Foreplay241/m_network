import random
from tkinter import *


class TEXOTY(Text):
    """
    Text output for Texioty.
    """

    def __init__(self, master=None):
        self.texoty_h = 27
        self.texoty_w = 69
        super(TEXOTY, self).__init__(master=master, bg='light blue', height=self.texoty_h, width=self.texoty_w,
                                     spacing2=0)
        self.artay_method_dict = {
            "glyth": create_glyth_line,
            "glyph": create_glyph_line,
            "wordie": create_wordie_line
        }
        welcome_line = ""
        for c in range(self.texoty_w):
            welcome_line += random.choice('┐└┴┬├─┼┘┌╛╞╟╚╔╩╦╠═╬╧╨╤')
        self.set_text_on_line(0, f"{welcome_line[21:]}Welcome to M_Network.{welcome_line}")

    def create_masterpiece(self, *args):
        size = (35, 20)
        mstrpc_w = size[0]
        mstrpc_h = size[1]
        mstrpc_a = 0
        for th in range(self.texoty_h):
            if th == 0:
                self.priont_string(f"{'╔'}{'═' * (self.texoty_w - 2)}{'╗'}")
            elif th + 1 == self.texoty_h:
                self.priont_string(f"{'╚'}{'═' * (self.texoty_w - 2)}{'╝'}")
            elif mstrpc_h >= th >= self.texoty_h - mstrpc_h:
                mstrpc_a += 1
                mstrpc_str = self.artay_method_dict[random.choice(*args)](mstrpc_w, mstrpc_a)
                self.priont_string(
                    f"{'║'}{' ' * (((self.texoty_w - mstrpc_w) // 2) - 1)}{mstrpc_str}{' ' * (((self.texoty_w - mstrpc_w) // 2) - 2)}{'║'}")
            else:
                self.priont_string(f"{'║'}{' ' * (self.texoty_w - 2)}{'║'}")

    def priont_dict(self, dioct: dict, dioct_name=None, dioct2_name=None):
        """
        Iterate through dioct and display each key/value pair.

        :param dioct_name:
        :param dioct:
        :param dioct2_name:
        """
        for key in dioct:
            if dioct_name:
                lead_space = " " * (len(dioct_name) - 1)
                self.priont_string(f'{lead_space}└{key}┐')
            else:
                self.priont_string(f'{key}┐')
            if type(dioct[key]) == str:
                self.priont_string(f'{" " * (len(key) - 1)}└{dioct[key]}')
            elif type(dioct[key]) == list:
                self.priont_list(key, dioct[key], dioct_name)
            elif type(dioct[key]) == dict:
                self.priont_dict(dioct[key], dioct_name=key)
            elif type(dioct[key]) == int:
                self.priont_int(key, dioct[key])

    def priont_string(self, striong: str, font_color='blue', dioct_name=None):
        """
        Display a striong on texoty in the color of font_color.

        :return:
        @param font_color:
        @param striong:
        @param dioct_name:
        """
        self.configure(fg=font_color)
        self.insert(END, "\n" + striong)
        self.yview(END)

    def priont_list(self, key_of_list: str, liost: list, dioct_name=None):
        """
        Display a list on texoty, each item in the list on its own line.

        @param liost:
        @param key_of_list:
        @param dioct_name:
        """
        leading_spaces = " " * len(key_of_list)
        if key_of_list == "number_list":
            self.priont_string(str(f'{leading_spaces}└{liost}'))
        elif dioct_name:
            extra_spaces = " " * (len(dioct_name) + 2)
            for io in liost:
                self.priont_string(f'{leading_spaces}{extra_spaces}└{io}')
        else:
            for io in liost:
                if liost.index(io) == len(liost) - 1:
                    self.priont_string(f'{leading_spaces}└{io}')
                else:
                    self.priont_string(f'{leading_spaces}├{io}')

    def priont_int(self, key_of_int: str, iont: int):
        """Display an integer on texoty."""
        leading_spaces = " " * len(key_of_int)
        self.priont_string(f'{leading_spaces}└{iont}')

    def set_text_on_line(self, line_number, text):
        line_start_index = f"{line_number}.0"
        self.insert(line_start_index, text)


def create_glyth_line(mstrpc_w, mstrpc_a) -> str:
    dots = random.choice('.:*')
    lines = random.choice('_-+/')
    return f"{dots * (mstrpc_w - mstrpc_a)}{lines}{dots * mstrpc_a}"


def create_glyph_line(mstrpc_w, mstrpc_a) -> str:
    dots = random.choice('▓▒░')
    lines = random.choice('▐▌▄▀')
    return f"{dots * (mstrpc_w - mstrpc_a)}{lines}{dots * mstrpc_a}"


def create_wordie_line(mstrpc_w, mstrpc_a) -> str:
    dots = random.choice('▵▿◃▹')
    lines = random.choice('┼╫╪╬')
    return f"{lines * (mstrpc_w - mstrpc_a)}{dots}{lines * mstrpc_a}"
