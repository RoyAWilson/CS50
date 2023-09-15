'''

to validate if email address contains @ char - very basic version

'''

email = input('What is your email address? ').strip()

# Validate email address if string contains @ symbol anywhere in it

# if '@' in email and '.' in email:
#     print('Valid')
# else:
#     print('Not Valid')

# split the user name and domain_name into two variables:

# user_name, domain_name = email.split('@')

# if user_name and '.' in domain_name:
#     print('Valid')
# else:
#     print('Invalid')

# To check if the email address is a '.edu' domain name:

user_name, domain_name = email.split('@')

if user_name and domain_name.endswith('.edu'):
    print('Valid')

else:
    print('Invalid')
## This code above prints out 'Valid' or 'Invalid' 2c! even prints out 'Valid' Iinvalid' if half valid
## The lecturer's code only prints one result!  Can;t seem to get mine to work like his.  Seems to be looping through
## The tests and printing a result for each.  Suppose could try nesting the if statements.