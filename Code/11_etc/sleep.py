# to print out some number of sheep.

def main():
    
    n = int(input('What\'s n? '))

    for s in sheep(n):
        print(s)
## This looks pretty dangerous!  There is no control over the upper limit of sheep to produce!
def sheep(n):
    # return '🐏' * n
    for i in range(n):
        yield '🐏' * i
        ## this will return 1 value at a time.  If return were used it would return zero and jump out of the loop
        # back into main.  Still think this could do with an upper bound on the iterations allowable.
if __name__ == '__main__':
    main()
    
