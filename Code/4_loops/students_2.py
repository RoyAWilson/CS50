'''

dictionary to assign students to houses by key/value pairs

'''

# Intro to dicts and iterating over dictionaries

houses = {'Gryffindor':['Hermione','Harry','Ron'],
          'Slytherin':{'Draco'}}
students =  {'Hermione': 'Gryffindor','Harry': 'Gryffindor',
             'Ron': 'Gryffindor', 'Draco': 'Sltherin'}
# print(students['Hermione'])
for student in students:
    print(student, students[student], sep = ', ')

# add more info about the students my guess a dictionary of dictionaries:

student_info = {'Hermione':{'house':'Gryffindor', 'patronus':'Otter'},
                'Harry':{'house': ' Gryffindor', 'patronus': 'Stag'},
                'Ron':{'house': 'Gryffindor', 'patronus': 'Jack Russell Terrier'},
                'Draco': {'House':'Slytherin', 'patronus':'Unknown'}}
print(student_info)

# Lecturer's take a list of dictionaries see also students_3
student_list_info = [
    {'name': 'Hermione', 'House': 'Gryffindor', 'patronus':'Otter'},
    {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'Stag'},
    {'name': 'Ron', 'house':'Gryffindor', 'patronus': 'Jack Russell Terrier'},
    {'name': 'Draco', 'house':'Slytherin', 'patronus': None}
]
print(student_list_info)
