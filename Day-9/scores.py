scores = {
    "Meet": 100,
    "Vishal": 90,
    "Dharmik": 95,
    "Yash": 93,
    "Ujas": 70,
    "Bhumika": 75,
}

student_grades = {}

for i, j in scores.items():
    if (j > 90):
        student_grades[i] = "Outstanding"
    elif (j > 80):
        student_grades[i] = "Exceeds Exeptations"
    elif (j > 70):
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Kyu nai ho rahi padhai?"

print(student_grades)