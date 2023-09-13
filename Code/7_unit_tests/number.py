'''
Main
'''

def main():
    '''
    To square a number
    
    '''
    
    x = int(input('What is x? '))
    print(square(x))
    
def square(x):
    '''
    return the square of the entered number
    '''
    return x ** 2
    
if __name__ == '__main__':
    main()
