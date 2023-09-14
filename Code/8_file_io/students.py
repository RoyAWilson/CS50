'''
Simple read CSV file

'''

with open('../../Data/Students.csv','r', encoding='utf-8') as file:
    for line in file:
        row = line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')
file.close()
 