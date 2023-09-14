'''

Write to CSV file with DictWriter

'''

import csv

name = input('Enter you name: ')
home = input('Enter your home: ')

with open('../../Data/names_dictwriter.csv', 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name, 'home': home})
file.close()
