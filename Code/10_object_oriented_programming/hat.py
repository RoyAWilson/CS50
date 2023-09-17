'''

implement a class to sort students into houses using a hat

'''

import random

class Hat:
    
    '''
    to return a house for any student
    
    '''
    
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    # set up list of houses as a class variable.
    
    @classmethod
    def sort(cls, name):
        
        # set house as a classmethod to a random selection from houses and pass it to the print function
        
        print(name, 'Is in', random.choice(cls.houses))

# Call Hat.sort NB the capital H!

Hat.sort('Harry')
