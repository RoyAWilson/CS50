'''

To read the names.txt file

'''

names = []
with open('Name.txt', 'r') as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f'Hello, {name}')

