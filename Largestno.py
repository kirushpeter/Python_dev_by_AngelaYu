students_heights = input("Input a list of students heights: ").split()

for n in range(0, len(students_heights)): 

    students_heights[n] = int(students_heights[n])

print(students_heights)