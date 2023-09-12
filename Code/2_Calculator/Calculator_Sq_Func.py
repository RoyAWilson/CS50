def main():
    '''
    
    Calculator as function with return
    
    '''
    x = int(input('What\'s x? ' ))
    print(f'{x} squared is:  {square(x)}')
    
def square(n):
    '''
    square n
    
    '''
    return n ** 2

main()
