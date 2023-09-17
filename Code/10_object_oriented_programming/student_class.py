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

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house} patronus {self.patronus}'
    
    # getter for name:
    
    @property
    def name(self):
        '''
        Getter for name
        '''
        return self._name

    @name.setter
    def name(self, name):
        '''
        Setter for House
        '''
        if not name:
            raise ValueError('Missing Name')
        self._name = name

    # Getter
    @property
    def house(self):
        '''
        Getter for House
        '''
        return self._house

    @house.setter
    def house(self, house):
        '''
        Setter for House
        '''
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid House")
        self._house = house

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
    # Print statement to test that programmatically added incorrect information
    # not validated after the fact.
    
    # student.house = '4 The Street, The Town'
    print(student)


def get_student():
    '''
    
    return a student
    
    '''

    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name, house, patronus)


if __name__ == '__main__':
    main()
