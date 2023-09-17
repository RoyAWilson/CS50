# to take an input and yell it back in all caps

def main():
    yell('This', 'is', 'CS50')

def yell(*words):
    # *words is just a rename of *args
    uppercased = [word.upper() for word in words]
    # Note the use of () on upper has returned.
    print(*uppercased)
    # Note the * in the print statement to unpack the vaules.
        
## Note the single *, this is saying print the unpacked list - it is passing 3 arguments to the print func.

if __name__ == '__main__':
    main()