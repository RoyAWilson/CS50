def meow(n: int) -> str:
    '''
    to meow n times
    
    :param n: Number of tiems to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    '''
    return 'meow\n' * n

number: int = int(input('Number: '))
meows: str = meow(number)
print(meows)
