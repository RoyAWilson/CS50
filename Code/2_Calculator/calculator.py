x = float(input('What is x? '))
y = float(input('What is y? '))
print(f'{round(x)} plus {round(y)} = {round(x + y):,}')
# Or:
z = round(x + y)
print(f'{z:,}')
