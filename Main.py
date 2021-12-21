from Box import Box
import tkinter as tk
from Functions import calculate
from Datas import get_common_boxes, get_CS_boxes, get_CE_boxes

win = tk.Tk()
win.title("Average Calculator")
win.geometry("800x800")

common_boxes = get_common_boxes(win)
CS_boxes = get_CS_boxes(win)
boxes = common_boxes + CS_boxes

for index, box in enumerate(common_boxes):
    box.place(10, 10 + index * 50)
for index, box in enumerate(CS_boxes):
    box.place(320, 10 + index * 50)

btn = tk.Button(master = win, text="calc", command = lambda : print(calculate(boxes)))

btn.place(x = 400, y = 10)

tk.mainloop()