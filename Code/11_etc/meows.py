'''
constants intro
'''

class Cat:
    MEOWS = 3 #Class variable
    def meow(self):
        for _ in range(Cat.MEOWS): # variable has class name so only the var inside the class used
            print('meow')

cat = Cat()
cat.meow()
