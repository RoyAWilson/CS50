'''

Introduction to OOP

'''
def main():

    '''
    main function
    
    '''

    name = get_name()
    house = get_house()
    print(f'{name} from {house}')

def get_name():
    '''
    return he name
    
    '''
    return input('Name: ')

def get_house():
    '''
    
    return the house
    
    '''
    return input('House: ')


if __name__ == '__main__':
    main()
    