# Ask user to input their name:

name = input("What's your name? ").strip().title()

# Split out the first and last name:

first, second = name.split(' ')

# Say hello to the user:

print(f'Hello, {first}')
