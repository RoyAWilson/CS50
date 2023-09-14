'''
Simple read CSV file and sort by house with lambda

'''
students = []
student = {}
with open('Students.csv','r', encoding='utf-8') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {'name': name, 'house': house}
        students.append(student)
file.close()

# Grab the key with a lambda functin:

for student in sorted(students, key=lambda student: student['name']):
    print(f'{student["name"]} is in house {student["house"]}')
    