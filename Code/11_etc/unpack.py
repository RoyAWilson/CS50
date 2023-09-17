# input a name and split on space make title case. Not good code to actually write - too many assumptions
# cannot use .title() on this as it is returning a from the .split() however moving the .title before
# the .spit will work as expected.
first, laset = input('What\'s your name? ').title().split(' ')

print(f'Hello, {first}!')
