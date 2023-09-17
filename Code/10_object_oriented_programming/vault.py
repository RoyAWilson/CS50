'''
Intro to Operator Overloading
'''

class Vault:
    '''
    To represent a bank vault
    '''
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        ## Trust the operator to enter values that are ok to concentrate solely on the new stuff

    ## Define at __str__ method:
    
    def __str__(self):
        return f'Galleons {self.galleons}, Sickles {self.sickles}, knuts {self.knuts}'

    ## Define a function to add the contents of 2 vaults together:
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
total = potter + weasley
print(potter)
print(weasley)
print(total)
