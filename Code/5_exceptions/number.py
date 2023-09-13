
'''

basic error handling

'''

# using try.  Will also catch entering float here.
while True:
    try:
        x = int(input('What\'s x? '))
    except ValueError:
        print('Please only type an integer')
    else:
        break
print(f'x is {x}')

    ## This code needs to be indented after and Else statement as any other way of doing it
    ## throws a name error as input never passes value to int() and thus never
    #  passes the value if it is not an integer to x, the try
    # statement interupts the flow before the value is passed as it is an incorrect type.
    # Adding the while loop with loop until user enters a correct input.
    # Would prefer to have a counter so the loop eventually either gives more explicit instructions
    # or leaves the program with a failure message.