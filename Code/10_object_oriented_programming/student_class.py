'''

Introduction to OOP Student as a class

'''

class Student:
    '''
    
    Student Class
    
    '''

    def __init__(self, name, house, patronus):

        '''
        
        self to initialise the objects required
        
        '''
        if not name:
            raise ValueError('Missing name')
        if house not in [ 'Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw' ]:
            raise ValueError('Invalid house')
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house} patronus {self.patronus}'
    
    def charm(self):
        '''
        Return an emoji of the patronus or a wand in the case of none'''
        
        match self.patronus:
            case 'Stag':
                return '🦌'
            case 'Otter':
                return '🦦'
            case 'Jack Russell Terrier':
                return '🐕'
            case _:
                return '🪄'

    # Really there should be a try:...except errortype at the end of this code to catch errors
    # before returning the Student to the caller.

def main():

    '''
    main function
    
    '''

    student = get_student()
    print(student)
    print(f'Expecto Patronum {student.charm()}')

def get_student():
    '''
    
    return a student
    
    '''

    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name, house, patronus)

## Help - how can this class work, where is the .. = self...
## Why did the lecturer write an empty class?

if __name__ == '__main__':
    main()
