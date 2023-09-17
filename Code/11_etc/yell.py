# to take an input and yell it back in all caps

def main():
    yell(['This', 'is', 'CS50'])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
## Note the single *, this is saying print the unpacked list - it is passing 3 arguments to the print func.

if __name__ == '__main__':
    main()