'''

To read the names.txt file

'''

names = []
with open('Name.txt', 'r') as file:
    for line in sorted(file):
        names.append(line.rstrip())
for name in names:
    print(f'Hello, {name}')
