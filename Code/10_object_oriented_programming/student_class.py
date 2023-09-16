'''

Introduction to OOP Student as a class

'''

class Student:
    '''
    
    Student Class
    
    '''
    ...
    

def main():

    '''
    main function
    
    '''

    student = get_student()
    print(f'{student.name} from {student.name}')
1
def get_student():
    '''
    
    return a student
    
    '''

    student = Student()
    student.name = input('Name: ')
    student.house = input('House: ')
    return student

## Help - how can this class work, where is the .. = self...
## Why did the lecturer write an empty class?

if __name__ == '__main__':
    main()
