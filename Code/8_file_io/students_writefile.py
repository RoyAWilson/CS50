'''
# Simple write CSV file and sort by home with lambda and file containing
# gramatical commas and now headers too using a dictionary.

# '''
import csv

name, home = input('What is your name? '), input('What is your home? ')

with open('names_writer.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

file.close()
## Had to add the newline = '' to the open statement as otherwise writer was adding an
## extraneous row after every write.