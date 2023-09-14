'''
Simple read CSV file and sort by home with lambda and file containing
gramatical commas and now headers too using a dictionary.

'''

import csv

students = []
student = {}
with open('../../Data/names_headers.csv','r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name': row['name'], 'home': row['home']})
file.close()

# Grab the key with a lambda functin:

for student in sorted(students, key=lambda student: student['name']):
    print(f'{student["name"]}\'s home {student["home"]}')
    