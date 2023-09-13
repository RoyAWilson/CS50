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
    assert( square(2)) == 4
    assert(square(3)) == 9

if __name__ == '__main__':
    main()