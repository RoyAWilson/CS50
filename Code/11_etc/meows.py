## Meow to run for the command line.  Using argparse library

import argparse

parser = argparse.ArgumentParser(description = 'Meow like a cat')

# Configure argparser to recognise the argument we want to pass and parse

parser.add_argument('-n', default = 1, help = 'Number of times to meow', type = int)
args = parser.parse_args()
# argparser will automaticalls read sys.argsv for me.  No need to bother doing it for myself
# args will now contain all the arguments passed at the command line and can be
# iterated over using a loop:

# start loop in a the range of
for _ in range(args.n):
    print('meow')
