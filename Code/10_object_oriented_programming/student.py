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
    
    student = {}
    
    student['Name'] = input('Name: ').strip().title()
    student['House'] = input('House: ').strip().title()
    return student

# lecturer's version seems to do exactly the same

if __name__ == '__main__':
    main()
