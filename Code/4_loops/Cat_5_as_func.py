'''

Meow input number of times as a function

'''


def main():
    '''
    get the print out
    
    '''
    number = get_number()
    meow(number)
    
def get_number():
    
    '''
    
    Grab user input
    
    '''
    while True:
        n = int(input('What\'s n? '))
        if n >0:
            return n

def meow(n):
    '''
    
    function to get user input
    
    '''
    for _ in range(n):
        print('Meow')

main()
