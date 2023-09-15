'''

To reformat data input to expected format

'''

import re

# input user name and format it to first name last name:

name = input('What\'s your name? ').title().strip()
# input name and strip off extra spaces from front back

# Dealer with user name input as last, first and turn to first last space with if statement

# if ',' in name:
#     last, first = name.split(', ')
#     name = f'{first} {last}'
# print(name)

# Now to do something like the same with regex
# run re.search() on the string and assign to a variable

# matches = re.search(r'^(.+), (.+)$', name)
# if matches:
#     last, first = matches.groups()
#     name = f'{first} {last}'
# print(f'Hello, {name}')

# Spit the groups explicitly and recombine.  Can see this being useful to split names to first
# and last for saving to a data file with first and last name headings.

# matches = re.search(r'^(.+), (.+)$', name)
# if matches:
#     last = matches.group(1)
#     first = mateches.group(2)
#     name = f'{first} {last}'
# print(f'Hello, {name}')

# To tighten the code even further the following is also possible adding of the star after 
# the comma allows for more than 1 white space:

# matches = re.search(r'^(.+), *(.+)$', name)
# if matches:
#     name = f'{matches.group(2)} {matches.group(1)}'
# print(f'Hello, {name}')

# You can further tighten the code by putting the if statement in front of the regex and using the 'walrus' 
# operator := :

# To tighten the code even further the following is also possible adding of the star after 
# the comma allows for more than 1 white space:

if matches:= re.search(r'^(.+), *(.+)$', name):
    name = f'{matches.group(2)} {matches.group(1)}'
print(f'Hello, {name}')
