import tkinter as tk
from tkinter import StringVar
from functions import Functions

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Menu")
        self.root.geometry("400x300")  # Set window size to 400x300 pixels
        self.lv_total = 0.00
        self.functions = Functions()  # Create an instance of Functions
        self.lv_oostock_mes = ''

        self.setup_ui()

    def setup_ui(self):
        self.create_labels()
        self.create_item_buttons()

    def create_labels(self):
        self.l_menu = tk.Label(self.root, text='Please click any item to buy.')
        self.l_menu.grid(row=0, column=0, columnspan=10)

        self.l_total = tk.Label(self.root, text='Bill')
        self.l_total.grid(row=1, column=5)

        # Create a StringVar to link label text to lv_total
        self.lv_total_str = StringVar()
        self.lv_total_str.set('$0.00')  # Set initial value

        self.l_total_display = tk.Label(self.root, textvariable=self.lv_total_str)
        self.l_total_display.grid(row=2, column=5)

        self.l_instruction = tk.Label(self.root, text='Left click to add item to the bill, right click to remove.')
        self.l_instruction.grid(row=3, column=0, columnspan=10)

        self.l_oostock = tk.Label(self.root, text=self.lv_oostock_mes)
        self.l_oostock.grid(row=4, column=0, columnspan=10)

    def create_item_buttons(self):
        self.b_apple = tk.Button(self.root, text='Apple', command=lambda: self.functions.bill('Apple', self))
        self.b_apple.grid(row=1, column=0)

        self.b_orange = tk.Button(self.root, text='Orange', command=lambda: self.functions.bill('Orange', self))
        self.b_orange.grid(row=1, column=1)

        self.b_banana = tk.Button(self.root, text='Banana', command=lambda: self.functions.bill('Banana', self))
        self.b_banana.grid(row=1, column=2)

        self.b_pear = tk.Button(self.root, text='Pear', command=lambda: self.functions.bill('Pear', self))
        self.b_pear.grid(row=1, column=3)

        self.b_kiwi = tk.Button(self.root, text='Kiwi', command=lambda: self.functions.bill('Kiwi', self))
        self.b_kiwi.grid(row=1, column=4)

        self.b_choco = tk.Button(self.root, text='Cake', command=lambda: self.functions.bill('Cake', self))
        self.b_choco.grid(row=2, column=0)

        self.b_wafer = tk.Button(self.root, text='Wafer', command=lambda: self.functions.bill('Wafer', self))
        self.b_wafer.grid(row=2, column=1)

        self.b_bicky = tk.Button(self.root, text='Bicky', command=lambda: self.functions.bill('Bicky', self))
        self.b_bicky.grid(row=2, column=2)

        self.b_choco = tk.Button(self.root, text='Choco', command=lambda: self.functions.bill('Choco', self))
        self.b_choco.grid(row=2, column=3)

        self.b_fudge = tk.Button(self.root, text='Fudge', command=lambda: self.functions.bill('Fudge', self))
        self.b_fudge.grid(row=2, column=4)

    def update_total_display(self):
        self.lv_total_str.set(f'${self.lv_total:.2f}')

    def update_oostock_message(self, message):
        self.lv_oostock_mes = message
        self.l_oostock.config(text=self.lv_oostock_mes)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
