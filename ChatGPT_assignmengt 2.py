import numpy as np

student = []

for i in range(5):
    name = input("Enter the student's name: " )
    grade = int(input("Enter student's grade: "))
    student.append({"name":name, "grade":grade})

# seperating the students

for index, student in enumerate(student , start = 1):
    print(f" student {index} : Name ={student['name']}  , grade = {student['grade']}")
    total = 0
    total += student['grade']
    average = total / len(student)

print(f' the average of the 5 students = {average}')

    







