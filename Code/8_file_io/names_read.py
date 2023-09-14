'''

To read the names.txt file

'''

with open('Name.txt', 'r') as file:
    for line in file:
        print('Hello, ', line.rstrip())
