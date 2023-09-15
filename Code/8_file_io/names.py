'''

Basics of file io to save a few names in a text file

'''

name = input('What\'s your name? ')
with open('../../Data/Name.txt','a', encoding='utf-8') as file:
    file.write(f'{name}\n')
file.close()
