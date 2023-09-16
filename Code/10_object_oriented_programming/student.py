'''

Introduction to OOP

'''
def main():

    '''
    main function
    
    '''

    student = get_student()
    if student["Name"] == 'Padma':
        student["House"] = 'Ravenclaw'
    print(f'{student["Name"]} from {student["House"]}')

def get_student():
    '''
    
    return a student
    
    '''
    name = input('Name: ').strip().title()
    house = input('House: ').strip().title()
    return {'Name': name, 'House': house}
# return changed to Dictionary also allows editing of the input if necessary.
# my guess at how to do it.  Lecturer came up with a longer version.

if __name__ == '__main__':
    main()
    