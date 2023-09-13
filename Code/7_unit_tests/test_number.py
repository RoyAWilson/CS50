# '''

# Test number.py

# '''
# # import the file to be tested

# from  number import square

# def main():
#     test_square()

# def test_square():
#     if square(2) != 2:
#         print('2 squared was not 4')
#     if square(3) != 9:
#         print('2 squared was not 9')

# if __name__ = '__main__':
#     main()

'''

Checking the code using the assert keyword'

'''

from  number import square

def main():
    test_square()

def test_square():
    try:
        assert( square(2)) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert(square(3)) == 9
    except AssertionError:
        print('3 squared was not 9')
    try:
        assert( square(-2)) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert(square(-3)) == 9
    except AssertionError:
        print('-3 squared was not 9')
    try:
        assert(square(0)) == 0
    except AssertionError:
        print('0 squared was not 0')            
     
# puttin in error handling.  To handle the assertion error and make the output more user friendly    


if __name__ == '__main__':
    main()
    