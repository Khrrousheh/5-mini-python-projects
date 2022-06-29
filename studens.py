import random

def alphaMarks(n: float)->str:
    if n< 60.0:
        return 'f'
    else:
        if n<70.0:
            return 'e'
        else:
            if n<80.0:
                return 'c'
            else:
                if n<90.0:
                    return 'b'
                else:
                    return 'a' 

names = ['ahmad', 'rami', 'mohammad', 'sami', 'malik']
students = {}


myavg = 0
for i in names:
    marks = []
    for _ in range(5):
        mark = random.randrange(60,101)
        marks.append(mark)
        myavg += mark
    students[i] = marks

myavg /= (len(names)*5)
del names


students_evaluate = {}

for name, marks in students.items():
    grade = alphaMarks(sum(marks)/len(marks))
    students_evaluate[name] = grade
    print(f"student: {name} marks_list: {marks} overall_grade: {grade}")

