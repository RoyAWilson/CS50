'''

Introduction to OOP

'''
def main():

    '''
    main function
    
    '''

    student = get_student()
    print(f'{student[0]} from {student[1]}')

def get_student():
    '''
    
    return a student
    
    '''
    name = input('Name: ').strip().title()
    house = input('House: ').strip().title()
    return name, house
# I think I would prefer to return a dictionary as easier to write to a database
# and is mutable rather than unmutable

if __name__ == '__main__':
    main()
    