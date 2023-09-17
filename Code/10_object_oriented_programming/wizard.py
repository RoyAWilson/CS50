'''
Superclass Wizard
'''

class Wizard:
    '''
    Wiazard class: Super
    
    '''

    def __init__(self, name):
        '''
        initialise super class
        
        '''
        if not name:
            raise ValueError('Missing Name')
        self.name = name
    ...

class Student(Wizard):
    '''
    Subclass to grab student details.  Inherits Wizard
    
    '''

    def __init__(self, name, house):
        '''
        initialise Student class with super()
        
        '''

        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    '''
    subclass to grabe detail of the Proffessor, inherits Wizard
    
    '''

    def __init__(self, name, subject):
        '''
        initialise subclass Professor
        '''

        super().__init__(name)
        self.name = name
        self.subject = subject
    ...

# Get a student's details:
student = Student('Harry', 'Griffindor')
# and a professor's details.
professor = Professor('Severus', 'Defense Against the Dark Arts')
# and the details of someone only known as a wizard with any other status being given.  It is not
# necessary to have a Wizard to have the other 2.
wizard = Wizard('Albus')
