Student_scores = {

    "kamau":97,
    "john":90,
    "susan":97,
    "Francis":97,
}
'''
print(marks_report["kamau"])

marks_report['Festus'] = 100

print(marks_report)

for marks in marks_report:

    score = marks_report[marks]

    if score == 97:

        print(marks)
'''

# Create an empty dictionsry called students grades

student_grades = {}


# Write code below to add grades to the students grades

for student in Student_scores:

    score = Student_scores[student]

    if score > 90:

        student_grades[student] = 'Outstanding'

    elif score > 80:

        student_grades[student] = 'Exceeds expectation'

    elif score > 70:

        student_grades[student] = 'Acceptable'

    else:

        student_grades[student] = 'pass'

    
print(student_grades)