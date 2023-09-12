def main():
    '''
    
    Print a horizontal n of ?s
    
    '''
  
    print_square(3)
 
def print_square(size):
    '''
    
    define the function to print the ?s
    
    '''
    for i in range(size):
        print('#' * size, end='\n')
# Lecturer used nested loops to acheive same effect

main()
