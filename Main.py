import tkinter as tk
from Box import Box
from Functions import calculate, render_boxes, reset_boxes
from Datas import get_GE_boxes, get_PE_boxes, get_common_boxes, get_CS_boxes, get_CE_boxes
from Output import Output

win = tk.Tk()
win.title("Average Calculator")
win.geometry("630x690")

output = Output(win)

common_boxes = get_common_boxes(win)
CS_boxes = get_CS_boxes(win)
CE_boxes = get_CE_boxes(win)
GE_boxes = get_GE_boxes(win)
PE_boxes = get_PE_boxes(win) # should be completed
boxes : list[Box] = []

Calc_btn = tk.Button(master = win, text="Calculate", command = lambda : calculate(boxes, output))
Reset_btn = tk.Button(master = win, text="Reset", command = lambda : reset_boxes(boxes))

CS_btn = tk.Button(master = win, text = "CS", command = lambda : render_boxes(boxes, common_boxes, CS_boxes, Calc_btn, Reset_btn))
CE_btn = tk.Button(master = win, text = "CE", command = lambda : render_boxes(boxes, common_boxes, CE_boxes, Calc_btn, Reset_btn))
GE_btn = tk.Button(master = win, text = "GE", command = lambda : render_boxes(boxes, common_boxes, GE_boxes, Calc_btn, Reset_btn))
PE_btn = tk.Button(master = win, text = "PE", command = lambda : render_boxes(boxes, common_boxes, PE_boxes, Calc_btn, Reset_btn))

CS_btn.place(x = 10, y = 510)
CE_btn.place(x = 80, y = 510)
GE_btn.place(x = 150, y = 510)
#PE_btn.place(x = 220, y = 510) # should be completed

output.place(10, 610)

tk.mainloop()