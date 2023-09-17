'''

Global Variables intro

'''

# set global balance variable:

balance = 0

def main():
    print('Balance=', balance)
    deposit(100)
    withdraw(50)
    print('New balance= ', balance)
    
def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == '__main__':
    main()