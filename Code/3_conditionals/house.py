'''

using match

'''

name = input('What\'s your name? ').title()

if name == 'Harry' or name == 'Hermione' or name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who?')
