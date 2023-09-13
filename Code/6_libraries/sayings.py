def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f'Hello, {name}')
def goodbye(name):
    print(f'Goodbye, {name}')
    
if __name__=='__main--':
# the above is needed to stop main running if this code is called by another file and should really always be added.
    main()
