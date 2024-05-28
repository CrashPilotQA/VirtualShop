import tkinter as tk
from tkinter import StringVar
from functions import Functions

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Menu")
        self.root.geometry("400x300")  # Set window size to 400x300 pixels
        self.lv_total = 0.00

        self.create_labels()

    def create_labels(self):
        self.l_menu = tk.Label(root, text='Please click any item to buy.')
        self.l_menu.grid(row=0, column=0, columnspan=10)

        self.l_total = tk.Label(root, text='Bill')
        self.l_total.grid(row=1, column=5)

        # Create a StringVar to link label text to lv_total
        self.lv_total_str = StringVar()
        self.lv_total_str.set('$0.00')  # Set initial value

        self.l_total_display = tk.Label(root, textvariable=self.lv_total_str)
        self.l_total_display.grid(row=2, column=5)

        self.l_instruction = tk.Label(root, text='Left click to add item to the bill, right click to remove.')
        self.l_instruction.grid(row=3, column=0, columnspan=10)

        self.create_item_buttons()

    def create_item_buttons(self):
        self.b_apple = tk.Button(root, text='Apple', command=lambda: Functions.bill('Apple', self))
        self.b_apple.grid(row=1, column=0)

        self.b_orange = tk.Button(root, text='Orange', command=lambda: Functions.bill('Orange', self))
        self.b_orange.grid(row=1, column=1)

        self.b_banana = tk.Button(root, text='Banana', command=lambda: Functions.bill('Banana', self))
        self.b_banana.grid(row=1, column=2)

        self.b_pear = tk.Button(root, text='Pear', command=lambda: Functions.bill('Pear', self))
        self.b_pear.grid(row=1, column=3)

        self.b_kiwi = tk.Button(root, text='Kiwi', command=lambda: Functions.bill('Kiwi', self))
        self.b_kiwi.grid(row=1, column=4)

        self.b_choco = tk.Button(root, text='Cake', command=lambda: Functions.bill('Cake', self))
        self.b_choco.grid(row=2, column=0)

        self.b_wafer = tk.Button(root, text='Wafer', command=lambda: Functions.bill('Wafer', self))
        self.b_wafer.grid(row=2, column=1)

        self.b_bicky = tk.Button(root, text='Bicky', command=lambda: Functions.bill('Bicky', self))
        self.b_bicky.grid(row=2, column=2)

        self.b_choco = tk.Button(root, text='Choco', command=lambda: Functions.bill('Choco', self))
        self.b_choco.grid(row=2, column=3)

        self.b_fudge = tk.Button(root, text='Fudge', command=lambda: Functions.bill('Fudge', self))
        self.b_fudge.grid(row=2, column=4)

    def update_total_display(self):
        self.lv_total_str.set(f'${self.lv_total:.2f}')






if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
