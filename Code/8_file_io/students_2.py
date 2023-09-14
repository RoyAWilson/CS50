'''
Simple read CSV file

'''
students = []
student = {}
with open('../../Data/Students.csv','r', encoding='utf-8') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {'name': name, 'house': house}
        students.append(student)
file.close()

# Define func to get name of student for sorting by key:

def get_name(student):
    '''
    func to get name for sorting purposes:
    '''
    return student['name']

for student in sorted(students, key=get_name):
    print(f'{student["name"]} is in house {student["house"]}')
    