import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Menu")
        self.root.geometry("400x300")  # Set window size to 400x300 pixels

        self.create_labels()

    def create_labels(self):
        self.l_menu = tk.Label(root, text='Please click any item to buy.')
        self.l_menu.grid(row=0, column=0, columnspan=10)

        self.create_item_buttons()

    def create_item_buttons(self):
        self.b_apple = tk.Button(root, text='Apple')
        self.b_apple.grid(row=1, column=0)

        self.b_orange = tk.Button(root, text='Orange')
        self.b_orange.grid(row=1, column=1)

        self.b_banana = tk.Button(root, text='Banana')
        self.b_banana.grid(row=1, column=2)

        self.b_pear = tk.Button(root, text='Pear')
        self.b_pear.grid(row=1, column=3)

        self.b_kiwi = tk.Button(root, text='Kiwi')
        self.b_kiwi.grid(row=1, column=4)

        self.b_choco = tk.Button(root, text='Choco')
        self.b_choco.grid(row=2, column=0)

        self.b_wafer = tk.Button(root, text='Wafer')
        self.b_wafer.grid(row=2, column=1)

        self.b_bicky = tk.Button(root, text='Bicky')
        self.b_bicky.grid(row=2, column=2)

        self.b_choco = tk.Button(root, text='Choco')
        self.b_choco.grid(row=2, column=3)

        self.b_fudge = tk.Button(root, text='Fudge')
        self.b_fudge.grid(row=2, column=4)




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
