'''

Validate using regex

'''

import re

# # simple validate if contains '@'

# email = input('What is your email address: '). strip()

# if re.search('@', email):
#     print('Valid')
# else:
#     print('Invalid')

# Slightly better way using some of the special characters to refine the match

# simple validate if contains '@'

# email = input('What is your email address: '). strip()

# # Should match only if there is more than one char to left of @ and more than 1 to right
# if re.search('.+@.+', email):
#     print('Valid')
# else:
#     print('Invalid')

## Check for .edu at end of email address:

# email = input('What is your email address: '). strip()

# # r in expression before quotes - trat as raw.  \ escapes the l char so it is considered as a string
# # not a any character marker.
# if re.search(r'.+@.+\.edu', email):
#     print('Valid')
# else:
#     print('Invalid')

# email = input('What is your email address: '). strip()

# # To refine further the validation and remove the fact that even a sentence containing at and .edu
# # would validate.  The following validates that there is more than one char before @ and the string
# # ends with .edu.  ^ at start - begins with $ at end finishes with

# if re.search(r'^.+@.+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# email = input('What is your email address: '). strip()

# # To remove the problem of allowing multiple @ signs replace the . with [^@] before and after the @:

# if re.search(r'^[^@]+@[^@]+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# # To allow only certain characters in user name and domain name

# email = input('What is your email address: '). strip()


# if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# To allow only certain characters in user name and domain name by using inbuilt matching criteria
# for instance replace the [a-z...] with \w and to ignore the case of the input and add more domain names:

# email = input('What is your email address: '). strip()


# if re.search(r'^\w+@\w+(.edu|.com|.gov|.net)', email, re.IGNORECASE):
#     print('Valid')
# else:
#     print('Invalid')
    
# Handle multiple dots in a domain name using groups only works with 1 subdomain without the ? would allow however many
# also to allow usre to have a dot in the user name:

email = input('What is your email address: '). strip()


if re.search(r'^(\w+|\.)+@(\w+\.)?\w+(.edu|.com|.gov|.net)', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')
