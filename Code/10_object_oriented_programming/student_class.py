'''

Introduction to OOP Student as a class

'''

class Student:
    '''
    
    Student Class
    
    '''

    def __init__(self, name, house):

        '''
        
        self to initialise the objects required
        
        '''
        if not name:
            raise ValueError('Missing name')
        if house not in [ 'Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw' ]:
            raise ValueError('Invalid house')
        self.name = name
        self.house = house

    # Really there should be a try:...except errortype at the end of this code to catch errors
    # before returning the Student to the caller.

def main():

    '''
    main function
    
    '''

    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    '''
    
    return a student
    
    '''

    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)

## Help - how can this class work, where is the .. = self...
## Why did the lecturer write an empty class?

if __name__ == '__main__':
    main()
