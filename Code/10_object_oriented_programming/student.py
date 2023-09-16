'''

Introduction to OOP

'''
def main():

    '''
    main function
    
    '''

    student = get_student()
    if student[0] == 'Padma':
        student[1] = 'Ravenclaw'
    print(f'{student[0]} from {student[1]}')

def get_student():
    '''
    
    return a student
    
    '''
    name = input('Name: ').strip().title()
    house = input('House: ').strip().title()
    return [name, house]
# return changed to list to allow editing of the input if necessary.

if __name__ == '__main__':
    main()
    