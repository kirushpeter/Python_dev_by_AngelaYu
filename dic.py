

programming_dictionary = {

    "bug":"a new bug is detected in system one",

    "Functions": "functions are breaking the program",

    "Loop" : "Doing something over and over",

}


# print(programming_dictionary["Functions"])


# adding a new entry.

#programming_dictionary["new_loop"] = "THe new loop is here"


print(programming_dictionary)


student_scores = {

    "harry" : 84,
    "john" : 94,
    "potter" : 47,
}

for students in student_scores:
    score = student_scores[students]

    if score > 90:

        student_grades[students] = "Outstanding"