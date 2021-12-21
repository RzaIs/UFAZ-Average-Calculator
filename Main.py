from Box import Box
import tkinter as tk
from Functions import calculate

win = tk.Tk()
win.title("Average Calculator")
win.geometry("800x800")

boxes = [
    Box(win, "French CC1", 1.0),
    Box(win, "Network CC1", 0.75),
    Box(win, "Math CC1", 1.5),
    Box(win, "System P. CC1", 1.0),
    Box(win, "Signal P. CC1", 0.3),
    Box(win, "Signal P. CC2", 1.5)
]

for index, box in enumerate(boxes):
    box.place(10, 10 + index * 50)

btn = tk.Button(master = win, text="calc", command = lambda : print(calculate(boxes)))

btn.place(x = 400, y = 10)

tk.mainloop()