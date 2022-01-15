import tkinter as tk
from Grade import Grade
class Box:
    def __init__(self, win : tk.Tk, label_name : str, coeff : float) -> None:
        self.label = tk.Label(master = win, text = label_name)
        self.field = tk.Text(master = win, width = 8, height = 1)
        self.coeffField = tk.Text(master = win, width=8, height = 1)
        self.defaultCoeff = str(coeff)
        self.coeffField.insert(tk.END, self.defaultCoeff)

    def place(self, X : int, Y : int) -> None:
        self.label.place(x = X, y = Y)
        self.field.place(x = X + 200, y = Y)
        self.coeffField.place(x = X + 300, y = Y)

    def hide(self) -> None:
        self.label.place_forget()
        self.field.place_forget()
        self.coeffField.place_forget()

    def clear(self) -> None:
        self.field.delete("1.0", "end")
        self.coeffField.delete("1.0", "end")
        self.coeffField.insert(tk.END, self.defaultCoeff)
    
    def calc(self) -> Grade:
        value : float
        coeff : float
        try:
            value = float(self.field.get(1.0, "end-1c"))
            coeff = float(self.coeffField.get(1.0, "end-1c"))
        except:
            if self.field.get(1.0, "end-1c") == 'n':
                return Grade(0, 0)
            return None
        return Grade(value * coeff, coeff)