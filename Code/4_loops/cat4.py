'''

Get input and ensure it is not a negative number with while loop
and introducing break and continue

'''

while True:
    n = int(input('What\'s n? '))
    if n > 0:
        break
print('Meow\n' * n, end = '')
