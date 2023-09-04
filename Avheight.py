students_heights = input(iii"Input a list of students heights: ").split()

for n in range(0, len(students_heights)):

    students_heights[n] = int(students_heights[n])

print(students_heights)


total_height = sum(students_heights)


# the len() function to get the number of 

number_of_students = len(students_heights)

average_height = round(total_height / number_of_students)

print("Average_height is: ", average_height)

