from Box import Box
from Grade import Grade
from Box import Box
from tkinter import Button
from tkinter import Label
from Output import Output

def sum_coeffs(grades : list[Grade]) -> float:
    sum_of_coeffs = 0.0
    for grade in grades:
        sum_of_coeffs += grade.coeff
    return sum_of_coeffs

def sum_grades(grades : list[Grade]) -> float:
    sum_of_grades = 0.0
    for grade in  grades:
        sum_of_grades += grade.grade
    return sum_of_grades

def calculate(boxes : list[Box], output : Output) -> None:
    grades = []
    for box in boxes:
        grade = box.calc()
        grades.append(grade)
        if grade == None:
            output.write("please enter the grades correctly")
            return
    sum_of_coeffs : float = sum_coeffs(grades)
    sum_of_grades : float = sum_grades(grades)
    if sum_of_coeffs == 0:
        output.write("0\n0\n0")
    else:
        average : float = sum_of_grades / sum_of_coeffs
        total : float = sum_of_grades / 20
        output.write(f"Average: {round(average, 4)}\nTotal: {round(total, 4)}\nSum of coeffs: {round(sum_of_coeffs, 4)}\n")

def place_boxes(boxes : list[Box]) -> None:
    for index, box in enumerate(boxes):
        if index < 10:
            box.place(10, 50 + index * 50)
        else:
            box.place(420, 50 + index * 50 - 500)

def hide_and_clear_boxes(boxes : list[Box]) -> None:
    for box in boxes:
        box.hide()
    boxes.clear()

def render_boxes(boxes : list[Box], boxes1 : list[Box], boxes2 :list[Box], calc_btn : Button, rst_btn : Button) -> None:
    hide_and_clear_boxes(boxes)
    for box in (boxes1 + boxes2):
        boxes.append(box)
    place_boxes(boxes)
    calc_btn.place(x = 10, y = 610)
    rst_btn.place(x = 127, y = 610)

def reset_boxes(boxes : list[Box]) -> None:
    for box in boxes:
        box.clear()

def render_headers(headers : list[Label]) -> None:
    headers[0].place(x = 10, y = 10)
    headers[1].place(x = 210, y = 10)
    headers[2].place(x = 310, y = 10)

    headers[3].place(x = 420, y = 10)
    headers[4].place(x = 620, y = 10)
    headers[5].place(x = 720, y = 10)
