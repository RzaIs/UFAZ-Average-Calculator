import tkinter as tk
from Grade import Grade
class Box:
    def __init__(self, win : tk.Tk, label_name : str, coeff : float) -> None:
        self.label = tk.Label(master = win, text = label_name)
        self.field = tk.Text(master = win, width = 8, height = 1)
        self.coeff = coeff

    def place(self, X : int, Y : int) -> None:
        self.label.place(x = X, y = Y)
        self.field.place(x = X + 200, y = Y)
    
    def calc(self) -> Grade:
        value : float
        try:
            value = float(self.field.get(1.0, "end-1c"))
        except:
            return None
        return Grade(value * self.coeff, self.coeff)