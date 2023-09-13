def main():
    '''

    simple hello name
    '''

    name = input('What is your name? ')
    print(hello(name.title()))
# Changes made make code more testable than the code in 1_hello as returns can be tested.
def hello(to = 'World'):
    return f'Hello, {to}'

if __name__ == '__main__':
    main()
