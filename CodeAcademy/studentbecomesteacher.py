"""Going through CodeAcademy for practice.  I'm quickly doing the exercises and then writing everything by 
hand and talking through it to give myself whiteboarding practice.  Pushing to Git because I want to be 
disciplined in continuing to push code and work on it even if I'm not working at on a project right now""" 

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!

students = [lloyd, alice, tyler]

def average(lst):
    return float(sum(lst))/len(lst)

def get_average(student):
    return average(student["homework"]) * 0.1 + average(student["quizzes"]) * 0.3 + average(student["tests"]) * 0.6
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
    group = []
    for i in class_list:
        group.append(get_average(i))
    return average(group)

print get_class_average(students)

print get_letter_grade(get_class_average(students))

