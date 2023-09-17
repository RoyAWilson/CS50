## Meow to run for the command line.

import sys

if len(sys.argv) == 1:
    print('meow')
## check if len of argsv is 3 and that the second entry is -n
elif len(sys.argv) == 3 and sys.argv[1] == '-n':
    # if so then grab second entry and covert to integer
    n = int(sys.argv[2])
    # pring number of meows with a loop.
    for _ in range(n):
        print('meow')
    
else:
    print('Usage of: meows.py')
