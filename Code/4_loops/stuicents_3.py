student_list_info = [
    {'name': 'Hermione', 'house': 'Gryffindor', 'patronus':'Otter'},
    {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'Stag'},
    {'name': 'Ron', 'house':'Gryffindor', 'patronus': 'Jack Russell Terrier'},
    {'name': 'Draco', 'house':'Slytherin', 'patronus': None}
]
for student in student_list_info:
    print(student['name'], student['house'], student['patronus'], sep = ', ')
