'''
Simple read CSV file and sort by home with lambda and file containing
gramatical commas.

'''

import csv

students = []
student = {}
with open('new_name.csv','r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for name, home in reader:
        student = {'name': name, 'home': home}
        students.append(student)
file.close()

# Grab the key with a lambda functin:

for student in sorted(students, key=lambda student: student['name']):
    print(f'{student["name"]}\'s home {student["home"]}')
    