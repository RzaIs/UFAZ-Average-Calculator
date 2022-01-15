import tkinter as tk
class Output:
    def __init__(self,  win : tk.Tk) -> None:
        self.field = tk.Text(master = win, width = 33, height = 3)

    def place(self, X : int, Y : int) -> None:
        self.field.place(x = X, y = Y)

    def write(self, text : str) -> None:
        self.field.delete("1.0", "end")
        self.field.insert("1.0", text)