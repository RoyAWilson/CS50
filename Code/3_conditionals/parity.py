'''
    
    Determine if number is odd or even
    
    '''

def main():
    '''
    
    Determine if number is odd or even
    
    '''
    x = int(input('What\'s x? '))
    if iseven(x):
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
def iseven(n):
    '''

    calculate if x is even or odd

    '''
    return n % 2

main()
