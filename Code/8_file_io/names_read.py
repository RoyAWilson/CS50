'''

To read the names.txt file

'''

with open('Name.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    print('Hello ,', line.rstrip())
