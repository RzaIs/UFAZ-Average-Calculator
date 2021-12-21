from Box import Box
from Grade import Grade
from Box import Box

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

def calculate(boxes : list[Box]) -> float:
    grades = []
    for box in boxes:
        grade = box.calc()
        grades.append(grade)
        if grade == None:
            return None
    return sum_grades(grades) / sum_coeffs(grades)
