def process_student(student_data):
    grade = student_data.get('grade')
    return grade

def average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

class1 = [
    {'name': 'Alice', 'grade': 0},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 250.01},
    {'name': 'Jane', 'grade': 100},
]

def collect_grades(students):
    grades = []
    for student in students:
        grade = process_student(student)
        if isinstance(grade, (int, float)):
            if 0 <= grade < 200:
                grades.append(grade)

    return grades


grades1 = collect_grades(class1)
print(average_grade(grades1))