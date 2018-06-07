import sys

students = []

for _ in range(int(raw_input())):
    student = []
    name = raw_input()
    score = float(raw_input())
    student.extend([name, score])
    students.append(student);

sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
second_lowest_grade = None

# start iteration from the second element
for student in sorted_students:
    if second_lowest_grade is None and student[1] > sorted_students[0][1]:
        second_lowest_grade = student[1]

    if second_lowest_grade is not None and student[1] == second_lowest_grade:
        print(student[0])
