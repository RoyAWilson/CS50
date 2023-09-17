'''

Introduction to OOP Student as a class pt 2 refine further

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

# Set up a class method to get the student information:
    @classmethod
    def get(cls):
        ''' get input of student information:
        '''
        name = input('Name: ')
        house = input('House: ')
        patronus = input('Patronus: ')
        return cls(name, house, patronus)

def main():

    '''
    main function
    
    '''

    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()
