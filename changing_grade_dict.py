student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


student_grades = {}
for key, value in student_scores.items():
    if value > 90:
        student_grades.update({
            key: 'Outstanding'
        })
    elif 80 < value < 91:
        student_grades[key] = 'Exceeds Expectations'
    elif 70 < value < 81:
        student_grades[key] = 'Acceptable'
    elif value <= 70:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)