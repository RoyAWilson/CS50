'''

Attempt to make function to assign houses

'''

def main():
    '''
    
    main func
    
    '''

    name = input('What\'s your name? ').title()
    print(house(name))
def house(x):
    
    '''
    
    Func to return house name
    
    '''
    match x:
        case 'Harry' | 'Hermione' | 'Ron':
            return 'Gryffindor'
        case 'Draco':
            return 'Slytherin'
        case _:
            return 'Who?'
main()
