students = int(input()) # inputing the number of students
students_grades = {} #dictionary

for st in range(students):
    name, grade_as_word = input().split() # two input values
    grade = float(grade_as_word) # setting the second value as a float number

    if name not in students_grades:
        students_grades[name] = [] # a list
    students_grades[name].append(grade) # adding grades to the list of students

for name, grades in students_grades.items():
    avg_grade = sum(grades) / len(grades) #summing all the grades and devide them by their number
    formatted_marks = f"{' '.join([f'{g:.2f}' for g in grades])}" #putting all the grades of a student on a single line and setting the grades to be printed with 2 numbers after the ","
    print(f"{name} -> {formatted_marks} (avg: {avg_grade:.2f})") # printing the resluts