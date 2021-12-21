import tkinter as tk
from Box import Box

def get_common_boxes(win : tk.Tk):
    return [
        Box(win, "Math CC1(copybook)", 1),
        Box(win, "Math CC2(midterm)", 1.5),
        Box(win, "Math Final", 2.5),
        Box(win, "Electricity CC1", 0.5),
        Box(win, "Electricity final", 1.5),
        Box(win, "French CC1", 1.0),
        Box(win, "French CC2", 1.0),
        Box(win, "French Final", 1.0),
        Box(win, "Management CC1", 1.0),
        Box(win, "Management Final", 1.0)
    ]
def get_CS_boxes(win : tk.Tk):
    return [
        Box(win, "Signal P. CC1", 0.3),
        Box(win, "Signal P. CC2", 1.5),
        Box(win, "Signal P. Final", 1.2),
        Box(win, "System P. CC1", 1.0),
        Box(win, "System P. HW", 1.0),
        Box(win, "System P. Final", 1.0),
        Box(win, "Network CC1", 0.75),
        Box(win, "Network PWs", 0.75),
        Box(win, "Network Final", 1.5),
        Box(win, "Back-end PWs", 0.3),
        Box(win, "Back-end HW", 1.2),
        Box(win, "Back-end Final", 1.5)
    ]

def get_CE_boxes(win : tk.Tk):
    return [
        Box(win, "Chemical React CC1", 0.75),
        Box(win, "Chemical React CC2", 1.25),
        Box(win, "Chemical Thermo CC1", 0.75),
        Box(win, "Chemical Thermo CC2", 1.25),
        Box(win, "Exper chem PW", 1.0),
        Box(win, "Exper chem Report", 1.0),
        Box(win, "Distillation", 2.0),
        Box(win, "Operation on solids CC1", 2.0),
        Box(win, "Operation on solids CC2", 2.0),
        Box(win, "Back-end PWs", 0.3),
        Box(win, "Back-end HW", 1.2),
        Box(win, "Back-end Final", 1.5)
    ]
def get_GE_boxes(win : tk.Tk):
    return [
        Box(win, "Continuum Mechanics CC1", 3.0),
        Box(win, "Continuum Mechanics CC2", 3.0),
        Box(win, "Mineralogy", 2.0),
        Box(win, "Petrography", 2.0),
        Box(win, "Logging", 2.0),
        Box(win, "Py for Geo CC1", 0.75),
        Box(win, "Py for Geo CC2", 0.75),
        Box(win, "Py for Geo Project", 1.5)
    ]

def get_PE_boxes(win : tk.Tk):
    pass