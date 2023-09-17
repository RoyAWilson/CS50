# to print out some number of sheep.

def main():
    
    n = int(input('What\'s n? '))

    for s in sheep(n):
        print(s)
## This looks pretty dangerous!  There is no control over the upper limit of sheep to produce!
def sheep(n):
    # return '🐏' * n
    flock = []
    for i in range(n):
        flock.append('🐏' * i)
    return flock

if __name__ == '__main__':
    main()
    
