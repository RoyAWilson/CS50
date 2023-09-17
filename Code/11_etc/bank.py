'''
to implement a bank account class
and allow it to have a balance 
and deposit and withdrawal methods
'''

class Account:
    '''
    set up a banking account
    '''
    def __init__(self,):
        self._balance = 0
        # _balance as visual reminder this variable should only be changed by this class

    @property
    def balance(self):
        '''
        return the balance
        '''
        return self._balance

    def deposit(self, n):
        '''
        Make a deposit
        '''
        self._balance += n

    def withdraw(self, n):
        '''
        Make a withdrawal
        '''
        self._balance -= n

def main():
    '''
    Account transactions
    '''
    account = Account()
    print(account.balance)
    account.deposit(100)
    account.withdraw(50)
    print('Balance = ', account.balance)

if __name__ == '__main__':
    main()
